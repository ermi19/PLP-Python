# task 1: Create an empty list
my_list = []

# task 2: Append elements to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# task 3: Insert the value 15 at the second position
my_list.insert(1, 15)

# task 4: Extend my_list with another list
my_list.extend([50, 60, 70])

# task 5: Remove the last element from my_list
my_list.pop()  # This removes the last element (70)

# task 6: Sort my_list in ascending order
my_list.sort()

# task 7: Find and print the index of the value 30 in my_list
index_of_30 = my_list.index(30)

# Print results
print("Final list:", my_list)
print("Index of value 30:", index_of_30)