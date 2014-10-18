class SparseMatrix :
    
    def __init__( self, numRows, numCols ):
        self._numRows = numRows
        self._numCols = numCols
        self._elementList = list()

    def numRows( self ):
        return self._numRows

    def numCols( self ):
        return self._numCols

    def __getitem__( self, ndxTuple ):
        if not ndxTuple[0] < self._numRows and ndxTuple[1] < self._numCols :
            raise IndexError('list index out of range')
        if not type(ndxTuple[0]) is int and type(ndxTuple[1]) is int :
            raise TypeError('list indices must be integers, not float')

        ndx = self._findPostion( ndxTuple[0], ndxTuple[1] )
        if ndx is None :
            return 0
        else :
            return self._elementList[ndx].value

    def __setitem__( self, ndxTuple, scalar ):
        ndx = self._findPostion( ndxTuple[0], ndxTuple[1] )
        if ndx is not None :
            if float( scalar ) != 0.0 :
                self._elementList[ndx].value = scalar
            else:
                self._elementList.pop( ndx )
        else:
            if float( scalar ) != 0.0 :
                element = _MatrixElement( ndxTuple[0], ndxTuple[1], scalar )
                self._elementList.append( element )

    def scaleBy( self, scalar ):
        for element in self._elementList:
            element.value *= scalar

    def __add__( self, rhsMatrix ):
        assert self._numRows == rhsMatrix._numRows and self._numCols == rhsMatrix._numCols, 'Matrix sizes not compatible for the add operation'

        newMatrix = SparseMatrix( self._numRows, self._numCols )
        
        for element in self._elementList :
            newElement = _MatrixElement( element.row, element.col, element.value )
            newMatrix._elementList.append( newMatrix )

        for element in rhsMatrix._elementList :
            value = newMatrix[ element.row, element.col ]
            value += element.value
            newMatrix[ element.row, element.col ] = value

        return newMatrix

    def _findPostion(self, row, col ):
        for i in range(len( self._elementList )) :
            if self._elementList[i].row == row and self._elementList[i].col == col :
                return i
        return None


class _MatrixElement :
    def __init__( self, row, col, value ):
        self.row = row
        self.col = col
        self.value = value

