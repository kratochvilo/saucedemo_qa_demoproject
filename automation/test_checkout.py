from playwright.sync_api import Page, expect
import pytest

def test_checkout(setup_cart, page: Page):
    page.locator("[data-test='checkout']").click()
    page.locator("[data-test='firstName']").fill("Marek")
    page.locator("[data-test='lastName']").fill("Vrána")
    page.locator("[data-test='postalCode']").fill("53001")
    page.locator("[data-test='continue']").click()

    expect(page.locator("[data-test='inventory-item-name']")).to_contain_text("Sauce Labs Backpack")
    expect(page.locator("[data-test='subtotal-label']")).to_contain_text("29.99")
    expect(page.locator("[data-test='tax-label']")).to_contain_text("2.40")
    expect(page.locator("[data-test='total-label']")).to_contain_text("32.39")


    page.locator("[data-test='finish']").click()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(page.locator("[data-test='complete-header']")).to_contain_text("Thank you for your order!")
    expect(page.locator("[data-test='complete-text']")).to_contain_text("Your order has been dispatched, and will arrive just as fast as the pony can get there!")



    
