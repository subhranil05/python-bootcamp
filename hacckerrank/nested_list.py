# First took all the inputs and make a combined list of name and score as nested list like [['Subhranil', 25.5], ['Sayan', 24.5], ['Rivu', 28.5]]

# Make a separate list only for scores from the above list

# Convert the score list to a set to remove duplicates

# sort the score set, now 2nd element of the set should be the 2nd higest score

# Find that score in the first list and make a separte list  of names only.

# Print the items of the name list in a for loop to get the answers

if __name__ == '__main__':
    list1 = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list1.append([name,score])
    
    findscore = [i[1] for i in list1]
    setscore = sorted(set(findscore))
    
    ans_list = [j[0] for j in list1 if j[1] == setscore[1]]
    
    sorted_list = sorted(ans_list)
    for i in sorted_list:
        print(i)
        