from arraypy import Array
class DLX :
    def __init__( self, numCols, numRows=1 ):
        self._listOfCols = Array( numCols )
        self._listOfRows = Array( numRows )
        for i in range( numCols ) :
            self._listOfCols[i] = _ColumnNode()
        for i in range( numCols ) :
            if i == 0 :
                self._listOfCols[i].right = self._listOfCols[i+1]
                self._listOfCols[i].left = self._listOfCols[numCols-1]
            elif i == (numCols - 1) :
                self._listOfCols[i].right = self._listOfCols[0]
                self._listOfCols[i].left = self._listOfCols[i-1]
            else :
                self._listOfCols[i].right = self._listOfCols[i+1]
                self._listOfCols[i].left = self._listOfCols[i-1]
        self._head = _ColumnNode()
        self._head.right = self._listOfCols[0]
        self._head.left = self._listOfCols[numCols-1]
        self._listOfCols[0].left = self._head
        self._listOfCols[numCols-1].right = self._head
        self._solutions = []

    def numRows( self ):
        return len( self._listOfRows )
    
    def numCols( self ):
        return len( self._listOfCols )

    def __setitem__( self, ndxTuple, value ):
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
                and col >= 0 and col < self.numCols(), \
                "subscript is out of range"
        
        curNode = self._listOfRows[ row ]
        done = curNode is None
        while not done and curNode.col != col :
            curNode = curNode.right
            done = curNode is self._listOfRows[ row ]

        if curNode is not None and curNode.col == col :
            if float(value) != 0.0 :
                curNode.value = value
            else :
                if curNode.right == curNode or curNode.down == curNode :
                    if curNode.right == curNode :
                        self._listOfRows[ row ] = None
                    else :
                        curNode.left.right = curNode.right
                        curNode.right.left = curNode.left
                    if curNode.down == curNode :
                        self._listOfCols[ col ] = None
                    else :
                        curNode.up.down = curNode.down
                        curNode.down.up = curNode.up
                else :
                    curNode.left.right = curNode.right
                    curNode.right.left = curNode.left
                    curNode.up.down = curNode.down
                    curNode.down.up = curNode.up
        else :
            if float(value) != 0.0 :
                newNode = self._SparseMatrixMListNode( row, col, value )
                self._listOfCols[ col ].size += 1
                #把newNode 链接到row 链中
                curNode = self._listOfRows[ row ]
                prevNode = None
                done = curNode is None
                while not done and curNode.col < col :
                    prevNode = curNode
                    curNode = curNode.right
                    done = curNode is self._listOfRows[ row ]

                newNode.right = curNode
                newNode.left = prevNode
                if curNode is self._listOfRows[ row ] and prevNode is None :
                    self._listOfRows[ row ] = newNode
                    if curNode is None :
                        newNode.right = self._listOfRows[ row ]
                        newNode.left = self._listOfRows[ row ]
                    else :
                        newNode.left = curNode.left
                        curNode.left.right = self._listOfRows[ row ]
                        curNode.left = self._listOfRows[ row ]
                elif prevNode is not None and curNode is self._listOfRows[ row ] :
                    newNode.right = prevNode.right
                    prevNode.right.left = newNode
                    prevNode.right = newNode
                else :
                    prevNode.right = newNode
                    curNode.left = newNode
                
                #把newNode 链接到 col 链中
                curNode = self._listOfCols[ col ]
                prevNode = None
                done = curNode is None
                while not done and curNode.row < row :
                    prevNode = curNode
                    curNode = curNode.down
                    done = curNode is self._listOfCols[ col ]
                newNode.down = curNode
                newNode.up = prevNode
                if prevNode is not None and curNode is self._listOfCols[ col ] :
                    #print curNode
                    newNode.down = prevNode.down
                    prevNode.down.up = newNode
                    prevNode.down = newNode
                else :
                    #print curNode
                    prevNode.down = newNode
                    curNode.up = newNode
    
    def __getitem__( self, ndxTuple ):
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
                and col >= 0 and col < self.numCols(), \
                "subscript is out of range"
        
        curNode = self._listOfRows[ row ]
        done = curNode is None
        while not done and curNode.col != col :
            curNode = curNode.right
            done = curNode is self._listOfRows[ row ]

        if curNode is not None and curNode.col == col :
            return curNode.value
        else :
            return 0

    def appendRows( self, rowList ) :
        self._listOfRows = Array( len(rowList) )
        for i in range(len( rowList )) :
            for j in range(len( rowList[i] )) :
                self[i, j] = rowList[i][j]

    def search( self ):
        if self._head.right is self._head :
            return True
        else :
            resL = self._findNextColumn()
            for col in resL :
                curNode = col.down
                while curNode != col :
                    self._solutions.append(curNode)
                    rowNode = curNode
                    done = rowNode is None
                    while not done :
                        rowNode = rowNode.right
                        self._cover(rowNode)
                        done = curNode is curNode
                    self.search()
                    if self._head.right is self._head :
                        return True
                    self._un
                    curNode = curNode.down


    def _cover( self, targetNode ):
        pass

    def _uncover( self, targetNode ):
        pass

    def _findNextColumn( self ):
        L = self._sort()
        resL = []
        minValue = L[0]
        resL.append(minValue)
        j = 1
        while L[j].size == minValue :
            resL.append(l[j])
            j += 1
        return resL

    def _sort( self ):
        L = self._listOfCols.copy()
        for i in range(len(L)) :
            minIndex = i
            minValue = L[i].size
            j = i + 1
            while j < len(L) :
                if minValue > L[j].size :
                    minValue = L[j].size
                    minIndex = j
                j += 1

            temp = L[i]
            L[i] = L[minIndex]
            L[minIndex] = temp
            return L

    def __iter__( self ):
        return self._SparseMatrixMListIterator( self._listOfRows )


    class _SparseMatrixMListNode :
        def __init__( self, row, col, value ):
            self.col = col
            self.row = row
            self.value = value
            self.down = self
            self.up = self
            self.right = self
            self.left = self


    class _SparseMatrixMListIterator :
        def __init__( self, rowArray ):
            self._rowArray = rowArray
            self._curRow = -1
            self._curNode = None
            self._findNextRow()

        def __iter__( self ):
            return self

        def next( self ):
            if self._curNode is None :
                raise StopIteration
            else :
                value = self._curNode.value
                self._curNode = self._curNode.right
                if self._curNode is self._rowArray[self._curRow] :
                    self._findNextRow()
                return value

        def _findNextRow( self ):
            i = self._curRow
            i += 1
            while i < len( self._rowArray ) and self._rowArray[i] is None :
                i += 1
            self._curRow = i
            if i < len( self._rowArray ) :
                self._curNode = self._rowArray[i]
            else :
                self._curNode = None


class _ColumnNode :
    def __init__( self, name=None):
        self.row = -1
        self.col = -1
        self.right = self
        self.left = self
        self.up = self
        self.down = self
        self.name = name
        self.size = 0

class _DLXNode :
    def __init__( self, value=1 ):
        self.right = None
        self.left = None
        self.up = None
        self.down = None
        self.value = value
