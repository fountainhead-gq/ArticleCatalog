#!/url/bin/env python
# -*- coding: utf-8 -*-

from .spider import Spider
import os, re, http
import urllib, sys
import random, time

zhihu_url = 'https://www.zhihu.com'

class ZhihuQuestion(Spider):
    def __init__(self, url):
        self.url = url

    def getQuestion(self):
        url = self.url
        content = self.getUrl(url)
        contentList = content.find_all('div', {'class': 'zm-item-answer  zm-item-expanded'})  # 获取所有问题答案

        # foder_title = str(content.find('h2', {'class': 'zm-item-title zm-editable-content'}))  # 标题
        # foder_title = re.sub('<h2 class="zm-item-title zm-editable-content">|</h2>', '', foder_title).strip()
        # foder_title = re.sub('["?]', '', foder_title).strip()
        foder_title= content.find('h2', {'class': 'zm-item-title zm-editable-content'}).string.strip()
        store_path = os.getcwd()
        store_path = os.path.join(store_path, foder_title)
        print('----路径: %s' % store_path)

        j = 0
        for content in contentList:
            j = j + 1
            time.sleep(random.random()*3)
            voteCount = content.find('span', {'class': 'count'}).string.replace('K', '000')
            if int(voteCount) < 20:
                continue

            authorInfo = content.find('div', {'class': 'zm-item-answer-author-info'})  # 获取作者信息

            try:
                authorName = authorInfo.find('a', {'class': 'author-link'}).string  # 作者姓名
            except AttributeError:
                authorName = '匿名用户' + str(j)
            except TypeError:
                pass



            try:
                authorItro = authorInfo.find('span', {'class': 'bio'})['title']  # 作者简介
            except Exception:
                pass

            try:
                authorLink = authorInfo.find('a', {'class': 'author-link'})['href']  # 作者链接
                authorLink = zhihu_url + authorLink
            except Exception:
                pass

            Qanswer = content.find('div', {'class': 'zm-editable-content clearfix'})  # 问题答案
            if Qanswer is None:
                continue

            if str(Qanswer) is not None:
                path_name = os.path.join(store_path, 'answer', authorName + '_answer.txt')  # 创建answer文件夹
                if os.path.exists(path_name):  # 是否已经抓取
                    continue

                try:
                    answer = self.filter_tags(str(Qanswer))
                    # answer = re.sub('', '', Qanswer)
                except Exception:
                    pass

                try:
                    self.saveText(path_name, authorName + ':  ' + authorItro + '\n\r' + authorLink + '\n\r' + answer)
                    print('正获取「%s」的答案' % authorName)
                except Exception:
                    pass

            images = content.find_all('img')  # 图片
            i = 0
            if len(images) == 0:
                pass
            else:
                for img in images:
                    if 'inline-image' in img['class']:
                        continue
                    i = i + 1
                    imgUrl = img['src']
                    attachName = os.path.splitext(imgUrl)[1]
                    imgPath = os.path.join(store_path, 'image', authorName + '_'+str(i) + attachName)
                    if os.path.exists(imgPath):  # 是否已存在
                        continue
                    try:
                        self.saveImg(imgUrl, imgPath)
                    except ValueError:
                        pass
                    except KeyError:
                        pass
                    except Exception:
                        pass


if __name__ == '__main__':

    paramsNum = len(sys.argv)
    if paramsNum > 2:
        url = ''
    elif paramsNum == 2:
        url = sys.argv[1]
    else:
        url = ''

    if paramsNum > 2:
        print('==='*10+'参数只能是url'+'==='*10)
        print('命令格式: python zhihu_question.py [url 必填]')
        print('==='*10+'参数只能是url'+'==='*10)
    elif len(url) == 0:
        print('==='*10+'URL参数必须为有效的url链接'+'==='*10)
        print('命令格式: python zhihu_question.py [url 必填]')
        print('==='*10+'URL参数必须为有效的url链接'+'==='*10)
    else:
        zh = ZhihuQuestion(url)
        zh.getQuestion()