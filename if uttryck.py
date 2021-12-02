fortnite = print("Gör en fortnite dans")

svar = input("vill du göra en fortnite dans? ")

if svar == "okej": 
    print("Du gör en fortnite dans! Wow du är så cool!")

if svar == "nej":
    print("Du sket nyss på dig! hahahahaha!")


t = float(input("temp? "))
if t < 18:
    print("Det är kallt")
    print("Sätt på värmen")
print(f"Det är {t} grader")

if t > 27:
    print("det är för vamt")
p = input("vill du sänka värmen? ")

g = input("vill du sätta på värmen? ")
if g == "ja":
    print("Du satt på värmet, du klara dig!")
    exit()

if g == "nej":
    print("Du dog! Dödsorsak: Frös ihjäl.")
    exit()

if t > 18.0 and t < 26.0:
    print("det är lagomt varmt")
    exit()


if p == "ja":
    print("Du sänkte värmen, nu blev det skönare")
    exit()

if p == "nej":
    print("Du dog! Dödsorsak: Värmeslag.")
    exit()


