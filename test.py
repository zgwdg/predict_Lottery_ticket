
import os
import requests
import pandas as pd
from bs4 import BeautifulSoup
from config import *
# import http.client


def get_current_number():
    """ 获取最新一期数字
    :return: int
    """
    # http.client.HTTPConnection._http_vsn = 11
    # http.client.HTTPConnection._http_vsn_str = 'HTTP/1.1'
    r = requests.get(URL)
    r.encoding = "gb2312"
    soup = BeautifulSoup(r.text, "lxml")
    current_num = soup.find('tbody',id='data-tab').contents[00].contents[00].text
    return current_num

def spider(start, end, mode):
    """ 爬取历史数据
    :param start 开始一期
    :param end 最近一期
    :param mode 模式
    :return:
    """
    # http.client.HTTPConnection._http_vsn = 10
    # http.client.HTTPConnection._http_vsn_str = 'HTTP/1.0'
    url = "{}?{}".format(URL, path.format(start, end))
    r = requests.get(url=url)
    r.encoding = "gb2312"
    soup = BeautifulSoup(r.text, "lxml")
    trs = soup.find('tbody', id='data-tab').find_all("tr")
    data = []
    for tr in trs:
        """[<td>2013065</td>, <td>2013-06-06(四)</td>, <td><span class="ball_5">07</span> <span class="ball_5">18</span> <span class="ball_5">19</span> <span class="ball_5">23</span> <span class="ball_5">29</span> <span class="ball_5">30</span> </td>, <td><span class="ball_1">02<span></span></span></td>, <td>334,460,176</td>, <td>5</td>, <td>9,309,082</td>, <td>165</td>, <td>195,867</td>, <td>2亿0167万5690元</td>, <td><a href="http://cp.360.cn/experience/ssq?Issue=2013065" target="_blank">查看统计</a></td>]"""
        item = dict()
        item[u"期数"] = tr.find_all('td')[0].get_text().strip()
        item[u"红球号码_1"] = tr.find_all("td")[2].get_text().strip().split()[0]
        item[u"红球号码_2"] = tr.find_all("td")[2].get_text().strip().split()[1]
        item[u"红球号码_3"] = tr.find_all("td")[2].get_text().strip().split()[2]
        item[u"红球号码_4"] = tr.find_all("td")[2].get_text().strip().split()[3]
        item[u"红球号码_5"] = tr.find_all("td")[2].get_text().strip().split()[4]
        item[u"红球号码_6"] = tr.find_all("td")[2].get_text().strip().split()[5]
        item[u"蓝球"] = tr.find_all("td")[3].get_text().strip()
        # item[u"快乐星期天"] = tr.find_all("td")[8].get_text().strip()
        item[u"奖池奖金(元)"] = tr.find_all("td")[9].get_text().strip()
        item[u"一等奖_注数"] = tr.find_all("td")[5].get_text().strip()
        item[u"一等奖_奖金(元)"] = tr.find_all("td")[6].get_text().strip()
        item[u"二等奖_注数"] = tr.find_all("td")[7].get_text().strip()
        item[u"二等奖_奖金(元)"] = tr.find_all("td")[8].get_text().strip()
        item[u"总投注额(元)"] = tr.find_all("td")[4].get_text().strip()
        item[u"开奖日期"] = tr.find_all("td")[1].get_text().strip().split('(')[0]
        data.append(item)

    if mode == "train":
        df = pd.DataFrame(data)
        df.to_csv("{}{}".format(train_data_path, train_data_file), encoding="utf-8")
    elif mode == "predict":
        return pd.DataFrame(data)


spider(2013061, get_current_number(), "train")
