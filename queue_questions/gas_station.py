class Solution:
    def canCompleteCircuit(self, A, B):
        start = 0
        i = 0
        start_limit = 0
        petrolleft = 0
        s = len(A)
        path = [0]
        while True:
            if start >= len(A):
                return -1
            if len(path)==len(A)+1:
                return path[0]
            petrolleft += A[i]
            if petrolleft - B[i] < 0:
                start = start_limit+1
                petrolleft = 0
                path = []
                path.append((i+1)%s)

            else:
                petrolleft-=B[i]
                path.append((i+1)%s)
            i = (i+1)%s
            start_limit+=1


# A = [ 959, 329, 987, 951, 942, 410, 282, 376, 581, 507, 546, 299, 564, 114, 474, 163, 953, 481, 337, 395, 679, 21, 335, 846, 878, 961, 663, 413, 610, 937, 32, 831, 239, 899, 659, 718, 738, 7, 209 ]
# B = [ 862, 783, 134, 441, 177, 416, 329, 43, 997, 920, 289, 117, 573, 672, 574, 797, 512, 887, 571, 657, 420, 686, 411, 817, 185, 326, 891, 122, 496, 905, 910, 810, 226, 462, 759, 637, 517, 237, 884 ]
# A = [1, 2]
# B = [1, 3]
A = [ 383, 521, 491, 907, 871, 705 ]
B = [ 96, 197, 592, 67, 77, 641 ]
print(Solution().canCompleteCircuit(A, B))