from playwright.sync_api import Page, expect

import pytest

@pytest.fixture
def setup_login(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("secret_sauce")
    page.locator("[data-test='login-button']").click()

def test_add_to_cart(setup_login, page: Page):
    page.locator("[data-test='add-to-cart-sauce-labs-backpack']").click()
    page.locator("[data-test='shopping-cart-link']").click()

    expect(page.locator("[data-test='inventory-item-name']")).to_contain_text("Sauce Labs Backpack")
    expect(page.locator("[data-test='remove-sauce-labs-backpack']")).to_be_visible()
