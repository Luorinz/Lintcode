from random import randint

class BSTnode():
    # Node of BST
    def __init__(self, val = 0,left = None, right = None):
        self.val = val
        self.left = left
        self.right = right


class BST():
    #Binary search tree
    def __init__(self, root = None):
        self.root = root

    def add(self,node):
        #add new nodes
        if self.root == None:
            self.root = node
            return
        temp = self.root
        while temp != None:
            if node.val < temp.val:
                if temp.left == None:
                    temp.left = node
                    # print("node {} successfully added!".format(node.val))
                    return
                temp = temp.left
            elif node.val > temp.val:
                if temp.right == None:
                    temp.right = node
                    # print("node {} successfully added!".format(node.val))
                    return
                temp = temp.right
            else:
                # print("node {} already exists".format(temp.val))
                return
  
    def in_order(self,node,l):
        #generate a list of nodes from min to max
        if node == None:
            return
        self.in_order(node.left,l)
        l.append(node.val)
        self.in_order(node.right,l)
   
    def print(self):
        #print all nodes
        if not self.root:
            print("no nodes")
        l = []
        self.in_order(self.root,l)
        print(l)

class LLnode():
    #Linked list node
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class LL():
    #Linked list
    def __init__(self, root = None):
        self.root = None

    def add(self, node, from_end = True):
        #when end is False, add from start
        #when end is True, add from end.
        #The default value is True

        if not self.root:
            self.root = node
            # print("node {} successfully added".format(node.val))
            return
        if from_end:
            temp = self.root
            while temp.next:
                temp = temp.next
            temp.next = node
            # print("node {} successfully added".format(node.val))
            return
        else:
            node.next = self.root
            self.root = node
            # print("node {} successfully added".format(node.val))
            return

    def delete_val(self, num, delete_all = False):
        if not self.root:
            print("root not exists")
            return
        temp = self.root
        #It is gonna need a lot of modifications
        if temp.val == num:
            self.root = 
        while temp.next:
            if temp.next.val != num:
                temp = temp.next
            elif:
                pass
            else:
                temp.next = temp.next.next
                print("node {} successfully deleted".format(num))
                if delete_all == False:
                    return
                if not temp.next:
                    return
                if not temp.next.next:
                    break
                
        if temp.next == num:
            temp.next= None
        

    def delete_ind(self, ind, from_end):
        pass

    def print(self):
        if not self.root:
            print("no nodes")
            return
        temp = self.root
        l = []
        while temp:
            l.append(temp.val)
            temp = temp.next
        print(l)


def testBST():
    BST1  = BST()
    for i in range(10):
        node = BSTnode(i)
        BST1.add(node)
    BST1.print()

def testLL():
    LL1 = LL()
    for i in range(10):
        node = LLnode(i)
        LL1.add(node, from_end = True)
    for i in range(10):
        node = LLnode(i)
        LL1.add(node, from_end = False)
    LL1.print()
    LL1.delete_val(8, delete_all= True)
    LL1.print()

def main():
    testLL()


main()
        