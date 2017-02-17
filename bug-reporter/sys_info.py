import platform
import sys

def sys_info():
    system_platform = platform.system()
    if system_platform == "Linux":
        a, b, _ = platform.dist()
        c = platform.machine()
        return a, b, c
    elif system_platform == "Windows":
        pass
    else:
        b, _ , c = platform.mac_ver()
        a = "OS X"
        return a, b, c

# a = sys_info()
# print(a)
