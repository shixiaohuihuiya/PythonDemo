import requests
from bs4 import BeautifulSoup

# 爬取的目标网址
url = 'https://zsxxw.e21.cn/e21html/zsarticles/gaozhao/2024_06_25/81681.html'

# 发送 HTTP GET 请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 解析网页内容
    soup = BeautifulSoup(response.text, 'html.parser')

    # 获取所有文本内容
    text_content = soup.get_text()

    # 获取所有 HTML 内容
    html_content = soup.prettify()
    print(html_content)
    # 保存文本内容到文件
    with open('page_text.txt', 'w', encoding='utf-8') as text_file:
        text_file.write(text_content)

    # 保存 HTML 内容到文件
    with open('page_html.html', 'w', encoding='utf-8') as html_file:
        html_file.write(html_content)

    print('页面内容已保存到文件')
    with open('page_html.html', 'r', encoding='GBK') as file:
        content = file.read()


else:
    print('Failed to retrieve the webpage')
