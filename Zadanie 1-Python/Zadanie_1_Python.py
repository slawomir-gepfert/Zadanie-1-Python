def zadanie1():
    print("Zadanie 1: Prosty kalkulator dwoch liczb")
    a = float(input("Podaj pierwsza liczbe: "))
    b = float(input("Podaj druga liczbe: "))
    op = input("Wybierz operacje (+, -, *, /): ")

    if op == "+":
        wynik = a + b
    elif op == "-":
        wynik = a - b
    elif op == "*":
        wynik = a * b
    elif op == "/":
        if b == 0:
            print("Blad: Dzielisz przez zero!")
            return
        wynik = a / b
    else:
        print("Niepoprawny wybor.")
        return

    print(f"Wynik: {wynik}")


def zadanie2():
    print("Zadanie 2: Konwerter temperatur")
    kierunek = input("Wybierz kierunek konwersji (C → F, F → C). Wpisz C lub F: ")

    if kierunek.upper() == "C":
        c = float(input("Podaj temperature w stopniach °C: "))
        f = c * 1.8 + 32
        print(f"{c}°C = {f}°F")
    elif kierunek.upper() == "F":
        f = float(input("Podaj temperature w stopniach °F: "))
        c = (f - 32) / 1.8
        print(f"{f}°F = {c}°C")
    else:
        print("Niepoprawny wybor.")


def zadanie3():
    print("Zadanie 3: Srednia ocen ucznia")
    n = int(input("Podaj liczbe ocen: "))

    suma = 0
    for i in range(n):
        ocena = float(input(f"Podaj ocene {i+1}: "))
        suma += ocena

    srednia = suma / n
    print(f"Srednia: {srednia:.2f}")

    if srednia >= 3.0:
        print("Uczen zdal.")
    else:
        print("Uczen nie zdal.")


def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Kalkulator")
        print("2 - Konwerter temperatur")
        print("3 - Srednia ocen")
        print("0 - Wyjscie")

        wybor = input("Wybierz opcje: ")

        if wybor == "1":
            zadanie1()
        elif wybor == "2":
            zadanie2()
        elif wybor == "3":
            zadanie3()
        elif wybor == "0":
            print("Koniec programu.")
            break
        else:
            print("Niepoprawny wybor.")

menu()
