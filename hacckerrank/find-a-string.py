def count_substring(string, sub_string):
    for i in range(len(string)):
        
    count = string.find(sub_string)
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)



# str = "I am an Indian, by birth"

# count = str.find("birth")
# print(count)