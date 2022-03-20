any_string = "hhaai"
for char in any_string:
    if any_string.count(char) > 1:
        return "-"
    else:
        return char

