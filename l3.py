from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 隱含等待時間
#OK
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
#環境政策
def lesson3(name,coursename):
    try:
        driver.get('https://elearn.hrd.gov.tw/info/10022315')
        driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[4]/div/div[1]/div[2]/div/div[3]/div[2]/button').click()
        driver.switch_to.frame('s_catalog')
        driver.switch_to.frame('pathtree')
        driver.find_element_by_xpath('//*[@id="I_SCO_10000070_1536908073421686"]/span/a').click()
        time.sleep(380)
        driver.find_element_by_xpath('//*[@id="I_SCO_10000070_1536908084765909"]/span/a').click()
        time.sleep(670)
        driver.find_element_by_xpath('//*[@id="I_SCO_10000070_1536908095565114"]/span/a').click()
        time.sleep(1160)
        print(name + '[' + coursename + ']' + '完成了!!')

    except:
        print(name + '[' + coursename + ']' + '出現問題!!')
    driver.close()