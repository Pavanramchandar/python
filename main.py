import data
import functions
import test_storage
x=y=0
while x<8:
    print("itteration no:",x)
    functions.matrix_presentation(data.list2)
    test_storage.user_input(data.user1_symbol,data.user2_symbol,data.list1)
    """
    while y<1:
        print("inner while loop is working")
        test_storage.user_input(data.user1_symbol,data.user2_symbol,data.list1)

        y+=1
    """
    if test_storage.x111=="break":
        break
    elif test_storage.same_element_u1=="true" or  test_storage.same_element_u2=="true":
        break
    x+=1
