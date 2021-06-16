from selenium import webdriver
import time

driver = webdriver.Chrome(r"C:\Users\1E\PycharmProjects\auto_MMSE_ADL\chromedriver.exe")
driver.implicitly_wait(10)  # 隱含等待時間
PATH = 'https://ecpa.dgpa.gov.tw/uIAM/clogin.asp?destid=CrossHRD'  # 登入網址
def set(a,b):
    driver.get(PATH)
    driver.find_element_by_id('username').send_keys(a)
    driver.find_element_by_id('password').send_keys(b)
    driver.find_element_by_name('submit').click()
    driver.find_element_by_xpath('/html/body/div[4]/div/div/a').click()
    return driver
#CEDAW第5條「社會文化之改變與母性之保障」
def lesson6(name,coursename):
    try:
        driver.get('https://elearn.hrd.gov.tw/info/10020975')
        driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[4]/div/div[1]/div[2]/div/div[3]/div[2]/button').click()
        driver.switch_to.frame('s_catalog')
        driver.switch_to.frame('pathtree')
        driver.find_element_by_xpath('//*[@id="tree11"]/span/a').click()
        time.sleep(500)
        driver.find_element_by_xpath('//*[@id="tree2_1"]/span/a').click()
        time.sleep(380)
        driver.find_element_by_xpath('//*[@id="tree2_2"]/span/a').click()
        time.sleep(740)
        driver.find_element_by_xpath('//*[@id="tree2_3"]/span/a').click()
        time.sleep(380)
        driver.find_element_by_xpath('//*[@id="tree2_4"]/span/a').click()
        time.sleep(325)
        driver.find_element_by_xpath('//*[@id="tree2_5"]/span/a').click()
        time.sleep(335)
        driver.find_element_by_xpath('//*[@id="tree2_6"]/span/a').click()
        time.sleep(345)
        driver.find_element_by_xpath('//*[@id="tree2_7"]/span/a').click()
        time.sleep(140)
        driver.find_element_by_xpath('//*[@id="tree3_1"]/span/a').click()
        time.sleep(210)
        driver.find_element_by_xpath('//*[@id="tree3_2"]/span/a').click()
        time.sleep(400)
        driver.find_element_by_xpath('//*[@id="tree3_3"]/span/a').click()
        time.sleep(225)
        driver.find_element_by_xpath('//*[@id="tree3_4"]/span/a').click()
        time.sleep(80)
        driver.find_element_by_xpath('//*[@id="tree4_1"]/span/a').click()
        time.sleep(580)
        driver.find_element_by_xpath('//*[@id="tree4_2"]/span/a').click()
        time.sleep(180)
        driver.find_element_by_xpath('//*[@id="tree4_3"]/span/a').click()
        time.sleep(450)
        driver.find_element_by_xpath('//*[@id="tree4_4"]/span/a').click()
        time.sleep(300)
        driver.find_element_by_xpath('//*[@id="tree4_5"]/span/a').click()
        time.sleep(500)

        print(name + '[' + coursename + ']' + '完成了!!')

    except:
        print(name + '[' + coursename + ']' + '出現問題!!')
    # driver.close()