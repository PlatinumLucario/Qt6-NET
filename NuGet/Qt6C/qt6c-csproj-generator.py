# /// Native Library NuGet Project Generator
# requires-python = ">=3.13"
import argparse
import re
from pathlib import Path
import subprocess
import jinja2

def get_version():
    ver = ""
    try:
        # The RPM command will only work on RPM-based distributions, such as Fedora.
        ver = subprocess.run("rpm -q qt6-qtbase-devel | grep '\\-6.*.*-' -o", shell=True, stdout=subprocess.PIPE, text=True).stdout.replace('-', '').replace("\n", "")
    except:
        ver = input("Unable to detect qt6-qtbase-devel version number due to an error.\n" \
        "Please enter the Qt6 library version number manually and press enter:\n"
        "> ")
    return ver

def template_values():
    return {
        "qt6_lib_ver": get_version()
    }

def generate_linux():
    v = template_values()
    v["libs_linux_x64"] = subprocess.run("ls ./runtimes/linux-x64/native/", shell=True, stdout=subprocess.PIPE, text=True).stdout.rstrip("\n").replace("\n", ";\n      ").replace("libq", "./runtimes/linux-x64/native/libq")
    env = jinja2.Environment()
    s = open("./Qt6C.csproj.jinja").read()
    t = env.from_string(s)
    s = t.render(**v)
    open("Qt6C.csproj", "w").write(s)

def main():
    generate_linux()


if __name__ == "__main__":
    main()
