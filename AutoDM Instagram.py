#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[2]:


from selenium import webdriver
import time


# In[3]:


#Login 
def login(driver):
    driver.get('https://www.instagram.com/')
    time.sleep(2)
    username = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
    username.send_keys('')# ta3228 abhilash.datta

    password = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
    password.send_keys('')

    login_button = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
    login_button.click()


# In[4]:


#clearing notifs
def clear_notifs(driver):
    time.sleep(5)
    not_now = driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
    not_now.click()
    time.sleep(2)
    not_now2 = driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    not_now2.click()


# In[5]:


#sending message
def group_create_n_dm(driver,users,message):
    
    driver.get('https://www.instagram.com/direct/inbox/')
    time.sleep(2)

    send_message_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button')
    send_message_button.click()

    for user in users:
        time.sleep(5)
        search_user = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input')
        search_user.send_keys(user)

        time.sleep(2)
        selector = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div/div/div[3]/button/span')
        selector.click()

    next_button = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div')
    next_button.click()

    time.sleep(2)
    text = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
    text.send_keys(message)

    send = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
    send.click()


# In[6]:


def multiple_dm(driver,users,message):
    
    driver.get('https://www.instagram.com/direct/inbox/')
    time.sleep(2)
    
    for user in users:
        send_message_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div/button')
        send_message_button.click()
        #driver.get('https://www.instagram.com/direct/new')
        time.sleep(2)

        search_user = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[1]/div/div[2]/input')
        search_user.send_keys(user)

        time.sleep(4)
        selector = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div[2]/div/div/div[3]/button/span')
        selector.click()

        next_button = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[1]/div/div[2]/div/button/div')
        next_button.click()

        time.sleep(4)
        text = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea')
        text.send_keys(message)

        send = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button')
        send.click()
        driver.get('https://www.instagram.com/direct/inbox/')
        time.sleep(2)


# In[7]:


def logout(driver):
    profile_button = driver.find_element_by_xpath('//*[@id="react-root"]/section/div/div[1]/div/div[3]/div/div[5]/span/img')
    profile_button.click()
    time.sleep(2)
    logout_button = driver.find_element_by_xpath('/html/body/div[1]/section/div/div[1]/div/div[3]/div/div[5]/div[2]/div[2]/div[2]/div[2]/div/div/div/div/div/div')
    logout_button.click()


# In[8]:


users = ['test']
message = 'Hello! this is an automated message.'


# In[9]:


def auto_greeter(driver,users):
    greetings = 'Hi there!! this is Abhilash Datta, this message is automated but I am surely real' 
    driver.maximize_window()
    login(driver)
    clear_notifs(driver)
    multiple_dm(driver,users,greetings)
    logout(driver)


# In[10]:


driver = webdriver.Chrome("/Users/ABHILASH/Downloads/chromedriver/chromedriver.exe")
auto_greeter(driver,users)


# In[ ]:





# In[ ]:





# In[ ]:




