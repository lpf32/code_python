#coding = utf-8
class CircularList :
    
    def __init__( self ):
        self._tail = None

    def add( self, value ):
        newNode = _CircularListNode( value )
        if self._tail is None : #判断是否为empty linked list
            self._tail = newNode 
            newNode.next_node = self._tail
        else : #把new node 加到最后面
            newNode.next_node = self._tail.next_node #保证最后一个链接到第一个
            self._tail.next_node = newNode #新node 链接到原最后一个的后面
            self._tail = newNode

    def traversals( self ):
        curNode = self._tail
        done = curNode is None
        while not done :
            curNode = curNode.next_node
            print curNode.value
            done = curNode is self._tail

    def __contains__( self, target ):
        curNode = self._tail
        done = curNode is None
        while not done :
            curNode = curNode.next_node
            if curNode.value == target :
                return True
            else :
                done = curNode is self._tail

        return False

    def remove( self, value ) :
        curNode = self._tail
        preNode = None
        done = curNode is None
        while not done :
            preNode = curNode
            curNode = curNode.next_node
            if curNode.value == value :
                done = True
            else :
                done = curNode is self._tail

        if curNode.value != value :
            raise ValueError('the item must be in list')
        elif curNode is preNode :
            self._tail = None
        else :
            preNode.next_node = curNode.next_node


class DoublyCircularList :
    def __init__( self ):
        self._tail = None

    def add( self, value ):
        newNode = _DoublyCircularListNode(value)
        if self._tail == None :
            self._tail = newNode
            newNode.next_node = newNode
            newNode.prev_node = newNode
        else :
            newNode.next_node = self._tail.next_node
            newNode.prev_node = self._tail
            self._tail.next_node.prev_node = newNode
            self._tail.next_node = newNode
            self._tail = newNode

    def traversals( self ):
        curNode = self._tail
        done = curNode is None
        while not done :
            curNode = curNode.next_node
            print curNode.value
            done = curNode is self._tail
    
    def __contains__( self, target ):
        curNode = self._tail
        done = curNode is None
        while not done :
            curNode = curNode.next_node
            if curNode.value == target :
                return True
            else :
                done = curNode is self._tail

        return False

    def remove( self, value ):
        curNode = self._tail
        done = curNode is None
        while not done :
            curNode = curNode.next_node
            if curNode.value == value :
                done = True
            else :
                done = curNode is self._tail
        
        if curNode.value != value :
            raise ValueError('the item must be in list')
        else :
            curNode.next_node.prev_node = curNode.prev_node
            curNode.prev_node.next_node = curNode.next_node

    def reTraversals( self ):
        curNode = self._tail.next_node
        done = curNode is None
        while not done :
            curNode = curNode.prev_node
            print curNode.value
            done = curNode is self._tail.next_node
            


class _CircularListNode :
    
    def __init__( self, value ):
        self.next_node = None
        self.value = value


class _DoublyCircularListNode :
    
    def __init__( self, value ):
        self.next_node = None
        self.prev_node = None
        self.value = value
