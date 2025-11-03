from os import system
system("cls")

ids = [1, 2, 3, 4]
names = ["Phan", "Tang", "Seav E", "Zana"]
scores = [85, 90, 78, 92]

for i, n, s in zip(ids, names, scores):
    if s > 90:
        print(i, n, s, "Top student")
    else:
        print(i, n, s)
