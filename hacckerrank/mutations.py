def mutate_string(string, position, character):
    mut_list= list(string)
    mut_list[position] = character
    mut_string = ''.join(mut_list)
    return mut_string

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
    
    
# str = "abrackdabra"
    
# mut_list= str.split(',')
# print(mut_list)