# Schreiben Sie ein kurzes Programm, das jede Zahl von 1 bis 100 in einer neuen Zeile (oder Spalte) ausgibt.
# Für jedes Vielfache von 3, schreibe “Fizz” anstelle der Zahl.
# Für jedes Vielfache von 5, schreibe “Buzz” anstelle der Zahl.
# Für Zahlen, die ein Vielfaches von 3 und 5 sind, schreibe “FizzBuzz” statt der Zahl.

liste = []

for i in range(1,101):
    drei = i % 3
    funf = i % 5
    if drei == 0 and not funf == 0:
        liste.append("Fizz")
    elif funf == 0 and not drei == 0:
        liste.append("Buzz")
    elif funf == 0 and drei == 0:
        liste.append("FizzBuzz")
    else:
        liste.append(i)

for i in range(0,100):
    print(liste[i])