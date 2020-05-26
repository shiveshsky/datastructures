def maxSubArraySum(array):
    rsum = 0
    maxsum = rsum
    for i in range(0, len(array)):
        rsum += array[i]
        if rsum <= 0:
            rsum = 0
        maxsum = max(maxsum, rsum)
    if maxsum <= 0:
        return max(array)
    else:
        return maxsum


if __name__ == '__main__':
    print(maxSubArraySum([-2, -5, -1]))
