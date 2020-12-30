from selenium import webdriver
import time
import json
 
PATH = "C:\Program Files (x86)\chromedriver.exe"
 
driver = webdriver.Firefox()
kyuLvls = ["-1","-2","-3","-4","-5","-6","-7","-8"]
topics = ["Algorithms","Logic", "Fundamentals", "Games", "Data Types"]

for kyuLvl in kyuLvls:
    for topic in topics:
        driver.get("https://www.codewars.com/kata/search/?q=&r[]="+kyuLvl+"&tags="+topic+"&beta=false")
        amountOfKatas = driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/section/div[2]/p').text.split()[0]

        #Scroll to make all the titles available
        scrollTimes = int(int(amountOfKatas)/30)+1 #One more just to get to the bottom of the webpage, and 30 is the limit per page
        for x in range(scrollTimes):
            time.sleep(2) #Depends on the internet, cause in take a while to load the screen
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
        #Save the json file in data
        with open('data.json','r') as f:
            data = json.load(f)
        print(data)
        
        #Get all the Kata Titles
        for x in range(1,int(amountOfKatas)):
            kataTitle = driver.find_element_by_xpath('/html/body/div[1]/div[1]/main/section/div[2]/div['+str(x)+']/div/div[1]/div[1]/a')
            if kataTitle.text not in data[kyuLvl.replace('-','')][topic]: data[kyuLvl.replace('-','')][topic].append(kataTitle.text) #Add the title to the dict
            print(kataTitle.text)
        
        #Uploads the data to the json file
        with open('data.json','w') as f:
            json.dump(data,f)
        
    
driver.quit()