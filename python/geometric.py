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

import math

def find_geo_seq(l, r):
    
    count = 0

    this_dict = {}

    for i in range(len(l)-1, -1, -1): # Step backwards through the list and add index found to dictionary 
    	if(l[i] in this_dict):
    		this_dict[l[i]].append(i)
    	else:
    		this_dict[l[i]] = [i]

    	if(i < len(l) - 2): # start checking once there are at least 3 numbers in dictionary
    		if(r * l[i] in this_dict): # if the second number is in the dictionary
    			second_values = this_dict[r * l[i]].copy()
    			if(len(second_values) < 1):
    				continue
    			if(second_values[0] == len(l)-1 ):
    				second_values.pop(0)
    			if(len(second_values) < 1):
    				continue
    			if(l[i] == l[second_values[0]]):
    				second_values.remove(i)
    			lowVal = second_values[len(second_values) - 1]

    			if(r * r * l[i] in this_dict):
    				third_values = this_dict[r * r * l[i]].copy()

    				if(third_values[len(third_values) - 1] == i):
    					third_values.remove(i)

    				if(third_values[len(third_values) - 1] == i+1):
    					third_values.remove(lowVal)

    				if(len(third_values) < 1):
    					continue

    				if(len(second_values) > 1 and len(third_values) > 1):
    					for index in range(len(second_values) - 1, -1, -1):
    						if(index == 0):
    							count += 1
    						else:
    							count += len(third_values) - (len(second_values) - index - 1 )

    				else:
    					count += len(second_values) * len(third_values)

    # for i in range(0,len(l)-2): # Will search through 0 -> n-2, i can't be n-1 or n for a group to be valid

    # 	for j in range(i+1, len(l)-1): # Will search through i+1 -> n-1, j can't be <= i or  == n

    # 		for k in range(j+1, len(l)): # Will search for valid k from j+1 -> n

    # 			if(r*l[i] == l[j] and r*l[j] == l[k]):
    # 				count+=1
    return count

test_cases = [
    ([1, 2, 2, 4], 2, 2),
   	([2, 1, 3, 9], 3, 1),
    ([0, 0, 0, 0,], 1, 4),
    ([1,1,5,25,25,125,625], 5, 8),
    ([1, 3, 9, 9, 9, 9, 9, 10, 27, 81], 3, 15),
    ([345]*10000, 1, 166616670000)
]

for case in test_cases:
    l, r, output = case
    print(find_geo_seq(l, r) == output)