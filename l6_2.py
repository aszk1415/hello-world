from selenium import webdriver
import time
#21/6/19測試OK 因為測試起來不知道為何抓不到2_6的影片
#撥放到2_5會自動跳出，打算寫l6用兩個Py檔案去開

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 隱含等待時間
PATH = 'https://ecpa.dgpa.gov.tw/uIAM/clogin.asp?destid=CrossHRD'  # 登入網址
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
#CEDAW第5條「社會文化之改變與母性之保障」
def lesson6(name,coursename):
    try:
        driver.get('https://elearn.hrd.gov.tw/info/10020975')
        driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[4]/div/div[1]/div[2]/div/div[3]/div[2]/button').click()
        driver.switch_to.frame('s_catalog')
        driver.switch_to.frame('pathtree')
        print(driver.page_source)
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
        print(name + '[' + coursename + ']' + '完成了!!')

    except:
        print(name + '[' + coursename + ']' + '出現問題!!')
    # driver.close()