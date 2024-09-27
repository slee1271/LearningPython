# **kwargs = allows you to pass multiple keyword arguments

def print_address(**kwargs):
    for value in kwargs.values():
        print(value)

    for key in kwargs.keys():
        print(key)

    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_address(street="123 Fake Street",apt= "987", city="Calgary", province="Alberta", zip="T1Y 1A2")