import expanddouban
from bs4 import BeautifulSoup
import time
import sys


def getMovieUrl(category, location):
    url = "https://movie.douban.com/tag/#/?sort=S&range=9,10&tags=电影" + ',' + category + ',' + location
    return url


category = ['剧情', '科幻', '喜剧']
location = ['大陆', '美国', '香港', '台湾', '日本', '韩国', '英国', '法国', '德国', '意大利', '西班牙', '印度', '泰国', '俄罗斯', '伊朗', '加拿大', '澳大利亚',
            '爱尔兰', '瑞典', '巴西', '丹麦']


def getData(html):
    soup = BeautifulSoup(html, "html.parser")
    movieList = soup.find('div', attrs={'class': 'list-wp'})  # 找到第一个class属性值为list-wp的div标签
    moveInfo = []
    for movieA in movieList.find_all('a'):  # 找到所有a标签
        data = []
        movieName = movieA.find('span', attrs={'class': 'title'}).getText()  # 找到第一个class属性值为title的span标签
        data.append(movieName)

        movieScore = movieA.find('span', attrs={'class': 'rate'}).getText()  # 找到第一个class属性值为rate的span标签
        data.append(movieScore)

        data.append(movieA['href'])

        MovieCoverLink = movieA.find('img').attrs['src']
        data.append(MovieCoverLink)

        moveInfo.append(data)
    return (moveInfo)


Movie_information = []
fine = []
for i in range(0, 3):
    for j in range(0, 21):
        url = getMovieUrl(category[i], location[j])
        html = expanddouban.getHtml(url, loadmore=True, waittime=2)
        fine.append(len(getData(html)))
        Movie_information.append(getData(html))

fine1 = fine[0:21]
fine2 = fine[21:42]
fine3 = fine[42:63]

total1 = 0
total2 = 0
total3 = 0
for i in range(0, 21):
    total1 += fine1[i]
    total2 += fine2[i]
    total3 += fine3[i]

max1 = []
max2 = []
max3 = []
for i in range(0, 3):
    max1.append(fine1.index(max(fine1)))
    fine1[fine1.index(max(fine1))] = 0
    max2.append(fine2.index(max(fine2)))
    fine2[fine2.index(max(fine2))] = 0
    max3.append(fine3.index(max(fine3)))
    fine3[fine3.index(max(fine3))] = 0

for m in range(0, 63):
    for n in range(0, len(Movie_information[m])):
        if -1 < m < 21:
            if len(Movie_information[m][n]):
                Movie_information[m][n].insert(1, category[0])
                Movie_information[m][n].insert(1, location[m])
        elif 20 < m < 42:
            if len(Movie_information[m][n]):
                Movie_information[m][n].insert(1, category[1])
                Movie_information[m][n].insert(1, location[m - 21])
        else:
            if len(Movie_information[m][n]):
                Movie_information[m][n].insert(1, category[2])
                Movie_information[m][n].insert(1, location[m - 42])

Movie_info = []
for m in range(0, 63):
    for n in range(0, len(Movie_information[m])):
        if len(Movie_information[m][n]):
            Movie_info.append(Movie_information[m][n])

output = sys.stdout
outputfile = open("movies.csv", 'w', encoding='utf-8')
sys.stdout = outputfile

for list in Movie_info:
    print(list)

outputfile.close()
sys.stdout = output

output = sys.stdout
outputfile = open("output.txt", 'w', encoding='utf-8')
sys.stdout = outputfile

print("剧情数量排名前三的地区有:", location[max1[0]], "%.2f%%" % (fine[max1[0]] / total1 * 100), location[max1[1]],
      "%.2f%%" % (fine[max1[1]] / total1 * 100), location[max1[2]], "%.2f%%" % (fine[max1[2]] / total1 * 100))
print("科幻数量排名前三的地区有:", location[max2[0]], "%.2f%%" % (fine[max2[0] + 21] / total2 * 100), location[max2[1]],
      "%.2f%%" % (fine[max2[1] + 21] / total2 * 100), location[max2[2]], "%.2f%%" % (fine[max2[2] + 21] / total2 * 100))
print("喜剧数量排名前三的地区有:", location[max3[0]], "%.2f%%" % (fine[max3[0] + 42] / total3 * 100), location[max3[1]],
      "%.2f%%" % (fine[max3[1] + 42] / total3 * 100), location[max3[2]], "%.2f%%" % (fine[max3[2] + 42] / total3 * 100))

outputfile.close()
sys.stdout = output
