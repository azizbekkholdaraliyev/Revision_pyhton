# Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. 
# Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan 
# ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)

class user():
    def __init__(self, ism, username, email, address):
        self.ism = ism
        self.username = username
        self.email = email
        self.address = address

# Klassga bir nechta metodlar qo'shing, jumladan get_info() metodi foydalanuvchi haqida yig'ilgan ma'lumotlarni 
# chiroyli qilib chiqarsin (masalan: "Foydalanuvchi: alijon1994, ismi: Alijon Valiyev, email: alijon1994@gmail.com).
    def get_info(self):
        return f"Foydalanuvchi: {self.username}, ismi: {self.ism}, email: {self.email}, address: {self.address}"

# Klassdan bir nechta obyektlar yarating va uning xususiyatlari va metodlariga murojat qiling.
    def get_ism(self):
        return self.ism

    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_address(self):
        return self.address

user1 = user('Asad', 'asad4323432', 'asad43bek32@gamil.com', 'Fergana')
user2 = user('Anvar', 'a23vardon', 'folgka3r343@gmail.com', 'Tashkent')
user3 = user('Farrux', 'farruxbekismoilov', 'farrux32uzbk@gmail.com', 'Samarkand')

print(user1.get_info())
print(user2.get_ism())
print(user3.get_email())