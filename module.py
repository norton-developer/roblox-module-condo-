
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import asyncio


# Status
error_login = "Error: Incorrect username or password."
success_login = "Succes: You are logged in to your account."
fast_login = ""


#Status Code


class RobloxModule:
    def __init__(self):
        self.chrome = webdriver.Chrome(ChromeDriverManager().install())

    async def login(self, username, password):
        # A regular login for a full error check when logging in.

        self.chrome.get("https://www.roblox.com/login")

        username_field = self.chrome.find_element("id", "login-username")
        username_field.send_keys(username)

        password_field = self.chrome.find_element("id", "login-password")
        password_field.send_keys(password)

        login_button = self.chrome.find_element("id", "login-button")
        login_button.click()
        await asyncio.sleep(4)

        try:
         login_error = self.chrome.find_element("id", "login-form-error")
         return error_login
        except Exception as error:
            self.chrome.get("https://www.roblox.com/home")
            await asyncio.sleep(4)
            return success_login



    async def fast_login(self, username, password):
        #Use fast_login if you are sure that your account username and password are correct and you have a good Internet connection.

        self.chrome.get("https://www.roblox.com/login")

        username_field = self.chrome.find_element("id", "login-username")
        username_field.send_keys(username)

        password_field = self.chrome.find_element("id", "login-password")
        password_field.send_keys(password)

        login_button = self.chrome.find_element("id", "login-button")
        login_button.click()
        await asyncio.sleep(3)
        self.chrome.get("https://www.roblox.com/home")
        return 200



