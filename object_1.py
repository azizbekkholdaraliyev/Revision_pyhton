#+ Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar 
#+ (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0)

#+ Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing
#+ get_info() metodi avto haqida to'liq ma'lumotni matn ko'rinishida qaytarsin
#+ Avto ga oid obyektning xususiyatlarini yangilaydigan metodlar yozing.
#+ update_km() metodi son qabul qilib olib, avtomobilning yurgan kilometrajini yangilab borsin

class Avto():
    def __init__(self, model, rang, karobka, narx):
        self.model = model
        self.rang = rang
        self.karobka = karobka
        self.narx = narx
        self.km = 0

    def get_model(self):
        return self.model
    def get_rang(self):
        return self.rang
    def get_karobka(self):
        return self.karobka
    def get_narx(self):
        return self.narx

    def get_info(self):
        return f"model: {self.model}, rangi: {self.rang}, karobkasi: {self.karobka}, narxi: {self.narx}, km: {self.km}"
    
    def update_model(self, yangi_model):
        self.model = yangi_model
    def update_rang(self, yangi_rang):
        self.rang = yangi_rang
    def update_karobka(self, yangi_karobka):
        self.karobka = yangi_karobka
    def update_narx(self, yangi_narx):
        self.narx = yangi_narx

    def update_km(self, kilometr):
        self.km = kilometr


car1 = Avto('Mercedes', 'qora', 'avto', 230000)
car2 = Avto('BMW', 'qizil', 'mexanik', 80000)
car3 = Avto('Hundai', 'sariq', 'avto', 110000)

print(car1.get_info())
print(car2.get_model())
print(car3.get_narx())

car2.update_model('BYD')
car3.update_km(12000)
car2.update_karobka('avto')

print(car1.get_info())
print(car2.get_info())
print(car3.get_info())