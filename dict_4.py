# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. 
# Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, 
# alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 

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
for lug in sorted(lugat.items()) and sorted(lugat.values()):
    print(lug)
