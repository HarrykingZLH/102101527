import get_video
import get_danmu
from collections import Counter
import pandas as pd
import tqdm
import make_cloud


def write_txt(context_list, filename):
    with open(filename, 'a', encoding='utf-8') as f:
        for context in context_list:
            f.write(str(context) + '\n')


if __name__ == '__main__':
    keyword = '日本核污染水排海'
    n = 300
    cnt = []
    # 获取视频地址
    urls = get_video.main(keyword, n)

    danmu = []
    for url in tqdm.tqdm(urls):
        contexts = get_danmu.main(url)
        cnt.append(len(contexts))
        danmu += contexts

    print(len(danmu))

    word_counts = Counter(danmu)
    df = pd.DataFrame(word_counts.items(), columns=["弹幕", "频次"])
    df.to_excel("output.xlsx", index=False)

    top_20_words = word_counts.most_common(20)
    for word, count in top_20_words:
        print(f"{word}: {count} ")

    write_txt(danmu, './danmu.txt')
    make_cloud.cloud_making()
