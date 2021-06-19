from selenium import webdriver
import time
name = ['曾建閎','同事']
user = ['aszk1415','JAJN3FMP']
pws = ['aszk3131','Gt@555888']
userurl = ['1','2']
course_name =['臺灣AI行動計畫','捍衛環境好空氣','環境政策','「原」夢茂林，蛻變展翅','樂活、慢活、橋頭新生活','CEDAW第5條「社會文化之改變與母性之保障」','人權議題與發展','晚近全球化的發展']
#課程網址
course_url=['https://elearn.hrd.gov.tw/info/10022749',
            'https://elearn.hrd.gov.tw/info/10021253',
            'https://elearn.hrd.gov.tw/info/10022315',
            'https://elearn.hrd.gov.tw/info/10021309',
            'https://elearn.hrd.gov.tw/info/10021308',
            'https://elearn.hrd.gov.tw/info/10020975',
            'https://elearn.hrd.gov.tw/info/10022335',
            'https://elearn.hrd.gov.tw/info/10021291']


i = 1
# for i in range(len(name)):
# import signup
# signup.set(user[i],pws[i],userurl[i])
# for a in course_url:
#     signup.signup(a)
# import l1
# l1.set(user[i],pws[i],userurl[i])
# l1.lesson1(name[i],course_name[0])
import l2
l2.set(user[i],pws[i],userurl[i])
l2.lesson2(name[i],course_name[1])
# import l3
# l3.set(user[i],pws[i],userurl[i])
# l3.lesson3(name[i],course_name[2])
# import l4
# l4.set(user[i],pws[i],userurl[i])
# l4.lesson4(name[i],course_name[3])
# import l5
# l5.set(user[i],pws[i],userurl[i])
# l5.lesson5(name[i],course_name[4])
# import l6_1
# l6_1.set(user[i],pws[i],userurl[i])
# l6_1.lesson6(name[i],course_name[5])
# import l6_2
# l6_2.set(user[i],pws[i],userurl[i])
# l6_2.lesson6(name[i],course_name[5])
# import l7
# l7.set(user[i],pws[i],userurl[i])
# l7.lesson7(name[i],course_name[6])
# import l8
# l8.set(user[i],pws[i],userurl[i])
# l8.lesson8(name[i],course_name[7])