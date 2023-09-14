import get_video
import get_danmu
from collections import Counter
import pandas as pd
import tqdm
import visualization
import time
import multiprocessing


def main(urls):
    print(urls)
    pool = multiprocessing.Pool(30)  # 创建30个进程，一页有30个视频
    for url in urls:
        pool.apply_async(get_danmu.main(url))  # 并行爬取弹幕数据
    pool.close()  # 关闭进程池，表示不再接受新的任务
    pool.join()  # 等待所有进程任务完成



if __name__ == '__main__':
    try:

        time_start = time.time()  # 记录开始时间
        keyword = '日本核污染水排海'  # 设置搜索关键词
        n = 300  # 设置总视频数
        danmu = []  # 弹幕列表
        urls = get_video.main(keyword, n)

        for url in tqdm.tqdm(urls):
            main(url)

        with open('./danmu.txt', 'r', encoding='utf-8') as file:
            danmu = [danmu.strip() for danmu in file.readlines()]  # 读取弹幕
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
        visualization.cloud_making()  # 制作词云
        time_end = time.time()  # 记录结束时间
        time_sum = time_end - time_start  # 计算的时间差为程序的执行时间，单位为秒/s
        print(time_sum)
    except Exception as e:
        print(f"main出现异常: {e}")
