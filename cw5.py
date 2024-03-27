def bmi(wysokość, masa):
    return masa / (wysokość ** 2)

def kategoria(bmi):
    if bmi < 18.5: 
        return "niedowaga"
    elif bmi < 24.9:
        return "prawidłowa masa ciała"
    elif bmi < 29.9:
        return "nadwaga"
    else:
        return "otyłość"
    
wysokość = float(input("Podaj wzrost w metrach: "))
masa = float(input("Podaj wagę w kg"))

wynik = bmi(wysokość,masa)

print(f"Twoje BMI wynosi: {bmi}")
print("Kategoria BMI:" , kategoria(bmi))
