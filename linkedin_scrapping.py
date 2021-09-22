from selenium import webdriver
import bs4 as bs
from selenium.webdriver.common.keys import Keys
import time
import os
import traceback
from selenium.common.exceptions import NoSuchElementException

chrome_options=webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("disable-dev-shm-usage")
chrome_options.add_argument("disable-gpu")
chrome_options.add_argument("disable-features=NetworkService")
chrome_options.add_argument("no-sandbox")
#hrome_options.add_argument('headless') #Set the parameters of the option
browser = webdriver.Chrome(chrome_options=chrome_options)
username="wiramaw300@tmednews.com"
password="Chowdary1@"
try:
    browser.get("https://www.linkedin.com/checkpoint/rm/sign-in-another-account?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")
    browser.maximize_window()
    time.sleep(5)
    #Enter login info:
    elementID = browser.find_element_by_id('username')
    elementID.send_keys(username)
    elementID = browser.find_element_by_id('password')
    elementID.send_keys(password)
    #Note: replace the keys "username" and "password" with your LinkedIn login info
    elementID.submit()
    time.sleep(5)


    job="Backend Developer"
    browser.get('https://www.linkedin.com/jobs/?showJobAlertsModal=false')
    jobID = browser.find_element_by_class_name('jobs-search-box__text-input')
    jobID.send_keys(job)
    time.sleep(5)
    browser.find_element_by_xpath("/html/body/div[6]/header/div/div/div/div[2]/button[1]").click()
    time.sleep(5)
    # src = browser.page_source
    # soup = bs.BeautifulSoup(src, 'lxml')
    # results = soup.find("small", {"class": "display-flex t-12 t-black--light t-normal"}).get_text().strip().split()[0]
    # results = int(results.replace(',', ''))
    # print(results)

    data=browser.find_elements_by_xpath("/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/header/div[1]/small")
    time.sleep(10)
    #data=browser.find_element_by_class_name("display-flex t-12 t-black--light t-normal")
    print(data[0].text)
    company_Name=[]
    page=2
    count=0
    while True:
        try:
            cname=1
            while cname<=8:
            	p=1
            	try:
            		#job_details=browser.find_element_by_xpath("")
            		while True:
            			try:
            				job=browser.find_elements_by_xpath("/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{0}]/div/div/div/div[2]/div[1]/a".format(cname))
            				comp=browser.find_elements_by_xpath("/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{0}]/div/div/div/div[2]/div[2]/a".format(cname))
            				loc=browser.find_elements_by_xpath("/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/ul/li[{0}]/div/div/div/div[2]/div[3]/ul".format(cname))
            				company_Name.append(job[0].text)
            				print(job[0].text)
            				print(comp[0].text)
            				print(loc[0].text)
            				count+=1
            				break
            			except Exception as e:
            				break
            			p=p+1
            	except Exception as e:
            		break
            		print("all have not printed")

            	cname=cname+1
            browser.find_element_by_xpath("/html/body/div[6]/div[3]/div[3]/div[2]/div/section[1]/div/div/section/div/ul/li[{0}]/button".format(page)).click()
            time.sleep(6)
            page+=1
        except Exception as e:
            print("jobs are over")
            print(count)
            break

except:
	traceback.print_exc()
	print("Page not found")
