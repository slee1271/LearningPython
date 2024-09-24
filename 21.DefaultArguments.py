# default arguments = a default name for certain parameters. default is used when that argument is omitted which makes your functions more flexible, reduced # of arguments

# most of the time people dont have discount and tax is usually 5%
def net_price(list_price, discount=0, tax=0.05): # discount will normally be 0 and tax will normally be 5%
    return list_price * (1 - discount) * (1 + tax)

print(net_price(500, 0, 0.05))
print(net_price(500))
print(net_price(500,0.1))
print(net_price(500,0.1,0))


