# yosh = int(input('Yoshingiz nechida'))
# if yosh<=4:
#     print('Sizga kirish bepul')
# elif yosh<=12:
#     print('Sizga kirish 5000 won')
# else:
#     print('Sizga kirish 10 000 won')


# yosh = int(input('Yoshingiz nechida'))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# else:
#     price = 8000
# print(f"Sizga kirish {price}")    

# kun = input("Bugun qanday kun")    
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("Bugun dam olish kuni.") 
# else:
#     print("Bugun ish kuni")


kun = input("Bugun nima kun ?")
harorat = float(input('Havo harorati qanday ? '))
if kun.lower=='yakshanba' and harorat>=30:
    print('chomilishga kettik')
    print('Chomilish')
elif kun.lower()=='yakshanba' and harorat<30:
    print('Uyda qolamiz')
                 