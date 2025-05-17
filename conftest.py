import pytest
from selenium import webdriver

# фикстура иницализации драйвера
@pytest.fixture(autouse=True)
def driver(request):
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--window-size=1920,1080")
    chrome_options.add_argument("--disable-cache")
    chrome_options.page_load_strategy = "normal"
    chrome_options.add_argument(
        "--user-agent=Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36")
    chrome_options.add_argument("disable-blink-features=AutomationControlled")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    chrome_options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver # создаем атрибут класса внутри класса (не надо прокидывать фикстуру в тест). driver доступен через self, но без автодополнения
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    yield
    driver.quit()