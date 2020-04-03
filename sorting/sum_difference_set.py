class Solution:
	# @param A : list of integers
	# @return an integer
	def solve(self, A):
	    sum = 0
	    A.sort()
	    for i in range(0, len(A)):
	        for j in range(i+1, len(A)):
	            sum+=(A[j]-A[i])%(1000000007)
	    return sum%1000000007
