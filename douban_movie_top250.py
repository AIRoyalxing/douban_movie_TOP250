import requests, json, bs4

#定义存储电影名称及评分的列表
movieName1 = []
movieScore1 = []

#循环获取TOP25的数据
for pages in range(10):
    #豆瓣网址
    if pages == 0:
        url = 'https://movie.douban.com/top250'
    else:
        url = 'https://movie.douban.com/top250?start='+str(pages*25)+'&filter='
    #请求数据
    res = requests.get(url)

    #用解释器解释源码
    movie = bs4.BeautifulSoup(res.text, 'html.parser')
    movieName = movie.select('div.hd a .title')
    movieScore = movie.select('ol li .rating_num')

    #print(movieName)
    for names in movieName:
        #将电影名称添加至电影名列表，舍去英文名
        if names.getText().find('\xa0/\xa0') == -1:
            movieName1.append(names.getText())
        else:
            continue

    for scores in movieScore:
        #将电影评分添加至评分列表
        movieScore1.append(scores.getText())

#打印TOP250的电影数据
for num in range(len(movieScore1)):

    print(movieName1[num]+'的电影评分是'+movieScore1[num]+'分')
