class DList :
    
    def __init__( self ):
        self._head = None
        self._tail = None

    def insert( self, value ):
        newNode = _DListNode( value )
        prevNode = None
        curNode = self._head

        while curNode is not None and curNode.value < value :
            prevNode = curNode
            curNode = curNode.next_node

        newNode.prev_node = prevNode
        newNode.next_node = curNode
        if self._head is None and self._tail is None :
            self._tail = newNode
            self._head = newNode
            
        elif curNode is self._head :
            self._head = newNode
            curNode.prev_node = newNode
        
        elif prevNode is self._tail :
            self._tail = newNode
            prevNode.next_node = newNode
        else:
            prev_node.next_node = newNode
            curNode.prev_node = newNode

    def __contains__( self, value ):
        curNode = self._head
        while curNode is not None and curNode.value != value :
            curNode = curNode.next_node

        return curNode is not None

    def remove( self, value ):
        curNode = self._head
        while curNode is not None and curNode.value != value :
            curNode = curNode.next_node

        if curNode is None :
            raise ValueError('the item removed must be in list')

        if curNode is self._head :
            self._head = curNode.next_node
        elif curNode is self._tail :
            self._tail = curNode.prev_node
        else:
            curNode.prev_node.next_node = curNode.next_node
            curNode.next_node.prev_node = curNode.prev_node

        

    def revTraversal( self ):
        curNode = self._tail
        while curNode is not None :
            print curNode.value
            curNode = curNode.prev_node
    
    def traversal( self ):
        curNode = self._head
        while curNode is not None :
            print curNode.value
            curNode = curNode.next_node

class _DListNode :
    def __init__( self, value ):
        self.value = value
        self.next_node = None
        self.prev_node = None
