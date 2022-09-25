#!/usr/bin/python3
import atheris
import pdb
with atheris.instrument_imports():
    import sys
    import mailparser


@atheris.instrument_func
def TestOneInput(data):
    try:
        mail = mailparser.parse_from_bytes(data)
        if mail:
            mail.get_server_ipaddress('localhost')
    except mailparser.exceptions.MailParserError:
        pass


def main():
    atheris.Setup(sys.argv, TestOneInput, enable_python_coverage=True)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
