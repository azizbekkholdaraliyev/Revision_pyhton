# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
def kva_kub(son):
    """foydalanuvchidan son olib uni kvadrati va kubini ekranga chiqaruvchi funksiya"""
    print(f"{son} ning kvadrati: {son**2} \n"
          f"{son} ning kubi: {son**3}")

kva_kub(son=int(input("son krit: ")))