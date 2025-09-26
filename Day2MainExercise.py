# input tuples
t1 = (0.0,0.0,"red")
t2 = (1,1,"blue")
# sqrt[delta x squared + delta y squared ]
eucludian_distance = ((t1[0] - t2[0])*(t1[0] -t2[0]) + (t1[1] - t2[1])*(t1[1] -t2[1]  ))**0.5
print(eucludian_distance)