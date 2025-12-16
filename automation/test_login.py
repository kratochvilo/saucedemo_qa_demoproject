from playwright.sync_api import Page, expect
import pytest


def test_login_success(setup_login, page: Page):
    expect(page).to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator(".title")).to_contain_text("Products")


def test_login_failed_invalid_password(page: Page):
    page.goto("https://www.saucedemo.com/")
    page.locator("[data-test='username']").fill("standard_user")
    page.locator("[data-test='password']").fill("invalidword")
    page.locator("[data-test='login-button']").click()

    error_message = page.locator("[data-test='error']")
    expect(error_message).to_contain_text("Epic sadface: Username and password do not match any user in this service")


def test_logout(setup_login, page: Page):
    page.locator("#react-burger-menu-btn").click()
    logout_link = page.locator("#logout_sidebar_link")
    expect(logout_link).to_be_visible()
    #expect(page.locator)("#logout_sidebar_link").to_be_visible()

    page.locator("#logout_sidebar_link").click()

    expect(page).to_have_url("https://www.saucedemo.com/")


    