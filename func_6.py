# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini
# tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.

def qoldiq(son):
    """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga
       qoldiqsiz bolinganlarini ekranga chiqaruvchi funksiya"""
    qoldiqsiz = []
    for n in range(2,11):
        if son%n == 0:
            qoldiqsiz.append(n)
    for i in qoldiqsiz:
        print(f"{son} {i} ga qoldiqsiz bolinadi")

qoldiq(son=int(input('son krit: ')))