from playwright.sync_api import Page, expect

import pytest

def test_add_to_cart(setup_login, page: Page):
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator("[data-test='shopping-cart-link']").click()

    expect(page.locator("[data-test='inventory-item-name']")).to_contain_text("Sauce Labs Backpack")
    expect(page.locator("[data-test='remove-sauce-labs-backpack']")).to_be_visible()


def test_purchase_flow_with_item_removal(setup_cart, page: Page):
    backpack_item = page.locator("text=Sauce Labs Backpack")

    page.locator("[data-test='continue-shopping']").click()
    page.locator("[data-test='add-to-cart-sauce-labs-fleece-jacket']").click()

    page.locator("[data-test='shopping-cart-link']").click()
    page.locator("[data-test='remove-sauce-labs-backpack']").click()

    expect(backpack_item).not_to_be_visible()
    # expect(page.locator(".cart_item")).to_have_count(1)

    page.locator("[data-test='checkout']").click()
    page.locator("[data-test='firstName']").fill("Karel")
    page.locator("[data-test='lastName']").fill("Slavík")
    page.locator("[data-test='postalCode']").fill("12345")
    page.locator("[data-test='continue']").click()

    expect(page.locator("[data-test='inventory-item-name']")).to_contain_text("Sauce Labs Fleece Jacket")
    expect(page.locator("[data-test='subtotal-label']")).to_contain_text("49.99")
    expect(page.locator("[data-test='tax-label']")).to_contain_text("4.00")
    expect(page.locator("[data-test='total-label']")).to_contain_text("53.99")

    page.locator("[data-test='finish']").click()

    expect(page).to_have_url("https://www.saucedemo.com/checkout-complete.html")
    expect(page.locator("[data-test='complete-header']")).to_contain_text("Thank you for your order!")
    expect(page.locator("[data-test='complete-text']")).to_contain_text("Your order has been dispatched, and will arrive just as fast as the pony can get there!")

