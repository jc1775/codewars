def translate_lite(sentence):
    word_list = sentence.split(" ")
    new_string = ""
    for word in word_list:
        new_string += word[-1::-1] + " "
    return new_string

test = "This is a test string"
print(translate_lite(test))