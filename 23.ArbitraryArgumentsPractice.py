# exercise using both args and kwargs

def shipping_label(*args, **kwargs):
    for arg in args:
        print(arg, end=" ")
    print()
    # for value in kwargs.values():
    #     print(value, end=" ")

    # # changing the format of the address
    # print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    # print(f"{kwargs.get('city')} {kwargs.get('province')} {kwargs.get('zip')}")

    # using an if statement for if the address does not contain an apt number
    if "apt" in kwargs: # kwargs.get('apt') == None:
        print(f"{kwargs.get('street')} {kwargs.get('apt')}")
    elif "pobox" in kwargs:
        print(f"{kwargs.get('street')}")
        print(f"{kwargs.get('pobox')}")

    else:
        print(f"{kwargs.get('street')}")
    print(f"{kwargs.get('city')} {kwargs.get('province')} {kwargs.get('zip')}")


shipping_label("Dr.", "Shawn", "Lee", "III",
               street= "123 Fake St", city= "Calgary", province= "Alberta", zip="543210")

