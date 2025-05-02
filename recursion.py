def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def compareTo(s1, s2):
    if not s1 and not s2:  
        return 0
    elif not s1:  
        return -ord(s2[0])
    elif not s2:  
        return ord(s1[0])
    elif s1[0] != s2[0]:  
        return ord(s1[0]) - ord(s2[0])
    else: 
        return compareTo(s1[1:], s2[1:])


if __name__ == "__main__":
    print("Testing Fibonacci:")
    for n in [0, 1, 5, 10, 15]:
        print(f"fibonacci({n}) = {fibonacci(n)}")

    print("\nTesting GCD:")
    pairs = [(64, 48), (270, 192), (81, 27), (37, 600), (1, 5)]
    for a, b in pairs:
        print(f"gcd({a}, {b}) = {gcd(a, b)}")

    print("\nTesting compareTo:")
    test_cases = [
        ("hello", "world"),
        ("world", "hello"),
        ("abc", "abcd"),
        ("abcd", "abc"),
        ("same", "same"),
        ("", ""),
        ("a", ""),
        ("", "z"),
    ]
    for s1, s2 in test_cases:
        print(f'compareTo("{s1}", "{s2}") = {compareTo(s1, s2)}')
