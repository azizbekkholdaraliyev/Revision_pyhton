# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, 
# va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing

# Yuoqirdagi tsikl tugaganidan so'ng, ekranga "Kod n marta takrorlandi" degan xabarni chiqaring 
# (n o'rniga kod necha marta takrorlanganini yozing)

#natija shunday chiqishi kerak:
#salom Ali
#salom Vali
#salom Hasan
#salom Husan
#salom Olim
#kod 5 marta takrorlandi

ismlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for ism in ismlar:
    print(f"salom {ism}")
print(f"kod {len(ismlar)} marta takrorlandi")