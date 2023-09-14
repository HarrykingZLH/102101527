import requests
import tqdm


def headers_set(keyword, page):  # 设置每页的请求头和参数，方便遍历
    # 参数
    params = {
        'page': page,  # 页码
        'page_size': 30,  # 每页视频数
        'keyword': keyword,  # 搜索关键词
        '__refresh__': 'true',
        '_extra': '',
        'context': '',
        'from_source': '',
        'from_spmid': '333.337',
        'platform': 'pc',
        'highlight': '1',
        'single_column': '0',
        'qv_id': 'P7Rqx1Tf0QbNuWbq205FO1ZYVkAjGqTp',
        'ad_resource': '5654',
        'source_tag': '3',
        'gaia_vtoken': '',
        'category_id': '',
        'search_type': 'video',
        'dynamic_offset': '30',
        'web_location': '1430654',
        'w_rid': '290d9ab21d0ccafbc03b64cf4caf2dcc',
        'wts': '1694672250',
    }

    # 请求头
    headers = {
        'Cookie': 'buvid3=861CACD3-7529-9BE4-011D-839450D1136C63935infoc; b_nut=1689930863; i-wanna-go-back=-1; b_ut=7;'
                  ' _uuid=6F6A76108-9DE10-ABA7-B437-8CAE10310C954E66265infoc; FEED_LIVE_VERSION=V8; home_feed_column=5;'
                  ' header_theme_version=CLOSE; buvid4=0588C2CA-2D12-3F59-46C2-74BC731600EC79979-023072117-Rp%2FnGFzXU6'
                  '5im%2BMI2F7swA%3D%3D; CURRENT_FNVAL=4048; DedeUserID=527027219; DedeUserID__ckMd5=3ebec5c78356ced3; '
                  'rpdid=|(JlRmRu|Rmm0J\'uY)mmJuRJu; CURRENT_QUALITY=80; buvid_fp_plain=undefined; fingerprint=e9f9929d'
                  'e0331847ecc97ee929f44794; buvid_fp=e9f9929de0331847ecc97ee929f44794; LIVE_BUVID=AUTO6416940827147782'
                  '; PVID=1; SESSDATA=d985568c%2C1710063773%2C22d09%2A91CjCNxcT-pZHoVO_2t587TZ-4eV0GtA98O-OP6-lBGWwUtAZ'
                  'Ps3LsKAk1-YZwNo88lyYSVmtId0hrbmUxMS1IaWpUZXJvbnVqSDJ6Qm1BaURJNmh0eGhab1REeHB0a3cwblh6ZWpRZW5YbVBZRGR'
                  'HS1JhZGhpR2tKVFNSeXZFbmlqUEJmMXVnRU1RIIEC; bili_jct=82e70eda26b98e4c2f6fa5e5a4be9fdb; bili_ticket=ey'
                  'JhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTQ3ODIxMDQsImlhdCI6MTY5NDUyMjkwNCwic'
                  'Gx0IjotMX0.bUa2t0QSEHfXywA9V-v0n3wCHmbDfecBW1NesYf9W6M; bili_ticket_expires=1694782104; browser_reso'
                  'lution=1659-838; bp_video_offset_527027219=840796202468376612; innersign=0; b_lsid=419DEFE8_18A92561'
                  'C49',
        'Referer': 'https://search.bilibili.com/all',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.'
                      '0 Safari/537.36 Edg/116.0.1938.76'
    }
    return headers, params


def main(keyword, m):
    n = int(m / 30)  # 计算所需搜索页的页数，每页30个视频
    url = 'https://api.bilibili.com/x/web-interface/wbi/search/type'  # 搜索页网址
    urls = []  # 视频URL，列表
    for page in tqdm.tqdm(range(1, n+1)):  # 遍历页面，这里用tqdm.tqdm()函数显示进度条
        headers, params = headers_set(keyword, page)  # 获取请求头和参数
        response = requests.get(url, headers=headers, params=params)  # 请求网页
        file = response.json()  # 转json格式，便于提取信息
        results = file['data']['result']  # 提取每个视频的信息
        for result in tqdm.tqdm(results):
            urls.append(result['arcurl'])  # 每个视频的URL存储在arcurl变量中，添加进列表
    return urls
