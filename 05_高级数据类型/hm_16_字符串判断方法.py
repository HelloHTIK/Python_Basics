# 1. 判断空白字符
space_str = "  \t\n\r"
print(space_str)
print(space_str.isspace())

# 2. 判断字母或数字
alnum_str = "999"
print(alnum_str)
print(alnum_str.isalnum())

# 3. 判断是否所有字符为字母
alpha_str = "jjj"
print(alnum_str)
print(alpha_str.isalpha())

# 4. 判断是否只包含数字（全角数字）
decimal_str = "999"
print(decimal_str)
print(decimal_str.isdecimal())

# 5. 判断只包含数字 （全角数字，（1），、u00b2
digit_str = "\u00b2"
print(digit_str)
print(digit_str.isdigit())

# 6. 判断是否只包含数字 (全角数字，汉字数字)
numeric_str = "九九九"
print(numeric_str)
print(numeric_str.isnumeric())

# 7. 判断每个单词首字母是否为大写
title_str = "Email"
print(title_str)
print(title_str.istitle())

# 8. 判断中包含至少一个区分大小写的字符，并且所有这些（区分大小写的）字符都是小写
lower_str = "Email"
print(lower_str)
print(lower_str.islower())

# 9. 判断中包含至少一个区分大小写的字符，并且所有这些（区分大小写的）字符都是大写
upper_str = "Email"
print(upper_str)
print(upper_str.isupper())


