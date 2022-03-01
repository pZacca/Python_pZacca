"""
for / while
0 10
1 9
2 8
3 7
4 6
5 5
6 4
7 3
8 2
"""

# Jeito que fiz:
# i = 0
# j = 10
# for i in range(0, 9):
#     print(i, j)
#     i += 1
#     j -= 1

# Jeito mostrado pelo professor:
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)