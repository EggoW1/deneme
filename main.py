import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

harfkarakter = int(input("Sifreniz kac karakter olmali?")

parola = ""
for i in range(harfkarakter):

    karakter = random.choice(karakterler)
    parola += karakter 

print(parola)
