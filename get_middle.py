def get_middle(s):
    middish = (len(s)/2) - 1
    if len(s) % 2 != 0:
        return str(s[int(middish + 0.5)])
    else:
        return (str(s[int(middish)])) + (str(s[int(middish) + 1]))
