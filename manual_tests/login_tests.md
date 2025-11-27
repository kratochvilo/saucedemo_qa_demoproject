# Test Suite: Login Functionality

| ID | Title | Preconditions | Test Steps | Test Data | Expected Result |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **TC_LOGIN_01** | **Successful Login** | 1. Browser opened<br>2. URL `https://www.saucedemo.com/` | 1. Enter valid username<br>2. Enter valid password<br>3. Click "Login" button | **User:** standard_user<br>**Pass:** secret_sauce | User is redirected to `/inventory.html`, products are visible. |
| **TC_LOGIN_02** | **Login with invalid password** | 1. Browser opened<br>2. URL `https://www.saucedemo.com/` | 1. Enter valid username<br>2. Enter invalid password<br>3. Click "Login" button | **User:** standard_user<br>**Pass:** invalidword | Error message is displayed: *"Epic sadface: Username and password do not match any user in this service"* |