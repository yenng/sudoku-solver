import numpy

def sudoku():
    sudoku_struc = numpy.random.randint(10,size=(9,9))
    # The following data is a sudoku question.
    sudoku_struc[0] = [4,4,2,1,9,3,6,7,5]
    sudoku_struc[1] = [7,0,0,4,0,0,0,8,9]
    sudoku_struc[2] = [8,0,5,0,0,0,0,3,4]
    sudoku_struc[3] = [2,0,0,0,0,4,8,0,0]
    sudoku_struc[4] = [0,3,0,0,0,1,2,6,0]
    sudoku_struc[5] = [0,8,0,0,7,2,9,4,1]
    sudoku_struc[6] = [0,5,0,2,0,6,0,0,0]
    sudoku_struc[7] = [0,2,8,0,0,9,4,1,0]
    sudoku_struc[8] = [0,7,9,1,0,8,5,3,0]
    
    row_column_checking(sudoku_struc)
    group_checking_sudoku(sudoku_struc)
    # group, row and column are three different array that will be used for the sudoku rules.
    # The number in each line of these 3 arrays cannot repeat.
    '''
    print group
    print row
    print column
    '''
    
    display_sudoku(sudoku_struc)

def group_checking_sudoku(struc):
    groups = []
    for i in range(9):
        groups.append([])
        for row_count in range(3):
            for column_count in range(3):
                x = i/3*3 + row_count
                y = i%3*3 + column_count
                groups[i].append(struc[x][y])
    groups = numpy.asarray(groups)
    for count in range(len(groups)):
        group = groups[count]
        error = 0
        for i,num in enumerate(group):
            #print i, num
            if num:
                for j in range(8-i):
                    #print '\t', num, group[-1-j]
                    if num == group[-1-j]:
                        print 'Error occurs in group {} location {} and {}, with the value {}.'.format(count+1,i+1,9-j,num)
                        error+=1
        if error:
            print '{} error(s) occur in group {}'.format(error, count+1)
    
    
def row_column_checking(struc):
    for i in range(9):
        row_checking_sudoku(struc[i],i)
        column_checking_sudoku(numpy.transpose(struc)[i],i)
    
        
def row_checking_sudoku(group,row_num):
    error = 0
    for i,num in enumerate(group):
        #print i, num
        if num:
            for j in range(8-i):
                #print '\t', num, group[-1-j]
                if num == group[-1-j]:
                    print 'Error occurs in row {} location {} and {}, with the value {}.'.format(row_num+1,i+1,9-j,num)
                    error+=1
    if error:
        print '{} error(s) occur in row {}'.format(error, row_num+1)

def column_checking_sudoku(group,column_num):
    error = 0
    for i,num in enumerate(group):
        #print i, num
        if num:
            for j in range(8-i):
                #print '\t', num, group[-1-j]
                if num == group[-1-j]:
                    print 'Error occurs in column {} location {} and {}, with the value {}.'.format(column_num+1,i+1,9-j,num)
                    error+=1
    if error:
        print '{} error(s) occur in column {}'.format(error, column_num+1)

def display_sudoku(struc):
    row = []
    
    for x in range(9):
        string = ''
        for y in range(9):
            if y%3 == 0:
                string = string+'\t'
            string = string+' '+str(struc[x][y])
        row.append(string)
        
    for x in range(9):
        if x%3 == 0:
            print '\n'
        print row[x].replace('0','_')
sudoku()

