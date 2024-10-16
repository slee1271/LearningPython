class Car:
    def __init__(self, model, year, colour, for_sale):
        self.model = model
        self.year = year
        self.colour = colour 
        self.for_sale = for_sale

# methods are functions within a class

    def drive(self):
        print(f"You are driving the {self.colour} {self.model}")

    def stop(self):
        print(f"You are stopped in the {self.colour} {self.model}")

    def describe(self):
        print(f"{self.year} {self.colour} {self.model}")