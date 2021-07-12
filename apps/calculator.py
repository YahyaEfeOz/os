class Calculator:
    def question(self):
        print("↓Yapılacak işlemi seçiniz↓\n"
              "1.Toplama\n"
              "2.Çıkartma\n"
              "3.Bölme\n"
              "4.Çarpma\n")
        selection = (int(input("Seçim Yapınız (1/2/3/4):")))
        number1 = (int(input("1.Sayı:")))
        number2 = (int(input("2.Sayı:")))
        if selection == 1:
                toplam = number1 + number2
                print(number1, "+", number2, "=", toplam)

        elif selection == 2:
                toplam = number1 - number2
                print(number1, "-", number2, "=", toplam)

        elif selection == 3:
                toplam = number1 / number2
                print(number1, "/", number2, "=", toplam)

        elif selection == 4:
                toplam = number1 * number2
                print(number1, "*", number2, "=", toplam)
