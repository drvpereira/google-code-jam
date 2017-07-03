for case in range(1, int(input())+1):
    result = { i for i in range(1, 17) }
    
    for _ in range(2):
        l = int(input())
        cards = [ set(map(int, input().split())) for _ in range(4) ]
        result &= cards[l-1]

    print("Case #{}: {}".format(case, next(iter(result)) if len(result) == 1 else "Volunteer cheated!" if len(result) == 0 else "Bad magician!"))
