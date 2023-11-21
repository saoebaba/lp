import timeit


def recursive(n):
    if n <= 1:
        return n
    else:
        return recursive(n - 1) + recursive(n - 2)


def non_recursive(n):
    first = 0
    second = 1
    print(first)
    print(second)
    for i in range(2, n):
        third = first + second
        first = second
        second = third
        print(third)


start1 = timeit.default_timer()
for i in range(10):
    print(recursive(i),end=" ")
end1 = timeit.default_timer()
print(f'\nTime for recursive: {float(end1-start1)}')


start2 = timeit.default_timer()
non_recursive(10)
end2 = timeit.default_timer()
print(f'\nTime for Non-recursive: {float(end2-start2)}')

