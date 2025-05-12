import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

try:
    df = pd.read_csv('videos.csv')
except:
    print("Arquivo 'videos' não encontrado")

if 'Data' and 'View' not in df:
    df['Data'] = 'Data'
    df['View'] = 'View'

tamanho = df.index

options = Options()
try:
    driver = webdriver.Chrome('C:/Users/Danix/Downloads/chromedriver-win64/chromedriver.exe', options=options)
except:
    print("Arquivo chromedriver.exe não encontrado")

try:
    for i in range(tamanho.start, tamanho.stop):
        link = df['Link'][i]
        driver.get(link)
        time.sleep(2)
        driver.find_element_by_css_selector('#tabsContent > yt-tab-group-shape > div.yt-tab-group-shape-wiz__tabs > yt-tab-shape:nth-child(2) > div.yt-tab-shape-wiz__tab').click()
        time.sleep(2)
        driver.find_element_by_css_selector('#contents > ytd-rich-item-renderer:nth-child(1)').click()
        time.sleep(2)
        driver.find_element_by_css_selector('#bottom-row').click()
        time.sleep(2)
        infovideo = driver.find_element_by_id('ytd-watch-info-text')
        time.sleep(2)
        data = infovideo.text
        p = data.split()
        views = p[0]
        data = p[2] + " " +p[3] + " " + p[4] + " " + p[5] + " " + p[6]

        df['Data'][i] = data
        df['View'][i] = views

        time.sleep(5)
except:
    print('Erro ao usar o selenium driver')

driver.close()

print(df.to_string() + "\n")

opc = int(input("Deseja salvar?\n1 - Para sair\n2 - Para salvar no arquivo e sair\n"))

if(opc == 1):
    exit(1)
elif(opc == 2):
    current_time = time.localtime()
    current_date = time.strftime('%d-%m-%Y', current_time)

    df.to_csv(f"videos_{current_date}.csv", index=False)
    print(f"DataFrame salvo em videos_{current_date}.csv")
else:
    print("Opção invalida")
