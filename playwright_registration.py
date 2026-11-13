import pytest
import re
from playwright.sync_api import Page, expect

def test_registration_form(page: Page):
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    email_input = page.get_by_test_id("registration-form-email-input")
    username_input = page.get_by_test_id("registration-form-username-input")
    password_input = page.get_by_test_id("registration-form-password-input")
    reg_button = page.get_by_test_id("registration-page-registration-button")
    dashboard_title = page.get_by_test_id("dashboard-page-title")

    email_input.fill("user.name@gmail.com")
    username_input.fill("username")
    password_input.fill("password")

    expect(email_input).to_have_value("user.name@gmail.com")
    expect(username_input).to_have_value("username")
    expect(password_input).to_have_value("password")
    expect(reg_button).to_be_enabled()
    reg_button.click()
    expect(page).to_have_url(re.compile(".*dashboard"))
    expect(dashboard_title).to_be_visible()
