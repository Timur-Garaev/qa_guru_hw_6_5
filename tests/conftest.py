import pytest
from selene import browser
from selenium import webdriver
@pytest.fixture(scope='function', autouse=True) # scoupe =function - фикстура вызывается для функции. autouse=True функция всегда вызывается автоматически
def brawser_management():
    browser.config.driver_name = 'firefox'
    # на самом деле обычно делают так как ниже чтоб конфигурировать браузер верхний код для простаков
    # driver_options = webdriver.FirefoxOptions()
    # driver_options.add_argument('--headless') - добавляем аргумент -браузер в невидимом режиме
    # browser.config.driver_options = driver_options - передаём в конфиг настройки
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://lk.atolpay.ru'

    yield # команда которая передаёт выполнение тесту. все что выше это выполняется как предусловие все что ниже это выполняется после теста

    browser.quit()