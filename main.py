# Import neccesary modules for this application
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from termcolor import colored

# import time module so i can pause the program between tasks to let the page load
import time

# user inputs
username = input(colored('Please enter your username: ', 'green'))
password = input(colored("Please enter your password: ", 'red'))
bio = input(colored('Please enter your desired bio: ', "blue" ))

#initialize the driver, will install if not found
driver = webdriver.Chrome(ChromeDriverManager().install())

class InstagramBot: 
    def __init__(self, username, password, bio):
        self.username = username
        self.password = password
        self.bio = bio
        self.driver = driver

    def close(self):
        self.driver.close()

    def login(self):
        print("Logging in")
        self.driver.get("https://www.instagram.com/")
        time.sleep(1)
        login_button = self.driver.find_element_by_xpath("/html[@class='js not-logged-in client-root js-focus-visible sDN5V']/body/div[@id='react-root']/section[@class='_9eogI E3X2T']/main[@class='SCxLW  o64aR ']/article[@class='_4_yKc']/div[@class='rgFsT ']/div[@class='gr27e']/p[@class='izU2O']/a")
        login_button.click()
        time.sleep(.5)
        user_name_input = self.driver.find_element_by_xpath("//input[@name='username']")
        user_name_input.clear()
        user_name_input.send_keys(self.username)
        password_name_input = self.driver.find_element_by_xpath("//input[@name='password']")
        password_name_input.clear()
        password_name_input.send_keys(self.password)
        password_name_input.send_keys(Keys.RETURN)
        time.sleep(1.5)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]").click()
    
    def like_first_photo(self):
        print('liking first photo on time-line')
        self.driver.get('https://www.instagram.com/')
        # while self.driver.execute_script("return document.body.scrollHeight") < 50000:
        #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        like_buttons = self.driver.find_elements_by_xpath("//button[@class='wpO6b ']")
        like_buttons[0].click()

    def change_bio(self):
        self.driver.get("https://www.instagram.com/" + self.username)
        options_button = self.driver.find_element_by_xpath("//button[@class='sqdOP  L3NKy _4pI4F   _8A5w5    ']")
        options_button.click()
        time.sleep(1)
        bio_input_area = self.driver.find_element_by_xpath("//textarea[@class='p7vTm']")
        bio_input_area.clear()
        bio_input_area.send_keys(self.bio)
        edit_profile_submit_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Submit')]")
        time.sleep(.5)
        edit_profile_submit_button.click()
        self.driver.get("https://www.instagram.com/" + self.username)

bot1 = InstagramBot(username, password, bio)
bot1.login()
bot1.like_first_photo()
bot1.change_bio()
print('end')
time.sleep(60)
bot1.close()