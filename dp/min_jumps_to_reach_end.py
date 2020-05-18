def min_jumps(arr):
    # we can apply bfs here :) same as snake and ladder's type problem ::-))
    if len(arr) <= 1:
        return 0
    if arr[0] == 0:
        return -1
    maxReach = arr[0]
    step = arr[0]
    jump = 1
    for i in range(1, len(arr)):
        if i == len(arr) - 1:
            return jump
        maxReach = max(maxReach, i + arr[i])
        step -= 1
        if step == 0:
            jump += 1
            if i >= maxReach:
                return -1
            step = maxReach - 1
    return -1


if __name__ == '__main__':
    print(min_jumps([1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]))
