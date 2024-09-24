import time 

# def count(start, end):
def count(end, start=0): # (start=0, end) does not work

    for x in range(start,end+1):
        print(x)
        time.sleep(1)
    print("DONE!")

count(0,10)
count(30,15)