def capitalize(text):
    if text == '':
        return ''
    first_char = text[0].upper()
    other = text[1:]
    return f'{first_char}{other}'
