# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting 
# (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering
# Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
        
# kalit soz kiriting: intager \n Butun son
# kalit soz kiriting: float   \n Float sozi onlik son deb tarjima qilinadi
# kalit soz kiriting: dictionary \n bunday soz mavjud emas
# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.

lugat = {
    'integer':'son korinishidagi malumot turi',
    'float':'onli son korinishidagi malumot turi',
    'string':'matn korinishidagi malumot turi',
    'if':'shart operatori',
    'list':'royhat korinishidagi malumotlar jamlanmasi',
    'dict':'kalit va qiymatni oz ichiga oluvchi malumot turi',
    'for':'takrorlash operatori',
    'tuple':'ozgarmas qiymatni oz ichiga oladi',
    'input':'foydalanuvchidan malumot qabul qiluvchi funksiya',
    'print':'yozilgan malumotni ekranga chiqarish'
}
user = input('soz kiriting \n>>>')
if user in lugat:
    print(lugat[user])
elif user not in lugat:
    print("bunday soz mavjud emas!")