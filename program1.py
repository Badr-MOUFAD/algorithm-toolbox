import time

a, b = map(int, input("").split(" "))

start = time.time()

for i in range(10000):
    pass

print(a + b)

print(time.time() - start)
