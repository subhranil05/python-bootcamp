li = [9,5,2,3,6,7,8,1,4]

print(f"Original variable: {li}")

li.sort()
sort_list = sorted(li)

rev_sort_list = sorted(li, reverse=True)  # reverse sort list
# print(f"Original variable: {li}")
print(f"Sorted variable: {sort_list}")

print(f"list sorted: {li}")

print(f"Reversed Sorted variable: {rev_sort_list}")


tmp_li = [-6,-5,-4,1,2,3]

s_li = sorted(tmp_li, key=abs)

print(f"Absolute value sorted: {s_li}")