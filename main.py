from apps.guide import Guide
from model.people import People
from apps.rock_paper_sci import RockPaperSci
from apps.calculator import Calculator

guide = Guide()
rock_paper_sci = RockPaperSci()
calculator = Calculator

while True:

        choice = int(input("1-Rehber \n"
                           "2-Oyun(Taş Kağıt Makas) \n"
                           "3-Hesap Makinesı \n"
                           "Seçiminizi belirtiniz(1/2/3):"))



        if choice == 1:
                while True:
                    choice2 = int(input("1-Rehber Gösterme \n"
                                     "2-Kişi Ekleme \n"
                                     "3-Kişi Silme \n"
                                     "Seçiminizi Belirtiniz(1/2/3):"))
                    if choice2 == 1:
                        peoples = guide.person_list()
                        for item in peoples:
                            card = item.split(",")
                            print(f'{card[0]} {card[1]}\n{card[2]}\n{card[3]}')
                    elif choice2 == 2:
                        name = input("Kişinin ismini giriniz.")
                        surname = input("Kişinin soyadını giriniz.")
                        email = input("Kişinin epostasını giriniz.")
                        num = input("Kişinin telefon numarasını giriniz.")
                        people1 = People(name, surname, email, num)
                        guide.person_add(people1)
                    elif choice2 == 3:
                        num = input("Kişinin telefon numarasını giriniz:")
                        guide.person_delete_by_num(num)
                    else:
                        print("Lütfen istenen kraterlerde işlem yapınız.")
                    choice3 = int(input("1-Rehbere Geri Dön \n"
                                        "2-Üst Menüye Dön \n"
                                        "3-Programı Kapat \n"
                                        "Seçiminizi Yapınız:"))
                    if choice3 == 1:
                        continue
                    elif choice3 == 2:
                        break
                    elif choice3 == 3:
                        quit()
                    else:
                        print("Lütfen İstenen Değerlerde Seçim Yapınız!")


        elif choice == 2:
            while True:
                result = rock_paper_sci.start_game()
                print(result)
                choice3 = int(input("1-Tekrar Oyna \n"
                                    "2-Üst Menüye Dön \n"
                                    "3-Programı Kapat \n"
                                    "Seçiminizi Yapınız:"))
                if choice3 == 1:
                    continue
                elif choice3 == 2:
                    break
                elif choice3 == 3:
                    quit()
                else:
                    print("Lütfen İstenen Değerlerde Seçim Yapınız!")

        elif choice == 3:
            while True:
                result = calculator.question
                print(result)

                choice3 = int(input("1-Hesap Makinesine Geri Dön \n"
                                    "2-Üst Menüye Dön \n"
                                    "3-Programı Kapat \n"
                                    "Seçiminizi Yapınız:"))
                if choice3 == 1:
                    continue
                elif choice3 == 2:
                    break
                elif choice3 == 3:
                    quit()
                else:
                    print("Lütfen İstenen Değerlerde Seçim Yapınız!")
