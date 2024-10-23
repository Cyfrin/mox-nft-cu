

def test_encoding_string_combination(encoding):
    string_one = "Hi mom"
    string_two = "Miss you"
    combined = encoding.combine_strings(string_one, string_two)
    assert combined == string_one + string_two


def test_multi_encoding(encoding):
    decoded_strings = encoding.multi_decode()
    (string_one, string_two) = decoded_strings
    assert string_one == "Hi Mom"
    assert string_two == "Miss you"


# @pytest.mark.staging
def test_raw_call_call_anything(raw_call, call_anything):
    new_address = "0x874437B5a42aA6E6419eC2447C9e36c278c46532"
    new_amount = 888
    raw_call.call_function_directly(new_address, new_amount, call_anything.address)
    assert call_anything.some_address() == new_address
    assert call_anything.amount() == new_amount
