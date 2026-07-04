# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

def ikki_son(son1, son2):
    """foydalanuvchidan 2 ta son olib ulardan kattasini ekranga chiqaruvchi,
       agar ular teng bolsa ular teng degan javob qaytaruvchi funksiya"""
    if son1>son2:
        print(f"katta son - {son1}")
    elif son2>son1:
        print(f"katta son - {son2}")
    elif son1==son2:
        print(f"{son1} = {son2} (sonlar teng)")

ikki_son(son1=int(input("1-sonni krit:")), son2=int(input("2-sonni krit:")))