import os
import platform
import sys

# from pyfeatures import FreeThreading, JitCompiler


def print_details():
    lines = [
        system_details(),
        python_details(),
        # str(FreeThreading()),
        # str(JitCompiler()),
    ]
    print(header := "=" * max(map(len, lines)))
    print("\n".join(lines))
    print(header)


def system_details():
    name = platform.system()
    arch, _ = platform.architecture()
    cpu = platform.processor()
    cores = os.cpu_count()
    endian = f"{sys.byteorder} Endian".title()
    return (
        f"\N{PERSONAL COMPUTER} {name} {arch} with "
        f"{cores}x CPU cores ({cpu} {endian})"
    )


def python_details():
    implementation = platform.python_implementation()
    version = platform.python_version()
    path = sys.executable
    return f"\N{SNAKE} {implementation} {version} {path}"


if __name__ == "__main__":
    print_details()
