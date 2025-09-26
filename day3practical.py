import test_lbrary


print(test_lbrary.quad_solver(1,28,3))

array = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]

cut = int(input("cut off"))
appended = test_lbrary.i_can_slice(array,cut,False)
print(appended)


def times_table():
    """Prints a times table to the screen"""
    #first line is just the numbers 
    topline = "x  "
    for x in range (1,11):
        topline+=f"|{x:03}" 
        #print(f"{x:02}" )
    print(topline)  
    for x in range (1,11,1):
        line = f"{x:03}"
        for y in range (1,11,1):
            line+=f"|{x*y:03}"
        print(str(line))

    

    


def range_between(frm,to):
    if frm.isdigit() and to.isdigit():
        frm = int(frm) 
        to = int(to)
        rng = range(frm,to)
        for n in rng:
            if n==8 : break
            print(n)
    else :
        print("has to be a number chief")
#range_between("6","15h")
#times_table()