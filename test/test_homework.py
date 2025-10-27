import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_google_search(driver):
    
    url = 'https://www.google.com/'
    driver.get(url)
    assert driver.current_url == url


def test_github_web(driver):
    url = 'https://github.com/'
    driver.get(url)
    assert driver.current_url == url
