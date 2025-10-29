from selenium.webdriver.chrome.webdriver import WebDriver


def test_google_search(driver: WebDriver):
    
    url = 'https://www.google.com/'
    driver.get(url)
    assert driver.title == 'Google'
    assert driver.current_url == url


def test_github_web(driver: WebDriver):
    url = 'https://github.com/'
    driver.get(url)
    assert 'GitHub' in driver.title
    assert driver.current_url == url
