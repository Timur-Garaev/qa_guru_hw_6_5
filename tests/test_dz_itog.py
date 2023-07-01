from selene import browser, be, have


def test_filling_out_and_submitting_the_form():
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('#firstName').click().type('Timur')
    browser.element('#lastName').click().type('Garaev')
    browser.element('#userEmail').click().type('testguru@mail.ru')
    browser.element('#gender-radio-1').click()
    browser.element('#userNumber').click().type('8999999999')
    browser.element('#dateOfBirthInput').click().element('[class=react-datepicker__year-select]')\
        .click() ## тут надо разобраться как скроллить
    browser.element('#hobbies-checkbox-1').click()
    browser.element('#uploadPicture').click() ## тут надо разобраться как выбрать конкретный файл коорый хочу загрузить
    browser.element('#currentAddress').click().type('testaddress')
    browser.element('#state').click() # тут надо разобратсья как выбрать из выпадающего списка так как селектор скрыввается и нельзщя его определить а ещё не совсем правильон выбрал селектор надо все таки ориентироватсья на стрелочку
    browser.element('#city').click() # тут надо разобратсья как выбрать из выпадающего списка так как селектор скрыввается и нельзщя его определить а ещё не совсем правильон выбрал селектор надо все таки ориентироватсья на стрелочку
    browser.element('#submit').click()
    browser.element('#example-modal-sizes-title-lg').shoul(have.exact_text('Thanks for submitting the form'))