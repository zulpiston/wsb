import re

def passcheck(haslo):

    if len(haslo) < 8:
        return "Hasło powinno zawierać conajmniej 8 znaków"
    
    if not re.search(r'\d' , haslo):
        return "Hasło musi zawierać conajmniej jedną cyfrę"
    
    if not re.search(r'[!@#$%^&*()_+{}\[\]:;<>,.?/\\-]' , haslo):
        return "Hasło musi zawierać conajmniej jeden znak specjalny"
    
    return "Hasło zostało zaakceptowane"

def main():
    haslo = input("Proszę podać hasło")
    wynik = passcheck(haslo)
    print(wynik)

if __name__ == "__main__":
    main()


