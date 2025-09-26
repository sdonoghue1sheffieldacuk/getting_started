def quad_solver (a,b,c):
    if(b*b-4*a*c) < 0 : 
        return None
    x1 = (-b + (b*b -4*a*c)) /(2*a)
    x2 = (-b - (b*b -4*a*c)) /(2*a) 
    return x1,x2

def i_can_print(list):
    items_printed = 0 
    for li in list:
        if(is_unmentionable(li%10)):
            print("XX")
        else:
            print(li)
            items_printed+=1
    return items_printed
 
def is_unmentionable(x):
    if x <=7 or x>=9 : return False
    return True

def i_can_slice(list,cutoff,odds):
    new_list = []
    startat = 0
    if(odds):
        startat = 1
    #print(startat)
    for i in range(startat,cutoff+1,2):
        new_list.append(list[i])
    items_printed = i_can_print(new_list)
    list = list + [items_printed]
    return list


def main():
    items_rem = i_can_slice([0,1,2,3,4,5,6,7,8,9,10,11],6,False)

#if __name__ =="__main__" : main()