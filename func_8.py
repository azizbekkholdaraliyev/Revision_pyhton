# Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir matnning birinchi harfini
# katta harfga o'zgatiruvchi funksiya yozing. 

def katta(names):
    """berilgan royhatdagi ismlarni birinchi harfini katta harfga ozgartiruvchi funksiya"""
    for n in range(len(names)):
        names[n] = names[n].title()
    return names

    
ismlar = ['ali', 'vali', 'hasan', 'husan']
katta(ismlar)
print(ismlar)