import numpy

def sudoku():
    sudoku_struc = numpy.random.randint(10,size=(9,9))
    display_sudoku(sudoku_struc)
    

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
        print row[x]
sudoku()
