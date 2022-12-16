# Pakeisti 1 ir 3 užduotis taip, kad neteisingai įvedus duomenis ar įvykus klaidoms,
# programos mestų norimas klaidas lietuvių kalba (panaudoti try/except)
sk = 0
while True:
    try:
        sk = int(input("Įveskite skaičių: "))
        break
    except ValueError:
        print("Neteisingai įvestas skaičius")

        print(sk > 0)
        print(sk <= 0)


# print(sk > 0)
# print(sk <= 0)
