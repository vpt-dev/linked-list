# Node class takes in data and has attributes data and pointer
class Node:
    def __init__(self, data):
        self.data = data
        self.pointer = None


class My_Linked_List:
    # initialising linked list
    # list takes in initial node as a parameter
    def __init__(self, startNode: Node):
        self.startNode = startNode

    # print list method
    def print_list(self):
        # set current node to start node, and print data
        self.current = self.startNode
        print(self.current.data)

       # while current node has data, print data and set current to next node
        while self.current.pointer is not None:
            print(self.current.pointer.data)
            self.current = self.current.pointer

    def add_item(self, node, node_before):
        self.node = node

        self.node.pointer = self.node_before.pointer


# main program
node1 = Node("Dagenham East")
node2 = Node("Enbankment")
node3 = Node("Harlsedon")

node1.pointer = node2
node2.pointer = node3

my_linked_list = My_Linked_List(node1)
my_linked_list.print_list()
