#coding:utf-8
from datetime import datetime
FILE_NAME = 'sudo.txt'
'''数独算法'''

def loadSudo():
    '''
    load sudo from sudo.txt file
    return: the list of sudo
    '''
    sudo_list = []
    sudo = []
    try:
        inFile = open(FILE_NAME, 'r')
    except IOError:
        raise IOError
    else:
        for line in inFile:
            if line[0] != '-':
                sudo.append(map(int, line.split()))
            else:
                sudo_list.append(sudo)
                sudo = []
        if sudo != []:
            sudo_list.append(sudo)
    
    return sudo_list


def findBlock(sudo):
    '''find the block's location which is not complete'''
    j = None
    for i in range(len(sudo)):
        if 0 in sudo[i]:
            j = sudo[i].index(0)
            return (i, j)
    return None


def isComplete(sudo):
    '''return: Ture if sudo is completed otherwise False'''
    isOk = True
    for i in range(len(sudo)):
        if 0 in sudo[i]:
            isOk = False
    return isOk


def relationRowAndColumn(location):
    '''the block of the location'''
    '''坐标所在数独块所对应row 和 column 的值'''
    i, j = location
    row, column = 0, 0
    group = [(0,1,2),(3,4,5),(6,7,8)]
    for value in group:
        if i in value:
            row = value
        if j in value:
            column = value
    return (row, column)


def findNextBlock(sudo, location, notLocation = None):
    '''寻找下个有关联的数独块'''
    row, column = relationRowAndColumn(location)
    y = None
    for x in row:
        try:
            y = sudo[x].index(0, 0, column[0])
        except:
            pass
        else:
            if y != None and (x, y) != notLocation:
                return (x, y)
        try:
            y = sudo[x].index(0, column[2]+1, len(sudo[0]))
        except:
            pass
        else:
            if y != None and (x, y) != notLocation:
                return (x, y)

    for y in column:
        for x in range(0, row[0]):
            if sudo[x][y] == 0 and (x, y) != notLocation:
                return (x, y)
        for x in range(row[2], len(sudo)):
            if sudo[x][y] == 0 and (x, y) != notLocation:
                return (x, y)

    return None


def doSudo(sudo, location):
    '''解决坐标所在的数度块'''
    change = False
    row, column = relationRowAndColumn(location)
    sudo_block =[(x,y) for x in row for y in column]
    num_need = [x for x in range(1, 10)]
    for x in row:
        for y in column:
            if sudo[x][y] != 0:
                #print sudo[x][y]
                num_need.remove(sudo[x][y])
                sudo_block.remove((x, y))

    for num in num_need:
        sudo_block_cp = sudo_block[:]
        for r in row:
            if num in sudo[r]:
                #print num
                #print r
                #print sudo_block_cp
                for loc in sudo_block:
                    #print loc
                    #print loc[0] == 6
                    if loc[0] == r:
                        sudo_block_cp.remove(loc)
        for c in column:
            for r in range(len(sudo)):
                if sudo[r][c] == num:
                    for loc in sudo_block_cp[:]:
                        if loc[1] == c:
                            sudo_block_cp.remove(loc)

        if len(sudo_block_cp) == 1:
            location = sudo_block_cp[0]
            sudo[location[0]][location[1]] = num
            sudo_block.remove(location)
            change = True
            #print location
            #print sudo
            
       # if num == 7:
            #print sudo_block
            #print sudo_block_cp
           # print
    return change

def getPossibleNums(sudo, location):
    num_need = [x for x in range(1,10)]
    row, column = relationRowAndColumn(location)
    sudo_block = [(x,y) for x in row for y in column]
    for i in row:
        for j in column:
            if sudo[i][j] in num_need:
                num_need.remove(sudo[i][j])

    for i in sudo[location[0]]:
        if i in num_need:
            num_need.remove(i)

    for i in range(len(sudo)):
        if sudo[i][location[1]] in num_need:
            num_need.remove(sudo[i][location[1]])
    
    return num_need


def getNextLocation(location):
    next_location = location
    row, column = relationRowAndColumn(location)
    for i in column:
        if i == location[1]:
            if i < column[2]:
                next_location = (location[0], location[1] + 1)
                return next_location
            else:
                for j in row:
                    if j == location[0]:
                        if j < row[2]:
                            next_location = (location[0] + 1, column[0])
                            return next_location
                        else:
                            if column[2] < 8:
                                next_location = (row[0], column[2] + 1)
                                return next_location
                            else:
                                next_location = (row[2] + 1, 0)
                                return next_location


def getNextLocationWapper(sudo, location):
    if sudo[location[0]][location[1]] == 0:
        return location
    else:
        location = getNextLocation(location)
    while sudo[location[0]][location[1]] != 0:
        location = getNextLocation(location)

    return location


def doSudoRec(sudo, location):
    '''暴力破解'''
    if isComplete(sudo):
        print sudo
        return True
    else:
        index = 0
        num = getPossibleNums(sudo, location)
        if num == []:
            #print 'Location:' + str(location) + ':' + str(0),
            #print 'possibleNums:' + str(num)
            return False
        else:
            sudo[location[0]][location[1]] = num[index]
            #print 'Location:' + str(location) + ':' + str(num[index]),
            #print 'possibleNums:' + str(num)
        if isComplete(sudo):
            return True
        while not doSudoRec(sudo, getNextLocationWapper(sudo, location)):
            if isComplete(sudo):
                return True
            index += 1
            if index >= len(num):
                #print 'Location:' + str(location) + ':' + str(0),
                #print 'possibleNums:' + str(num)
                sudo[location[0]][location[1]] = 0
                return False
            else:
                sudo[location[0]][location[1]] = num[index]
                #print 'Location:' + str(location) + ':' + str(num[index]),
                #print 'possibleNums:' + str(num)

            if isComplete(sudo):
                return True


def main():
    sudo_list = loadSudo()
    #print sudo_list
    for sudo in sudo_list:
        now = datetime.now()
        while not isComplete(sudo):
            changed = False
            for x in range(0,9,3):
                for y in range(0,9,3):
                    changed = doSudo(sudo, (x, y))
            if not changed:
                break
        if not isComplete(sudo):
            doSudoRec(sudo,getNextLocationWapper(sudo, (0,0)))
        print sudo
        print datetime.now() - now

        
def main2():
    now = datetime.now()
    sudo = loadSudo()
    location = None
    for x in range(0,9,3):
        for y in range(0,9,3):
            if doSudo(sudo, (x, y)) == True:
                location = (x, y)
        else:
            continue
        break

    next_location = None
    while not isComplete(sudo):
        next_location = findNextBlock(sudo, location, next_location)
        isChanged = doSudo(sudo, next_location)
        if isChanged:
            location = next_location
    print sudo


if __name__ == "__main__":
    main()
