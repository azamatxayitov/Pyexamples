# juft_sonlar = list(range(0,20,2))
# toq_sonlar = list(range(1,20,2))
# print("Juft sonlar: ", juft_sonlar)
# print("Toq sonlar: ", toq_sonlar)

# narhlar = [12000, 25000, 23450, 45000, 220, 6789, 16790, 4000]
# qimmat = max(narhlar)
# arzon = min(narhlar)

# jami = sum(narhlar)
# print("Eng arzon narh ", arzon, ". Eng qimmat ", qimmat, ". Jami: ", jami)

# cars = ['bmw', 'volvo', 'buggati', 'ferrari', 'jaguar', 'lamborghini']
# my_cars = cars[0:3]
# print(my_cars)

# sonlar = [1, 2, 3, 4, 5, 6, 7]
# sonlar2 = sonlar

# sonlar2.append(16)
# sonlar2.append(23)

# print(sonlar)
# print(sonlar2)

# mehmonlar = ['Ali','Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(mehmonlar)
    
    
    
# mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print(f"Hurmatli {mehmon}, sizni 20 dekabr kuni nahorga taklif qilamiz")
#     print("Hurmat bilan, Plaonichiyevlar oilasi")
    
    
# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng") 
    
    
# sonlar = list(range(11))
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar)
# print(sonlar_kvadrati)           


# dostlar = []
# print("5 ta eng yaqin do'stingizni ismini kiriting") 
# for dost in range(5):
#     dostlar.append(input(f"{dost+1} dostingizni ismini kiriting"))
# print(dostlar)           


# avtolar = ['porsche', 'bmw', 'ferrari', 'mercedes', 'rolls-royse', 'pikap']

# for avto in avtolar:
#     if avto == "bmw":
#         print(avto.upper())
#     else:
#         print(avto.title())    


ism = input("Ismingizni kiriting")
if ism != 'ali':
    print(f"Uzur, {(ism.title())} biz Alini kutayabmiz")
else:
    print("Salom Ali")    