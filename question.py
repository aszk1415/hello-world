from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import re
driver = webdriver.Chrome()
driver.implicitly_wait(10)  # 隱含等待時間
PATH = 'https://ecpa.dgpa.gov.tw/uIAM/clogin.asp?destid=CrossHRD'
name = ['曾建閎','同事']
user = ['aszk1415','JAJN3FMP']
pws = ['aszk3131','Gt@555888']
userurl = ['1','2']
course_name =['臺灣AI行動計畫','捍衛環境好空氣','環境政策','「原」夢茂林，蛻變展翅','樂活、慢活、橋頭新生活','CEDAW第5條「社會文化之改變與母性之保障」','人權議題與發展','晚近全球化的發展']
course_url=['https://elearn.hrd.gov.tw/info/10022749',
            'https://elearn.hrd.gov.tw/info/10021253',
            'https://elearn.hrd.gov.tw/info/10022315',
            'https://elearn.hrd.gov.tw/info/10021309',
            'https://elearn.hrd.gov.tw/info/10021308',
            'https://elearn.hrd.gov.tw/info/10020975',
            'https://elearn.hrd.gov.tw/info/10022335',
            'https://elearn.hrd.gov.tw/info/10021291']
l1q = {'下列哪些為智慧應用實證場域？':[1,2,3,4,5],
       '為加速智慧科技發展，可實施下列哪些方法？':[1,2,3],
       '人才投資可參考國外42及C4Q coding school模式擴大培養軟體人才，擴大對中低階人才的投資。':[2],
       '資料是人工智慧發展的基礎。':[1],
       '為了保護資料安全，法規應嚴加規範資料分享環境，即使減緩智慧應用開發也沒關係。':[2],
       '加速智慧科技發展，政府應將資料開放。':[1],
       'AI僅能使用以下哪類資料進行運算？':[1],
       '為使AI人才匯集，應善用全球臺灣旅外人才，吸引回流，發展延攬國際級人才之前瞻研究機構。':[1],
       'AI發展可以開創資料的應用、提升資料經濟的價值。':[1],
       '人工智慧成功的必備條件是？':[2,4]}
l2q = {'固定性污染源包括發電廠、農地、住家等非移動性的來源，且最常排放出硫氧化物、一氧化碳、粒狀物污染物、揮發性有機物及戴奧辛等污染物質。':[1],
       '請問下列關於空氣污染指標(PSI)與健康影響<br>的敘述何者有誤？':[3],
       '請問下列選項何者不屬於毒性污染物？':[1],
       '下列有關空氣污染物對人體健康影響的描述何者有誤？':[2],
       '請問下列對於空氣污染物的來源及影響，何者描述正確？':[4],
       '請問下列選項何者不是面對空氣污染問題時自我防護的要訣？':[1],
       '請問依照微粒管制內容，下列各式粒子污染物的粒徑大小定義何者正確？':[4],
       '請問下列關於校園空氣品質旗幟宣導試辦計畫的描述何者錯誤？':[3],
       '細懸浮微粒PM2.5指標是採用英國每日空氣品質指標的細懸浮微粒預警濃度分級，將指標區分為5級並以顏色示警。':[2],
       '針對PM2.5，我國政府訂定改善空氣品質的目標值為：年平均值15μg/m3、24小時值35μg/m3。':[1]}
