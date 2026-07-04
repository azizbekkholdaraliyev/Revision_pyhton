# Foydalanuvchidan x va y sonlarini olib, x ning y-darajasini hisoblab bruvchi funksiya yozing.

# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.

def hisob(x, y):
    """foydalanuvchidan x va y sonlariga qiymat qabul qilib, x ning y-darajasini hisoblovchi funksiya"""
    print(f"natija: {x**y}")

hisob(x=int(input("x ni krit: ")), y=int(input("y ni krit: ")))