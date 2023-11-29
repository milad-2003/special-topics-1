"""
است؟ palindrome آیا
زرگیسو که تازه با برنامه نویسی آشنا شده، میخواد برنامه ای بنویسه که
هست یا خیر. به کلمه ای میگن plindrome تعیین کنه آیا یک کلمه
که چه از چپ و چه از راست بخونیش یه چیز بشه palindrome
کوچک یا بزرگ بودن حرف مهم نیست

ورودی نمونه اول:
mAdaM

خروجی نمونه اول:
palindrome

ورودی نمونه دوم:
tehran

خروجی نمونه دوم:
not palindrome
"""

word = input("Enter the word here: ").lower()
reversed_word = word[::-1]
if word == reversed_word:
    print("palindrome")
else:
    print("not palindrome")
