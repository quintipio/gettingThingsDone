
def string_to_int(s):
    try:
        v = int(s)
        return v
    except ValueError:
        return None
