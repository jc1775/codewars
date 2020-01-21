def tickets(people):
    twent = 0
    fift = 0
    hundo = 0
    for num in people:
        if num == 25:
           twent += 1
        elif num == 50:
            if twent < 1:
                return "NO"
            else:
                twent -= 1
                fift += 1
        elif num == 100:
            if (fift < 1 and twent < 1):
                return "NO"
            elif fift >= 1 and twent >= 1:
                fift -= 1
                twent -= 1
                hundo += 1
            elif twent >= 3:
                twent -= 3
            else:
                return "NO"
    return "YES"
