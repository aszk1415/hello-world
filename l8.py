from selenium import webdriver
import time
#時間不到
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
#晚近全球化的發展(Html5)
def lesson8(name,coursename):
    try:
        driver.get('https://elearn.hrd.gov.tw/info/10021291')
        driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[4]/div/div[1]/div[2]/div/div[3]/div[2]/button').click()
        driver.switch_to.frame('s_catalog')
        driver.switch_to.frame('pathtree')
        driver.find_element_by_xpath('//*[@id="tree1_1"]/span/a').click()
        time.sleep(660)
        driver.find_element_by_xpath('//*[@id="tree2_1"]/span/a').click()
        time.sleep(900)
        driver.find_element_by_xpath('//*[@id="tree3_1"]/span/a').click()
        time.sleep(600)
        print(name+'['+coursename+']'+'完成了!!')

    except:
        print(name + '[' + coursename + ']' + '出現問題!!')
    driver.close()