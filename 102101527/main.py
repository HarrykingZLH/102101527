import get_video
import get_danmu
import tqdm

def write_txt(contexts, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        for context in contexts:
            f.write(str(context) + '\n')

if __name__ == '__main__':
    keyword = '日本核污染水排海'
    sum = 300
    cnt = []
    # 获取视频地址
    urls = get_video.main(keyword, sum)
    # print(urls)
    danmu = []
    for url in tqdm.tqdm(urls):
        contexts = get_danmu.main(url)
        cnt.append(len(contexts))
        danmu += contexts

    print(len(danmu))
    write_txt(cnt, './cnt.txt')
    write_txt(danmu, './danmu.txt')