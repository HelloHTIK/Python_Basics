# 使用 多个键值对, 储存 描述一个 物体的相关信息 -- 描述复炸的数据信息
# 将 多个字典 放在一个列表中, 再进行遍历

card_list = [
    {"name": "小明",
     "age": 18,
     "phone": "54321d",
     "email": "12345@qq.com"},
    {"name": "大明",
     "age": 81,
     "phone": "12345",
     "email": "54321@qq.com"}
]

for card_info in card_list:

    print(card_info)
