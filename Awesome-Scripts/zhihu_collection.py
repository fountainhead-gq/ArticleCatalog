#!/url/bin/env python
# -*- coding: utf-8 -*-

from .spider import Spider
import os, re, http
import urllib, sys
import random, time


# store_path = os.getcwd()
# store_path = os.path.join(store_path, 'ceshi')

zhihu_url = 'https://www.zhihu.com'

class ZhihuColletion(Spider):
    def __init__(self, PageStart, PageEnd, url):
        self._url = url
        self._PageStart = int(PageStart)
        self._PageEnd = int(PageEnd) + 1
        # self.downlimit = 10  # 赞同数

    def start(self):
        for page in range(self._PageStart, self._PageEnd):  # 收藏夹的页数

            url = self._url + '?page=' + str(page)
            content = self.getUrl(url)
            # questionList = content.find_all('div', class_='zm-item')
            questionList = content.find_all('div', {'class': 'zm-item'})

            foder_title = str(content.find('h2', {'class': 'zm-item-title zm-editable-content'}))
            foder_title = re.sub('<h2 class="zm-item-title zm-editable-content" id="zh-fav-head-title">|</h2>', '', foder_title).strip()
            store_path = os.getcwd()
            store_path = os.path.join(store_path, foder_title)
            print('文件夹：%s' % store_path)

            for question in questionList:  # 获取收藏夹的问题
                # Qtitle = question.find('h2', class_='zm-item-title')
                Qtitle = question.find('h2', {'class': 'zm-item-title'})
                if Qtitle is None:  # 问题已不存在
                    continue

                questionStr = Qtitle.a.string  # 问题的题目
                Qurl = zhihu_url + Qtitle.a['href']  # 获取问题的链接
                Qtitle = re.sub(r'[\\/:*?"<>]', '#', Qtitle.a.string)
                print('-----正在获取的问题:%s' % questionStr)
                Qcontent = self.getUrl(Qurl)
                # answerlist = Qcontent.find_all('div', class_='zm-item-answer  zm-item-expanded')
                answerlist = Qcontent.find_all('div', {'class': 'zm-item-answer  zm-item-expanded'})
                self.processAnswer(answerlist, Qtitle, store_path)
                time.sleep(random.uniform(3, 5))


    def processAnswer(self, answerlist, Qtitle, store_path):
        j = 0
        for answer in answerlist:
            j = j + 1
            # upvoted = int(answer.find('span',class_='count').string.replace('K','000'))
            upvoted = answer.find('span', {'class': 'count'}).string.replace('K', '000')  # 获取答案的赞同数
            if int(upvoted) < 100:
                continue

            # authorInfo = answer.find('div', class_='zm-item-answer-author-info')
            authorInfo = answer.find('div', {'class': 'zm-item-answer-author-info'})  # 获取作者信息
            author = {'name': '', 'introduction': '', 'link': ''}
            try:
                author['name'] = authorInfo.find('a', {'class': 'author-link'}).string  # 作者姓名
            except AttributeError:
                author['name'] = '匿名用户'+str(j)
            except TypeError:  # 简介为空的情况
                pass

            try:
                author['introduction'] = authorInfo.find('span', {'class': 'bio'})['title']  # 作者简介
            except Exception:
                pass

            try:
                author['link'] = zhihu_url + answer.find('a', {'class': 'author-link'})['href']  # 作者链接
            except Exception:
                pass

            #file_name = os.path.join(store_path, Qtitle, 'info', author['name']+'_info.txt')  #
            #if os.path.exists(file_name):  # 是否已经抓取
                #continue

            # self.saveText(file_name, '{name}{introduction}\r\n{link}'.format(**author))
            # print('正在获取用户`{name}`的信息'.format(**author))

            # answerContent = answer.find('div', class_='zm-editable-content clearfix')
            answerContent = answer.find('div', {'class': 'zm-editable-content clearfix'})  # 答案内容

            if answerContent is None:
                continue

            # answerCont= answerContent.string  # 答案内容

            if str(answerContent) is not None:
                self.getTxtFormAnswer(str(answerContent), Qtitle, store_path, **author)
                print('正在获取用户`{name}`的答案'.format(**author))

            imgs = answerContent.find_all('img')
            if len(imgs) == 0:
                pass
            else:
                self.getImgFromAnswer(imgs, Qtitle, store_path,**author)
                print('正在获取用户`{name}`的图片'.format(**author))

    # 保存图片
    def getImgFromAnswer(self, imgs, Qtitle, store_path, **author):  # 获得图片
        i = 0
        for image in imgs:
            if 'inline-image' in image['class']:
                continue
            i = i + 1
            imageurl = image['src']
            extension = os.path.splitext(imageurl)[1]
            path_name = os.path.join(store_path, Qtitle, 'image', author['name']+'_'+str(i)+extension)
            if os.path.exists(path_name):  # 是否已存在
                continue
            try:
                self.saveImg(imageurl, path_name)
            except ValueError:
                pass
            except urllib.error.HTTPError as e:
                pass
            except KeyError:
                pass
            except http.client.IncompleteRead:
                pass

    # 保存文本内容
    def getTxtFormAnswer(self, answerContent, Qtitle, store_path, **author):  # 获取文字

        path_name = os.path.join(store_path, Qtitle, 'answer', author['name']+'_answer.txt')  # 创建answer文件夹

        try:
            # answerContent = re.sub('</?br>', '\n', answerContent)  # 替换换行
            answer = self.filter_tags(answerContent)
        except AttributeError:
            answer = '读取内容有误'
        except Exception:
            pass

        try:
            self.saveText(path_name, author['name'] + ': ' + author['introduction'] + '\n' + author['link'] + '\n' + answer)
        except Exception:
            pass


# 使用说明: zhihu_collection.py [page] [pageEnd] [url]
if __name__ == '__main__':
    # page, limit, paraUrl, paramsNum = 1, 0, 0, len(sys.argv)
    paramsNum = len(sys.argv)
    if paramsNum > 4:
        page, pageEnd, url = '', '', ''
    elif paramsNum == 4:  # 完整的参数
        page, pageEnd, url = sys.argv[1], sys.argv[2], sys.argv[3]
    elif paramsNum == 3:  # 缺省pageEnd参数
        page = sys.argv[1]
        pageEnd = page   # 默认省略pageEnd参数
        url = sys.argv[2]
    else:
        page, pageEnd = 1, 1
        url = ''

    # url = 'https://www.zhihu.com/collection/42240523'  # page参数改为代码添加
    # url = 'https://www.zhihu.com/collection/20054781'

    if paramsNum > 4:
        print('==='*10+'请检查参数个数是否有误'+'==='*10)
        print('命令格式: python zhihu_collection.py [page 必填] [pageEnd 可省略] [url 必填]')
        print('==='*10+'请检查参数个数是否有误'+'==='*10)

    elif len(url) == 0:
        print('==='*10+'缺少参数,请检查'+'==='*10)
        print('命令格式: python zhihu_collection.py [page 必填] [pageEnd 可省略] [url 必填]')
        print('==='*10+'缺少参数,请检查'+'==='*10)

    elif url.isdigit():
        print('==='*10+'URL参数必须为有效的url链接'+'==='*10)
        print('命令格式: python zhihu_collection.py [page 必填] [pageEnd 可省略] [url 必填]')
        print('==='*10+'URL参数必须为有效的url链接'+'==='*10)

    else:
        spider = ZhihuColletion(page, pageEnd, url)  #
        spider.start()