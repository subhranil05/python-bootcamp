range_num = int(input("Write the range: "))

fibonacci_list = [0,1]
x = 1
for i in range(0, (range_num - 2)):
    x+=i
    fibonacci_list.append(x)
print(fibonacci_list)