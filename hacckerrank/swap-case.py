def swap_case(s):
    swap_str = ''
    for char in s:
        if char.isupper():
            swap_str += char.lower()
        elif char.islower():
            swap_str += char.upper()
        elif char.isspace():
            swap_str += char
        else:
            swap_str += char
    return swap_str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)