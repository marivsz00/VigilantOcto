def kalkulator():
    print("Kalkulator")
    while True:
        try:
            num1 = float(input("Podaj pierwszą liczbę: "))
            operation = input("Wybierz operację (+, -, *, /): ").strip()
            num2 = float(input("Podaj drugą liczbę: "))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 == 0:
                    raise ZeroDivisionError
                result = num1 / num2
            else:
                print("Nieprawidłowa operacja.")
                continue

            print(f"Wynik: {result}")
            break

        except ValueError:
            print("Nieprawidłowe dane. Spróbuj jeszcze raz.")
        except ZeroDivisionError:
            print("Nie można dzielić przez zero. Spróbuj jeszcze raz.")

# Uruchomienie kalkulatora
kalkulator()

