from locators import *
from settings import fake_login, fake_phone, fake_email, invalid_ls


def test_tab_switching(browser):
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD ).text == 'Электронная почта'
    print( "\n'Почта' активна" )

    browser.find_element( *AutoPageLoc.LOCATOR_PHONE_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_PHONE_FIELD ).text == 'Мобильный телефон'
    print( "\n'Tелефон' активен" )

    browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_FIELD ).text == 'Логин'
    print( "\n'Логин' активен" )

    browser.find_element( *AutoPageLoc.LOCATOR_LS_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LS_FIELD ).text == 'Лицевой счёт'
    print( "\n'Лицевой счёт' активен" )

    print( "\nТест пройден" )


def test_tab_auto_switching_phone(browser):
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV ).send_keys( fake_phone )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()

    assert browser.find_element( *AutoPageLoc.LOCATOR_PHONE_FIELD ).text == 'Мобильный телефон'
    print( "\nПереход на 'Телефон' с 'Почта' произошел " )
    print( "\nТест пройден" )


def test_tab_auto_switching_mail(browser):
    browser.find_element( *AutoPageLoc.LOCATOR_PHONE_FIELD_ACTIV ).send_keys( fake_email )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD ).text == 'Электронная почта'
    print( "\nПереход на 'Почта' с 'Телефон' произошел " )

    browser.find_element( *AutoPageLoc.LOCATOR_LS_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_LS_FIELD_ACTIV ).send_keys( fake_email )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD ).text == 'Электронная почта'
    print( "\nПереход на 'Почта' с 'Лицевой счет' произошел " )

    browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_FIELD_ACTIV ).send_keys( fake_email )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD ).text == 'Электронная почта'
    print( "\nПереход на 'Почта' с 'Логин' произошел " )

    print( "\nТест пройден" )


def test_tab_auto_switching_login(browser):
    browser.find_element( *AutoPageLoc.LOCATOR_PHONE_FIELD_ACTIV ).send_keys( fake_login )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_FIELD ).text == 'Логин'
    print( "\nПереход на 'Логин' с 'Телефон' произошел " )

    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV ).send_keys( fake_login )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_FIELD ).text == 'Логин'
    print( "\nПереход на 'Логин' с 'Почта' произошел " )

    browser.find_element( *AutoPageLoc.LOCATOR_LS_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_LS_FIELD_ACTIV ).send_keys( fake_login )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LOGIN_FIELD ).text == 'Логин'
    print( "\nПереход на 'Логин' с 'Лицевой счет' произошел " )

    print( "\nТест пройден" )


def test_tab_auto_switching_ls(browser):
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_TAB ).click()
    browser.find_element( *AutoPageLoc.LOCATOR_MAIL_FIELD_ACTIV ).send_keys( invalid_ls )
    browser.find_element( *AutoPageLoc.LOCATOR_PASSWORD_TAB ).click()
    assert browser.find_element( *AutoPageLoc.LOCATOR_LS_FIELD ).text == 'Лицевой счёт'
    print( "\nПереход на 'Лицевой счет' с 'Почта' произошел " )
    print( "\nТест пройден" )