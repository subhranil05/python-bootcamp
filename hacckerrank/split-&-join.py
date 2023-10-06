def split_and_join(line):
    line = line.split()
    line_join = "-".join(line)
    return line_join

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)