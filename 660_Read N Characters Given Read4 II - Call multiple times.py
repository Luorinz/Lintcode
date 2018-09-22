#hard


# The API: int read4(char *buf) reads 4 characters at a time from a file.

# The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.

# By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.

# Notice
# The read function may be called multiple times.

"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""


"""
The read4 API is already defined for you.
@param buf a list of characters
@return an integer
you can call Reader.read4(buf)
"""


class Solution:


    # My solution(Jiuzhang solution)
    # Using queue
    # beat 72%
    def __init__(self):
        self.buffer = [""] * 4
        self.head = 0
        self.tail = 0

    # @param {char[]} buf destination buffer
    # @param {int} n maximum number of characters to read
    # @return {int} the number of characters read
    def read(self, buf, n):
        # Write your code here
        if n== 0:
            return 0
        i = 0
        while i <n:
            if self.head == self.tail:
                self.head = 0
                self.tail = Reader.read4(self.buffer)
                if self.tail == 0:
                    break
                
            while i < n and self.head < self.tail:
               # print(i)
                buf[i] = self.buffer[self.head]
                self.head+=1
                i+=1
        return i



#another solution in python
#using built-in queue
from Queue import Queue

class Solution1(object):
    def __init__(self):
        #self.curTotal = 0
        self.buffer = Queue()
        self.endOfFile = False
    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """
        if n == 0:
            return 0
        
        total = 0
        while self.buffer.qsize() < n and not self.endOfFile:
            temp = [""] * 4
            r = read4(temp)
            if r < 4:
                self.endOfFile = True
            for i in range(r):
                self.buffer.put(temp[i])
            
        for i in range(min(self.buffer.qsize(), n)):
            buf[i] = self.buffer.get()
            total += 1
        
        return total