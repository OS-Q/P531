"""
ESP8266 NONOS SDK

ESP8266 SDK C/C++ only

https://github.com/espressif/ESP8266_NONOS_SDK
"""
from os.path import join

from SCons.Script import COMMAND_LINE_TARGETS, DefaultEnvironment, SConscript


if "nobuild" not in COMMAND_LINE_TARGETS:
    SConscript(
        join(DefaultEnvironment().PioPlatform().get_package_dir(
            "framework-N13"), "tools", "platformio-build.py"))
