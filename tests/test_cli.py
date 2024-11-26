import re

from typer.testing import CliRunner

from sesamegen.cli import app

runner = CliRunner()


def test_app_with_zero_length():
    result = runner.invoke(app, ["0"])
    assert result.exit_code == 0
    assert "{'password': '', 'entropy': 0}" in result.stdout


def test_app_with_no_characters():
    result = runner.invoke(app, ["16", "--remove"])
    assert result.exit_code == 0
    assert "{'password': '', 'entropy': 0}" in result.stdout


def test_app_with_default_settings():
    result = runner.invoke(app)
    assert result.exit_code == 0
    default_password_regex = re.compile(r"{'password': '.*', 'entropy': 85\.7}")
    assert default_password_regex.match(result.stdout) is not None


def test_app_with_only_numbers():
    result = runner.invoke(app, ["--special"])
    assert result.exit_code == 0
    # A password with only special characters, no lower, upper or numbers
    only_numbers_regex = re.compile(r"{'password': '[^a-zA-Z0-9]*', 'entropy': 80\.0}")
    assert only_numbers_regex.match(result.stdout) is not None
