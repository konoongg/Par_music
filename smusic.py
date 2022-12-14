from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import csv
from tkinter import*

URL=''

music = []
path='music.csv'

def url():
    global URL
    
    URL=e.get()
    root.quit()
    

def xl(items,path):
    with open(path,'w',newline='') as csv_file:
        writer = csv.writer(csv_file,delimiter=';')
        writer.writerow(['название','исполнитель'])
        for item in items:
            writer.writerow([item[0],item[1]])


root=Tk()
l=Label(text='ведите url',width=30).pack(padx=2,pady=2)
e = Entry(width=30)
b = Button(width=15,text='Поиск',command = url)
e.pack(padx=2,pady=2)
b.pack(padx=2,pady=2)
root.mainloop()

driver = webdriver.Chrome(executable_path=r'C:\Users\User\Desktop\payton_prodgect\chromedriver.exe')
driver.maximize_window()
driver.get(URL)

driver.find_element_by_id('quick_email').send_keys('89133859940')
driver.find_element_by_id('quick_pass').send_keys('konoong')
driver.find_element_by_id('quick_login_button').click()

time.sleep(5)
page_counter = driver.find_elements_by_class_name('page_counter')
musik = page_counter[-1:]

audio = driver.find_element_by_xpath('//*[@id="wide_column"]/div[1]/div[2]/a[5]').text
if 'аудио' in audio:
    driver.find_element_by_xpath('//*[@id="wide_column"]/div[1]/div[2]/a[5]').click()
    

    time.sleep(5)
    title = driver.find_elements_by_class_name('audio_row__performer_title')
    for l in title:
        name=''
        des=''
        komp=[]
        r = 0
        one_m=l.text.replace('\uff0e','').replace('\xd8','').replace('\u210d','')
    
        komp = one_m.split('\n')
        if len(komp) == 2:
            music.append(komp)
        print(komp)
        
        try:  
            xl(music,path)
        except UnicodeEncodeError:
            print('дибильчики какую-то хрень написали туда')
else:
    print('у пользователя закрыта музыка')
        
            
                    
        
        
        

    
    
    
