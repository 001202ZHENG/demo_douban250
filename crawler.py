

#倒入模块
import requests
from lxml import etree
import pandas  as pd
#发起请求

url = 'https://movie.douban.com/top250'

#为了反爬 模拟请求头 F12 在network中找user_agent
headers = {
    'User-Agent':
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
}

urls=['https://movie.douban.com/top250?start={}&filter='.format(str(k*25)) for k in range(10)]

def get_first_text(list):
    try:
        return list[0].strip()
    except:
        return ''

df=pd.DataFrame(columns=['title','href','director','comment','summary','ratings'])

for url in urls:
    
    response = requests.get(url=url,headers=headers)
    
    html = etree.HTML(response.text)
    
    lis=html.xpath('//*[@id="content"]/div/div[1]/ol/li')

for li in lis :
    title=get_first_text(li.xpath('./div/div[2]/div[1]/a/span[1]/text()'))
    href=get_first_text(li.xpath('./div/div[2]/div[1]/a/@href'))
    director=get_first_text(li.xpath('./div/div[2]/div[2]/p[1]/text()'))
    comment=get_first_text(li.xpath('./div/div[2]/div[2]/div/span[4]/text()'))    
    summary=get_first_text(li.xpath('./div/div[2]/div[2]/p[2]/span/text()'))  
    ratings=get_first_text(li.xpath('./div/div[2]/div[2]/div/span[2]/text()'))  
    
    print( title,href,director,comment,summary,ratings)
    df.loc[len(df.index)]=[title,href,director,comment,summary,ratings]

#处理数据

df.to_excel('豆瓣电影top250数据.xlsx',sheet_name='豆瓣电影top250数据',na_rep=' ')
