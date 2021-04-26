from os.path import join, sep

from SCons.Script import Builder, DefaultEnvironment

from platformio.builder.tools import platformio as platformio_tool

#
# Backward compatibility with PlatformIO 2.0
#
platformio_tool.SRC_DEFAULT_FILTER = " ".join([
    "+<*>", "-<.git%s>" % sep, "-<svn%s>" % sep,
    "-<example%s>" % sep, "-<examples%s>" % sep,
    "-<test%s>" % sep, "-<tests%s>" % sep
])


def LookupSources(env, variant_dir, src_dir, duplicate=True, src_filter=None):
    return env.CollectBuildFiles(variant_dir, src_dir, src_filter, duplicate)


def VariantDirWrap(env, variant_dir, src_dir, duplicate=False):
    env.VariantDir(variant_dir, src_dir, duplicate)


env = DefaultEnvironment()
platform = env.PioPlatform()

env.AddMethod(LookupSources)
env.AddMethod(VariantDirWrap)

env.Replace(
    PLATFORMFW_DIR=platform.get_package_dir("simba"),
    OBJCOPY=join(platform.get_package_dir("tool-esptool"), "esptool")
)

env.Append(
    CPPDEFINES=[
        ("F_CPU", "$BOARD_F_CPU")
    ],

    BUILDERS=dict(
        ElfToBin=Builder(
            action=env.VerboseAction(" ".join([
                join(platform.get_package_dir("tool-esptool"), "esptool"),
                "-eo", '"%s"' % join(
                    "$PLATFORMFW_DIR", "3pp", "esp8266Arduino", "2.3.0",
                    "bootloaders", "eboot", "eboot.elf"
                ),
                "-bo", "$TARGET",
                "-bm", "$BOARD_FLASH_MODE",
                "-bf", "${__get_board_f_flash(__env__)}",
                "-bz", "${__get_flash_size(__env__)}",
                "-bs", ".text",
                "-bp", "4096",
                "-ec",
                "-eo", "$SOURCES",
                "-bs", ".irom0.text",
                "-bs", ".text",
                "-bs", ".data",
                "-bs", ".rodata",
                "-bc", "-ec"
            ]), "Building $TARGET"),
            suffix=".bin"
        )
    )
)

env.SConscript(
    [env.subst(join("$PLATFORMFW_DIR", "make", "platformio.sconscript"))])
