from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import csv

driver = webdriver.Chrome()
url = 'https://app.podscribe.ai/series/2227781?allEpisodes=1'
driver.get(url)
time.sleep(4)

#Gather all the links
links = []
while True:
  link_elements = driver.find_elements(By.TAG_NAME, 'a')
  for element in link_elements:
    link = element.get_attribute("href")
    if "episode" in link:
      links.append(link)
  
  #Go to next page if possible
  next_page = driver.find_element(By.CSS_SELECTOR,"[aria-label='Go to next page']")
  if next_page.is_enabled():
    driver.execute_script("arguments[0].click();", next_page)
  else:
    break
driver.quit()

#Go to each link and grab the transcript    
transcripts = []
for link in links: 
  driver = webdriver.Chrome() 
  driver.get(link)
  time.sleep(4)
  
  wait = WebDriverWait(driver, 10)
  date_element = wait.until(EC.visibility_of_element_located((By.XPATH, "//*[text()='Published: ']")))
  date = date_element.text[11:]

  wait.until(EC.visibility_of_element_located((By.ID, "transcriptContainerContainer")))
  FanDuel_sections = driver.find_elements(By.XPATH,"//*[contains(@data-paragraph-text,'fanduel')]")

  transcripts.append({"date":date, "transcript":[section.text for section in FanDuel_sections]})
  print([section.text for section in FanDuel_sections])

  driver.quit()

#Write the transcripts into CSV file "transcripts.csv"
with open('transcripts2.csv', 'w', newline='') as csvfile:
    fieldnames = ['date', 'transcript']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(transcripts)