l3q = {'依據環保署的估計，民國107年擴大管制購物用塑膠袋後，預期每年約可再減少15億個購物用塑膠袋。':[1],
       '下列何者不屬於民國107年擴大管制購物用塑膠袋之管制對象：':[4],
       '依《環境影響評估法》規定，開發單位於通過環境影響說明書或評估書審查，並取得目的事業主管機關核發之開發許可後，逾三年始實施開發行為時，應提出　　　，送主管機關審查：':[3],
       '空氣品質指標（AQI）的數值在那個範圍屬「對所有族群不健康」：':[4],
       '《溫室氣體減量及管理法》規範之國家溫室氣體長期減量目標為：':[1],
       '下列何者不屬於「低碳永續家園認證評等」之實施對象：':[1],
       '環保署公告之「限制含塑膠微粒之化粧品與個人清潔用品製造、輸入及販賣」規範不得添加之塑膠微粒指的是粒徑　　毫米（mm）以下者：':[4],
       '台灣地區的細懸浮微粒PM2.5污染都是境內固定源的原生污染物直接排放。':[2],
       '《溫室氣體減量及管理法》定義之溫室氣體不包括：':[3],
       '依國際慣例，每年的4月22日訂為世界海洋日。':[2],
       '現行負責毒性化學物質管理之環保署下屬單位為：':[2],
       '依據《環境基本法》第2條之定義，環境係指「影響人類生存與發展之各種天然資源及經過人為影響之自然因素總稱」。':[1],
       '空氣品質指標（AQI）的副指標不包括：':[4],
       '為改善水體水質，環保署自民國104年起分階段開徵水污染防治費。':[1],
       '垃圾焚化廠焚化底渣於清除運輸時仍應以GPS追蹤管制其運輸路徑。':[1],
       '臺灣地區運轉中的都市生活垃圾焚化廠總計有　　座。':[3],
       '畜牧糞尿經厭氧發酵後，產生沼液、沼渣及沼氣資源利用，不僅可以回收氮肥及能源，也可改善河川環境品質。':[1],
       '依據《廢棄物清理法》之規定，一般廢棄物之回收、清除、處理由中央主管機關為之。':[2],
       '環保署於民國107年起逐步啟動化粧品及個人清潔用品塑膠微粒之管制措施。':[1],
       '依照環保署的統計，真正對環境有重大影響之虞的開發行為只占20%，但此類開發行為對環境所造成的影響卻有可能高達80%。':[1]}
l4q = {'紫斑蝶需要喝水代謝脂肪，因此形成蝶毯景觀。':[1],
       '下列哪個茂林景點在魯凱族語為「美麗的山谷〈Lumusu〉」意思？':[4],
       '關於龍頭山的敘述何者錯誤？':[3],
       '關於祖靈祭的描述何者正確？':[2],
       '「屯子役」事件的發生所在地為？':[1],
       '黑米祭由特定的家族執行，祭司世襲傳承。':[2],
       '多納高吊橋全長232公尺、高103公尺。':[1],
       '下列何者不是紫蝶的種類之一？':[3],
       '「紫蝶幽谷」為多種斑蝶群聚越冬的生態現象。':[1],
       '雙年賞蝶的月份在幾月？':[1],
       '何者不符合「紫蝶幽谷」的形成條件？':[3],
       '龍頭山被視為守護族人的聖山。':[2],
       '下列何者不是斑蝶的特色？':[4],
       '茂林國家風景區的成立年份？':[4],
       '茂林谷的魯凱族語為「吐拔魯」。':[2],
       '茂林的舊名為「多納」。':[1],
       '關於多納部落的描述何者正確？':[1],
       '茂林里仍保有三級古蹟：萬山岩雕群。':[2],
       '關於多納溫泉的敘述何者正確？':[2],
       '茂林10月會舉辦的祭典？':[2]}
l5q = {
    '以下關於橋頭糖廠內的景點，哪一個選項是錯誤的？':[3],
    '橋頭從過去的糖業轉為發展休閒觀光產業，使舊有的農產業逐漸轉型為酪農業等特色產業。':[1],
    '以下關於高雄新市鎮的敘述，哪一個選項是錯誤的？':[1],
    '三德三山國王廟現今為東林、西林地區主要的信仰廟宇。':[2],
    '橋頭老街的特色美食不包含以下哪一個選項？':[2],
    '橋頭區以橋為名，並不是因為當地有特別多的橋，而是源自於清朝時期所建造的允龜橋。':[1],
    '以下關於五里林聚落的由來及景點敘述，哪一個選項是錯誤的？':[2],
    '橋頭糖廠舊稱橋仔頭製糖所，是台灣第一座現代化製糖廠。':[1],
    '九甲圍義山宮是東南亞規模最大的三山國王廟。':[1],
    '橋頭的三山國王廟宇不包含下列哪一個選項？':[1],
    '以下有關橋頭的歷史敘述，哪一個選項是錯誤的？':[1],
    '以下哪一項不是五里林聚落的著名景點？':[4],
    '楊家古厝是陸厥修先生的故居。':[2],
    '以下關於橋頭糖廠的歷史沿革，哪一個選項是錯誤的？':[4],
    '橋頭糖廠內的五分車，是由於其載運甘蔗的車廂有五節而得名。':[2],
    '橋頭老街保留許多南洋式建築，見證了當時臺灣與南洋有密切的貿易往來。':[1],
    '以下有關橋頭老街的敘述，哪一個選項是錯誤的？':[3],
    '橋頭不僅在107年時擁有全高雄市最多的乳牛數量，更曾獲得行政院農委會最高榮譽的全國五梅獎項。':[1],
    '清朝時期時，由於小店仔街位於圳道北岸的橋頭處，因此被當地人稱為「橋仔頭」。':[1],
    '五里林原本是一片茂密的樹林，因其連續五里遠而得名。':[1]}
