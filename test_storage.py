import data
import functions
#from old function module
def user1_check(list1):
   if list1[0][0]==list1[0][1]==list1[0][2]:
       """
       this if statement is true if the matrix matches to like this:
       1 1 1
       - - -
       - - -


       """
       return "winner_user1"

   elif list1[1][0]==list1[1][1]==list1[1][2]:
       """
       this if statement is true if the matrix matches to like this:
        - - -
        1 1 1
        - - -


       """
       return "winner_user1"
   elif list1[2][0]==list1[2][1]==list1[2][0]:
       """
       this if statement is true if the matrix matches to like this:
       - - -
       - - -
       1 1 1


       """
       return "winner_user1"
   elif list1[0][1]==list1[1][1]==list1[2][1]:
       """
       this if statement is true if the matrix matches to like this:
       - 1 -
       - 1 -
       - 1 -


       """
       return "winner_user1"
   elif list1[0][2]==list1[1][2]==list1[2][2]:
       """
       this if statement is true if the matrix matches to like this:
       - - 1
       - - 1
       - - 1


       """
       return "winner_user1"
   elif list1[0][0]==list1[1][0]==list1[2][0]:
       """
       this if statement is true if the matrix matches to like this:
       1 - -
       1 - -
       1 - -


       """
       return "winner_user1"
   elif list1[0][0]==list1[1][1]==list1[2][2]:
       """
       this if statement is true if the matrix matches to like this:
       1 - -
       - 1 -
       - - 1


       """
       return "winner_user1"
   elif list1[0][2]==list1[1][1]==list1[2][0]:
       """
       this if statement is true if the matrix matches to like this:
       - - 1
       - 1 -
       1 - -


       """
       return "winner_user1"
   else:
       return "decision_pending"

#
def user2_check(list1):
   if list1[0][0]==list1[0][1]==list1[0][2]:
       """
       this if statement is true if the matrix matches to like this:
       1 1 1
       - - -
       - - -


       """
       return "winner_user1"

   elif list1[1][0]==list1[1][1]==list1[1][2]:
       """
       this if statement is true if the matrix matches to like this:
        - - -
        1 1 1
        - - -


       """
       return "winner_user2"
   elif list1[2][0]==list1[2][1]==list1[2][0]:
       """
       this if statement is true if the matrix matches to like this:
       - - -
       - - -
       1 1 1


       """
       return "winner_user2"
   elif list1[0][1]==list1[1][1]==list1[2][1]:
       """
       this if statement is true if the matrix matches to like this:
       - 1 -
       - 1 -
       - 1 -


       """
       return "winner_user2"
   elif list1[0][2]==list1[1][2]==list1[2][2]:
       """
       this if statement is true if the matrix matches to like this:
       - - 1
       - - 1
       - - 1


       """
       return "winner_user2"
   elif list1[0][0]==list1[1][0]==list1[2][0]:
       """
       this if statement is true if the matrix matches to like this:
       1 - -
       1 - -
       1 - -


       """
       return "winner_user2"
   elif list1[0][0]==list1[1][1]==list1[2][2]:
       """
       this if statement is true if the matrix matches to like this:
       1 - -
       - 1 -
       - - 1


       """
       return "winner_user2"
   elif list1[0][2]==list1[1][1]==list1[2][0]:
       """
       this if statement is true if the matrix matches to like this:
       - - 1
       - 1 -
       1 - -


       """
       return "winner_user2"
   else:
       return "decision_pending"
"""
x=user1_check(data.list1)
y=user2_check(data.list1)
print("x=",x)
print("y=",y)
"""
#this is the old point of function module
same_element_u1=None
same_element_u2=None
def user1_input(user1_symbol,list1):
    """
    documentation about user2_input function:

    This function is used to take the input from the user2
    """
    if user1_symbol=="x":
        print("user1 input")
        x=int(input("Enter the location of x_axis:"))
        y=int(input("Enter the location of y_axis:"))
        if data.list1[x-1][y-1]=="x" or data.list1[x-1][y-1]=="o":
            global same_element_u1  
            same_element_u1="true"
            print("This game is ended due to same element entry-u11")
            return "true"
        global before_change
        before_change=data.list1[x-1][y-1]
        data.list1[x-1][y-1]="x"
        data.list2[x-1][y-1]="x"

    elif  user1_symbol=="o":
        print("user1 input")
        x=int(input("Enter the location of x_axis:"))
        y=int(input("Enter the location of y_axis:"))
        if data.list1[x-1][y-1]=="x" or data.list1[x-1][y-1]=="o":
            same_element_u1="true"
            print("This game is ended due to same element entry-u12")
            return "true"
        before_change=data.list1[x-1][y-1]
        data.list1[x-1][y-1]="o"
        data.list2[x-1][y-1]="o"

def user2_input(user2_symbol,list2):
    """
    documentation about user2_input function:

    This function is used to take the input from the user2
    """
    if user2_symbol=="x":
        print("user2 input")
        x=int(input("Enter the location of x_axis:"))
        y=int(input("Enter the location of y_axis:"))
        global same_element_u2
        if data.list1[x-1][y-1]=="x" or data.list1[x-1][y-1]=="o":
            same_element_u2="true"
            print("This game is ended due to same element entry-u21")
            return "true"
        global before_change
        before_change=data.list1[x-1][y-1]
        data.list1[x-1][y-1]="x"
        data.list2[x-1][y-1]="x"

    elif  user2_symbol=="o":
        print("user2 input")
        x=int(input("Enter the location of x_axis:"))
        y=int(input("Enter the location of y_axis:"))
        if data.list1[x-1][y-1]=="x" or data.list1[x-1][y-1]=="o":
            same_element_u2="true"
            print("This game is ended due to same element entry-22")
            return "true"
        before_change=data.list1[x-1][y-1]
        data.list1[x-1][y-1]="o"
        data.list2[x-1][y-1]="o"
def user_input(user1_symbol,user2_symbol,list1):
    global x111
    global same_element_u1
    global same_element_u2
    same_element=None
    x111=None
    user1_input(user1_symbol,list1)
    x=user1_check(data.list1)
    
    #y=user1_input(user1_symbol,data.list1)
    #print("x value in input_check_statement",x)
    #print("x=",x)
    if same_element_u1=="true":
            print("the game has been ended because user1 has entered element is already entered location")
            same_element_u1="true"
    elif x=="winner_user1":
        print("====================================================")
        print("winner is user1")
        #print("This loop is breaked by user_input")
        x111= "break"
    
    functions.matrix_presentation(data.list2)
    user2_input(user2_symbol,list1)
    y=user2_check(data.list1)
    #print("y=",y)
    if same_element_u2=="true":
        print("the game has been ended because user2 has entered element is already entered location")
        same_element_u2="true"
    elif y=="winner_user2":
        print("====================================================")
        print("winner is user2")
        #print("This loop is breaked by user_input")
        x111= "break"
    
    

