from selenium import webdriver
import time
#沒有自動開始撥放
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
#捍衛環境好空氣 (html5)
def lesson2(name,coursename):
    try:
        driver.get('https://elearn.hrd.gov.tw/info/10021253')
        driver.find_element_by_xpath('/html/body/div[2]/div[4]/div[4]/div/div[1]/div[2]/div/div[3]/div[2]/button').click()
        driver.switch_to.frame('s_catalog')
        driver.switch_to.frame('pathtree')
        driver.find_element_by_xpath('//*[@id="tree1_1_1"]/span/a').click()
        driver.switch_to.default_content()
        driver.switch_to.frame('s_main')
        video = driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[3]/div[1]/div/video')
        driver.execute_script("return arguments[0].play()", video)
        time.sleep(1550)#1550
        driver.switch_to.default_content()
        driver.switch_to.frame('s_dialog')
        driver.find_element_by_xpath('/html/body/div[3]/input[2]').click()
        time.sleep(2)
        driver.switch_to.default_content()
        driver.switch_to.frame('s_catalog')
        driver.switch_to.frame('pathtree')
        driver.find_element_by_xpath('/html/body/form[1]/div/div/ul/li[8]/ul/li[1]/span/a').click()
        driver.switch_to.default_content()
        driver.switch_to.frame('s_main')
        driver.execute_script("return arguments[0].play()", driver.find_element_by_xpath('//*[@id="Count_Box"]/div[1]/div/video'))
        time.sleep(400)
        print(name + '[' + coursename + ']' + '完成了!!')


    except Exception as ex:

        print("出現如下異常%s" % ex)
        print(name + '[' + coursename + ']' + '出現問題!!')


    driver.close()