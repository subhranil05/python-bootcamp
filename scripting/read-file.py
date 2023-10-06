# file = open('file.txt', 'r')

# print(file.name)

# print(file.mode)

# file.close()

# with context manager

# with open('scripting/file.txt', 'r') as fi:
#     file_content = fi.read()
#     print(file_content)
    
    
with open('scripting/file.txt', 'r') as file1:
        with open('scripting/file2.txt', 'w') as file2:
            for line in file1:
                file2.write(line)