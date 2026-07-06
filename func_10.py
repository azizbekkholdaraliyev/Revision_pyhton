# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funkisya yozing. '
# 'Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa 
# ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

def talaba_lugat(ism, familiya, **malumotlar):
    malumotlar['ism'] = ism
    malumotlar['familiya'] = familiya
    return malumotlar

talaba1 = talaba_lugat('fariz', 'otabekov')
talaba2 = talaba_lugat('orif', 'olimov', yosh=20, kasb='dasturlash')

print(talaba1)
print(talaba2)