l6q = {'傳統是由人類社群所制定，當然也就可以由人類社群來調整，甚至廢止。以下哪些婚禮傳統帶有性別歧視，我們應該去思考、調整或廢止的？':[1,3,4],
       '以下哪些社會現象具有性別歧視？':[1,2,4],
       '請依臺灣目前的社會風氣，將男性與女性拋棄繼承常發生的時機進行配對。':[2,1],
       'CEDAW第5條的b強調教養子女是父母的共同責任，我國的三字經中有哪幾句可以看到這種父母都有責任教養子女的精神？':[1,2,3],
       'CEDAW第3號一般性建議要求締約國需採取哪些的方法來宣傳消除在文化上對婦女的歧視？':[1,3],
       '下列哪些行為透露出社會對於媽媽的定型任務？':[1,2,3,4],
       '下列哪種傳統沒有歧視女性的意思？':[3],
       '下列哪些是常出現的性別刻板化現象？':[1,2,3],
       'CEDAW第19號建議著重在保護婦女不受各種暴力脅迫，是為了要破除下列哪些傳統迷思？':[1,2,3,4],
       '我們常發現女性在結婚或懷孕後可能會被迫辭職，這會造成女性失去了經濟能力，連帶失去了主張自我意見的權利。':[1]}
l7q = {'以事後司法訴訟救濟，作為因應氣候變遷的權利保障方式，是目前我國法制中最重要且唯一的作法。':[2], 
       '有關原住民族持有獵槍有無觸法的問題，我國最高法院判決認為：「供作生活工具之用」之解釋，應以專恃狩獵維生或以狩獵為其生活主要內容者為限，理由係基於罪行法定主義，與其傳統習俗文化的考量無關。':[2],
       '對非本國籍愛滋病毒感染者之入出境管制，為保障我國國人健康與生命安全，目前法規仍維持對外國感染者之入境限制。':[2],
       '有關集會遊行法申請許可規定未排除緊急性及偶發性集會遊行之部分，是否違憲的問題，大法官釋字第718號解釋認為，舊法因違反《憲法》第23條比例原則，不符《憲法》第14條保障集會自由之意旨，釋字第445號解釋應予變更。':[2],
       ' 根據兒童權利公約的規定，基於父母為兒童的法定代理人，所有關係兒童之事務，無論是由公私社會福利機構、法院、行政機關或立法機關作為，均應以父母親之最佳利益為優先考量。':[2],
       '氣候變遷的課題與人權無關，純粹是西方工業先進國家為了阻撓開發中國家經濟發展的謊言，更無科學上的具體根據。':[2],
       '根據兒童權利公約的規定，基於父母為兒童的法定代理人，所有關係兒童之事務，無論是由公私社會福利機構、法院、行政機關或立法機關作為，均應以父母親之最佳利益為優先考量。':[2],
       '經濟社會文化權利國際公約任擇議定書，賦予個人就經濟、社會及文化權利受侵害，向聯合國申訴與尋求救濟之權。':[1],
       '基於對世界各國文化傳統差異之尊重，世界人權宣言並未就「文化權」的部分，予以明文保障。':[2],
       ' 以事後司法訴訟救濟，作為因應氣候變遷的權利保障方式，是目前我國法制中最重要且唯一的作法。':[2],
       '責任追究的困難度，從傳統的「明顯人為」性質，到「非明顯人為結果」，是氣候變遷災難對國際人權體系的深層挑戰之一。':[1],
       ' 有關氣候變遷問題的因應對策，可分別從「減緩」與「調適」兩個面向來思考。':[1],
       '依據我國環境基本法的規定，中央政府應策定國家環境保護計畫，建立永續發展指標，並推動實施之。':[1],
       '兩公約施行法中，明文指定外交部為主管機關，應與各國政府、國際間非政府組織及人權機構共同合作，以保護及促進「兩公約」所保障各項人權之實現。':[2],
       '人權問題不僅牽涉當代人的權益，也包含所謂世代正義。':[1],
       ' 有關原住民族持有獵槍有無觸法的問題，我國最高法院判決認為：「供作生活工具之用」之解釋，應以專恃狩獵維生或以狩獵為其生活主要內容者為限，理由係基於罪行法定主義，與其傳統習俗文化的考量無關。':[2],
       '有關氣候變遷問題的因應對策，可分別從「減緩」與「調適」兩個面向來思考。':[1],
       '根據兒童權利公約的規定：「為本公約之目的，兒童係指未滿十八歲之人。」':[1],
       ' 氣候變遷的課題與人權無關，純粹是西方工業先進國家為了阻撓開發中國家經濟發展的謊言，更無科學上的具體根據。':[2],
       '2009年，兩公約由立法院審議通過，總統於同年批准，並於同年由聯合國秘書以兩岸同屬一中為由而接受。':[2]
}
l8q = {'下列哪個政權封鎖了Facebook與YouTube使民眾無法瀏覽?':[1],
       '現今的流動台灣傳1個訊息或匯1筆錢到地球另一端只需幾小時。':[2],
       '從社會科學的角度，全球化最大的特色就是流動flow。':[1],
       '流動並不是什麼嶄新的現象，因為產品、人員、資訊，與資金早就不斷地挑戰人為的疆界。':[1],
       '全球化的關係資本家將手上資本移轉到其他地區去獲得更大的利益。':[1],
       '匯款二十年前需要親自跑銀行填寫文件，現今社會只需在網路上按下幾個鍵即可。':[1],
       '1990年代末期全球貨幣市場每天流通的資金已經超過多少美元?':[4],
       '找一篇國際期刊二十年前需要到圖書館找館藏，現今社會進學校圖書館的電子資料庫、Google等入口網站去搜尋就可以下載PDF檔。':[1],
       '第一次世界大戰結束後跨國企業越來越普遍，規模越來越大。':[2],
       '糧食流動是全球化流通現象的根基所在。':[2],
       '美國國務院曾經準備在台灣發動政變，但當時的飛機航程還不夠遠，導致計畫擱置。':[1],
       '金融市場全球化所引發的房地產與股市泡沫化最早於哪個國家開始 ?':[2],
       '跨國貿易的演進讓下面哪一間企業的市場價值甚至超越泰國的GDP?':[1],
       '晚近二十年的科技發達導致產品、人員、資訊、資金無法誇越國家疆界來流動。':[2],
       '大航海時代以前跨國貿易就是以海路為主。':[2],
       '下列哪個城市所雇用的高科技人才，多達2/3並不是該國家的人?':[4],
       '大航海時代以前的流動從一個國家到另一個國家需要數月到數年。':[1],
       '現今社會人人都可以成為公民記者，反應速度更快，傳遞層面更廣。':[1],
       '二十年前專制政權可控制媒體，封鎖各種消息。':[1],
       '西方國家在19世紀開始建立大型的____，進行直接投資。':[3],
       '全球化與資本家為了追求利潤而在世界各地活動，為了達到此目的，人員也會跨國疆域而流動。':[1]}
