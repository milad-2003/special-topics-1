"""
استاندارد سازی اسامی

مهدی داره لیست نهایی اسامی شرکت کننده در مراسم اختتامیه فیلم فجر رو
میفرسته برای کمیته اجرایی تا بتونن کارت های ورود رو چاپ کنن. ولی یه مشکلی
هست. موقع ثبت نام شرکت کننده ها اسم هاشون رو به صورت استاندارد ننوشته اند.
استاندارد یعنی دقیقا حرف اول اسم بزرگ باشه و بقیه حروف اسم کوچک باشد.
برنامه ای بنویسید که 10 اسم از ورودی بخواند و استاندارد شده ی آنها را در خروجی
چاپ کند.

ورودی نمونه:
BaHram MaHnaZ hooman FaribORZ barAN HedieH ALI EZATOLLAH MOHAMADALI JAMSHID

خروجی نمونه:
Bahram
Mahnaz
Hooman
Fariborz
Baran
Hedieh
Ali
Ezatollah
Mohamadali
Jamshid
"""

names = input("Enter the names, separated with spaces: ")
names_list = names.split(" ")
final_list = []
for name in names_list:
    word_list = [x for x in name.lower()]
    word_list[0] = word_list[0].upper()
    final_list.append("".join(word_list))
print("\n".join(final_list))
