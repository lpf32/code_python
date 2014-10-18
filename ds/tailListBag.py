class Bag(object):
    
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def add(self, item):
        newNode = _BagListNode(item)
        if self._head == None :
            self._head = newNode
        else:
            self._tail.next_node = newNode
        self._tail = newNode
        self._size += 1

    def remove(self, item):
        preNode = None
        curNode = self._head

        while curNode is not None and curNode.item != item :
            preNode = curNode
            curNode = curNode.next_node

        assert curNode is not None, 'the item must be in bag'

        if curNode is self._head :
            self._head = curNode.next_node
        else:
            preNode.next_node = curNode.next_node
        if curNode is self._tail :
            self._tail = preNode
        self._size -= 1
        
        return curNode.item


    def __contains__(self, target):
        curNode = self._head

        while curNode is not None and curNode.item != target :
            curNode = curNode.next_node

        return curNode is not None

    def __len__(self):
        return self._size

    def __iter__(self):
        return _BagIterator(self._head)


class _BagListNode(object):
    
    def __init__(self, item):
        self.item = item
        self.next_node = None

class _BagIterator(object):
    
    def __init__(self, headNode):
        self._curNode = headNode

    def __iter__(self):
        return self
    
    def next(self):
        if self._curNode is None:
            raise StopIteration
        else:
            item = self._curNode.item
            self._curNode = self._curNode.next_node
            return item
