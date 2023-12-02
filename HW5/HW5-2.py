"""
مترجم آنلاین

آرتادخت برای پایان نامه ی دانشگاهش در حال آماده سازی یک مترجم آنلاین هستش. مترجم
آنلاینی که آرتادخت داره آماده میکنه یک دیکشنری داره و در انتها این مترجم باید یک جمله رو
ترجمه کنه.
وجود دارد که نمایانگر تعداد  کلمات دیکشنری است. هر یک از n در خط اول ورودی یک عدد
خط بعدی شامل دو کلمه است که نشان می دهد کلمه ی دوم معنی کلمه ی اول است. خط بعدی n
از هم جدا شده اند. حال space شامل یک جمله است. یک جمله شامل چند کلمه می باشد که با
شما باید به آرتادخت کمک کنید و مترجمی بنویسید که دیکشنری و جمله ی مربوطه را از ورودی
بخواند و جمله را ترجمه کند. در پروسه ی ترجمه اگر کلمه ای در دیکشنری وجود نداشت، خود کلمه
را در خروجی چاپ کنید. برای اطلاعات بیشتر به ورودی نمونه و خروجی نمونه توجه کنید.

ورودی نمونه: 
5
hello salam
goodbye khodafez
say goftan
we ma
you shoma
we say goodbye to you tonight

خروجی نمونه: 
ma goftan khodafez to shoma tonight
"""

num_of_words = int(input("Enter the number of words: "))

my_dict = {}
for _ in range(num_of_words):
    word_meaning = input().split(" ")
    my_dict[word_meaning[0]] = word_meaning[1]

sentence = input("Enter the sentence to be translated: ")
words_of_sentence = sentence.split(" ")

for word in words_of_sentence:
    if word in my_dict:
        print(my_dict[word], end=" ")
    else:
        print(word, end=" ")
