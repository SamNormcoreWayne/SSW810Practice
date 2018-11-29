def covers_alphabet(setence):
    alphabet = set()
    tmp = str()
    for i in range(97, 123):
        alphabet.add(chr(i))
    for item in setence:
        if item.isalpha():
            tmp += item.lower()
    return set(tmp) == alphabet