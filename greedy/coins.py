'''
greedy observation:


so I have coins as


1,10, 25
100, 1000, 2500,
10000, 100000, 250000 ans so on..


now take some A = 15,
then you can solve it using 1 coin of Rs 10 and 5 coin of Rs 1


if we take A = 1500,


then you can take 1 coin of 1000 ( 10 * 100 ) and 5 coins of Rs 100 ( 1 * 100)


can we say that we have done same thing for A=15 and A=1500.
coz 1500 can be written as 15 * 100, and out coins we used are also
10100 and 1100.


so basically we can solve the problem optimally till A=100.
and then use that answers to solve bigger A.


say A = 1355454
then the answer will be sum of answers of following values
(1) (35) (54) (54)
we have already computed answer for <100 values. and this all are less than 100.


this is greedy part.


so now we want to find the min num of coins for creating value x.
using coins 1, 10 and 25 only.


we can say to make X, we need X coins of Rs 1
so that we will store in initial array dp.
for( i=0; i<100;i++) dp[i] = i;


now next we will use coin 10.


so for value X, I will say either take currnt coins
or use one coin of 10 and rest use dp[X-10].
that is
dp[X] = min ( dp[X] , 1 + dp[X - 10] )
it will give smallest possible value for X.
and we will traverse from 0 to 100. so we can say that when we are processing X, out all values from 0 to X-1 has optimal answers till now.


for example,


dp[0] = 0, and dp[10] = 10 after we process first iteration using coins of Rs1.


now as per the formula,
dp[X] = min ( dp[X] , 1 + dp[X - 10] )
it will be this:
dp[10] = min( dp[10] , 1 + dp[10 - 10]
dp[10] = min( 10, 1 ) = 1.
so we can say we will get 10 from using 1 coin of 10.


now when we are processing 20,
10 will already has value 1.
so dp[20] = 1 + dp[20 - 10] = 1 + dp[10] = 1+1 = 2.
so dp[20] = 2.


and same for loop for processing 25.


this is the solution for reference.


int Solution::solve(int A) {
long long dp[100];
for(int i = 0; i < 100; i++){
dp[i] = 1000;
}
dp[0] = 0;
for(int i = 1; i < 100; i++){
dp[i] = min(dp[i-1] + 1, dp[i]);
}
for(int i = 10; i < 100; i++){
dp[i] = min(dp[i-10] + 1, dp[i]);
}
for(int i = 25; i < 100; i++){
dp[i] = min(dp[i-25] + 1, dp[i]);
}
int ans = 0;
while(A > 0) {
ans += dp[(A % 100)];
A /= 100;
}
return ans;
}

'''


class Solution:
    def solve(self, A):
        dp = [0]*100
        for i in range(0, 100):
            dp[i]=1000
        dp[0]=0
        for i in range(1, 100):
            dp[i]=min(dp[i-1]+1, dp[i])
        for i in range(10, 100):
            dp[i]=min(dp[i-10]+1, dp[i])
        for i in range(25, 100):
            dp[i]=min(dp[i-25]+1, dp[i])
        ans = 0
        while A>0:
            ans+=dp[int(A%100)]
            A//=100
        return ans
if __name__ == '__main__':
    print(Solution().solve(69))

