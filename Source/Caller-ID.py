
#
# This Is Free Tool By Mr. Lyrica Alanzi AKA @8Y
# Dont Try Sell It Cuz It's Fucking Free
# Github: https://github.com/Soud69
# Instagram: https://instagram.com/8Y
# Telegram: https://t.me/Soud69
# Discord: Soud#5866
#

try:
	import os, requests, colorama, json
	from os import system
	from colorama import Fore
	system("title " + "Lyrica Was Here - @8Y - Soud#5866")
except Exception as m:
  print("Something Went Wrong\n")
  print(m)
  input()
  exit()

logo = """
         _______   __ 
   ____ |  _  \ \ / /
  / __ \ \ V / \ V /
 / / _` |/ _ \  \ /
| | (_| | |_| | | |
 \ \__,_\_____/ \_/
  \____/
"""
print(Fore.CYAN+logo)
print(Fore.GREEN+"Made with Love by @8Y - Soud#5866\n\n"+Fore.RESET)
print("1) KWT\n2) KSA\n3) UAE\n4) OMN\n5) QTR\n6) BHR")
mode = int(input("Enter Country Number: "))
phone = input("Enter Phone Number: ")
if mode == 1: country = "KW"
elif mode == 2: country = "SA"
elif mode == 3: country = "AE"
elif mode == 4: country = "OM"
elif mode == 5: country = "QA"
elif mode == 6: country = "BH"
print(Fore.GREEN+'\n===================================\n'+Fore.RESET)
req = requests.get(f"http://caller-id.saedhamdan.com/index.php/UserManagement/search_number?number={phone}&country_code={country}",headers={"User-Agent":"8Y/69"}).text
try: print(f'Name: {json.loads(req)["result"][0]["name"]}')
except: print(Fore.RED+"Name: Not Found!")
input("Press Enter To Exit...")
