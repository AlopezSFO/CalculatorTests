from selenium import webdriver
from selenium.webdriver.common.keys import Keys



browser = webdriver.Firefox()
browser.get('http://jeremydomasian.github.io/supercalc_v1-4/SuperCalc-v3.html')

#input email 
clearElem = browser.find_element_by_name('clear')
clearElem.click()

print ('yay its there')
print ('okay now lets see if it works')

num4Elem = browser.find_element_by_name('four')
num4Elem.click()

num5Elem = browser.find_element_by_name('five')
num5Elem.click()

num6Elem = browser.find_element_by_name('six')
num6Elem.click()

clearElem = browser.find_element_by_name('clear')
clearElem.click()

print ('yay it works')
print ('now check the division thing')

divElem = browser.find_element_by_name('div')
divElem.click()

print('yay its there')
print('lets see if this works')

clearElem.click()

num8Elem = browser.find_element_by_name('eight')
num8Elem.click()

divElem = browser.find_element_by_name('div')
divElem.click()

num2Elem = browser.find_element_by_name('two')
num2Elem.click()

eqElem =browser.find_element_by_name('DoIt')
eqElem.click()

print ('yayyyyyy')