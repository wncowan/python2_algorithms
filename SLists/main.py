class SLNode(object):
    def __init__(self, value):
        self.val = value
        self.next = None

class SList(object):
    def __init__(self):
        self.head = None
        self.tail = None
    def PrintAllVals(self):
        runner = self.head
        while runner != None :
            print(runner.val)
            runner = runner.next
    def AddBack(self, node_to_add):
        runner = self.head
        while runner.next != None:
            runner = runner.next
        runner.next = node_to_add
        self.tail = node_to_add
    def AddFront(self, node_to_add):
        # head = self.head
        node_to_add.next = self.head
        self.head = node_to_add
    def InsertBefore(self, nextVal, val):
        runner = self.head
        while runner.next.val != nextVal:
            runner = runner.next
        node_to_insert = SLNode(val)
        final_next_node = runner.next
        runner.next = node_to_insert
        node_to_insert.next = final_next_node
    def InsertAfter(self, preVal, val):
        runner = self.head
        while runner.val != preVal:
            runner = runner.next
        node_to_insert = SLNode(val)
        final_next_node = runner.next
        runner.next = node_to_insert
        node_to_insert.next = final_next_node
    def RemoveNode(self, val):
        runner = self.head
        while runner.next.val != val:
            runner = runner.next
        runner.next = runner.next.next
    def ReverseList(self):
        prev_node = None
        curr_node = self.head
        next_node = curr_node.next
        while curr_node:
            curr_node.next = prev_node
            prev_node = curr_node
            curr_node = next_node
            if next_node:
                next_node = next_node.next
        self.head = prev_node



# def reverseList(list):
    
#        #Initializing values
#        prev = None
#        curr = list.head
#        nex = curr.getNextNode()
  
#        #looping
#        while curr:
#            #reversing the link
#            curr.setNextNode(prev)     

#            #moving to next node      
#            prev = curr
#            curr = nex
#            if nex:
#                nex = nex.getNextNode()

#        #initializing head
#        list.head = prev



my_list = SList()
my_list.head = SLNode('Alice')
my_list.head.next = SLNode('Chad')
my_list.head.next.next = SLNode('Debra')
evan = SLNode("Evan")
my_list.AddBack(evan)
fred = SLNode("Fred")
my_list.AddFront(fred)
my_list.InsertBefore("Debra", "Sally")
my_list.InsertAfter("Chad", "Larry")
my_list.RemoveNode("Larry")
my_list.ReverseList()




# something close to this should be utilized for all of the above problems

my_list.PrintAllVals()



