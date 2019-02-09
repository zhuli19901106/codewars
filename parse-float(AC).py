def parse_float(string):
    try:
        return float(string)
    except (ValueError, TypeError):
        return None
