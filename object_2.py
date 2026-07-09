# Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring 
# (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)
# Avtosalonga yangi avtomobillar qo'shish uchun metod yozing
# Avtosalondagi avtomobillar haqida ma'lumot qaytaruvchi metod yozing
# Yuqoridagi obyektlar va ularga tegishli metodlarni tekshirib ko'ring
# dir() funksyasi va __dict__ metodi yordamida o'zingiz yozgan va Pythondagi turli klass va obyektlarning xususiyatlari va
# metodlarini toping (dir(str), dir(int) va hokazo)

class Avtosalon():
    def __init__(self, avto_market):
        self.avto_market = avto_market