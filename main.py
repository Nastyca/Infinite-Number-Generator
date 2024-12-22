chiffres = 0
with open("chiffres.txt", "a") as f:
    while True:
        chiffres += 1
        print(chiffres)
        f.write(str(f"{chiffres}\n"))

input()
