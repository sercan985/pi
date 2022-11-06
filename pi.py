import math

iterate_values = [i for i in range(1,6)] + [10**i for i in range(1,6)] + [200000]

def Leibniz(run):
    x = 1
    pi = 0
    add_or_sub = 1
    for i in range(run):
        if add_or_sub: #add
            add_or_sub = 0
            pi += 4/x
        else: #sub
            add_or_sub = 1
            pi -= 4/x
        x += 2
    return pi

def Nilakantha(run):
    pi = 3
    x = 0
    add_or_sub = 1
    for i in range(run):
        x += 2
        if add_or_sub: #add
            add_or_sub = 0
            pi += 4/(x*(x+1)*(x+2))
        else: #sub
            add_or_sub = 1
            pi -= 4/(x*(x+1)*(x+2))
    return pi

for i in iterate_values:
    print(f"Leibniz pi runs={i} {Leibniz(i)}")

for i in iterate_values:
    print(f"Nilakantha pi runs={i} {Nilakantha(i)}")
