#wap to convert all the strings in the list to upper case using map
# l = ['apple', 'gmail', 'infosys', 'Junkcart']
# def upper(char):
#         return char.upper()
# res = map(upper, l)
# print(list(res))


#wap to convert all negative numbers in the list to positive ######
# l = [-1, -2, -3]
# def neg(num):
#     return abs(num)
# res = map(neg, l)
# print(list(res))

#wap that returns the list of numbers raised to the power of their indeces using maps
# l = [10, 20, 30, 40]
# def index_(arg):
#     return l.index(arg)
#
# res = map(index_, l)
# print(list(res))


#wap that returns all the words in lower case in the given sentance
# l = ['APPLE', 'GNMMAIL', 'YAHOO', 'CUBES']
# def lower(char):

        # return char.lower()
# res = map(lower, l)
# print(list(res))

"""length of each word"""
sentence = "Hello world"
list_ = sentence.split()
res = map(len, list_)
print(res)