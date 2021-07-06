from helper.guide import Guide
from model.people import People

guide = Guide()

while True:

    choice =int( input("1-Rehberi Gösterme \n2-Kişi Ekleme \n3-Kişi Silme \nSeçiminizi belirtiniz(1/2/3):"))

    if choice == 1:
        peoples = guide.person_list()
        for item in peoples:
            card = item.split(",")
            print(f'{card[0]} {card[1]}\n{card[2]}\n{card[3]}')
    elif choice == 2:
        name = input("Kişinin ismini giriniz.")
        surname = input("Kişinin soyadını giriniz.")
        email = input("Kişinin epostasını giriniz.")
        num = input("Kişinin telefon numarasını giriniz.")
        people1 = People(name, surname, email, num)
        guide.person_add(people1)
    elif choice == 3:
        num = input("Kişinin telefon numarasını giriniz:")
        guide.person_delete_by_num(num)
    else:
        print("Lütfen istenen kraterlerde işlem yapınız.")
    question = input("İşlemelere devam etmek istiyor musunuz(E/H)?").upper()
    if question == "E":
        continue
    elif question == "H":
        quit()