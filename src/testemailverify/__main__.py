"""re."""

import re
import typing
import click


@click.command()
@click.version_option()
def main() -> None:
    """Dan."""


string = """sdfsdfdsfds
donh128@gomail.com
www.google.com
fel123
"""


def verify_email(file: typing.TextIO) -> str:
    """Checks text for valid email addresses."""
    email_pattern = re.compile(r"\w+@\w+\.\w+")
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            for match in re.finditer(email_pattern, line):
                print('Found on line %s: %s' % (i+1, match.group()))
    return 'Checks Complete'


print(verify_email('D:/Backup/Work/DevOps/Programming/Apps/EmailVerify/emailverify/src/testemailverify/text.txt'))

if __name__ == "__main__":
    main(prog_name="emailverify")  # pragma: no cover
