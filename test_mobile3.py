#Проверка
# «Создание заказа на доставку с оплатой
# через Kaspi для авторизированного пользователя с добавлением нового адреса»
from playwright.sync_api import sync_playwright, expect
import time
import allure
import json


@allure.step("Нажатие на продукт Парацетамол")
def test_click_paracetomol():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(**p.devices["Pixel 5"],
                                      permissions=["geolocation"],
                                      geolocation={"latitude": 37.7749, "longitude": -122.4194},
                                      locale='en-US')
        page = context.new_page()
        page.goto("https://daribar.kz/")
        # Загрузка данных в localStorage
        with open("storage_load_deskctop.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)

        page.evaluate('''(data) => {
                               for (const key in data) {
                                   localStorage.setItem(key, data[key]);
                                   }
                               }''', local_storage_data)
        page.reload()
        page.locator("input").click()
        page.locator("input").fill("Парацетомол")
        sel = page.get_by_text("Парацетамол таблетки 500 мг №10").first
        if sel:
            sel.click()
        else:
            print("ERROR: test_click_paracetomol")
        page.wait_for_timeout(3000)
        local_storage = page.evaluate('''() => {
                                        let data = {};
                                        for (let i = 0; i < localStorage.length; i++) {
                                            let key = localStorage.key(i);
                                            data[key] = localStorage.getItem(key);
                                        }
                                        return data;
                                    }''')
        with open("storage_load.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        time.sleep(2)
        browser.close()


@allure.step("Добавление в корзину (верхняя панель)")
def test_h_korzina():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(**p.devices["Pixel 5"],
                                      permissions=["geolocation"],
                                      geolocation={"latitude": 37.7749, "longitude": -122.4194},
                                      locale='en-US')
        page = context.new_page()
        page.goto("https://daribar.kz/products/paracetamol-0-5-10--3c20eebe-3ee1-4d9e-bd34-0ba2afd85286")
        # Загрузка данных в localStorage
        with open("storage_load.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)

        page.evaluate('''(data) => {
                                      for (const key in data) {
                                          localStorage.setItem(key, data[key]);
                                          }
                                      }''', local_storage_data)
        page.reload()
        sel = page.locator(".mobile_buttonCartMobile__5VkmO")
        sel.click()
        time.sleep(2)
        local_storage = page.evaluate('''() => {
                                                let data = {};
                                                for (let i = 0; i < localStorage.length; i++) {
                                                    let key = localStorage.key(i);
                                                    data[key] = localStorage.getItem(key);
                                                }
                                                return data;
                                            }''')
        with open("storage_load2.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        browser.close()


@allure.step("Поиск ближайшей аптеки")
def test_naiti_apteka():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(**p.devices["Pixel 5"],
                                      permissions=["geolocation"],
                                      geolocation={"latitude": 37.7749, "longitude": -122.4194},
                                      locale='en-US')
        page = context.new_page()
        page.goto("https://daribar.kz/cart")
        with open("storage_load2.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)

        page.evaluate('''(data) => {
                                      for (const key in data) {
                                          localStorage.setItem(key, data[key]);
                                          }
                                      }''', local_storage_data)
        page.reload()
        page.get_by_text("Найти в аптеках").click()
        local_storage = page.evaluate('''() => {
                                                        let data = {};
                                                        for (let i = 0; i < localStorage.length; i++) {
                                                            let key = localStorage.key(i);
                                                            data[key] = localStorage.getItem(key);
                                                        }
                                                        return data;
                                                    }''')
        with open("storage_load3.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        browser.close()


@allure.step("Переход к оформлению заказа")
def test_ofo_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(**p.devices["Pixel 5"],
                                      permissions=["geolocation"],
                                      geolocation={"latitude": 37.7749, "longitude": -122.4194},
                                      locale='en-US')
        page = context.new_page()
        page.goto("https://daribar.kz/pharmacies")
        with open("storage_load3.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)

        page.evaluate('''(data) => {
                                      for (const key in data) {
                                          localStorage.setItem(key, data[key]);
                                          }
                                      }''', local_storage_data)
        page.reload()
        sel = page.get_by_text("Перейти к оформлению 110₸").first
        sel.click()
        time.sleep(2)
        local_storage = page.evaluate('''() => {
                                                                let data = {};
                                                                for (let i = 0; i < localStorage.length; i++) {
                                                                    let key = localStorage.key(i);
                                                                    data[key] = localStorage.getItem(key);
                                                                }
                                                                return data;
                                                            }''')
        with open("storage_load4.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        browser.close()


@allure.step("Выбор метода доставки")
def test_dos():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(**p.devices["Pixel 5"],
                                      permissions=["geolocation"],
                                      geolocation={"latitude": 37.7749, "longitude": -122.4194},
                                      locale='en-US')
        page = context.new_page()
        page.goto("https://daribar.kz/checkout")
        with open("storage_load4.json", 'r', encoding='utf-8') as f:
            local_storage_data = json.load(f)

        page.evaluate('''(data) => {
                                             for (const key in data) {
                                                 localStorage.setItem(key, data[key]);
                                                 }
                                             }''', local_storage_data)
        page.reload()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="Доставка").click()
        page.locator(".AllAddressesModalModal_buttonApply__YP6oz").click()
        page.wait_for_timeout(3000)
        sel = page.locator("#suggest")
        sel.fill("Гоголя,20")
        page.wait_for_timeout(2000)
        page.click('input[name="address"]')
        page.type('input[name="address"]', 'Улица Гоголя,20')
        sel=page.locator('.AddressModalMap_listContainer__6bBgb').first
        sel.click()
        page.locator(".AddressModalMap_submitButton__OKRE5").click()
        page.wait_for_timeout(2000)
        page.get_by_role("button", name="Сохранить").click()
        page.wait_for_timeout(2000)
        sel2=page.locator(".DeliveryTimeSwitchContent_descriptionContainer__4ug7N").first
        sel2.click()
        page.get_by_text("Оформить заказ").click()
        local_storage = page.evaluate('''() => {
                                                                let data = {};
                                                                for (let i = 0; i < localStorage.length; i++) {
                                                                    let key = localStorage.key(i);
                                                                    data[key] = localStorage.getItem(key);
                                                                }
                                                                return data;
                                                            }''')
        with open("storage_load5.json", 'w', encoding='utf-8') as f:
            json.dump(local_storage, f, ensure_ascii=False, indent=4)
        browser.close()

def test_dari():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Установите headless=True, если не хотите открывать браузер
        context = browser.new_context(**p.devices["Pixel 5"],permissions=["geolocation"],
            geolocation={"latitude": 37.7749, "longitude": -122.4194},
            locale='en-US')
        page1 = context.new_page()
        page1.goto("https://dev.daribar.kz/")

