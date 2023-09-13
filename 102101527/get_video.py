import requests
import tqdm

def set(keyword, page):
    params = {
        'page': page,
        'page_size': 30,
        'keyword': keyword,
        '__refresh__': 'true',
        '_extra':'',
        'context':'',
        'from_source':'',
        'from_spmid': '333.337',
        'platform': 'pc',
        'highlight': '1',
        'single_column': '0',
        'qv_id': 'j0n8stR8I8FhcsSmC6u8BlAsZBISwdbP',
        'ad_resource': '5654',
        'source_tag': '3',
        'gaia_vtoken':'',
        'category_id':'',
        'search_type': 'video',
        'dynamic_offset': '30',
        'web_location': '1430654',
        'w_rid': '98fa32816d6efc942c5a611db484268c',
        'wts': '1694575610',
    }
    headers = {
        'Cookie':'buvid3=861CACD3-7529-9BE4-011D-839450D1136C63935infoc; b_nut=1689930863; i-wanna-go-back=-1; b_ut=7; _uuid=6F6A76108-9DE10-ABA7-B437-8CAE10310C954E66265infoc; FEED_LIVE_VERSION=V8; home_feed_column=5; header_theme_version=CLOSE; buvid4=0588C2CA-2D12-3F59-46C2-74BC731600EC79979-023072117-Rp%2FnGFzXU65im%2BMI2F7swA%3D%3D; CURRENT_FNVAL=4048; DedeUserID=527027219; DedeUserID__ckMd5=3ebec5c78356ced3; rpdid=|(JlRmRu|Rmm0J\'uY)mmJuRJu; CURRENT_QUALITY=80; buvid_fp_plain=undefined; fingerprint=e9f9929de0331847ecc97ee929f44794; buvid_fp=e9f9929de0331847ecc97ee929f44794; LIVE_BUVID=AUTO6416940827147782; PVID=1; bp_video_offset_527027219=839156959471992836; SESSDATA=d985568c%2C1710063773%2C22d09%2A91CjCNxcT-pZHoVO_2t587TZ-4eV0GtA98O-OP6-lBGWwUtAZPs3LsKAk1-YZwNo88lyYSVmtId0hrbmUxMS1IaWpUZXJvbnVqSDJ6Qm1BaURJNmh0eGhab1REeHB0a3cwblh6ZWpRZW5YbVBZRGRHS1JhZGhpR2tKVFNSeXZFbmlqUEJmMXVnRU1RIIEC; bili_jct=82e70eda26b98e4c2f6fa5e5a4be9fdb; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ3ODIxMDQsImlhdCI6MTY5NDUyMjkwNCwicGx0IjotMX0.bUa2t0QSEHfXywA9V-v0n3wCHmbDfecBW1NesYf9W6M; bili_ticket_expires=1694782104; b_lsid=42E556E3_18A8C8408E0; bsource=search_bing; sid=4smckbgx; browser_resolution=1655-838',
        'Referer':'https://search.bilibili.com/all',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.76',
    }
    return headers, params

def main(keyword, sum):
    n = int(sum / 30)
    url = 'https://api.bilibili.com/x/web-interface/wbi/search/type'
    urls = []
    for page in tqdm.tqdm(range(1, n+1)):
        headers, params = set(keyword, page)
        response = requests.get(url, headers=headers, params=params)
        file = response.json()
        results = file['data']['result']
        for result in tqdm.tqdm(results):
            urls.append(result['arcurl'])
    print(len(urls))
    return urls
