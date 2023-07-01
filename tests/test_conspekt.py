from selene import browser, have
browser.config.driver = 'firefox' # Указываем через какой браузер открываем
browser.config.window_width = 1920 # Указываем размеры экрана
browser.config.window_height = 1080 # Указываем размеры экрана

# Открытие браузера через относительный урл. Просто передаём урл через .config. А в browser.open указываем '/'
# Удобно использовать когда нужно много раз в тестах открывать конкретный урл- его достаточно прописать тут а в опен проста ставить слэш
def test_openbrowser():
    browser.open('/')
    browser.element('[name=login]').click().type('timur.garaev.91@mail.ru') # находит элемент по селектуру. кликаем/пишем текст/нажимаем таб
    browser.element('[name=password]').click().type('qazwsx123').press_enter()
    browser.element('').should(have.text('Транзакции'))
    # browser.all() # находит все элементы по селектуру
    # Открытие браузера через browser.open
def test_openbrowser_test2():
    browser.open('https://lk.atolpay.ru')