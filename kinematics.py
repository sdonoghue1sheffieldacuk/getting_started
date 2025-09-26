r=int(input("Radius please: "))
print(f"The area of a circle of radius {r} is {3.14 * r} \nThe circumference is {2*3.14*r}")
print("we calculate the shaded area by taking one quarter of the diagram, this is an square of side 2r and area 4rr, remove from this the include circle of radius r and area pi*r. strictly speaking we now divide by 4 to get the area in our original slice but then we multiply by 4 again to account for the fact that our slice is only part of the diagram ")
print("effectively its just 4rr - pi*rr")
print(f"shaded ={(4-3.14)*r*r}")

u = int(input("Initial Velocity: "))
a = int(input("Acceleration: "))
t = int(input("Time: "))

print("V=U+AT")
v = u + a*t 
print("Final Velocity V = " + str(v))

print("S=UT+AT*T/2")
s = u*t + 0.5*a*t*t
print("Distance Traveled = " + str(s))
print(f"Distance Traveled = {s:.3f} units")