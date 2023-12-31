"""
سیستم شمارش آرا

آقای ژوبین آرتاباز رییس سازمان ملل متحد هست و قراره راجع به انتخاب هیئت رئیسه
یک رای گیری انجام بده! دادمهر جمشیدی که مسئول کامپیوتر سازمان ملل هست
برنامه ای نوشته که می شمره هر کشور چند رای رو کسب کرده. شما قراره با نوشتن
برنامه ای به دادمهر کمک کنید تا آرا رو شمارش کنه.
خط n هست که تعداد کل آرا رو نمانش میده. هر یک از n خط اول ورودی شامل عدد
بعدی شامل اسم یک کشور می باشد. اسم کشورها از حروف کوچک انگلیسی ساخته
شده اند.
خط چاپ کنید که شامل تعداد آرا هر یک از کشورها می باشد. نام m در خروجی
کشورها را به ترتیب حروف الفبا در خروجی بنویسید. برای اطلاعات بیشتر به ورودی نمونه و
خروجی نمونه توجه کنید.

ورودی نمونه:
5
usa
uk
iran
usa
usa

خروجی نمونه: 
iran: 1
uk: 1
usa: 3
"""

num_of_votes = int(input("Enter the total number of votes: "))

list_of_votes = []
for _ in range(num_of_votes):
    list_of_votes.append(input())

list_of_votes.sort()

result_dict = {}
for vote in list_of_votes:
    result_dict[vote] = result_dict.get(vote, 0) + 1

for k, v in result_dict.items():
    print(f"{k}: {v}")
