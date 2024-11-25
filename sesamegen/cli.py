from typing import Annotated

import typer

from sesamegen.generator import get_password
from sesamegen.gui import start_gui


def main(
    gui: Annotated[
        bool,
        typer.Option(
            help=(
                "Show the graphical user interface (GUI). When this option is set, "
                "all other options are ignored as they are set in the GUI itself."
            )
        ),
    ] = False,
    length: Annotated[
        int, typer.Argument(help="Length of the password to generate")
    ] = 16,
    lower: Annotated[bool, typer.Option(help="Include lower case characters")] = False,
    upper: Annotated[bool, typer.Option(help="Include upper case characters")] = False,
    numbers: Annotated[bool, typer.Option(help="Include lowercase characters")] = False,
    special: Annotated[bool, typer.Option(help="Include lowercase characters")] = False,
    remove: Annotated[bool, typer.Option(help="Include lowercase characters")] = False,
):
    """
    Generate passwords
    """
    if gui:
        start_gui()
    if lower or upper or numbers or special or remove:
        print(
            get_password(
                length=length,
                lower_case=lower,
                upper_case=upper,
                numbers=numbers,
                special_characters=special,
                remove_ambiguous_characters=remove,
            )
        )
    else:
        print(
            get_password(
                length=length,
            )
        )
