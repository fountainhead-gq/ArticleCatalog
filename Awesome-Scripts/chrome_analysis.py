# -*- coding: utf-8 -*-

import os
import sqlite3
import operator
from collections import OrderedDict
import matplotlib.pyplot as plt


def parse(get_url):
	try:
		parsed_url_components = get_url.split('//')
		sublevel_split = parsed_url_components[1].split('/', 1)
		domain = sublevel_split[0].replace("www.", "")
		return domain
	except IndexError:
		print("URL format error!")


def analyze(results):
	prompt = input("输入type<a>以字符串展示，输入type<p>以图表展示\n input: ")

	if prompt.lower() == "a":
		for site, count in sites_count_sorted.items():
			print(site, count)
	elif prompt.lower() == "p":
		plt.bar(range(len(results)), results.values(), align='edge')
		plt.xticks(rotation=45)
		plt.xticks(range(len(results)), results.keys())
		plt.show()
	else:
		print("ah?")
		quit()


# Chrome历史数据存储路径
data_path = os.path.expanduser('~') + r"\AppData\Local\Google\Chrome\User Data\Default"
history_db = os.path.join(data_path, 'History')

# 打开一个到 SQLite 数据库文件 database 的链接，【当一个数据库被多个连接访问，且其中一个修改了数据库，此时 SQLite 数据库被锁定，直到事务提交。】
c = sqlite3.connect(history_db)
cursor = c.cursor()  # 创建一个 cursor
select_statement = "SELECT urls.url, urls.visit_count FROM urls, visits WHERE urls.id = visits.url;"
cursor.execute(select_statement)  # 执行SQL 语句
results = cursor.fetchall()  # 获取查询结果集中所有行

sites_count = {}
for url, count in results:
	url = parse(url)
	if url in sites_count:
		sites_count[url] += 1
	else:
		sites_count[url] = 1

sites_count_sorted = OrderedDict(sorted(sites_count.items(), key=operator.itemgetter(1), reverse=True))


# 关闭chrome后再执行
if __name__ == "__main__":
	analyze = analyze(sites_count_sorted)
	print(analyze)
