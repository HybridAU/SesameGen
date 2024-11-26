from typing import Annotated

import typer

from sesamegen.generator import get_password

try:
    from sesamegen.gui import start_gui
except ImportError:
    # Can't import PyQt6
    def start_gui():
        print(
            "Failed to import PyQt. "
            "Possibly running in headless environment GUI will be unable to start."
        )


app = typer.Typer()


@app.command()
def main(
    show_gui: Annotated[
        bool,
        typer.Option(
            "--gui",
            help=(
                "Show the graphical user interface (GUI). When this option is set, "
                "all other options are ignored as they are set in the GUI itself."
            ),
        ),
    ] = False,
    length: Annotated[
        int, typer.Argument(help="Length of the password to generate")
    ] = 16,
    lower_case: Annotated[
        bool, typer.Option("--lower", "-l", help="Include lower case characters")
    ] = False,
    upper_case: Annotated[
        bool, typer.Option("--upper", "-u", help="Include upper case characters")
    ] = False,
    numbers: Annotated[
        bool, typer.Option("--numbers", "-n", help="Include numbers")
    ] = False,
    special_characters: Annotated[
        bool, typer.Option("--special", "-s", help="Include special characters")
    ] = False,
    remove_ambiguous_characters: Annotated[
        bool, typer.Option("--remove", "-r", help="Remove ambiguous characters")
    ] = False,
):
    """
    Generate passwords, if no options are passed the default password includes
    lower case, upper case, numbers, and removes ambiguous characters.
    If any options are set it will only include those options.
    """
    if show_gui:
        start_gui()
    elif (
        lower_case
        or upper_case
        or numbers
        or special_characters
        or remove_ambiguous_characters
    ):
        print(
            get_password(
                length=length,
                lower_case=lower_case,
                upper_case=upper_case,
                numbers=numbers,
                special_characters=special_characters,
                remove_ambiguous_characters=remove_ambiguous_characters,
            )
        )
    else:
        print(
            get_password(
                length=length,
            )
        )
