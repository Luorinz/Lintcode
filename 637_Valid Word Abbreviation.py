#Easy

# Given a non-empty string word and an abbreviation abbr, return whether the string matches with the given abbreviation.

# A string such as "word" contains only the following valid abbreviations:

# ["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
# Example
# Example 1:

# Given s = "internationalization", abbr = "i12iz4n":
# Return true.
# Example 2:

# Given s = "apple", abbr = "a2e":
# Return false.
# Notice
# Notice that only the above abbreviations are valid abbreviations of the string word. Any other string is not a valid abbreviation of word.


class Solution:
    """
    @param word: a non-empty string
    @param abbr: an abbreviation
    @return: true if string matches with the given abbr or false
    """
    def validWordAbbreviation(self, word, abbr):
        # write your code here

        #My solution
        if not word and abbr:
            return False
        elif not abbr and word:
            return False
        elif not word and not abbr:
            return True

        ind1 = 0
        ind2 = 0
        len1 = len(word)
        len2 = len(abbr)
        while ind1< len1 and ind2 < len2:
            if abbr[ind2] == '0':
                return False
            if abbr[ind2].isnumeric():
                count = 0
                while abbr[ind2].isnumeric() and ind2<len2-1:
                    ind2+=1
                    count+=1
                if abbr[ind2].isnumeric():
                    ind1+=int(abbr[ind2-count:ind2+1])
                    if ind1>len1:
                        return False
                else:
                    ind1+=int(abbr[ind2-count:ind2])
                
            elif word[ind1]!=abbr[ind2]:
                return False
            else:
                ind1+=1
                ind2+=1
        if ind1<len1-1 or ind2<len2-1:
            return False
        else:
            return True

testcase = Solution()
print(testcase.validWordAbbreviation("internationalization","i12iz4n"))