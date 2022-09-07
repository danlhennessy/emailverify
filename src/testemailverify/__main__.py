"""re."""

import os
import re

import click


@click.command()
@click.version_option()
def main() -> None:
    """Dan."""


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "text.txt")

print(filename)


def verify_email(file: str) -> str:
    """Checks text for valid email addresses."""
    email_pattern = re.compile(r"\w+@\w+\.\w+")
    with open(file) as f:
        for i, line in enumerate(f.readlines()):
            for match in re.finditer(email_pattern, line):
                print(f"Found on line {i + 1}: {match.group()}")
    return "Checks Complete"


print(verify_email(filename))

if __name__ == "__main__":
    main(prog_name="emailverify")  # pragma: no cover
