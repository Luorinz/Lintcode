#easy

# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.

# Example
# MovingAverage m = new MovingAverage(3);
# m.next(1) = 1 // return 1.00000
# m.next(10) = (1 + 10) / 2 // return 5.50000
# m.next(3) = (1 + 10 + 3) / 3 // return 4.66667
# m.next(5) = (10 + 3 + 5) / 3 // return 6.00000

class MovingAverage:

    #My solution 
    # beat 55.25%
    # O(n) =n
    # use a linkedlist to save space complexity

    """
    @param: size: An integer
    """
    def __init__(self, size):
        # do intialization if necessary
        self.size = size
        self.currSize = 0
        self.currSum = []

    """
    @param: val: An integer
    @return:  
    """
    def next(self, val):
        # write your code here
        res = 0
        if self.currSize <self.size:
            self.currSize+=1
            if not self.currSum:
                self.currSum.append(val)
            else:
                self.currSum.append(self.currSum[-1]+val)
            res = self.currSum[-1] /self.currSize
        else:
            self.currSum.append(self.currSum[-1]+val)
            res = (self.currSum[-1]-self.currSum[0]) /self.size
            self.currSum.pop(0)

        return res
        

#Jiuzhang solution
#rotating arraylist in Java
"""
public class MovingAverage {
    /**
     * Initialize your data structure here.
     */
    int id, size;
    double[] sum;

    MovingAverage(int s) {
        id = 0;
        size = s;
        sum = new double[size + 1];
    }

    int mod(int x) {
        return x % (size + 1);
    }

    public double next(int val) {
        // Write your code here
        id++;
        sum[mod(id)] = sum[mod(id - 1)] + val;
        if (id - size >= 0) {
            return (sum[mod(id)] - sum[mod(id - size)]) / size;
        } else {
            return sum[mod(id)] / id;
        }

    }
}


"""




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param = obj.next(val)

testcase = MovingAverage(3)
print(testcase.next(9))
print(testcase.next(3))
print(testcase.next(2))
print(testcase.next(4))
print(testcase.next(8))