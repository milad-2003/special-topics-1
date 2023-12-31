"""
کار با رشته ها

سامان تازه کار با رشته ها رو یاد گرفته. برای شروع کار با رشته ها یه سوال
نسبتا ساده پیش روی اون قرار گرفته ولی به کمک شما نیاز داره تا بتونه
انجامش بده. سامان باید برنامه ای بنویسه که یه رشته ی حرفی رو از ورودی
بخونه و تغییرات زیر رو در اون اعمال کنه

1. تمامی حروف صدا دار رو پاک کنه
2. قبل از هر حرف بی صدا یک نقطه چاپ کنه
3. تمام حروف بی صدا که باقی مانده اند را به صورت کوچک بنویسد
(حروف صدادار: aeiou)

ورودی نمونه:
aBAcAba

خروجی نمونه:
.b.c.b
"""

vowel_letters = "aeiou"
word = input("Enter a word: ").lower()
result_arr = [x for x in word if x not in vowel_letters]
if result_arr:
    print("." + ".".join(result_arr))