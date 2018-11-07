##### Finding Geometric Sequences

# Given a list (l) and a ratio (r), find the number of groups of 3 indices (i,j,k) in the list such that: 
# 1. i < j < k
# 2. {l[i], l[j], l[k]} is a geometric sequence with a common ratio r
# i.e. r*l[i] == l[j], r*l[j] == l[k] 

# Example:
# l = [1,1,5,25,25,125,625]
# r = 5

# quads = [
#     (0, 2, 3)
#     (0, 2, 4),
#     (1, 2, 3),
#     (1, 2, 4),
#     (2, 3, 5),
#     (2, 4, 5),
#     (3, 5, 6),
#     (4, 5, 6)
# ]
# count = 8

def find_geo_seq(l, r):
    
    count = 0

    this_dict = {}

    # for i in range(len(l)-1, -1, -1): # Step backwards through the list and add index found to dictionary 
    # 	if(l[i] in this_dict):
    # 		this_dict[l[i]].append(i)
    # 	else:
    # 		this_dict[l[i]] = [i]

    # 	if(i < len(l) - 2): # start checking once there are at least 3 numbers in dictionary
    # 		if(r * l[i] in this_dict): # if the second number is in the dictionary

    # 			second_values = []

    # 			for j in this_dict[r * l[i]]: # check the indicies for ones that are greater than i
    # 				if(j > i):
    # 					second_values.append(j)

    # 			if(r * r *l[i] in this_dict): # check if there is third value that will be valid for geometric group

    # 				third_values = this_dict[r * r * l[i]].copy()
    # 				third_values.remove(i)




    for i in range(0,len(l)-2): # Will search through 0 -> n-2, i can't be n-1 or n for a group to be valid

    	for j in range(i+1, len(l)-1): # Will search through i+1 -> n-1, j can't be <= i or  == n

    		for k in range(j+1, len(l)): # Will search for valid k from j+1 -> n

    			if(r*l[i] == l[j] and r*l[j] == l[k]):
    				count+=1
    return count

test_cases = [
    ([1, 2, 2, 4], 2, 2),
    ([2, 1, 3, 9], 3, 1),
    ([0, 0, 0, 0], 1, 4),
    ([1,1,5,25,25,125,625], 5, 8),
   	([1, 3, 9, 9, 9, 9, 9, 10, 27, 81], 3, 15),
    ([345]*10000, 1, 166616670000)
]

for case in test_cases:
    l, r, output = case
    print(find_geo_seq(l, r) == output)