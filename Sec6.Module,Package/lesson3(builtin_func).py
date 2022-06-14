# 組込関数

ranking = {
    'A': 100,
    'B': 85,
    'C': 90
}

print(sorted(ranking))
print(sorted(ranking, key=ranking.get))
print(sorted(ranking, key=ranking.get, reverse=True))

