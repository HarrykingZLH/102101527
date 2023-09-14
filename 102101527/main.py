import get_video
import get_danmu
from collections import Counter
import pandas as pd
import tqdm
import visualization
import time


def write_txt(context_list, filename):
    with open(filename, 'w', encoding='utf-8') as f:  # 创建TXT文件存储弹幕
        for context in context_list:
            f.write(str(context) + '\n')  # 弹幕竖直排列写入


if __name__ == '__main__':
    time_start = time.time()  # 记录开始时间

    keyword = '日本核污染水排海'  # 设置搜索关键词
    n = 300  # 设置总视频数
    urls = get_video.main(keyword, n)  # 获取视频URL
    danmu = []  # 弹幕列表
    for url in tqdm.tqdm(urls):  # 设置进度条更加直观
        contexts = get_danmu.main(url)  # 获取单个视频的弹幕
        danmu += contexts  # 添加入总列表

    print(len(danmu))  # 输出总爬取弹幕数

    word_counts = Counter(danmu)  # 记录频次
    df = pd.DataFrame(word_counts.items(), columns=["弹幕", "频次"])  # 写入xlsx文件
    df.to_excel("danmu.xlsx", index=False)  # 生成文件

    top_20_words = word_counts.most_common(20)  # 提取频次前二十的弹幕
    keys = []
    values = []
    for word, count in top_20_words:
        keys.append(word)
        values.append(count)
        print(f"{word}: {count} ")  # 输出到控制台
    visualization.chart_making(keys, values)  # 数据可视化

    write_txt(danmu, './danmu.txt')  # 将弹幕存储到txt文件
    visualization.cloud_making()  # 制作词云

    time_end = time.time()  # 记录结束时间
    time_sum = time_end - time_start  # 计算的时间差为程序的执行时间，单位为秒/s
    print(time_sum)
