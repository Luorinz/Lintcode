# Medium

# Given a sorted integer array where the range of elements are in the inclusive range [lower, upper], return its missing ranges.

# Example
# Given nums = [0, 1, 3, 50, 75], lower = 0 and upper = 99
# return ["2", "4->49", "51->74", "76->99"].

class Solution:
    """
    @param: nums: a sorted integer array
    @param: lower: An integer
    @param: upper: An integer
    @return: a list of its missing ranges
    """

    #My solution 
    #O(n) = n
    #beats 68.47%

    def addRange(self,left ,right ):
        if left == right:
            return str(left)
        if left< right:
            return str(left) + "->" + str(right)    

    def findMissingRanges(self, nums, lower, upper):
        # write your code here

        ans = []
        if nums ==[]:
            ans.append(self.addRange(lower,upper))
            return ans
        
        l = len(nums)

        i = 0
        if nums[0] > lower:
            ans.append(self. addRange(lower,nums[0]-1))
        while i< l-1:
            if lower <= nums[i] <= upper :
                if nums[i] < nums[i+1]-1:
                    ans.append(self. addRange(nums[i]+1,nums[i+1]-1))
            i+=1

        if nums[-1]<upper:
            ans.append(self.addRange(nums[-1]+1,upper))        


        return ans     

    """
    Jiuzhang
    #小心输入为空
    #小心超过int范围
    Java

    public List<String> findMissingRanges(int[] nums, int lower, int upper) {
        // Write your code here
        List<String> ans = new ArrayList<>();
        if (nums == null || nums.length == 0) {
            addRange(ans, lower, upper);
            return ans;
        }

        addRange(ans, lower, (long)nums[0] - 1);

        for (int i = 1; i < nums.length; i++) {
            addRange(ans, (long)nums[i - 1] + 1, (long)nums[i] - 1);
        }
        addRange(ans, (long)nums[nums.length - 1] + 1, upper);

        return ans;
    }

    void addRange(List<String> ans, long st, long ed) {
        if (st > ed) {
            return;
        }
        if (st == ed) {
            ans.add(st + "");
            return;
        }
        ans.add(st + "->" + ed);
    }    
    """    

testcase = Solution()
print(testcase.findMissingRanges([0, 1, 3, 50, 75],0,99))
print(testcase.findMissingRanges([],1,1))