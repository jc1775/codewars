def find_it(seq):
    counted = []
    for num in seq:
        if num not in counted:
            if seq.count(num) % 2 != 0:
                return num
            else:
                counted.append(num)
        else:
            continue
