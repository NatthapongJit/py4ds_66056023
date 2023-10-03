def calculateSum(input):
    count = 0
    for i in input:
        count = count + i

    return count


def calculateProduct(input):
    count = 1
    for i in input:
        count = count * i

    return count


def average(input):
    count = 0
    for i in input:
        count += i
    return count / len(input)


def median(input):
    if not input:
        return None
    s_input = sorted(input)
    n = len(s_input)
    if n % 2 == 1:
        return s_input[n // 2]
    else:
        m1, m2 = s_input[n // 2 - 1], s_input[n // 2]
        return (m1 + m2) / 2


def mode(input):
    if not input:
        return None
    countd = {}
    for num in input:
        if num in countd:
            countd[num] += 1
        else:
            countd[num] = 1
    max_count = max(countd.values())
    modes = [num for num, count in countd.items() if count == max_count]
    return modes if modes else None


if __name__ == '__main__':
    # calculateSum
    print(calculateSum([]) == 0)
    print(calculateSum([2, 4, 6, 8, 10]) == 30)
    print(calculateSum([1, 3, 5, 7, 9]) == 25)

    # calculateProduct
    print(calculateProduct([]) == 1)
    print(calculateProduct([2, 4, 6, 8, 10]) == 3840)

    # calculateAvg
    print(average([1, 2, 3]) == 2)
    print(average([1, 2, 3, 1, 2, 3, 1, 2, 3]) == 2)
    print(average([12, 20, 37]) == 23)
    print(average([0, 0, 0, 0, 0]) == 0)

    # calculateMedian
    print(median([]) == None)
    print(median([1, 2, 3]) == 2)
    print(median([3, 7, 10, 4, 1, 9, 6, 5, 2, 8]) == 5.5)
    print(median([3, 7, 10, 4, 1, 9, 6, 2, 8]) == 6)

    # calculateMode
    print(mode([]) == None)
    print(mode([1, 2, 3, 4, 4]) == [4])
    print(mode([1, 1, 2, 3, 4]) == [1])
