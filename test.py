class Solution(object):
    def smallestRangeII(self, A, K):
        A.sort()
        mi, ma = A[0], A[-1]
        ans = ma - mi
        curr = 0
        for i in range(len(A) - 1):
            a, b = A[i], A[i+1]
            curr  =max(ma-K, a+K) - min(mi+K, b-K)
            ans = min(ans, curr)
        return ans

testcase = Solution()
print(testcase.smallestRangeII([1,3,6],3))