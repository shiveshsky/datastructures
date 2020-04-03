class Solution:
    # @param A : integer
    # @param B : list of list of integers
    # @return a list of integers
    def solve(self, A, B):
        flights = [0]*A
        for bookings in B:
            i=bookings[0]-1
            j=bookings[1]-1
            flights[i] += bookings[2]
            if j+1<len(flights):
                flights[j+1]-=bookings[2]
        prefix = []
        prefix.append(flights[0])
        for i in range(1, len(flights)):
            prefix.append(prefix[-1]+flights[i])
        return prefix
print(Solution().solve(5, [[1, 2, 10], [2, 3, 20], [2, 5, 25]]))