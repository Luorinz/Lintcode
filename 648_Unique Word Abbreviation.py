# medium

# An abbreviation of a word follows the form . Below are some examples of word abbreviations:

# a) it                      --> it    (no abbreviation)

#      1
# b) d|o|g                   --> d1g

#               1    1  1
#      1---5----0----5--8
# c) i|nternationalizatio|n  --> i18n

#               1
#      1---5----0
# d) l|ocalizatio|n          --> l10n
# Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

# Example
# Given dictionary = [ "deer", "door", "cake", "card" ]
# isUnique("dear") // return false
# isUnique("cart") // return true
# isUnique("cane") // return false
# isUnique("make") // return true


#My solution(Jiuzhang solution)
#Compare the word itself and its abbr appreances in each hashmap.
class ValidWordAbbr:

    def __init__(self, dictionary):
        # do intialization if necessary
        self.dictionary = dictionary
        self.old_dic = {}
        self.new_dic = {}
        for i in self.dictionary:
            if i not in self.old_dic:
                self.old_dic[i] = 1
            else:
                self.old_dic[i] +=1
            abr = self.getAbbr(i)
            if abr not in self.new_dic:
                self.new_dic[abr] = 1
            else:
                self.new_dic[abr] +=1

    def getAbbr(self,s):
        l = len(s)
        res = ""
        if l <=2:
            return s
        else:
            res = s[0]+str(l-2)+s[-1]
        return res

    """
    @param: word: a string
    @return: true if its abbreviation is unique or false
    """
    def isUnique(self, word):
        # write your code here


        new_key = self.getAbbr(word)
        if new_key not in self.new_dic:
            return True
        elif word not in self.old_dic:
            return False
        else:
            return self.new_dic[new_key] == self.old_dic[word]
# param = obj.isUnique(word)