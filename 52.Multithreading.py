# Multithreading = used to peform multiple tasks concurrently 
# Good for I/O bound tasks like reading files or fetching data from APIs 
# threading.Thread(target=my_fucntion)

import threading
import time

def walk_dog(first_name):
    time.sleep(8)
    print(f"You finished walking {first_name}")

def take_out_trash():
    time.sleep(2)
    print("You took out the trash")

def get_mail():
    time.sleep(4)
    print("You got the mail")

# this would take 14 seconds to complete because they go in order when they should take a total of 8 seconds with multithreading
# walk_dog()
# take_out_trash()
# get_mail()

# now it takes a total of 8 seconds like multitasking
chore1 = threading.Thread(target=walk_dog, args=("Ellie",)) # comma is neccessary
chore1.start()
chore2 = threading.Thread(target=take_out_trash)
chore2.start()
chore3 = threading.Thread(target=get_mail)
chore3.start()

# without this line "All chores are complete" gets printed right away so this makes it so that all the chores finishes running then message gets printed
chore1.join()
chore2.join()
chore3.join()

print("All chores are complete")