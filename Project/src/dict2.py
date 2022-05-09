#def createorder():
keys = []
with open ("Project\data\orders.txt") as file:
    for line in file:
        line = line.strip()
        x = line.split(",")
        if len(x) == 2:
            pair = x[0], x[1]
            keys.append(pair)
print(keys)

#keys = createorder()

#y = "Order Number"
#for pair in keys:
#    if y == pair[0]:
#        print(pair[1])

#createorder()
   