def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    last_two = [0, 1]
    A = int(input())
    if A == 0:
        return 0
    elif A == 1:
        return 1
    for i in range(2, A+1):
        first = last_two[-1]
        last_two[-1] = last_two[-1] + last_two[-2]
        last_two[-2] = first
    return last_two[-1]

if __name__ == '__main__':
    print(main())