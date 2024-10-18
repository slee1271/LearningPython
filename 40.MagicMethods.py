# Magin methods = dunder methods __init__, __str__, __eq__. They are automatically called by Python's built-in Operations
# allow developers to define or customize the behaviour of objects 

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self,other):
        return self.num_pages < other.num_pages
    
    def __gt__(self,other):
        return self.num_pages > other.num_pages
    
    def __add__(self,other):
        return self.num_pages + other.num_pages
    
    def __contains__(self, keyword):
        return keyword in self.author
    
    def __getitem__(self, key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key '{key}' was not found"
        


book1 = Book("The Hobbit", "JRR Tolkien", 310)
book2 = Book("Harry Potter", "JK Rowling", 223)
book3 = Book("Harry Potter", "JK Rowling", 300)


print(book1) # without __str__ it gives memory address
print(book2 == book3) # gives false even tho they the same. Use __str__
print(book2 < book3) # gives error unless __lt__ which stands for less than
print(book2 > book3) 
print(book2 + book3) # error unless __add__
print("JRR" in book1) # error unless __contains__
print(book1['title'])
print(book2['author'])
print(book3['num_pages'])
print(book3['audio'])