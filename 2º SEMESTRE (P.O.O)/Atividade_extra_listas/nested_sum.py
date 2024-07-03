list = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]

count = 0
i = 0
new_list = []
while count < len(list):
    new_list += (list[i])
    i += 1
    count += 1

ns = sum(new_list)
print(ns)