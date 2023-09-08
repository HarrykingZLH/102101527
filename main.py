#coding=utf-8
import requests
import re

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'
}
url = 'https://www.bilibili.com/video/BV1yF411C7ZJ/?spm_id_from=333.337.search-card.all.click&vd_source=884af3d08eeae21ab00e4b40b06e8ca8'

response = requests.get(url, headers=headers)
html = response.text

cid = re.search('"cid":(.*?),', html).groups()[0]
print(cid)
danmu_url = f'https://comment.bilibili.com/{cid}.xml'


response = requests.get(danmu_url, headers=headers)
response.encoding = 'utf-8'
html = response.text

contexts = re.findall('<d p=".*?">(.*?)</d>', html)
print(contexts)
with open('./danum.txt', 'w', encoding='utf-8') as f:
    for context in contexts:
        f.write(context + '\n')




