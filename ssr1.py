import requests
from lxml import etree

url = 'https://ssr1.scrape.center'
headers ={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
resp = requests.get(url, headers=headers)
ehtml = etree.HTML(resp.text)
phrase = ehtml.xpath('//*[@id="index"]/div[1]/div[1]/div')
for p in phrase:
    name = p.xpath('./div/div/div[2]/a/h2/text()')[0]
    print(name,end=' ')
    classification = p.xpath('./div/div/div[2]/div/button/span/text()')
    for c in classification:
        print(c,end=' ')
    country = p.xpath('./div/div/div[2]/div[2]/span/text()')[0]
    duration = p.xpath('./div/div/div[2]/div[2]/span/text()')[2]
    rating_num = p.xpath('./div/div/div[3]/p[1]/text()')[0].replace('\n                ','')
    print(country,duration,rating_num)
