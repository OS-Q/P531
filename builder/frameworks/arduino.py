
from os.path import join

from SCons.Script import COMMAND_LINE_TARGETS, DefaultEnvironment, SConscript


if "nobuild" not in COMMAND_LINE_TARGETS:
    SConscript(
        join(DefaultEnvironment().PioPlatform().get_package_dir(
            "A51"), "tools", "platformio-build.py"))
