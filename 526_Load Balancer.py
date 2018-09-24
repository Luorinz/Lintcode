# medium

# Implement a load balancer for web servers. It provide the following functionality:

# Add a new server to the cluster => add(server_id).
# Remove a bad server from the cluster => remove(server_id).
# Pick a server in the cluster randomly with equal probability => pick().
# Example
# At beginning, the cluster is empty => {}.

# add(1)
# add(2)
# add(3)
# pick()
# >> 1         // the return value is random, it can be either 1, 2, or 3.
# pick()
# >> 2
# pick()
# >> 1
# pick()
# >> 3
# remove(1)
# pick()
# >> 2
# pick()
# >> 3
# pick()
# >> 3

from random import randint
#My solution(Jiuzhang solution)
#Use a list to make add and rand O(1)
#Use a hashset(dic) to make delete O(1)
#Don't use list.index(). It will increase the time complexity massively.
class LoadBalancer:
    def __init__(self):
        # do intialization if necessary
        self.list = []
        self.dic = {}

    """
    @param: server_id: add a new server to the cluster
    @return: nothing
    """
    def add(self, server_id):
        # write your code here
        if server_id in self.dic:
            return
        self.list.append(server_id)
        self.dic[server_id] = len(self.list) -1


    """
    @param: server_id: server_id remove a bad server from the cluster
    @return: nothing
    """
    def remove(self, server_id):
        # write your code here
        if server_id not in self.dic:
            return
        ind = self.dic[server_id]
        l = len(self.list)
        
        del self.dic[server_id]
        
        self.list[ind] = self.list[l-1]
        self.dic[self.list[ind]] = ind
        self.list.pop()

    """
    @return: pick a server in the cluster randomly with equal probability
    """
    def pick(self):
        # write your code here
        r_ind = randint(0,len(self.list)-1)
        return self.list[r_ind]