def num_increasing(numtup):
    sequence = []
    for num in numtup:
        if len(sequence) == 0:
            sequence.append(num)
        elif sequence[-1] >= num and len(sequence) == 1:
            sequence[0] = num
        elif sequence[-1] < num:
            sequence.append(num)
        else:
            if len(sequence) > 1:
                return sequence
    if len(sequence) > 1:
        return sequence


