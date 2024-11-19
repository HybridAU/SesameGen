import math
import secrets
import string

# Characters like 'C', K' and 'S' are not a really ambiguous,
# but it can be hard to tell if they are upper or lower case.
# fmt: off
AMBIGUOUS_CHARACTERS = [
    "8", "B", "c", "C", "g", "9", "I", "L", "1", "l", "|", "0", "o",
    "O", "k", "K", "s", "S", "u", "U", "v", "V", ";", ":", "'", '"',
]
# fmt: on


def generate_password(character_set, length):
    """
    Uses the secretes module to pick a given number of characters
    from the available character set. https://docs.python.org/3/library/secrets.html
    """
    # "complexity is the worst enemy of security" - Bruce Schneier.
    return "".join(secrets.choice(character_set) for _character in range(length))


def calculate_entropy(character_set, length):
    """
    Calculates the bits of entropy used to generate the password.
    """
    return round(math.log2(len(character_set) ** length), 1)


def get_password(
    length=16,
    lower_case=True,
    upper_case=True,
    numbers=True,
    special_characters=False,
    remove_ambiguous_characters=False,
):
    """
    Return a password that meets the requirements and
    the amount of entropy those requirements provide
    """
    character_set = []

    if lower_case:
        character_set += string.ascii_lowercase
    if upper_case:
        character_set += string.ascii_uppercase
    if numbers:
        character_set += string.digits
    if special_characters:
        character_set += string.punctuation
    if remove_ambiguous_characters:
        for char in AMBIGUOUS_CHARACTERS:
            if char in character_set:
                character_set.remove(char)

    if character_set and length:
        password = generate_password(character_set, length)
        entropy = calculate_entropy(character_set, length)
    else:
        # No characters have been set or the length is 0.
        # We can't generate a password, so we just give a blank string and zero bits.
        password = ""
        entropy = 0
    return {"password": password, "entropy": entropy}
