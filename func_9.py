# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

def kopaytma(*sonlar):
    """istalgancha sonlarni qabul qilib ularni kopaytmasini hisoblovchi funksiya"""
    kopaytma = 1
    for son in sonlar:
        kopaytma = kopaytma * son
    return kopaytma


print(kopaytma(4, 5, 6))    