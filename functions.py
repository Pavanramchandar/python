def matrix_presentation(list2):
        """
        matrix_presentation function documentation:

        this function is used to print the matrix representation of the list2 which is in data.py file 
        """
        print(" ",end=" ")
        for x1 in range(1,4):
            print(x1,end=" ")
        print(" ")
        for x in range(0,3):
            print(x+1,end=" ")
            for y in range(0,3):
                 print(list2[x][y],end=" ")
            print("")