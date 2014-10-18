from sudo import *

def test_findNextBlock():
        sudo1 = [[1,2,0,0,1,0],[1,0,4,5,6,0],[3,4,0,1,2,0],[2,4,0,8,5,3],[2,0,9,7,3,0],[4,0,1,3,0,0,0]]
        ori_location = (3,2)
        new_location = findNextBlock(sudo1, ori_location)
        print new_location
        row, column = relationRowAndColumn(ori_location)
        sudo_location = [(x, y) for x in row for y in column]
        print sudo_location

def test_doSudo():
    sudo = loadSudo()
    print sudo
    doSudo(sudo, (8,1))
    print sudo

def test_loadSudo():
    sudo_list = loadSudo()
    #print sudo_list
    for sudo in sudo_list:
        print sudo


def test_getPossibleNums():
    sudo_list = loadSudo()
    sudo = sudo_list[0]
    print sudo
    nums = getPossibleNums(sudo, (2,2))
    print '(2,2)' + str(sudo[2][2])
    print nums


def test_getNextLocationWapper():
    sudo_list = loadSudo()
    sudo = sudo_list[0]
    next_location = getNextLocationWapper(sudo, (2,8))
    print next_location


def test_doSudoRec():
    sudo_list = loadSudo()
    sudo = sudo_list[3]
    doSudoRec(sudo, getNextLocationWapper(sudo, (0,0)))
    print sudo
test_doSudoRec()
