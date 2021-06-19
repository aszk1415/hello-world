from selenium import webdriver
import time
#OK
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 隱含等待時間

def set(a,b,c):
    if c == '1':
        driver.get('https://ecpa.dgpa.gov.tw/uIAM/clogin.asp?destid=CrossHRD')
        driver.find_element_by_id('username').send_keys(a)
        driver.find_element_by_id('password').send_keys(b)
        driver.find_element_by_name('submit').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/a').click()
        return driver
    elif c == '2':
        driver.get('https://www.cp.gov.tw/portal/Clogin.aspx?ReturnUrl=https%3A%2F%2Felearn.hrd.gov.tw%2Fegov_login.php')
        driver.find_element_by_id('ctl00_ContentPlaceHolder1_AccountPassword1_txt_account').send_keys(a)
        driver.find_element_by_id('ctl00_ContentPlaceHolder1_AccountPassword1_txt_password').send_keys(b)
        driver.find_element_by_id('ctl00_ContentPlaceHolder1_AccountPassword1_btn_LoginHandler').click()
        driver.find_element_by_xpath('/html/body/div[4]/div/div/a').click()
        return driver
#人權議題與發展
def lesson7(name,coursename):
    try:
        driver.get('https://elearn.hrd.gov.tw/info/10022335')
        driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[4]/div/div[1]/div[2]/div/div[3]/div[2]/button').click()
        driver.switch_to.frame('s_catalog')
        driver.switch_to.frame('pathtree')
        driver.find_element_by_xpath('//*[@id="ITEM-E9225BAA2862D0BCD31F45FF017E89CB"]/span/a').click()
        time.sleep(1400)
        driver.find_element_by_xpath('//*[@id="ITEM-90188609C1680C9426310711013CF7E8"]/span/a').click()
        time.sleep(1400)
        driver.find_element_by_xpath('//*[@id="ITEM-23B96A2A1CDA009BC2D97D36AA3C8756"]/span/a').click()
        time.sleep(1400)
        print(name + '[' + coursename + ']' + '完成了!!')

    except:
        print(name + '[' + coursename + ']' + '出現問題!!')
    driver.close()