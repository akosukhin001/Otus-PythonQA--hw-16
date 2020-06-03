import time


# '''
def test_google_0(remote):
    remote.get("https://google.ru")
    remote.find_element_by_id("footer")
    remote.find_element_by_id("hplogo")
    assert remote.title == "Google"
    time.sleep(2)


def test_yandex_0(remote):
    remote.get("https://ya.ru")
    remote.find_element_by_id("text")
    remote.find_element_by_css_selector("a[title='Яндекс']")
    assert remote.title == "Яндекс"
    time.sleep(2)


def test_avito_0(remote):
    remote.get("https://avito.ru")
    remote.find_element_by_id("category")
    remote.find_element_by_id("search")
    assert "Авито" in remote.title
    time.sleep(2)


def test_google_1(remote):
    remote.get("https://google.ru")
    remote.find_element_by_id("footer")
    remote.find_element_by_id("hplogo")
    assert remote.title == "Google"
    time.sleep(2)


def test_yandex_1(remote):
    remote.get("https://ya.ru")
    remote.find_element_by_id("text")
    remote.find_element_by_css_selector("a[title='Яндекс']")
    assert remote.title == "Яндекс"
    time.sleep(2)


def test_avito_1(remote):
    remote.get("https://avito.ru")
    remote.find_element_by_id("category")
    remote.find_element_by_id("search")
    assert "Авито" in remote.title
    time.sleep(2)


# '''


def test_cart(remote):
    remote.get("https://demo.opencart.com/")
    cart = remote.find_element_by_css_selector('#cart-total')
    cart.click()
    time.sleep(2)


def test_nav_links(remote):
    remote.get("https://demo.opencart.com/")
    remote.find_element_by_css_selector('ul.nav > li')
    time.sleep(2)


def test_search(remote):
    remote.get("https://demo.opencart.com/")
    search = remote.find_element_by_css_selector('[name=search]')
    search.send_keys('test')
    search.clear()
    time.sleep(2)


def test_currency(remote):
    remote.get("https://demo.opencart.com/")
    remote.find_element_by_css_selector('#form-currency')
    time.sleep(2)
