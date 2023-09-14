import stylecloud
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd


def cloud_making():
    try:
        stylecloud.gen_stylecloud(file_path='danmu.txt',  # 存储弹幕的文件位置
                                  icon_name='fas fa-dog',  # 云图图标
                                  palette='cmocean.diverging.Balance_6',  # 调色板
                                  font_path="msyh.ttc",  # 字体信息
                                  background_color='black',  # 背景颜色
                                  output_name='cloud.jpg',  # 输出图片文件名
                                  gradient='horizontal',  # 渐变
                                  invert_mask=False,  # 是否反转
                                  size=2048,  # 图片大小
                                  )
    except Exception as e:
        print(f"词云生成出现异常: {e}")


def chart_making(labels, values):
    try:
        plt.rc("font", family='YouYuan')  # 设置字体防止乱码
        _, ax = plt.subplots(figsize=(12, 6))  # 创建一个图表
        sns.barplot(x=labels, y=values, ax=ax, color='red')  # 绘制柱状图
        ax.set_title("弹幕频次前20")
        ax.set_xlabel("弹幕")
        ax.set_ylabel("频次")
        ax.set_xticklabels(labels, rotation=45, ha='right')  # 设置x轴标签为斜着显示
        plt.show()  # 显示图表
    except Exception as e:
        print(f"图表生成出现异常: {e}")


if __name__ == '__main__':

    # 用pandas读取xlsx文件
    df = pd.read_excel('file.xlsx')

    # 将DataFrame转换为字典
    data_dict = df.to_dict(orient='split')

    # 提取字典中的数据
    key = [row[0] for row in data_dict['data']]
    value = [row[1] for row in data_dict['data']]
    chart_making(key, value)

    # cloud_making()
