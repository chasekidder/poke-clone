import time

i = True
j = 0
while i:
    print("Hello World!")
    time.sleep(1)
    j = j + 1

    if j > 10:
        i = False