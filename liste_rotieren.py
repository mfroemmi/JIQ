# Eine Liste aus Integern rotieren lassen.

rotate = 1
liste = [1, 2, 3, 4, 5, 6]
for i in range(0, rotate):
    liste = [liste[-1]] + liste[:-1]
print(liste)