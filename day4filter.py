list_of_names = [["Alvin",25],["Simon",17],["ted",9],["esme",7]]
me = ["boris",22]
list_of_names.insert(0,me)
print(list_of_names)
list_of_names[0][1] +=1
print(list_of_names)

def age(tuple):
    return tuple[1]

def name(tuple):
    return tuple[0]

def over18(tuple):
    return (age(tuple)>=18)

by_age = sorted(list_of_names,key=age)
by_name = sorted(list_of_names,key=name)
overage = filter(over18,list_of_names)

print(by_age)
print(by_name)
for o in overage:
    print(o)

print(sorted(list_of_names,key=over18))

print(sorted(list_of_names, key= lambda x:x[0]))
print(sorted(list_of_names, key= lambda x:x[1]))
print(sorted(list_of_names, key= lambda x:x[1]>18))

def contains_o(tuple):
    return "o" in tuple[0]

o_list =(filter(contains_o,list_of_names))

for o_name in o_list: 
    print (o_name)

#x for x in fruits if "" in x
thing = [name for name in list_of_names if name[1]>18 ]
print(thing) 
