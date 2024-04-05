import random

link = 'https://discord.gift/'
chars = '+-abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
number = input('количество ссылок?'+ "\n")
length = input('длина ссылок? (24 стандарт)'+ "\n")
number = int(number)
length = int(length)
for n in range(number):
    password =''
    for i in range(length):
        password += random.choice(chars)
    print( link + password)
    