"""
زیررشته

جهانگیر توی یه شرکت کامپیوتری کار می کنه. قراره جهانگیر برنامه ای
رو در یک رشته ی دیگه پیدا کرد BA و AB بنویسه که تعیین کنه آیا میتوان
هم AB و BA بدون اینکه با هم همپوشانی داشته باشن؟ ترتیب 
هست. اگه ورودی YES باشه پاسخ ABBA مهم نیست. یعنی مثلا اگه ورودی
هست YES هم باشه بازم پاسخ BAAB
هست یا اگه ورودی NO باشه پاسخ ABA ولی اگه ورودی
هست. میتونید کمک NO باشه بازم پاسخ ABHA
کنید جهانگیر این برنامه رو بنویسه؟

را دقیقا به همین شکل با حروف بزرگ در خروجی چاپ کنید NO و YES
"""

user_input = input("Enter the string: ")

answer = "NO"

if "AB" in user_input:
    if "BA" in user_input[user_input.index("AB") + 2:]:
        answer = "YES"

if "BA" in user_input:
    if "AB" in user_input[user_input.index("BA") + 2:]:
        answer = "YES"

print(answer)
