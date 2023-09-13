import requests
import re
def get_cid(url, headers):
    response = requests.get(url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    cid = re.search('"cid":(.*?),', html).groups()[0]
    return cid



def get_danmu(cid, headers):
    danmu_url = f'https://comment.bilibili.com/{cid}.xml'
    response = requests.get(danmu_url, headers=headers)
    response.encoding = 'utf-8'
    html = response.text
    contexts = re.findall('<d p=".*?">(.*?)</d>', html)
    return contexts

def main(url):
    headers = {
        'Cookie': 'buvid3=861CACD3-7529-9BE4-011D-839450D1136C63935infoc; b_nut=1689930863; i-wanna-go-back=-1; b_ut=7; _uuid=6F6A76108-9DE10-ABA7-B437-8CAE10310C954E66265infoc; FEED_LIVE_VERSION=V8; home_feed_column=5; header_theme_version=CLOSE; buvid4=0588C2CA-2D12-3F59-46C2-74BC731600EC79979-023072117-Rp%2FnGFzXU65im%2BMI2F7swA%3D%3D; CURRENT_FNVAL=4048; DedeUserID=527027219; DedeUserID__ckMd5=3ebec5c78356ced3; rpdid=|(JlRmRu|Rmm0J\'uY)mmJuRJu; CURRENT_QUALITY=80; buvid_fp_plain=undefined; fingerprint=e9f9929de0331847ecc97ee929f44794; buvid_fp=e9f9929de0331847ecc97ee929f44794; LIVE_BUVID=AUTO6416940827147782; PVID=1; SESSDATA=d985568c%2C1710063773%2C22d09%2A91CjCNxcT-pZHoVO_2t587TZ-4eV0GtA98O-OP6-lBGWwUtAZPs3LsKAk1-YZwNo88lyYSVmtId0hrbmUxMS1IaWpUZXJvbnVqSDJ6Qm1BaURJNmh0eGhab1REeHB0a3cwblh6ZWpRZW5YbVBZRGRHS1JhZGhpR2tKVFNSeXZFbmlqUEJmMXVnRU1RIIEC; bili_jct=82e70eda26b98e4c2f6fa5e5a4be9fdb; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ3ODIxMDQsImlhdCI6MTY5NDUyMjkwNCwicGx0IjotMX0.bUa2t0QSEHfXywA9V-v0n3wCHmbDfecBW1NesYf9W6M; bili_ticket_expires=1694782104; bp_video_offset_527027219=840662564552572963; browser_resolution=1659-838; sid=4p0xyyhl; bsource=search_bing; b_lsid=4C6FAD109_18A8E09E243',
        'Referer': 'https://www.bilibili.com/video/BV1yF411C7ZJ/?spm_id_from=333.337.search-card.all.click&vd_source=884af3d08eeae21ab00e4b40b06e8ca8',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76',
    }

    cid = get_cid(url, headers)
    return get_danmu(cid, headers)

if __name__ == '__main__':
    url = 'http://www.bilibili.com/video/av275130756'
    print(main(url))
