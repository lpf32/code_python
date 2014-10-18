from arraypy import Array2D, Array

class Matrix :
    def __init__( self, numRows, numCols ):
        self._theGrid = Array2D( numRows, numCols )
        self._theGrid.clear(0)

    def numRows( self ):
        return self._theGrid.numRows()

    def numCols( self ):
        return self._theGrid.numCols()

    def __getitem__( self, ndxTuple ):
        return self._theGrid[ ndxTuple[0], ndxTuple[1] ]

    def __setitem__( self, ndxTuple, scalar ):
        self._theGrid[ ndxTuple[0], ndxTuple[1] ] = scalar

    def scaleBy( scalar ):
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                self[ r, c ] *= scalar

    def tranpose( self ):
        pass

    def __add__( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numRows() and \
                rhsMatrix.numCols() == self.numCols(), \
                "Matrix sizes not compatible for the add operation"

        newMatrix = Matrix( self.numRows(), self.numCols() )

        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                newMatrix[ r, c ] = self[ r, c ] + rhsMatrix[ r, c ]

        return newMatrix
    
    def __sub__( self, rhsMatrix ):
        assert rhsMatrix.numRows() == self.numRows() and \
                rhsMatrix.numCols() == self.numCols(), \
                "Matrix sizes not compatible for the add operation"

        newMatrix = Matrix( self.numRows(), self.numCols() )
        for r in range( self.numRows() ) :
            for c in range( self.numCols() ) :
                newMatrix[ r, c ] = self[ r, c ] - rhsMatrix[ r, c ]

        return newMatrix

    def __mul__( self, rhsMatrix ):
        pass

# the below is linked list matrix
class SparseMatrix :
    def __init__( self, numRows, numCols ):
        self._numCols = numCols
        self._listOfRows = Array( numRows )

    def numRows( self ):
        return len( self._listOfRows )

    def numCols( self ):
        return self._numCols
    
    # Returns the value of element (i,j): x[i,j]
    def __getitem__( self, ndxTuple ):
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
                and col >= 0 and col < self.numCols(), \
                "subscript is out of range"

        curNode = self._listOfRows[ row ]
        while curNode is not None and curNode.col != col :
            curNode = curNode.next_node

        if curNode is not None :
            return curNode.value
        else :
            return 0

    #Sets the value of element (i,j) to the scalar s: x[i,j] = s
    def __setitem__( self, ndxTuple, scalar ):
        row = ndxTuple[0]
        col = ndxTuple[1]
        assert row >= 0 and row < self.numRows() \
                and col >= 0 and col < self.numCols(), \
                "subscript is out of range"

        preNode = None
        curNode = self._listOfRows[ row ]
        while curNode is not None and curNode.col != col :
            preNode = curNode
            curNode = curNode.next_node

        if curNode is not None :
            if float( scalar ) != 0.0 :
                curNode.value = scalar
            else:
                if curNode is not self._listOfRows[ row ] :
                    preNode.next_node = curNode.next_node
                else :
                    self._listOfRows[ row ] = curNode.next_node
        else :
            if float( scalar ) != 0.0 :
                newNode = _MatrixElementNode( col, scalar )
                newNode.next_node = self._listOfRows[ row ]
                self._listOfRows[ row ] = newNode

    def scaleBy( self, scalar ):
        for row in range( self.numRows() ) :
            curNode = self._listOfRows[row]
            while curNode is not None :
                curNode.value *= scalar
                curNode = curNode.next_node


class _MatrixElementNode :
    def __init__( self, col, value ):
        self.col = col
        self.value = value
        self.next_node = None


class SparseMatrixMList :
    def __init__( self, numRows, numCols ):
        self._listOfCols = Array( numCols )
        self._listOfRows = Array( numRows )

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
                if curNode is self._listOfCols[ col ] and prevNode is None:
                    self._listOfCols[ col ] = newNode
                    if curNode is None :
                        newNode.up = self._listOfCols[ col ]
                        newNode.down = self._listOfCols[ col ]
                    else :
                        newNode.up = curNode.up
                        curNode.up.down = self._listOfCols[ col ]
                        curNode.up = self._listOfCols[ co ]
                elif prevNode is not None and curNode is self._listOfCols[ col ] :
                    newNode.down = prevNode.down
                    prevNode.down.up = newNode
                    prevNode.down = newNode
                else :
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

    def __iter__( self ):
        return self._SparseMatrixMListIterator( self._listOfRows )


    class _SparseMatrixMListNode :
        def __init__( self, row, col, value ):
            self.col = col
            self.row = row
            self.value = value
            self.down = None
            self.up = None
            self.right = None
            self.left = None


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
