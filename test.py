T = int(input())
for test_case in range(1, T+1):
    n = int(input())

    if n > 4500:
        print(f"Case #{test_case}: Round 1")
    elif n > 1000:
        print(f"Case #{test_case}: Round 2")
    elif n > 25:
        print(f"Case #{test_case}: Round 3")
    else:
        print(f"Case #{test_case}: World Finals")