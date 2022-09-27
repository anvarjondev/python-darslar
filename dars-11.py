# -*- coding: utf-8 -*-
"""
Created on Wed Sep 21 08:46:11 2022

@author: Dasturchi
"""

# yosh = int(input("Yoshingizni kiriting >>>"))
# if yosh <= 4:
#     price = 0
# elif yosh <= 12:
#     price = 5000
# elif yosh <65:
#     price = 10000
# else:
#     price = 8000
# print(f"Sizga kirish {price} so'm")

# kun = input("Bugun kun nima >>>")
# if kun.lower() == 'shanba' or 'yakshanba':
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni")

# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat>=30:
#     print("Cho'milgani ketdik")
# elif (kun.lower() == 'yakshanba' or kun.lower() == 'shanba') and harorat<=30:
#     print("Uyda dam olamiz")

# narx = 15000
# choy = True
# salat = False

# if choy and salat:
#     narx = narx + 10000
# elif choy or salat :
#     narx = narx + 5000
# print(f"Jami {narx} so'm")    

# narh = 15000
# choy = True
# salat = False
# non = True
# kampot = True
# assorti = False

# if choy:
#     print("Mijoz choy oldi")
#     narh = narh + 3000
# if salat:
#     print("Mijoz salat oldi")
#     narh = narh + 5000
# if non: 
#     print("Mijoz non oldi")
#     narh = narh + 2000
# if kampot:
#     print("Mijoz kamport oldi")
#     narh = narh + 5000
#     if assorti:
#         print("Mijoz assorti oldi")
#         narh = narh + 15000
# print(f"Jami {narh} so'm")

# menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa']
# ovqat = input("Nima ovqat yeysiz?>>>")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi.")
# else:
#     print('Afsuski bizda bunday ovqat yo\'q.')

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
 # 'manti' not in menu # menu da manti yo'qmi?

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ['somsa', 'mastava' ,'osh', 'norin']
# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz menuda {taom} yo'q")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]
# if buyurtmalar:
#     print(f"Buyurtmada {len(buyurtmalar)} ta taom bor")
# else:
#     print("Ro'yhat bo'sh")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = []
# if buyurtmalar:
#     print(f"Buyurtmada {len(buyurtmalar)} ta taom bor")
# else:
#     print("Ro'yhat bo'sh")

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menyuda {taom} bor")
#         else:
#             print(f"Kechirasiz menyuda {taom} yo'q")
# else:
#     print("Savatchangiz bo'sh!")

#amaliyot
# juft_son = int(input("Juft son kiritng>>>"))
# if juft_son%2 == 0:
#     print("Rahmat")
# else:
#     print("Bu son juft emas")

# yosh = int(input("Yoshingizni kiriting: "))
# if yosh <=4 or yosh >=60:
#     narx = 'bepul'
# elif yosh<=18 :
#     narx = 10000
# else:
#     narx = 2000
# print(f"Sizga kirish {narx} so'm")

# son1 = float(input("1-sonni kiriting: "))
# son2 = float(input("1-sonni kiriting: "))
# if son1 > son2:
#     ishora = ">"
# elif son1 < son2:
#     ishora = '<'
# else:
#     ishora = '='
# print(f"{son1} {ishora} {son2}")

# mahsulotlar = [    "un",
#     "yog'",
#     "sovun",
#     "tuxum",
#     "piyoz",
#     "kartoshka",
#     "olma",
#     "banan",
#     "uzum",
#     "qovun"]
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-maxsulotni qo'shing: ") )    
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Do'konimizda {mahsulot} bor")
#         else:
#             print(f"Do'konizmizda {mahsulot} yo'q")
# else :
#     print("Savatingiz bo'sh")
# mahsulotlar = [
#     "un",
#     "yog'",
#     "sovun",
#     "tuxum",
#     "piyoz",
#     "kartoshka",
#     "olma",
#     "banan",
#     "uzum",
#     "qovun",
# ]


# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q: ")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)


# else:
#     print("Siz so'ragan mahsulotlar barchasi do'konimizda bor")

# foydalanuvchilar = ['rustam', 'ruxsora', 'bola', 'chaqmoq', 'arra']
# login = input("Yangi login tanlang: ")
# if  login in foydalanuvchilar:
#     print("Login band, yangi login tanlang!")
# else:
#     print("Xush kelibsiz")

# son = int(input("Istalgan butun sonni kiriting: "))
# for n in range(2, 11):
#     if not (son % n):
#         print(f"{son} soni {n} qoldiqsiz bo'linadi")










