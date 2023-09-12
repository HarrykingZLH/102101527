import requests
import re
from bs4 import BeautifulSoup


def get_urls():
    url = 'https://search.bilibili.com/all?vt=04065809&keyword=%E6%97%A5%E6%9C%AC%E6%A0%B8%E6%B1%A1%E6%9F%93%E6%B0%B4%E6%8E%92%E6%B5%B7'
    urls = [url]
    for i in range(1, 10):
        new_url = url + f'&page={i+1}&o={30*i}'
        urls.append(new_url)
    return urls


def get_web_url(url):

    response = requests.get(url,  headers=headers, cookies=cookies)
    response.encoding = 'utf-8'
    html = response.text
    urls = re.findall('<a href="//(.*?)/".*?title=".*?" data-v-15c84221>', html)
    return urls


def get_cid(url):
    response = requests.get(url, headers=headers, cookies=cookies)
    response.encoding = 'utf-8'
    html = response.text
    cid = re.search('"cid":(.*?),', html).groups()[0]
    return cid


def get_danmu(cid):
    danmu_url = f'https://comment.bilibili.com/{cid}.xml'
    response = requests.get(danmu_url, headers=headers, cookies=cookies)
    response.encoding = 'utf-8'
    html = response.text
    contexts = re.findall('<d p=".*?">(.*?)</d>', html)
    return contexts


def write_txt(contects):
    with open('./danum.txt', 'a', encoding='utf-8') as f:
        for context in contexts:
            f.write(context + '\n')


if __name__ == '__main__':
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69'}
    cookies_str = 'buvid3=861CACD3-7529-9BE4-011D-839450D1136C63935infoc; b_nut=1689930863; i-wanna-go-back=-1; b_ut=7; _uuid=6F6A76108-9DE10-ABA7-B437-8CAE10310C954E66265infoc; FEED_LIVE_VERSION=V8; home_feed_column=5; header_theme_version=CLOSE; buvid4=0588C2CA-2D12-3F59-46C2-74BC731600EC79979-023072117-Rp%2FnGFzXU65im%2BMI2F7swA%3D%3D; CURRENT_FNVAL=4048; DedeUserID=527027219; DedeUserID__ckMd5=3ebec5c78356ced3; rpdid=|(JlRmRu|Rmm0J\'uY)mmJuRJu; CURRENT_QUALITY=80; buvid_fp_plain=undefined; fingerprint=e9f9929de0331847ecc97ee929f44794; buvid_fp=e9f9929de0331847ecc97ee929f44794; bsource=search_bing; SESSDATA=c706489d%2C1709536624%2C76fbe%2A91p25PNKMzaVRhGs2Q9CTNuZlsMqDAREPBTvT79qocACwhH0HFMpZr83V8CCH4pja4et0pGwAAEwA; bili_jct=8f0f46a3c97ee96dc2dfcfee18af685c; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQyNDM4NzEsImlhdCI6MTY5Mzk4NDY3MSwicGx0IjotMX0.J9N_eUJ07GgV0WAwdKEC2kazHcJhehg76MZKLBOLSgc; bili_ticket_expires=1694243871; bp_video_offset_527027219=838128078584545317; sid=7i6wqz56; PVID=1; browser_resolution=1643-820; b_lsid=8A52C394_18A6A81432E'
    cookies = {}
    for cookie in cookies_str.split(';'):
        cookies[cookie.split('=')[0]] = cookie.split('=')[1]

    urls = get_urls()
    for url in urls:
        webs = get_web_url(url)
        for web in webs:
            web = 'https://' + web
            cid = get_cid(web)
            contexts = get_danmu(cid)
            write_txt(contexts)


