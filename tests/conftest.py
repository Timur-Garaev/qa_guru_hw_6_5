import pytest
from selene import browser
from selenium import webdriver
@pytest.fixture(scope='function', autouse=True) # scoupe =function - фикстура вызывается для функции. autouse=True функция всегда вызывается автоматически
def brawser_management():
    browser.config.base_url = 'https://demoqa.com'
    yield # команда которая передаёт выполнение тесту. все что выше это выполняется как предусловие все что ниже это выполняется после теста

    browser.quit()