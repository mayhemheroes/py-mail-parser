#!/usr/bin/python3
import atheris
import sys

with atheris.instrument_imports():
    import mailparser


@atheris.instrument_func
def TestOneInput(data):
    try:
        mailparser.parse_from_bytes(data)
    except mailparser.exceptions.MailParserError:  # Want to ignore exceptions that are already handled by lib
        return


def main():
    atheris.Setup(sys.argv, TestOneInput)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
