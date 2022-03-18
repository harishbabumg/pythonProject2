
# for row in range(4):
#     for col in range(row + 1):
#         print("*", end=" ")
#     print()
# n = 1

# while n <= 4:
#     n + 1
#     print("*", end=" ")


# for row in range(1, 5):
#     print("* " * row)

# for row in range(1, 5):
#     print("*" * row)

# """ right aligned"""
# for row in range(1, 5):
#     print(f'{"* " * row:>8}')

"""centrally aligned"""
# for row in range(1, 5):
#     print(f'{"* " * row:^8}')

# """reversed order"""
# for row in range(4, 0, -1):
#     print(f'{"* " * row:^8}')
#
# """inverted right justified triangle"""
# for row in range(4, 0, -1):
#     print(f'{"* " * row:>8}')
#
# """"""
# for row in range(4, 0, -1):
#     print(f'{"* " * row:^8}')

"""printing number pattern"""
# for row in range(1, 5):
#     for col in range(1, row+1):
#         print(col, end=" ")
#     print()

"""in one for loop"""
# x = " "
# for row in range(1, 5):
#     x += " " + str(row)
#     print(x)

"""reverse inverted triangle"""
# for row in range(4, 0, -1):
#     for col in range(1, row+1):
#         print(col, end=" ")
#     print()

# """alphabets"""
# for row in range(ord("a"), ord("d")+1):
#     for col in range(ord("a"), row+1):
#         print(chr(col), end=" ")
#     print()
#
# x = ""
# for row in range(ord("a"), ord("d")+1):
#     x += chr(row) + " "
#     print(x)
#
# for row in range(1, 5):
#     for col in range(ord("a"), ord("a")+row):
#         print(chr(col), end=" ")
#     print()

