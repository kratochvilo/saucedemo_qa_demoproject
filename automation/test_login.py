from playwright.sync_api import Page, expect

import pytest
# ... importy playwright ...

@pytest.fixture
def setup_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test='username']").fill("standard_user")

def test_login_success(setup_login, page: Page):
    page.locator("[data-test='password']").fill("secret_sauce")
    
    page.locator("[data-test='login-button']").click()
    
    # Zkontrolujeme, že jsme na stránce inventory
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    
    # Zkontrolujeme, že je vidět nadpis "Products"
    expect(page.locator(".title")).to_contain_text("Products")


def test_login_failed_invalid_password(setup_login, page: Page):
    page.locator("[data-test='password']").fill("incorrect_password")

    # Klikni na Login tlačítko
    page.locator("[data-test='login-button']").click()

    # Ověř chybovou hlášku
    error_message = page.locator("[data-test='error']")
    
    # Ověříme, že text obsahuje "Epic sadface"
    expect(error_message).to_contain_text("Epic sadface: Username and password do not match any user in this service")