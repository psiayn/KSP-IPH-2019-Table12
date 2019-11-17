import csv
from parsel import selector
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import imageio
import sys
from urllib.parse import urlencode

#username=sys.argv[1]
#password=sys.argv[2]


writer = csv.writer(open('output.csv','w+',encoding='utf-8-sig',newline=''))
writer.writerow(['name','occupation','company','location','connections','url'])

driver=webdriver.Firefox()
driver.get('https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin')

username = driver.find_element_by_name('session_key')
#username.click()
username.send_keys('email') ##replace with your linkedin email
sleep(0.5)

password = driver.find_element_by_name('session_password')
#password.click()
password.send_keys('password') ##replace with your linkedin password
sleep(0.5)

sign_in_button = driver.find_element_by_class_name('login__form_action_container ')
sign_in_button.click()
sleep(0.5)

# q = "site:linkedin.com/in \"{}\" \"{}\"".format(n,l)
# q = "site:linkedin.com/in.format(n,l)
q = "site:linkedin.com/in "
for i in range(1, len(sys.argv)):
    q += '"{}" '.format(sys.argv[i])
print(q)
driver.get('https://www.google.com/search?'+urlencode({"q": q}))
# search_query=driver.find_element_by_name('q')
#search_query.send_keys('site:linkedin.com/in AND"'n'" AND"'l'"')
# print("site:linkedin.com/in AND \"{}\" AND \"{}\"".format(n,l))
# search_query.send_keys("site:linkedin.com/in AND \"{}\" AND \"{}\"".format(n,l))
# search_query.send_keys(Keys.RETURN)
sleep(0.5)



urls =  driver.find_elements_by_xpath('//*[@class="r"]/a')
urls = [url.get_attribute('href') for url in urls]
sleep(0.5)

for url in urls:
    driver.get(url)
    sleep(2)

    name = driver.find_element_by_xpath('//li[@class="inline t-24 t-black t-normal break-words"]').text
    current_occupation = driver.find_element_by_xpath('//h2[@class="mt1 t-18 t-black t-normal"]').text
    location = driver.find_element_by_xpath('//li[@class="t-16 t-black t-normal inline-block"]').text
    # profilepic = driver.find_element_by_xpath('//*[@id="ember2632"]')
    # dp = profilepic.get_attribute("src")
    #BufferedImage saveImage = ImageIO.read(dp)
    #ImageIO.write(saveImage, "png", new File("profile_pic.png"))
    connections = driver.find_elements_by_xpath('//span[@class="t-16 t-black t-normal"]')
    if connections:
        connections = connections[0].text.strip()
    else:
        connections = driver.find_elements_by_xpath('//a[@data-control-name="topcard_view_all_connections"]/span')
        if connections:
            connections = connections[0].text.strip()
        else:
            connections = "0"
    # if(not(connections)):
    #     connections= driver.find_element_by_xpath('//*[@id="ember2627"]/div[2]/div[2]/div[1]/ul[2]/li[2]/span/text()')
    # about = driver.find_elements_by_xpath('//*[@id="ember2801"]/header/h2/text')
    # if(not(about)):
        # about= "-"
    #about = ""
    contact = driver.find_element_by_xpath('//a[@data-control-name="contact_see_more"]')
    link=contact.get_attribute('href')
    driver.get(link)
    # DOB = driver.find_element_by_xpath('//*[@id="ember4923"]/div/section[2]/div/span/text()')
    linkedin_link= driver.find_element_by_xpath('//a[@class="pv-contact-info__contact-link t-14 t-black t-normal"]').text
    writer.writerow([name,current_occupation,location,connections,linkedin_link])

driver.quit()
