#coding:utf-8
import pickle
from os import path
import jieba
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import json
import io
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

def ciyun(filepath):
  comment = []
  with open(filepath,'r') as f:
    rows = f.readlines()
    for row in rows:
      if len(row.split(',')) == 5:
        comment.append(row.split(',')[4].replace('\n',''))

  comment2=json.dumps(comment, ensure_ascii=False)#转码显示中文
  print "comment2",comment2
  comment_after_split = jieba.cut(str(comment2),cut_all=False)

  wl_space_split= " ".join(comment_after_split)
  print "wl_space_split",wl_space_split
  #导入背景图
  backgroud_Image = plt.imread('1.jpg') 
  stopwords = STOPWORDS.copy()
  #可以加多个屏蔽词
  stopwords.add("电影")
  stopwords.add("一部")
  stopwords.add("一个")
  stopwords.add("没有")
  stopwords.add("什么")
  stopwords.add("有点")
  stopwords.add("这部")
  stopwords.add("这个")
  stopwords.add("不是")
  stopwords.add("真的")
  stopwords.add("感觉")
  stopwords.add("觉得")
  stopwords.add("还是")

  #设置词云参数 
  #参数分别是指定字体、背景颜色、最大的词的大小、使用给定图作为背景形状 
  wc = WordCloud(width=1024,height=768,background_color='white',
    mask=backgroud_Image,font_path='DroidSansFallbackFull.ttf',
    stopwords=stopwords,max_font_size=400,
    random_state=50)
  wc.generate_from_text(wl_space_split)
  img_colors= ImageColorGenerator(backgroud_Image)
  wc.recolor(color_func=img_colors)
  #plt.imshow(wc)
  #plt.axis('off')#不显示坐标轴  
  #plt.show()
  #保存结果到本地
  if filepath=='xie_zheng.txt':
    wc.to_file('xie_zheng_ciyun.jpg')
  elif filepath=='yaoshen.txt':
    wc.to_file('yaoshen_ciyun.jpg')
  
print "《邪不压正》："
ciyun('xie_zheng.txt')
print '\n'
print "《我不是药神》："
ciyun('yaoshen.txt')