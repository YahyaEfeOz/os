class Guide:
    def person_list(self):
        with open("./data/guide.txt", "r") as file:
            peoples = file.readlines()
            file.close()
            return peoples

    def person_add(self, People):
        #dosya adından sonra izin tanımlaması yapılıyor. w -> write
        with open("./data/guide.txt","a") as file:
            file.write("{},{},{},{}\n".format(People.name, People.surname, People.email, People.num))
            print("Başarıyla Kaydedilmiştir!")
            file.close()

    def person_delete_by_num(self, num):
        peoples = []
        with open("./data/guide.txt", "r") as file:
            peoples = file.readlines()
            print("Kişi Başarıyla Silinmiştir")
            file.close()
        for people in peoples:
            if(people.replace('\n', '').split(",")[-1] == num):
                del peoples[peoples.index(people)]
        with open("./data/guide.txt", "w") as file:
            file.writelines(peoples)
            file.close()




