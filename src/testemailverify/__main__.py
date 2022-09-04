"""re."""
import click

import re


@click.command()
@click.version_option()
def main() -> None:
    """Dan."""


string = """sdfsdfdsfds
donh128@gomail.com
www.google.com
fel123
"""


def verify_email(text: str) -> list[str]:
    """Checks text for valid email addresses."""
    email_pattern = re.compile(r"\w+@\w+\.\w+")
    return email_pattern.findall(text)


print(verify_email(string))

if __name__ == "__main__":
    main(prog_name="emailverify")  # pragma: no cover
