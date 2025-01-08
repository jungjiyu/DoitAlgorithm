a = 1


def test():
    global a
    a = 3


print(a)  # 1
test()
print(a)  # 3