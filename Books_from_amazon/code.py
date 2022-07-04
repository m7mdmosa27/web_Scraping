from selenium import webdriver
import csv

driver = webdriver.Chrome(r"E:\ITI AI-Pro Track\data perperation\chromedriver_win32\chromedriver.exe")
driver.set_script_timeout(5000)
driver.get("https://www.amazon.in/gp/bestsellers/books/")
nameofbook = driver.find_elements(by="xpath", value="//div[@class='p13n-sc-truncated']")
priceofbook = driver.find_elements(by="xpath", value="//span[@class='p13n-sc-price']")

# print(len(nameofbook), len(priceofbook))

for i in range(len(nameofbook)):
    print(nameofbook[i].text, priceofbook[i].text)

header = ["name of book", 'price']
with open('Books_Amazon_Dataset.csv', 'w', encoding='UTF8', newline='') as filecsv:
    writer = csv.writer(filecsv, delimiter=',')
    writer.writerow(header)
    for i in range(len(nameofbook)):
        writer.writerow([nameofbook[i].text, priceofbook[i].text])



driver.close()
