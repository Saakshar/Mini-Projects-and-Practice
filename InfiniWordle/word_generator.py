from selenium import webdriver
from selenium.webdriver.common.by import By
class file_gen():
    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("detach", True)
    def gen(self,num):
        d = webdriver.Chrome(options=self.options)
        d.get(f"https://www.wordsdetail.com/{num}-letter-words/")
        words=d.find_elements(By.CSS_SELECTOR, "ul li")
        # with open(f"words({num}).csv","w") as file:
        #     file.write("")
        with open(f"words({num}).csv", "a") as file:
            for word in words:
                try:
                    if len(word.text)==int(num):
                        print(word.text)
                        file.write(f"{word.text.lower()}\n")
                except:
                    pass
        print("***finished file generation***")
        d.quit()
    def gen2(self,num):
        d = webdriver.Chrome(options=self.options)
        d.get(f"https://byjus.com/english/{num}-letter-words/")
        words = d.find_elements(By.CSS_SELECTOR, "tr td")
        # with open(f"words({num})^#.csv", "w") as file:
        #     file.write("")
        with open(f"words({num})^#.csv", "a") as file:
            for word in words:
                try:
                    if len(word.text) == int(num):
                        print(word.text)
                        file.write(f"{word.text.lower()}\n")
                except:
                    pass
        print("***finished file generation***")
        d.quit()
