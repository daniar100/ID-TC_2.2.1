import os
import json
from playwright.sync_api import sync_playwright
import allure

def test_main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            **p.devices["Pixel 5"],
            permissions=["geolocation"],
            geolocation={"latitude": 37.7749, "longitude": -122.4194},
            locale='en-US',
        )

        page = context.new_page()
        page.goto("https://dev.daribar.kz/")
        # Загрузка данных в localStorage
        local_storage_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "local_storage.json")
        with open(local_storage_file_path, 'r', encoding='utf-8') as local_storage_file:
            local_storage = json.load(local_storage_file)
            page.evaluate("""(local_storage) => {
                        localStorage.setItem('daribar', JSON.stringify(local_storage.daribar));
                    }""", local_storage)

        # Обновление страницы
        page.reload()
        @allure.step("paracetomol")
        def test_paracetomol():
            page.locator("input").click()
            page.locator("input").fill("фен")
            page.wait_for_timeout(2000)

        test_paracetomol()

        @allure.step("click_paracetomol")
        def test_click_paracetomol():
            sel = page.get_by_text(" Нью капли 20 мл ")
            if sel:
                sel.click()
            else:
                print("ERROR: test_click_paracetomol")
            page.wait_for_timeout(2000)

        test_click_paracetomol()

        @allure.step("h_korzina")
        def test_h_korzina():
            page.locator(".mobile_cartButtonMobile__Vjy0_").click()
            page.wait_for_timeout(2000)

        test_h_korzina()

        @allure.step("mon_korzina")
        def test_mou_korzina():
            sel = page.locator(".mobile_counterBlockMobile__L_1De")
            if sel:
                sel.click()
            else:
                print("ERROR: test_mou_korzina")
            page.wait_for_timeout(2000)

        test_mou_korzina()

        @allure.step("naiti_apteka")
        def test_naiti_apteka():
            sel = page.get_by_text("Найти в аптеках")
            if sel:
                sel.click()
            else:
                print("ERROR: test_naiti_apteka")
            page.wait_for_timeout(2000)

        test_naiti_apteka()

        @allure.step("ofo_form")
        def test_ofo_form():
            sel = page.get_by_role("button", name="Перейти к оформлению 2560₸").first
            sel.click()
            page.wait_for_timeout(2000)

        test_ofo_form()

        @allure.step("apteka")
        def test_click_apteka():
            page.locator(".OrderForm_paymentBlockKaspi__NwO23").click()

        test_click_apteka()
        @allure.step("zak")
        def test_zak():
            page.get_by_text("Оформить заказ").click()
        test_zak()
        page.wait_for_timeout(4000)
        page.goto("https://dev.daribar.kz/")
        page.wait_for_timeout(4000)
        browser.close()

if __name__ == "__main__":
    test_main()



