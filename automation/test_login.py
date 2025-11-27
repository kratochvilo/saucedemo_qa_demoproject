from playwright.sync_api import Page, expect

def test_login_success(page: Page):
    # 1. Otevřít stránku (Precondition)
    page.goto("https://www.saucedemo.com/")
    
    # 2. Vyplnit Username (Step 1)
    # Playwright hledá element podle atributu 'data-test', což je best practice
    page.locator("[data-test='username']").fill("standard_user")
    
    # 3. Vyplnit Password (Step 2)
    page.locator("[data-test='password']").fill("secret_sauce")
    
    # 4. Kliknout na Login (Step 3)
    page.locator("[data-test='login-button']").click()
    
    # 5. Ověření (Expected Result)
    # Zkontrolujeme, že jsme na stránce inventory
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    # Zkontrolujeme, že je vidět nadpis "Products"
    expect(page.locator(".title")).to_contain_text("Products")


def test_login_failed_invalid_password(page: Page):
    # 1. Jdi na stránku
    page.goto("https://www.saucedemo.com/")
    
    # 2. Vyplň správné Username (standard_user)
    page.locator("[data-test='username']").fill("standard_user")

    # 3. Vyplň ŠPATNÉ Password (vymysli si ho)
    page.locator("[data-test='password']").fill("incorrect_password")

    # 4. Klikni na Login tlačítko
    page.locator("[data-test='login-button']").click()

    # 5. Ověř chybovou hlášku
    # Tady musíš použít ten selektor, který jsi našel v kroku "Tvoje mise"
    error_message = page.locator("[data-test='error']")
    
    # Ověříme, že text obsahuje "Epic sadface"
    expect(error_message).to_contain_text("Epic sadface: Username and password do not match any user in this service")