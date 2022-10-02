def factorial_recursive(x):
    if x == 0:
        return 1
    return factorial_recursive(x - 1) * x

def factorial_iterative(x):
    if x == 0:
        return 1
    result = 1
    for j in range(1, x + 1):
        result *= j
    return result


if __name__ == '__main__':
    print("Recursive:")
    for i in range(10):
        print(factorial_recursive(i))

    print("Iterative:")
    for i in range(10):
        print(factorial_iterative(i))
