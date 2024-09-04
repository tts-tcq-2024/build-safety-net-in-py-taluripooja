def generate_soundex(name):
    if not name:
        return ""

    # Start with the first letter (capitalized)
    soundex = [name[0].upper()]
    prev_code = get_soundex_code(soundex[0])

    for char in name[1:]:
        code = get_soundex_code(char)
        if code != '0' and code != prev_code:
            soundex.append(code)
            prev_code = code
        if len(soundex) == 4:
            break

    # Ensure the result is exactly 4 characters long
    return ''.join(soundex).ljust(4, '0')
