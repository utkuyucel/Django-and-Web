from selenium import webdriver

kelime = input("Aranılacak kelimeyi giriniz: ")

driver_path = "C:/Users/Utku/Desktop/driver/chromedriver.exe"
driver = webdriver.Chrome(executable_path = driver_path)


url = "https://sozluk.gov.tr/?kelime=" + kelime

driver.get(url)

data = driver.find_element_by_id("anlamlar-gts0")

print("Anlamı:" + "\n" + data.text + "\n")

driver.close()