# movie_comment_analysis
## 利用猫眼API爬取《我不是药神》和《邪不压正》电影评论，绘制出全国各地区评论人数，同时制作热评词云，并统计打一星到五星的人数比例
#### 每部电影我只爬取了100页数据
### 猫眼API：http://m.maoyan.com//mmdb/comments/movie/movieID(每部电影都有各自的ID，可通过猫眼电影官网查看).json?_v_=yes&

    keshihua.py：利用echarts中的地图包，绘制出全国各地区评论人数分布
    tongji,py:绘制出打一星到五星的人数饼状图
    ciyun.py:绘制出热评词云

  ### 《邪不压正》评论地区分布
  https://erikfather.github.io/movie_comment_analysis/xie_zheng.html
  ![image](https://github.com/Erikfather/movie_comment_analysis/blob/master/%E8%AF%B4%E6%98%8E%E6%96%87%E4%BB%B6/1.jpg)
  ### 《邪不压正》统计图
  https://erikfather.github.io/movie_comment_analysis/xie_zheng_pie.html
  ![image](https://github.com/Erikfather/movie_comment_analysis/blob/master/%E8%AF%B4%E6%98%8E%E6%96%87%E4%BB%B6/2.jpg)
  ### 《邪不压正》词云
  ![image](https://github.com/Erikfather/movie_comment_analysis/blob/master/xie_zheng_ciyun.jpg)


  ### 《我不是药神》评论地区分布
  https://erikfather.github.io/movie_comment_analysis/yaoshen.html
  ![image](https://github.com/Erikfather/movie_comment_analysis/blob/master/%E8%AF%B4%E6%98%8E%E6%96%87%E4%BB%B6/3.jpg)
  ### 《我不是药神》统计图
  https://erikfather.github.io/movie_comment_analysis/yaoshen_pie.html
  ![image](https://github.com/Erikfather/movie_comment_analysis/blob/master/%E8%AF%B4%E6%98%8E%E6%96%87%E4%BB%B6/4.jpg)
  ### 《我不是药神》词云
  ![image](https://github.com/Erikfather/movie_comment_analysis/blob/master/yaoshen_ciyun.jpg)
