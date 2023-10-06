# Take a empty list

# First variable N is the number of commands given in input, take a for loop of range N

# inside for loop take commands input in cmd input variable and split the input to convert the input string as lis. 
# ex: insert 1 5 ==> cmd = ['insert', '1', '5']

# Use if/else condition to check every condition of commands. cmd[0] = commands , cmd[1] = arguments

if __name__ == '__main__':
    N = int(input())
    lst = []
    for command in range(N):
        cmd = input().split()
        
        if cmd[0] == 'insert':
            lst.insert(int(cmd[1]), int(cmd[2]))
        elif cmd[0] == 'remove':
            lst.remove(int(cmd[1]))
        elif cmd[0] == 'append':
            lst.append(int(cmd[1]))
        elif cmd[0] == 'sort':
            lst.sort()
        elif cmd[0] == 'pop':
            lst.pop()
        elif cmd[0] == 'reverse':
            lst.reverse()
        else:
            print(lst)