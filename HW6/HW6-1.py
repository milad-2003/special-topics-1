"""
برنامه ی سلامت

دو برنامه ی سلامت متفاوت در نظر گرفته شده است. در یک مدرسه شیر توزیع B و A در دو مدرسه ی
می شود و در مدرسه ی دیگر شیر توزیع نمی شود. کارشناسان تغذیه در نظر دارند با بررسی قد و وزن و سن
دانش آموزان این دو کلاس را بگیرد و آنها را با یکدیگر مقایسه کند. برنامه ای بنویسید که تعداد دانش آموزان
هر کلاس به علاوه اطلاعات سن و قد و وزن آنها را بگیرد و در یک لیست هر کدام را ذخیره کند و میانگین
سن و قد و وزن هر کلاس را به ترتیب در یک خط جدا در خروجی چاپ کند
(چاپ شوند float به صورت)
و در ادامه کلاسی را که میانگین قد آن بیشتر است در خروجی چاپ کند.
B را وارد کنید و سپس اطلاعات کلاس A در ابتدا تعداد و اطلاعات کلاس 
در خروجی نیز به ترتیب اطلاعات ورودی چاپ شود. در صورتی هم که میانگین قد برابر بود
کلاس با میانگین وزن کمتر چاپ شود. در صورت برابر بودن میانگین قد و وزن، عبارت
در خروجی چاپ شود Same
باید در پیاده سازی از کلاس ها استفاده شود

ورودی نمونه: 
5
16 17 15 16 17
180 175 172 170 165
67 72 59 62 55
5
15 17 16 15 16
166 156 168 170 162
45 52 56 58 47

خروجی نمونه: 
16.2
172.4
63.0
15.8
164.4
51.6
A
"""


class Class:
    def __init__(self, num_of_students):
        self.num_of_students = num_of_students
        self.ages = [int(age) for age in input().split(" ")]
        self.heights = [int(height) for height in input().split(" ")]
        self.weights = [int(weight) for weight in input().split(" ")]
        self.average_age = sum(self.ages) / float(self.num_of_students)
        self.average_height = sum(self.heights) / float(self.num_of_students)
        self.average_weight = sum(self.weights) / float(self.num_of_students)
    

class_a = Class(input("Enter the information of class A:\n"))
class_b = Class(input("Enter the information of class B:\n"))

result_str = "Same"
if class_a.average_height > class_b.average_height:
    result_str = "A"
elif class_b.average_height > class_a.average_height:
    result_str = "B"
elif class_a.average_weight < class_b.average_weight:
    result_str = "A"
elif class_b.average_weight < class_a.average_weight:
    result_str = "B"

print("\n")
print(class_a.average_age)
print(class_a.average_height)
print(class_a.average_weight)
print(class_b.average_age)
print(class_b.average_height)
print(class_b.average_weight)
print(result_str)
