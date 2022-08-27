
# Press the green button in the gutter to run the script.
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time

invalidUrl=[
    "www.zhihu.com",
    "www.bilibili.com"
]

def checkValidUrl(url:str) -> bool:
    for inUrl in invalidUrl:
        if inUrl in url:
            return False
        else:
            return True


if __name__ == "__main__":
    options = Options()
    options.add_experimental_option("debuggerAddress", "127.0.0.1:12306")
    options.add_argument("headless")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    print(driver.title)
    # 打开新标签页（第二页）
    while(1):
        handles = driver.window_handles
        for handle in handles:
            driver.switch_to.window(handle)
            print(driver.current_url)
            if not checkValidUrl(driver.current_url):
                driver.close()
        driver.switch_to.window(handles[0])
        time.sleep(10)





