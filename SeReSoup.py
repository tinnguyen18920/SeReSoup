#python3.8
import requests
from requests.models import Response
from requests.sessions import Session
from requests.exceptions import RequestException
from bs4 import BeautifulSoup

import selenium
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
#from selenium.webdriver.support.ui import WebDriverWait
#from selenium.webdriver.support import expected_conditions as EC
#from selenium.webdriver.common.by import By

class ReSoup:
    '''
    '''
    def __init__(self) -> None:
        self.session_ = requests.Session()
        self.session_.headers.update({'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36'})
    
    def session(self) -> Session:
        '''
        param:
        return: 
        =====================================
        Default requests headers : {'User-Agent': 'python-requests/2.24.0', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

        >>> rs = ReSoup()
        >>> s = rs.session()
        >>> s.headers
        {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',\
         'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive'}

        >>>
        '''

        return self.session_
    
    def soup(self, url:str, soup=False, **kwargs):
        '''
        
        
        >>> url = 'http://httpbin.org/get'
        >>> type(ReSoup().soup(url))
        requests.models.Response
        >>> type(ReSoup().soup(url , soup=True))
        bs4.BeautifulSoup
        >>>
        >>> Ipad = "Ipad String"
        >>> res = ReSoup().soup(url , soup=False, headers={"User-Agent": Ipad})
        >>> res.json()
        {'args': {},
         'headers': {'Accept': '*/*',
          'Accept-Encoding': 'gzip, deflate',
          'Host': 'httpbin.org',
          'User-Agent': 'Ipad String',
          'X-Amzn-Trace-Id': 'Root=1-5f292a96-57a1bdc0303944e2afa8d018'},
         'origin': '113.172.252.62',
         'url': 'http://httpbin.org/get'}

        >>>

        '''
        try:
            res = self.session_.get(url,**kwargs)
            if soup == True:
                return BeautifulSoup(res.text, "lxml")
            return res
        except RequestException as err:
            print(rerp(err))
            raise Exception('Cannot Download Webpage' + url)


class SeSoup:
    def __init__(self):
        #self.driver_ = selenium.webdriver.chrome.webdriver.WebDriver
        pass
    def driver(self, wait=False) -> selenium.webdriver.chrome.webdriver.WebDriver:

        if wait:
            driver = webdriver.Chrome()
            return driver

        #CUSTOM DRIVER HEHE:

        capa = DesiredCapabilities.CHROME
        capa["pageLoadStrategy"] = "none"
        
        driver = webdriver.Chrome(desired_capabilities=capa)
        #self.driver_ = driver
        return driver

    def soup(self, url:str, mydriver=None , soup=True):
        ''' 



        '''
        if mydriver:
            driver = mydriver

            driver.get(url)
            html_ele = driver.find_element_by_tag_name('html')
            html_source = html_ele.get_attribute('outerHTML')

        else:
            driver = self.driver(wait=True)

            driver.get(url)

            html_ele = driver.find_element_by_tag_name('html')
            html_source = html_ele.get_attribute('outerHTML')
            
            driver.quit()

        if soup == False:
            return html_source
        return BeautifulSoup(html_source , 'lxml')
