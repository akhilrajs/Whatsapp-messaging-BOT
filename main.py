from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from time import strftime
from urllib.parse import quote
from os import system
from os import environ
from prettytable import PrettyTable
from telepot import Bot
from XPATH as xpath


system("")
environ["WDM_LOG_LEVEL"] = "0"
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'

print(style.BLUE)
print(style.RESET)

f = open("msg_url.txt", "r")
msg_url = f.read()
f.close()
print(style.RED + "[#] whatsapp_bot")
print(style.RED + "[#] author : Akhil Raj S")
print("")
print("")
import requests
print(style.GREEN + "[#] downloading message from GITHUB")
sleep(0.8)
try :
	url = msg_url
	data = requests.get(url)
	message = data.text
except Exception as e:
	print(style.RED + "[#] ERROR --> " + str(e) )
	print(style.RED + "[#] connect to the internet and try again " + style.RESET) 
	exit()


print(style.YELLOW + '\nThis is your message-')
print(style.WHITE + message)
print("\n" + style.RESET)
message = quote(message)
sleep(0.8)
numbers = []
f = open("numbers.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		numbers.append(line.strip())
f.close()

names = []
f = open("names.txt", "r")
for line in f.read().splitlines():
	if line.strip() != "":
		names.append(line.strip())
f.close()
total_number=len(numbers)
x = PrettyTable()
for n in names:
	idx_n = names.index(n)
	num = numbers[idx_n]
	x.add_row([n,num])
print(x)
sleep(1)
delay = 30
greet = ""
currentTime = int(strftime('%H'))
if currentTime < 12 :
     greet = "Good Morning "
if 12 < currentTime < 18 :
     greet = "Good Afternoon "
if currentTime > 18 :
     greet = "Good Evening "

options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=C:\\User\\Data\\Default")
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=options)
print('Once your browser opens up sign in to web whatsapp')
driver.get('https://web.whatsapp.com')
try:
	menu = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, xpath.menu_btn)))
except Exception as e:
	try:
		print("[#] ERROR : " + e)
		print("[#] failed to detect whatsapp login")
		print("[#] trying again")
		menu = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, xpath.menu_btn)))
	except Exception as e:
		print("[#] an error has occured. make sure the system is connected to the internet")
		print(e)
		print("[#] END PROGRAM")
		sleep(5)
		exit()
fail_ = []
for idx, number in enumerate(numbers):
	number = number.strip()
	if number == "":
		continue
	print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx+1), total_number, number) + style.RESET)
	try:
		sleep(2)
		msg = ""
		msg = greet + str(names[idx]).title() + '''
		 
		''' + str(message)
		url = 'https://web.whatsapp.com/send?phone=+91' + number + '&text=' + msg
		sleep(2)
		sent = False
		for i in range(3):
			if not sent:
				driver.get(url)
				try:
					click_btn = WebDriverWait(driver, delay).until(EC.element_to_be_clickable((By.XPATH, xpath.click_btn)))
				except Exception as e:
					print(style.RED + f"\nFailed to send message to: {number}, retry ({i+1}/3)" + style.RESET)
					print("Make sure your phone and computer is connected to the internet.")
					print("If there is an alert, please dismiss it." + style.RESET)
					fail_.append(number)
				else:
					sleep(1)
					click_btn.click()
					sent=True
					sleep(3)
					print(style.GREEN + 'Message sent to: ' + number + " " + names[idx].title() + style.RESET)
	except Exception as e:
		print(style.RED + 'Failed to send message to ' + number + str(e) + style.RESET)
		fail_.append(number)
print("Failed to send to : " + '\n' )
fail = []
for i in fail_:
	if i in fail:
		i = ""
	else:
		fail.append(i)
name_failed =[]
for number in fail : 
	idx = numbers.index(number)
	name = names[idx]
	name_failed.append(name)
x = PrettyTable()
for n in name_failed:
	idx_n = name_failed.index(n)
	num = fail[idx_n]
	x.add_row([n,num])
print(x)
sleep(10)
driver.close()
