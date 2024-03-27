def dodawanie(a, b):    
    return a + b

def odejmowanie(a, b):
    return a - b

def mnozenie(a, b):
    return a * b

def dzielenie(a, b):
    if b == 0:
        raise ValueError("Nie można dzielić przez zero!")
    return a / b

def arithmetic_operation(operation, num1, num2):
    operation_dict = {
        '+': dodawanie,
        '-': odejmowanie,
        '*': mnozenie,
        '/': dzielenie
    }

    try:
        operation_func = operation_dict[operation]
        return operation_func(num1, num2)
    except KeyError:
        print("Nieprawidłowa operacja!")
        return None
    except ValueError as e:
        print(e)
        return None

print("Witaj w kalkulatorze!\n")
print("Instrukcja: Podaj dwie liczby i operację (+, -, *, /) do wykonania.")
print("Aby zakończyć, wpisz 'koniec'.\n")

while True:
    user_input = input("Podaj dwie liczby i operację (+, -, *, /): ")

    if user_input.lower() == "koniec":
        break

    try:
        user_data = user_input.split()
        num1 = float(user_data[0])
        operation = user_data[1]
        num2 = float(user_data[2])

        result = arithmetic_operation(operation, num1, num2)

        if result is not None:
            print(f"Wynik: {result}")
    except ValueError as e:
        print(e)

print("Dziękujemy za skorzystanie z kalkulatora!")