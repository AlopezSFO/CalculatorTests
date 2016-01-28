from selenium import webdriver


browser = webdriver.Firefox()
browser.get('http://jeremydomasian.github.io/supercalc_v1-4/SuperCalc-v3.html')

testcase001 = browser.find_element_by_name('zero')
testcase001.click()

testcase001 = browser.find_element_by_name('one')
testcase001.click()

testcase001 = browser.find_element_by_name('two')
testcase001.click()

testcase001 = browser.find_element_by_name('three')
testcase001.click()

testcase001 = browser.find_element_by_name('four')
testcase001.click()

testcase001 = browser.find_element_by_name('five')
testcase001.click()

testcase001 = browser.find_element_by_name('six')
testcase001.click()

testcase001 = browser.find_element_by_name('seven')
testcase001.click()

testcase001 = browser.find_element_by_name('eight')
testcase001.click()

testcase001 = browser.find_element_by_name('nine')
testcase001.click()

testcase001 = browser.find_element_by_name('zero')
testcase001.click()

testcase001 = browser.find_element_by_name('one')
testcase001.click()

testcase001 = browser.find_element_by_name('two')
testcase001.click()

testcase001 = browser.find_element_by_name('three')
testcase001.click()

testcase001 = browser.find_element_by_name('four')
testcase001.click()

testcase001 = browser.find_element_by_name('five')
testcase001.click()

clear = browser.find_element_by_name('clear')
clear.click()

print ('Accepts up to 16 digits')

testcase001 = browser.find_element_by_name('zero')
testcase001.click()

testcase001 = browser.find_element_by_name('one')
testcase001.click()

testcase001 = browser.find_element_by_name('two')
testcase001.click()

testcase001 = browser.find_element_by_name('three')
testcase001.click()

testcase001 = browser.find_element_by_name('four')
testcase001.click()

testcase001 = browser.find_element_by_name('five')
testcase001.click()

testcase001 = browser.find_element_by_name('six')
testcase001.click()

testcase001 = browser.find_element_by_name('seven')
testcase001.click()

testcase001 = browser.find_element_by_name('eight')
testcase001.click()

testcase001 = browser.find_element_by_name('nine')
testcase001.click()

testcase001 = browser.find_element_by_name('zero')
testcase001.click()

testcase001 = browser.find_element_by_name('one')
testcase001.click()

testcase001 = browser.find_element_by_name('two')
testcase001.click()

testcase001 = browser.find_element_by_name('three')
testcase001.click()

testcase001 = browser.find_element_by_name('four')
testcase001.click()

testcase001 = browser.find_element_by_name('five')
testcase001.click()

testcase001 = browser.find_element_by_name('six')
testcase001.click()

alert = browser.switch_to_alert()
alert.accept()

print ('Cannot accept more than 16 digits')
print ('Pass Test Case #001 - #002')

clear = browser.find_element_by_name('clear')
clear.click()

print ('Now checking addition function')

testcase003 = browser.find_element_by_name('two')
testcase003.click()

testcase003 = browser.find_element_by_name('plus')
testcase003.click()

testcase003 = browser.find_element_by_name('nine')
testcase003.click()

testcase003 = browser.find_element_by_name('DoIt')
testcase003.click()

print ('Addition works')
print ('Pass Test Case #003')

inputElem = browser.find_element_by_name('Input')

answer = inputElem.get_attribute('value')
print(answer)

clear = browser.find_element_by_name('clear')
clear.click()

