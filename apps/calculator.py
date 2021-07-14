class Calculator:
    def main_calculator(self):
        print("↓Yapılacak işlemi seçiniz↓\n"
              "1.Toplama\n"
              "2.Çıkartma\n"
              "3.Bölme\n"
              "4.Çarpma\n")
        selection = (int(input("Seçim Yapınız (1/2/3/4):")))
        number1 = (int(input("1.Sayı:")))
        number2 = (int(input("2.Sayı:")))
        if selection == 1:
                total = number1 + number2
                print(number1, "+", number2, "=", total)

        elif selection == 2:
                total = number1 - number2
                print(number1, "-", number2, "=", total)

        elif selection == 3:
                total = number1 / number2
                print(number1, "/", number2, "=", total)

        elif selection == 4:
                total = number1 * number2
                print(number1, "*", number2, "=", total)
    def factorial(self):
        number = int(input("Faktariyeli Alınacak Sayıyı Giriniz:"))
        result = 1
        for Factorial in range(number):
            result *= Factorial + 1

        if number <= 0:
            print("1")
        elif number > 170:
            print("∞")
        else:
            print(result)