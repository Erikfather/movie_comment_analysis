#coding:utf-8
from pyecharts import ThemeRiver
import json

def tongji(filepath):
  rate = []
  with open(filepath,'r') as f:
    rows = f.readlines()
    for row in rows:
      if len(row.split(',')) == 5:
        rate.append(row.split(',')[3].replace('\n',''))

  v1=(rate.count('5')+rate.count('4.5'))
  v2=(rate.count('4')+rate.count('3.5'))
  v3=(rate.count('3')+rate.count('2.5'))
  v4=(rate.count('2')+rate.count('1.5'))
  v5=(rate.count('1')+rate.count('0.5'))

  #饼状图
  from pyecharts import Pie
  attr = [u"五星", u"四星", u"三星", u"二星", u"一星"]
  print json.dumps(attr,ensure_ascii=False)
  #分别代表各星级评论数
  v=[v1,v2,v3,v4,v5]
  print v
  if filepath=='xie_zheng.txt':
    pie = Pie(u"《邪不压正》饼图-星级玫瑰图示例", title_pos='center', width=900)
    pie.add("7-17", attr, v, center=[75, 50], is_random=True,
            radius=[30, 75], rosetype='area',
            is_legend_show=False, is_label_show=True)

    pie.render(filepath.split('.')[0]+'_pie.html')
  else:
    pie = Pie(u"《我不是药神》饼图-星级玫瑰图示例", title_pos='center', width=900)
    pie.add("7-17", attr, v, center=[75, 50], is_random=True,
            radius=[30, 75], rosetype='area',
            is_legend_show=False, is_label_show=True)

    pie.render(filepath.split('.')[0]+'_pie.html')

print "《邪不压正》："
tongji('xie_zheng.txt')
print '\n'
print "《我不是药神》："
tongji('yaoshen.txt')