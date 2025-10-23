def is_type(actual_type, expected_type) -> bool:
    if actual_type is None:
        return False
    elif isinstance(actual_type, str):
        return actual_type == expected_type
    elif isinstance(actual_type, list):
        return expected_type in actual_type
    else:
        raise ValueError(
            f"JSON schema is invalid: field type \"{actual_type}\" is invalid.")
