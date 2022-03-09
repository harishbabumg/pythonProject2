a = "r"
d = {"a": 10, "b": 20, "c": 30}
# print(d["a"])
quest = {}

for _ in a:
    if a in d:
        print(d[a])
    else:
        quest = quest.setdefault(a)

print(quest)
