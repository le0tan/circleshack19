def sanitize_postal_code(postal_code: int):
    # TODO: implement real sanitization
    return postal_code

def from_postal_code_to_income_distribution(postal_code: int):
    # TODO
    postal_code = sanitize_postal_code(postal_code)
    return {"0-100": postal_code}