lqn = [l1q,l2q,l3q,l4q,l5q,l6q,l7q,l8q]
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
def Questionnaire():
    # now_handle = driver.current_window_handle
    # print(now_handle)
    # all_handles = driver.window_handles
    # for handle in all_handles:
    #     if handle != now_handle:
    #         # 輸出待選擇的視窗控制程式碼
    #         print(handle)
    #         driver.switch_to.window(handle)
    #         time.sleep(1)
    driver.switch_to.default_content()
    driver.switch_to.frame('moocSysbar')
    driver.find_element_by_xpath('/html/body/div/div[3]/ul/li[2]/a').click()
    now_handle = driver.current_window_handle
    # print(now_handle)
    time.sleep(4)
    driver.switch_to.default_content()
    driver.switch_to.frame('s_main')
    driver.find_element_by_xpath('/html/body/div/div[2]/div/div[3]/div/div[1]/div/div[1]').click()
    all_handles = driver.window_handles
    for handle in all_handles:
        if handle != now_handle:
            # 輸出待選擇的視窗控制程式碼
            # print(handle)
            driver.switch_to.window(handle)
            time.sleep(1)
    #點問券
    driver.find_element_by_xpath('/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[2]/table/tbody/tr[1]/td[3]/ol/li[1]/span/input').click()
    driver.find_element_by_xpath(
        '/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[2]/table/tbody/tr[2]/td[3]/ol/li[1]/span/input').click()
    driver.find_element_by_xpath(
        '/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[2]/table/tbody/tr[3]/td[3]/ol/li[1]/span/input').click()
    driver.find_element_by_xpath(
        '/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[2]/td[2]/table/tbody/tr[4]/td[3]/ol/li[1]/span/input').click()
    #提交
    driver.find_element_by_xpath(
        '/html/body/table/tbody/tr[2]/td/form/table/tbody/tr[4]/td[2]/table/tbody/tr/td[2]/input').click()
    driver.switch_to.alert.accept()
    time.sleep(2)
    driver.switch_to.alert.accept()

