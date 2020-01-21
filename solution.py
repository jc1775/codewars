def solution(number):
    numList = []
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            numList.append(i)
    return sum(numList)