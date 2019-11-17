import os
import time
print("""
         _____               _____                 _____         ____________
________ ___(_)________      ___(_)_______ __________  /_______ ____  /___  /  _______ ________ _______ ___
___  __ \__  / ___  __ \     __  / __  __ \__  ___/_  __/_  __ `/__  / __  /   __  __ \___  __ \__  __ `__ \
__  /_/ /_  /  __  /_/ /     _  /  _  / / /_(__  ) / /_  / /_/ / _  /  _  /    _  / / /__  /_/ /_  / / / / /
_  .___/ /_/   _  .___/      /_/   /_/ /_/ /____/  \__/  \__,_/  /_/   /_/     /_/ /_/ _  .___/ /_/ /_/ /_/
/_/            /_/                                                                     /_/

""")

print("Welcome to our tool, choose one of the following:")

print("1. twitter user")
print("2. instagram user")
print("3. facebook user")
print("4. linkedin user ")
choice = int(input('pin>'))
if(choice == 1):
    print("Enter username")
    username = input("pin/twitter>")
    #os.system('sudo twint -u '+username+' --followers')
    print("Select an option")
    print("1. followers")
    print("2. following")
    print("3. favorites")
    print("4. all")
    option = int(input("pin/twitter>"))
    print(option)
    if(option == 1):
        os.system('sudo twint -u '+username+' --followers -o dump.txt')
        os.system('python3 twint/twt2hashtag.py')
    elif(option == 2):
        os.system('sudo twint -u '+username+' --following -o dump.txt')
        os.system('python3 twint/twt2hashtag.py')
    elif(option == 3):
        os.system('sudo twint -u '+username+' --favorites -o dump.txt')
        os.system('python3 twint/twt2hashtag.py')
    elif(option == 4):
        os.system('sudo twint -u '+username+' -o dump.txt')
        os.system('python3 twint/twt2hashtag.py')


elif(choice == 2):
    print("Enter username")
    username = input("pin/instagram>")
    os.system('python3 InstagramOSINT/main.py --username '+username+' --downloadPhotos')
    os.system('cp InstagramOSINT/insta2hashtag.py '+username+'/insta2hashtag.py ')
    #os.system('mv '+username+'/posts.txt '+username+'/posts.json')
    time.sleep(5)
    print("File copied")
    os.system('python3 '+username+'/insta2hashtag.py --username '+username)

elif(choice == 3):
    os.chdir(os.getcwd()+'/facebookscraper')
    os.system('python3 main.py')

elif (choice == 4):
    print("Enter all the arguments such as name , location, etc in quotes \" \" seperated by a white space ")
    args = input("pin/linkedin>")
    os.system("python3 linkedinscrape.py "+args)
