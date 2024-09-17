# roblox-module-condo

# 😎 This module will help you manage your account, log in to it, as well as register in the future.


The module file.py contains a class with functions that you can use.

# 🧐 DOCUMENTATION

# Important: The functions are completely asyncio and suitable for multitasking.

The function for logging in to the account (Checks for errors and increases the time of logging in to the account):

Python:
status_code = await module.login(username="user", password="password")

and 

Performs entry without checks quickly enough:

Python:
status = await module.login(username="user", password="password")



