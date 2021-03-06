# easy

# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 40,000.

# The order of output does not matter.

# Example
# Given s = "cbaebabacd" p = "abc"

# return [0, 6]

# The substring with start index = 0 is "cba", which is an anagram of "abc".
# The substring with start index = 6 is "bac", which is an anagram of "abc".

class Solution:
    """
    @param s: a string
    @param p: a string
    @return: a list of index
    """
    def findAnagrams(self, s, p):
        # write your code here
        if not s or not p:
            return []
        ls = len(s)
        lp = len(p)
        if ls < lp:
            return []
        cs = {}
        cp = {}
        for i in p :
            if i in cp:
                cp[i] +=1
            else:
                cp[i] = 1

        for i in range(lp):
            if s[i] in cs:
                cs[s[i]] +=1
            else:
                cs[s[i]] = 1
                
        res = []
        if cs == cp:
            res.append(0)
        

        k = 1
        while k+lp <= ls:
            if cs[s[k-1]] <= 1 :
                cs.pop(s[k-1])
            else:
                cs[s[k-1]] -= 1

            if s[k+lp - 1] in cs:
                cs[s[k+lp -1]] +=1
            else:
                cs[s[k+lp - 1]] = 1
            # print(cs,cp)
            if cs == cp:
                res.append(k)
            k+=1

        return res

testcase = Solution()
print(testcase.findAnagrams("babababababababababababab",
"aba"))


"""
//version 高频题班
public class Solution {

    public List<Integer> findAnagrams(String s, String p) {
        // Write your code here
        List<Integer> ans = new ArrayList<>();
        if (s.length() < p.length()) {
            return ans;
        }
        char[] sc = s.toCharArray();
        char[] pc = p.toCharArray();

        int[] det = new int[256];

        for (int i = 0; i < p.length(); i++) {
            det[pc[i]]--;
            det[sc[i]]++;
        }

        int absSum = 0;
        for (int item : det) {
            absSum += Math.abs(item);
        }
        if (absSum == 0) {
            ans.add(0);
        }

        for (int i = p.length(); i < s.length(); i++) {
            int r = sc[i];
            int l = sc[i - p.length()];
            absSum = absSum - Math.abs(det[r]) - Math.abs(det[l]);

            det[r]++;
            det[l]--;

            absSum = absSum + Math.abs(det[r]) + Math.abs(det[l]);
            if (absSum == 0) {
                ans.add(i - p.length() + 1);
            }
        }
        return ans;
    }
}


"""