# Zunächst soll eine Zahl in eine Binär-Zahl umgewandelt werden.
# Anschließend soll die Binär-Zahl umgekehrt werden.

zahl = 42
print("zahl: " + str(zahl))
bin = bin(zahl)[2:]
print("binär: " + bin)
bin = list(bin)

bin_list2 = []
for i in range(0, len(bin)):
    bin_list2.append(bin.pop(-1))

s = ""
for i in bin_list2:
    s += str(i)

print("binär-reverse: " + s)