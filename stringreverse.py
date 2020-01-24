def reverse_string(s):
    return s[-1::-1]


def loop_reverse(s):
    i = len(s) + 1
    newstring = ""
    for num in range(1, i):
        newstring += s[-num]
    return newstring


test = "This is a test string"
print(loop_reverse(test))

testsplit = test.split(" ")
print(testsplit)