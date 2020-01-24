def translate_lite(sentence):
    word_list = sentence.split(" ")
    new_string = ""
    for word in word_list:
        new_string += word[-1::-1] + " "
    return new_string


def onethird(n):
    sum = 0
    for i in range(1,(n+1)):
        sum += (i**2)
    ans = sum / (n**3)
    return ans

test = 5
print(onethird(test))