import os.path

from selene import browser, have

browser.config.window_width = 1920
browser.config.window_height = 1080

def test_filling_out():
    browser.open('/automation-practice-form')

    # WHEN
    browser.element('#firstName').type('Timur')
    browser.element('#lastName').type('Garaev')
    browser.element('#userEmail').type('testguru@mail.ru')
    browser.element('[name=gender][value=Male] + label').click()
    browser.element('#userNumber').type('8999999999')
    #browser.element('#dateOfBirthInput').click().element('.react-datepicker__year-select').click().element('[value="2010"]').click().element('[class="react-datepicker__day react-datepicker__day--013"]').click() ## тут надо разобраться как скроллить
    browser.element('#subjectsInput').type('Hindi') # тут пропустил одно поле
    browser.all('[id^=hobbies-checkbox]').element_by(have.exact_text('Sports')).click()
    #browser.element('#uploadPicture').send_value(os.path.abspath(os.path.join)) ## тут надо разобраться как выбрать конкретный файл коорый хочу загрузить
    browser.element('#currentAddress').type('testaddress')
    browser.element('#state').click().all('[id^=react-select][id*=option]').element_by(have.exact_text('Haryana')).click()
    browser.element('#city').click().all('[id^=react-select][id*=option]').element_by(have.exact_text('Karnal')).click()
    browser.element('#submit').click()

    # THEN
    browser.element('#example-modal-sizes-title-lg').should(have.exact_text('Thanks for submitting the form')) # тут плохой селектор но я решил оставить