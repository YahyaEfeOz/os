number = int(input("Faktariyeli Alınacak Sayıyı Giriniz:"))
result = 1
for Factorial in range (number):
        result *= Factorial+1
 
if number <= 0:
        print("1")
elif number > 170:
        print ("∞")
else:
        print(result)
#git degisiklik deneme