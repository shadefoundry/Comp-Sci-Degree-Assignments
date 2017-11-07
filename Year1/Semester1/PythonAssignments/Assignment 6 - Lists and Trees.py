__author__ = 'link491'
#Assignment 6 - Lists and Trees
#Kevin Lopez

#---------------------------------------------------------------------------------------------------------------------#
class BinaryTreeNode:
    def __init__(self, value, left = None, right = None):
        self.value = value
        self.left = left
        self.right = right
class BinarySearchTree:
    def __init__(self):
        self.root = None
    # returns True if 'needle' exists in the true; and False otherwise
    def search(self, needle):
        return bst_search(self.root, needle)
    def insert(self, new_value):
        self.root = bst_insert(self.root, new_value)
#---------------------------------------------------------------------------------------------------------------------#
class LinkedListNode:
    def __init__(self, data, next = None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def append(self, new_value):
        if self.head is None:
            self.head = LinkedListNode(new_value)
        else:
            # 1. find the current last node
            node = self.head        # start at the head node
            while node.next != None:
                node = node.next        # advance to the next node
            # 2. construct a new node and reference that from the previous last node
            node.next = LinkedListNode(new_value)
    def print_list(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next
    # calculates and returns (as an int) how many elements are in this list
    def length(self):
        node = self.head
        l = 0
        while node != None:
            l += 1
            node = node.next
        return l
    def remove(self, position):
        if position > 0:
            node = self.head
            l = 0
            while l != position - 1:    # we want a reference to the node BEFORE the node that's going to get deleted
                l += 1
                node = node.next
            node.next = node.next.next  # bypass the 'node.next' node (the node to be deleted)
        elif position == 0:
            self.head = self.head.next
#---------------------------------------------------------------------------------------------------------------------#
    #goes through the linked list and searches for the given value.
    #This is the only function in this part of the code that I actually did myself,
    #literally everything else is taken directly from the examples.
    def ll_search(self, data):
        node = self.head
        found=False
        while node and found is False:
            if node.data==data:
                found=True
                return True
            else:
                node=node.next
        if node is None:
            return False
        return node
#---------------------------------------------------------------------------------------------------------------------#
# returns True if 'node' contains 'needle' in any of its descendants
def bst_search(node, needle):
    if node is None:
        return False
    elif node.value == needle:
        return True
    elif needle < node.value:
        return bst_search(node.left, needle)
    elif needle > node.value:
        return bst_search(node.right, needle)
# adds a new node into an existing tree
# returns a reference to the root if this (sub)tree
def bst_insert(node, new_value):
    if node is None:
        return BinaryTreeNode(new_value)
    elif new_value < node.value:
        node.left = bst_insert(node.left, new_value)
        return node
    elif new_value > node.value:
        node.right = bst_insert(node.right, new_value)
        return node
# remove the value v from the (sub)tree rooted at 'node'
# returns a reference to the new root of this (sub)tree
def bst_remove(node, v):
    if node is None:
        return None # do nothing
    elif v < node.value:
        node.left = bst_remove(node.left, v)
        return node
    elif v > node.value:
        node.right = bst_remove(node.right, v)
        return node
    # if the node we want to remove has no children, we just return None and
    # forget about it
    elif v == node.value and node.left == None and node.right == None:
        return None
    # if we have a left child, but no right child, replace ourselves with our left child
    elif v == node.value and node.right == None:
        return node.left
    elif v == node.value and node.left == None:
        return node.right
    else:   # we have 2 children :(
        our_replacement = node.right    # go right first, then go left as far as we can
        while our_replacement.left != None:
            our_replacement = our_replacement.left
        # first, we copy our replacement's value over our own
        node.value = our_replacement.value
        # next, remove our replacement from our lineage
        node.right = bst_remove(node.right, our_replacement.value)
        return node
#---------------------------------------------------------------------------------------------------------------------#
#Define the three different list objects. They're empty right now.
List=[]
BinaryList=BinarySearchTree()
Linked_List=LinkedList()

def Captain_Morgans_Revenge_Binary(filename,searchtext):
    #open the portal
    f=open(filename,'r')
    #go through each line
    for line in f:
        #if there's a + we human centipede the value onto the list. We're using Dank Sorcery to do this.
        if line[0][0]=='+':
            line=line[1:]
            List.append(line.strip())
        #if there's a - though...
        elif line[0][0]=='-':
            line=line[1:]
            #and if the value's already in the list...
            if line in List:
                #extripate that shit
                List.remove(line)
    #close the portal
    f.close()
    for j in List:
        BinaryList.insert(j)
    print(BinaryList.search(searchtext))

def The_Shrekening_Linked(filename,searchtext):
    #open the portal
    f=open(filename,'r')
    #go through each line
    for line in f:
        #if theres a +, we add that shit to the list. We call upon Dank Sorcery to remove the + or - from the strings
        if line[0][0]=='+':
            line=line[1:]
            List.append(line.strip())
        #if there's a - though...
        elif line[0][0]=='-':
            line=line[1:]
            #and if the value is already in the list
            if line in List:
                #we extripate that shit
                List.remove(line)
    #close the portal
    f.close()
    #siphon the information from the list we just created and shoehorn it into a linked list format
    for i in List:
        Linked_List.append(i)
    #finally we display if the string we're searching for is in the bloody list (hint: it probably isn't)
    print(Linked_List.ll_search(filename))
#---------------------------------------------All Hail the Dank Sorcerers---------------------------------------------#
#                                                       ____                                                          #
#                                                     .'* *.'                                                         #
#                                                  __/_*_*(_                                                          #
#                                                 / _______ \                                                         #
#                                                _\_)/___\(_/_                                                        #
#                                               / _((\- -/))_ \                                                       #
#                                               \ \())(-)(()/ /                                                       #
#                                                ' \(((()))/ '                                                        #
#                                               / ' \)).))/ ' \                                                       #
#                                              / _ \ - | - /_  \                                                      #
#                                             (   ( .;''';. .'  )                                                     #
#                                             _\"__ /    )\ __"/_                                                     #
#                                               \/  \   ' /  \/                                                       #
#                                                .'  '...' ' )                                                        #
#                                                 / /  |  \ \                                                         #
#                                                / .   .   . \                                                        #
#                                               /   .     .   \                                                       #
#                                              /   /   |   \   \                                                      #
#                                            .'   /    b    '.  '.                                                    #
#                                        _.-'    /     Bb     '-. '-._                                                #
#                                    _.-'       |      BBb       '-.  '-.                                             #
#                                   (________mrf\____.dBBBb.________)____)                                            #
#                                                                                                                     #
#---------------------------------------------------------------------------------------------------------------------#