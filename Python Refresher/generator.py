def prod(a, b):
    return a * b

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        n = output
        i += 1

my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))
