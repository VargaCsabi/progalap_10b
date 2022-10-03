#beolvasas
o = int(input("Ora: "))
p = int(input("Perc: "))
mp = int(input("Masodperc: "))
#feldolgozas
ido = o * 60 * 60 + p * 60 + mp
#kiiras
print("Mostani ido:", ido)