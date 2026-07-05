
# Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm, 
# 7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl yozingki,
# dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin. 
# Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).

sora = "yoshiz nechida? \n>>>"
ishora = True
while ishora:
    qiymat = input(sora)
    if qiymat=='exit' or qiymat=='quit':
        ishora = False 
    elif int(qiymat)<7:
        print("2000 so'm")
    elif int(qiymat)>7 and int(qiymat)<18:
        print("3000 so'm")
    elif int(qiymat)>18 and int(qiymat)<65:
        print("10000 so'm")
    elif int(qiymat)>65:
        print("sizga bepul")