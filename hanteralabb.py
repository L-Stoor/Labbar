"""Denna fil importeras senare in till vårt huvudprogram i en annan fil"""

def lista(prompt):

    while True:
        try:
            fil = input(prompt)
            if fil != "students.txt":
                print("Den filen finns inte. Skriv in ny fil. ")
            else:
                return open("students.txt", "r")
        except FileNotFoundError:
            print("Den filen finns inte. Skriv in ny fil. ")