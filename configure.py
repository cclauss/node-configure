import inspect
import platform
import sys

print(sys.platform, sys.version)

for name, value in inspect.getmembers(platform):
    if name[0] != "_" and callable(value):
        try:
            value = value()
        except (IndexError, TypeError):
            continue
        if str(value).strip("(),' "):
            print("{:>21}() = {}".format(name, value))
