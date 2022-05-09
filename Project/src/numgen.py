def ordernumber():
    with open(r"Project\data\orders.txt", 'r') as file:
        x = len(file.readlines())
        print(x)

ordernumber()