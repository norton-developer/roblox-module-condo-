from module import RobloxModule
import  asyncio


# ! PLEASE LOOK AT THE DOCUMENTATION FOR THE GITHUB CODE TO GET TO KNOW ITS FUNCTIONS BETTER!
# * THE MODULE.py FILE CONTAINS ALL THE FUNCTIONALITY USE ITS FUNCTIONS IN THE MAIN.py FILE
# ? VERSION 1.5


async def main():
 module = RobloxModule()
 status_code = await module.fast_login(username="user", password="password")
 print(str(status_code))






asyncio.run(main())