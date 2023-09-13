import stylecloud


def cloud_making():
    stylecloud.gen_stylecloud(file_path='danmu.txt',
                              icon_name='fas fa-radiation',
                              palette='cmocean.diverging.Balance_20',
                              font_path="msyh.ttc",
                              background_color='black',
                              output_name='cloud.jpg',
                              gradient='horizontal',
                              invert_mask=True,
                              size=2048,
                              max_words=300
                              )


if __name__ == '__main__':
    cloud_making()
