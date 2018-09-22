# Medium


# Suppose we abstract our file system by a string in the following manner:

# The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:

# dir
#     subdir1
#     subdir2
#         file.ext
# The directory dir contains an empty sub-directory subdir1 and a sub-directory subdir2 containing a file file.ext.

# The string

# "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
# represents:

# dir
#     subdir1
#         file1.ext
#         subsubdir1
#     subdir2
#         subsubdir2
#             file2.ext
# The directory dir contains two sub-directories subdir1 and subdir2. subdir1 contains a file file1.ext and an empty second-level sub-directory subsubdir1. subdir2 contains a second-level sub-directory subsubdir2 containing a file file2.ext.

# We are interested in finding the longest (number of characters) absolute path to a file within our file system. For example, in the second example above, the longest absolute path is "dir/subdir2/subsubdir2/file2.ext", and its length is 32 (not including the double quotes).

# Given a string representing the file system in the above format, return the length of the longest absolute path to file in the abstracted file system. If there is no file in the system, return 0.

# Example
# Give input = "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" return 20

# Notice
# The name of a file contains at least a . and an extension.
# The name of a directory or sub-directory will not contain a ..
# Time complexity required: O(n) where n is the size of the input string.
# Notice that a/aa/aaa/file1.txt is not the longest file path, if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.

class Solution:
    """
    @param input: an abstract file system
    @return: return the length of the longest absolute path to file
    """

    # My solution(Jiuzhang)
    #O(n) = n
    # beat 98%
    def lengthLongestPath(self, input):
        # write your code here
        if not input:
            return  0
        input = input.split("\n")
        sum = []
        res = 0
        level = 0
   
        for i in input:
            sum.append(0)
            #find level
            #We can use i.count("/t") here, which could be much easier
            level = i.rfind("\t")+1
            l = len(i) - level
            # print("level=",level,"l=",l)
            if '.' in i:
                res = max(sum[level -1] + l ,res)
            else:
                if level>0:
                    sum[level] = sum[level-1] + l +1
                    # print(level,sum[level])
                else:
                    sum[0] = l +1
                    # print(level,sum[level])
        return res


testcase = Solution()
print(testcase.lengthLongestPath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext"))