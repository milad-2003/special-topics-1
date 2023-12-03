"""
فوتبال

برنامه ای بنویسید که در آن یک کلاس فوتبالیست وجود دارد که از کلاس انسان ویژگی هایی را به ارث می برد.
برنامه به اینگونه است که در ابتدا 22 شی فوتبالیست نیاز است ایجاد کنید، سپس اسامی بازیکنان زیر را به
تقسیم کنید و B و A هر شی اختصاص دهید. با استفاده از متد رندم و ارث بری، این 22 تا نام را بین دو تیم
در نهایت اسم هر بازیکن با نام تیمی که در آن قرار دارد را چاپ کنید.
اسامی بازیکنان:
hosein - mazyar - akbar - nima - mahdi - farhad - mohammad - khashayar - milad - mostafa - amin - saeed - 
pouya - pourya - reza - ali - behzad - soheil - behrooz - shahrooz - saman - mohsen
"""

import random


class Person:

    def __init__(self, name):
        self.name = name

    
    def introduce(self):
        print(f"Hello; My name is {self.name}!")


class Player(Person):

    nationality = "Iran"

    team = ""


players_list = [
    Player("hosein"),
    Player("mazyar"),
    Player("adbar"),
    Player("nima"),
    Player("mahdi"),
    Player("farhad"),
    Player("mohammad"),
    Player("khashayar"),
    Player("milad"),
    Player("mostafa"),
    Player("amin"),
    Player("saeed"),
    Player("pouya"),
    Player("pourya"),
    Player("reza"),
    Player("ali"),
    Player("behzad"),
    Player("soheil"),
    Player("behrooz"),
    Player("shahrooz"),
    Player("saman"),
    Player("mohsen"),
]

random.shuffle(players_list)

for player in players_list:
    if players_list.index(player) < len(players_list) // 2:
        player.team = "A"
    else:
        player.team = "B"
    print(f"Name: {player.name} === Team: {player.team}")
