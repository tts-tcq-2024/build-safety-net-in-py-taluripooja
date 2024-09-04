def generate_soundex(name):
    if not name:
        return ""

    soundex = [name[0].upper()]
    prev_code = get_soundex_code(soundex[0])

    def add_soundex_code(char, prev_code):
        code = get_soundex_code(char)
        if code != '0' and code != prev_code:
            soundex.append(code)
        return code

    prev_code = add_soundex_code(name[1], prev_code) if len(name) > 1 else prev_code

    for char in name[2:]:
        prev_code = add_soundex_code(char, prev_code)
        if len(soundex) == 4:
            break

    return ''.join(soundex).ljust(4, '0')
