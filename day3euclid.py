def HCF(first,second):
    x = first
    y = second
    print(f"first{first}, second{second}")
    if x<y : x ,y = y,x # force the larger of the pair to be x and the other to be y
    print(f"largest{x},smallest{y}")
    
    r =1 
    while r>0:
        r = x%y # set r as remainder of x/y 
        x,y = y,r 
    
    return x 

def main():
    hcf = HCF(35,42)
    print(hcf)

#if __name__ == "__main__" : main()