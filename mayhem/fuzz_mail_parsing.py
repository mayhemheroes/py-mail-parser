#!/usr/bin/python3
import atheris

with atheris.instrument_imports():
    import sys
    import mailparser


@atheris.instrument_func
def TestOneInput(data):

    try:
        mailparser.parse_from_bytes(data)
    except mailparser.exceptions.MailParserError:
        pass


def main():
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
