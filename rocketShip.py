def countDown(start):
    if start == 0:
        print("Blast off! Good work!")
    else:
        print(start)
        newStart = start - 1
        countDown(newStart)

print("Don't worry, this stuff doesn't need to be hard")
countDown(10)