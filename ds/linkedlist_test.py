class listNode(object):
    def __init__(self, data):
        self.data = data
        self.next_node = None


    def setLink(self, next_node):
        self.next_node = next_node


def traversal(head):
    curNode = head
    while curNode is not None:
        print curNode.data
        curNode = curNode.next_node

def unorderedSearch(head, target):
    curNode = head
    while curNode is not None and curNode.data != target :
        curNode = curNode.next_node

    return curNode

def removeItemFromList(head, target):
    curNode = unorderedSearch(head, target)
    if curNode is None:
        raise ValueError('not find the item of %d value' %(target))
    elif curNode == head:
        head = curNode.next_node
        curNode.next_node = None
    else:
        predNode = head
        while predNode is not None and predNode.next_node != curNode:
            predNode = predNode.next_node

        predNode.next_node = curNode.next_node
        curNode.next_node = None
    return head

def main():
    head = listNode(2)
    a = listNode(5)
    b = listNode(52)
    c = listNode(80)

    head.setLink(a)
    a.setLink(b)
    b.setLink(c)
    traversal(head)

    remove_data =  2
    print('remove the item whose data is %d from list' %(remove_data))
    head = removeItemFromList(head, remove_data)
    traversal(head)
main()
