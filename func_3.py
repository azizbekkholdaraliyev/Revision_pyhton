# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
def juft_toq(son):
    """foydalanuvchidan son olib uni juft yoki toqligini ekranga chiqaruvchi funksiya"""
    if son%2 == 0:
        print(f"{son} juft son")
    else:
        print(f"{son} toq son")

juft_toq(son=int(input("son kirit: ")))