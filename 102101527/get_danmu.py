import requests
import re


def write_txt(context_list, filename):
    try:
        with open(filename, 'a', encoding='utf-8') as f:  # 创建TXT文件存储弹幕
            for context in context_list:
                f.write(str(context) + '\n')  # 弹幕竖直排列写入
    except Exception as e:
        print(f"txt生成出现异常: {e}")


def get_cid(video_url, headers):
    try:
        response = requests.get(video_url, headers=headers)  # 请求页面
        response.encoding = 'utf-8'  # 更改编码格式，防止乱码
        html = response.text  # 保存请求返回的信息
        cid = re.search('"cid":(.*?),', html).groups()[0]  # 正则表达式匹配，提取信息中的cid码
        return cid
    except Exception as e:
        print(f"cid获取出现异常: {e}")


def get_danmu(cid, headers):
    try:
        danmu_url = f'https://comment.bilibili.com/{cid}.xml'  # B站用于存储弹幕的URL，规则
        response = requests.get(danmu_url, headers=headers)  # 请求网页
        response.encoding = 'utf-8'  # 更改编码格式，防止乱码
        html = response.text  # 保存请求返回的信息
        contexts = re.findall('<d p=".*?">(.*?)</d>', html)  # 正则表达式匹配，提取信息中的弹幕信息（字符串）
        return contexts
    except Exception as e:
        print(f"弹幕获取出现异常: {e}")


def main(video_url):
    try:
        headers = {  # 请求头，由于弹幕提取不涉及翻页操作，这里不需要参数
            'Cookie': 'buvid3=861CACD3-7529-9BE4-011D-839450D1136C63935infoc; b_nut=1689930863; i-wanna-go-back=-1; b_u'
                      't=7; _uuid=6F6A76108-9DE10-ABA7-B437-8CAE10310C954E66265infoc; FEED_LIVE_VERSION=V8; home_feed_c'
                      'olumn=5; header_theme_version=CLOSE; buvid4=0588C2CA-2D12-3F59-46C2-74BC731600EC79979-023072117-'
                      'Rp%2FnGFzXU65im%2BMI2F7swA%3D%3D; CURRENT_FNVAL=4048; DedeUserID=527027219; DedeUserID__ckMd5=3e'
                      'bec5c78356ced3; rpdid=|(JlRmRu|Rmm0J\'uY)mmJuRJu; CURRENT_QUALITY=80; buvid_fp_plain=undefined; '
                      'fingerprint=e9f9929de0331847ecc97ee929f44794; buvid_fp=e9f9929de0331847ecc97ee929f44794; LIVE_BU'
                      'VID=AUTO6416940827147782; PVID=1; SESSDATA=d985568c%2C1710063773%2C22d09%2A91CjCNxcT-pZHoVO_2t58'
                      '7TZ-4eV0GtA98O-OP6-lBGWwUtAZPs3LsKAk1-YZwNo88lyYSVmtId0hrbmUxMS1IaWpUZXJvbnVqSDJ6Qm1BaURJNmh0eGh'
                      'ab1REeHB0a3cwblh6ZWpRZW5YbVBZRGRHS1JhZGhpR2tKVFNSeXZFbmlqUEJmMXVnRU1RIIEC; bili_jct=82e70eda26b9'
                      '8e4c2f6fa5e5a4be9fdb; bili_ticket=eyJhbGciOiJIUzI1NiIsImtpZCI6InMwMyIsInR5cCI6IkpXVCJ9.eyJleHAiO'
                      'jE2OTQ3ODIxMDQsImlhdCI6MTY5NDUyMjkwNCwicGx0IjotMX0.bUa2t0QSEHfXywA9V-v0n3wCHmbDfecBW1NesYf9W6M; '
                      'bili_ticket_expires=1694782104; browser_resolution=1659-838; bp_video_offset_527027219=840796202'
                      '468376612; b_lsid=419DEFE8_18A92561C49; sid=7bbmxfrr',
            'Referer': 'https://search.bilibili.com/all',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.'
                          '0.0.0 Safari/537.36 Edg/116.0.1938.76',
        }
        cid = get_cid(video_url, headers)  # 获取cid码
        danmu = get_danmu(cid, headers)  # 获取弹幕列表
        write_txt(danmu, './danmu.txt')  # 写入文件
    except Exception as e:
        print(f"弹幕获取（总）出现异常: {e}")


if __name__ == '__main__':
    url = 'https://www.bilibili.com/video/av275130756'
    print(main(url))