def lessonqn(name,course_url,course_name,lqn):
    try:
        driver.get(course_url)
        #上課去
        gbtn = driver.find_element_by_xpath('//*[@id="course-info-bottom"]/div[2]/button')
        gbtn.click()

        time.sleep(4)

        driver.switch_to.frame('moocSysbar')
        driver.find_element_by_xpath('//*[@id="SYS_04_02_002"]').click()

        now_handle = driver.current_window_handle
        # print(now_handle)

        driver.switch_to.default_content()
        driver.switch_to.frame('s_main')
        driver.find_element_by_xpath('/html/body/div/div[2]/div/div[2]/div/div[1]/div/div[1]').click()

        # 獲取當前視窗控制程式碼


        # 獲取所有視窗控制程式碼
        all_handles = driver.window_handles
        for handle in all_handles:
            if handle != now_handle:
                # 輸出待選擇的視窗控制程式碼
                # print(handle)
                driver.switch_to.window(handle)
                time.sleep(1)
        o = driver.find_element_by_xpath(
            '/html/body/center/div[2]/table/tbody/tr[2]/td/form/table/tbody/tr[5]/td[2]').text
        print(o)
        n = re.search('[0-9]*',o).group()
        print(n)
        driver.find_element_by_xpath('//*[@id="presentPanel"]/table/tbody/tr[2]/td/form/table/tbody/tr[17]/td/input[1]').click()
        time.sleep(5)

        for i in range(int(n)):
            html = '/html/body/center/div[2]/table/tbody/tr[2]/td/form/table/tbody/tr['+ str(i+1) +']/td[3]'
            text = driver.find_element_by_xpath(html).text
            ttext = re.findall('\.(.*)',text)
            if ttext[0] == '':
                ttext = driver.find_element_by_xpath(html+'/p').text
            else:
                ttext = ttext[0][1:]
            # print(ttext)
            co = lqn[ttext]
            for coco in co:
                htmlan = html + '/ol/li['+str(coco)+']/span/input'
                driver.find_element_by_xpath(htmlan).click()
        driver.find_element_by_class_name('cssBtn').click()
        # driver.find_element_by_xpath('/html/body/center/div[2]/table/tbody/tr[2]/td/form/table/tbody/tr[11]/td/input[1]').click()
        driver.switch_to.alert.accept()
        time.sleep(5)
        driver.close()
        driver.switch_to.window(now_handle)
        Questionnaire()
        time.sleep(2)
        ActionChains(driver).key_down(Keys.CONTROL).send_keys("w").key_up(Keys.CONTROL).perform()
        driver.switch_to.window(now_handle)
        print(str(name)+str(course_name)+'答題正確')
    except:
        print(str(name)+str(course_name)+'的測驗出錯了')

set(user[1],pws[1],userurl[1])
# for i in range(8):
lessonqn(name[1],course_url[5],course_name[5],lqn[5])

