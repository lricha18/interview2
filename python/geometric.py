##### Finding Geometric Sequences

# Given a list (l) and a ratio (r), find the number of groups of 3 indices in the list such that: 
# 1. a < b < c
# 2. {a, b, c} is a geometric sequence with a common ratio r

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
    # code here
    return 0

test_cases = [
    ([1, 2, 2, 4], 2, 2),
    ([1,1,5,25,25,125,625], 5, 8),
    ([1, 3, 9, 9, 9, 9, 9, 10, 27, 81], 3, 17),
    ([345]*10000, 1, 166616670000)
]

for case in test_cases:
    l, r, output = case
    print(find_geo_seq(l, r) == output)