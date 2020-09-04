from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
driver.get('https://web.whatsapp.com')

name = input('Name of the person or the group: ')
msg = open ("mensaje.txt")
msgs = msg.readlines()

input('Press enter if you have scan the QR code')

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

#msg_box = driver.find_element_by_class_name("_2S1VP copyable-text selectable-text")
msg_box = driver.find_elements_by_xpath(".//div[normalize-space(@class)='_2S1VP copyable-text selectable-text']")
for linea in msgs:
    palabras = linea.split()
    for palabra in palabras:
        msg_box[1].send_keys(palabra)
        msg_box[1].send_keys(Keys.RETURN)
        time.sleep(0.5)


# SI VAS A INICIARLO DESDE LINUX ABRELO CON CON EL CODIGO:
# python3 "NombreDelArchivo" 
# ej:  python3 whtsp.py