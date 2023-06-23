numbers = int(input())
squares = list(map(int, input().split()))

squares.sort()

result=' '.join(map(str,squares))
print(result)
