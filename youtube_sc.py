from pyvirtualdisplay import Display
from selenium import webdriver

search = input("What do you want to search YouTube for?\n")
print("Looking for {} videos...".format(search))
display = Display(visible=0, size=(800, 600))
display.start()
driver = webdriver.Chrome()
driver.get("https://www.youtube.com/results?search_query="+search)
elems = driver.find_elements_by_id('video-title')
counter=0
for elem in elems:
    if counter >5:
        break
    else:  
        href = elem.get_attribute('href')
        aria_label = elem.get_attribute('aria-label')
        if href is not None:
            print("\n"+aria_label+":")
            print("Link: " +href)
            counter=counter+1
            
driver.close()
display.stop()