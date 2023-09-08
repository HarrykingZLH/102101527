import stylecloud
# from palettable.cartocolors.sequential

stylecloud.gen_stylecloud(file_path='danum.txt',
                          icon_name='fas fa-radiation',
                          palette= 'cmocean.diverging.Balance_20',
                          font_path="msyh.ttc",
                          background_color='black',
                          output_name='cloud.jpg',
                          gradient='horizontal',
                          invert_mask=True,
                          size= 2048,
                          )