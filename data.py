list1=[["x00","x01","x02"],
       ["x10","x11","x12"],
       ["x20","x21","x22"]]
list2=[["_","_","_"],
       ["_","_","_"],
       ["_","_","_"]]
user1_symbol=None
user2_symbol=None
def welcome_function():
    global user1_symbol
    global user2_symbol
    print("\tWelcome to the TIC_TAC_TOC game\t")
    print("\t\tthis is 3*3 game\t\t")
    print("""Game symbol is "x" or "o" """)
    user1_symbol=input("enter your game symbol:")
    print("===============================================")
    if user1_symbol=="x":
        print("""user1 symbol is "x" """)
        user2_symbol="o"
        print("""user2 symbol is "o" """)
    elif user1_symbol=="o":
        print("""user1 symbol is "o" """)
        user2_symbol="x"
        print("""user2 symbol is "x" """)
    elif user1_symbol != "x" or user1_symbol != "o":
        print("Entered symbol is invalied")
        
welcome_function()
