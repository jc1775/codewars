def toJadenCase(string):
    new_sent = ""
    i = 0
    while i < len(string):
        if string[i] == " " and string[i+1] != " ":
            new_sent += (string[i] + (string[i+1]).capitalize())
            i += 2
        elif i == 0 and string[i] != string[i].capitalize():
            new_sent += string[i].capitalize()
            i += 1
        else:
            new_sent += string[i]
            i += 1
    return new_sent