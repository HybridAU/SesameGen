from sesamegen.generator import calculate_entropy, generate_password, get_password


def test_generator_with_zero_length():
    assert get_password(length=0) == {"password": "", "entropy": 0}


def test_generator_with_no_characters():
    assert get_password(
        length=16,
        lower_case=False,
        upper_case=False,
        numbers=False,
        special_characters=False,
        remove_ambiguous_characters=True,
    ) == {
        "password": "",
        "entropy": 0,
    }


def test_generate_will_reuse_values():
    # Check that we reuse values (as opposed to `random.sample()`) which would only
    # get each value once, and fail if the length was larger than the character set
    assert generate_password("X", 3) == "XXX"


def test_calculate_entropy_bits():
    # By setting the character set to 1's and 0's, it's easy to see how many bits of
    # entropy are available. 16 digits is 16 bits of entropy. Nice simple test.
    assert calculate_entropy(["1", "0"], 16) == 16.0


def test_calculate_entropy_numbers():
    # Picking 3 numbers gives values from 000 to 999 (i.e. 1,000 possible values)
    # 10 bits (2**10) can store 1024 values, because we are rounding to the nearest
    # 1 decimal places it comes in a 10.0 bits
    assert (
        get_password(
            length=3,
            lower_case=False,
            upper_case=False,
            numbers=True,
            special_characters=False,
            remove_ambiguous_characters=False,
        )["entropy"]
        == 10.0
    )
