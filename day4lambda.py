def gen(point):
    return lambda x : ((point[0]-x[0])**2 + (point[1]-x[1])**2)**0.5 

l = [(1,2) , (6,6)]
print(l)
print(gen([0,0])([1,1]))
print(sorted(l,key=gen([7,7])))