class Bag(object):
    
    def __init__(self):
        self._head = None
        self._size = 0

    def add(self, item):
        newNode = _BagListNode(item)
        curNode = self._head
        preNode = None
        while curNode is not None and curNode.item < item :
            preNode = curNode
            curNode = curNode.next_node

        newNode.next_node = curNode
        if curNode is self._head :
            self._head = newNode
        else:
            preNode.next_node = newNode
        self._size += 1

    def remove(self, target):
        preNode = None
        curNode = self._head

        while curNode is not None and curNode.item < target :
            if curNode.item != target :
                preNode = curNode
                curNode = curNode.next_node
            else:
                break

        if curNode.item != target :
            raise ValueError('the target must be in bag')

        assert curNode is not None, 'the target must be in bag'

        if curNode is self._head :
            self._head = curNode.next_node
        else:
            preNode.next_node = curNode.next_node

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
