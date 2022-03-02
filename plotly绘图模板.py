'''
import plotly
plotly.__version__ # '4.4.1'

对于比较新版本的plotly，需要通过chart_studio来进行调用。
pip install chart_studio

之后需要到官网生成用户名和密钥。
官网：https://chart-studio.plotly.com
用户名：slowdive
密钥：OGf4ZagfnQuQ6ydJXc5H
'''
import chart_studio
chart_studio.tools.set_credentials_file(username='slowdive', api_key='OGf4ZagfnQuQ6ydJXc5H')
import chart_studio.plotly as py
import plotly.graph_objects as go

#-------先在线绘制一张样例----------
trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = [trace0, trace1]

py.plot(data, filename = 'basic-line', auto_open=True)


# ------------如果想在 jupyter 上离线绘制的话，需要再导入以下两句-----------------
# 并采用不同的绘制方法。用 iplot 绘制。 ！！强烈建议使用以下这种方式。
from plotly.offline import init_notebook_mode, iplot
init_notebook_mode(connected=True)

trace0 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[10, 15, 13, 17]
)
trace1 = go.Scatter(
    x=[1, 2, 3, 4],
    y=[16, 5, 11, 9]
)
data = [trace0, trace1]

# 添加图层layout
layout = dict(title = '折线图')

fig = dict(data = data, layout = layout)
iplot(fig)


# 读取数据用于作图
import pandas as pd
df = pd.read_csv("timesData.csv")
df = df.iloc[:100,:]

#-----------观察从1-100的大学的引用分数和教学分数。用两个折线图绘制在一个图上---------------
#第一条折线。 注：go.scatter可以用来绘制散点图或者折线图
trace1 = go.Scatter(
                    x = df.world_rank,
                    y = df.citations,
                    mode = 'lines',
                    name = '引用分数',
                    # maker用来定义点的性质，如颜色、大小等
                    marker = dict(color='red'),
                    # 这里的内容指的是当我们的鼠标在图上时，会自动显示大学的名字
                    text = df.university_name
                    )

#第二条折线
trace2 = go.Scatter(
                    x = df.world_rank,
                    y = df.teaching,
                    mode = 'lines',
                    name = '教学分数',
                    # maker用来定义点的性质，如颜色、大小等
                    marker = dict(color='blue'),
                    # 这里的内容指的是当我们的鼠标在图上时，会自动显示大学的名字
                    text = df.university_name
                    )

data = [trace1, trace2]

# 添加图层layout
              # 设置图像的标题
layout = dict(title = 'top100大学的引用分数和教学分数',
              # 设置x轴名称，x轴刻度线的长度，不显示零线
              xaxis= dict(title= '世界排名')
             ) 

# 将data与layout组合为一个图像
fig = dict(data = data, layout = layout)
# 绘制图像
iplot(fig)


#------------用柱状图统计前100大学的国家数量---------------
tmp = df['country'].value_counts()

trace1 = go.Bar(
                    x = tmp.index,
                    y = tmp.values,
                    name = '学校数量',
                    marker = dict(color='yellow'),
                    text = df.index
                    )

data = trace1

layout = dict(title = 'top100大学的国家分布',
              xaxis= dict(title= '国家')
             ) 

fig = dict(data = data, layout = layout)
iplot(fig)


#------------查看前100所学校的研究得分直方图--------------
trace1 = go.Histogram(
                    x = df.world_rank,
                    y = df.research,
                    name = '研究得分',
                    marker =dict(color='rgba(171, 50, 96, 0.6)'), #'rgba(12, 50, 196, 0.6)'也挺好看
                    text = df.university_name
                    )

data = trace1

layout = dict(title = 'top100大学的研究得分分布',
              xaxis= dict(title= '世界排名')
             ) 

fig = dict(data = data, layout = layout)
iplot(fig)


#----------学生数量的箱线图--------------
trace = go.Box(
                y = df.num_students,
                name = '学生数量的箱线图',
                marker = dict(color = 'rgb(12, 12, 140)')
                )

data = trace
    
layout = dict(title = '学生数量的箱线图') 

fig = dict(data = data, layout = layout)
iplot(fig)


#------------绘制多个子图--------------
trace1 = go.Scatter(x = df.world_rank, y = df.research, name = "research")
trace2 = go.Scatter(x = df.world_rank, y = df.citations, xaxis='x2', yaxis='y2', name = "citations")
trace3 = go.Scatter(x = df.world_rank, y = df.income, xaxis='x3', yaxis='y3', name = "income")
trace4 = go.Scatter(x = df.world_rank, y = df.total_score, xaxis='x4', yaxis='y4',name = "total_score")

data = [trace1, trace2, trace3, trace4]

layout = go.Layout(
    # 指定第一幅图x轴的范围，以此类推
    xaxis=dict(domain=[0, 0.45]),
    # anchor：锚。应该是对准的意思吧。。
    xaxis2=dict(domain=[0.55, 1],anchor='y2'),
    xaxis3=dict(domain=[0, 0.45],anchor='y3'),
    xaxis4=dict(domain=[0.55, 1],anchor='y4'),
    
    yaxis=dict(domain=[0, 0.45]),
    yaxis2=dict(domain=[0, 0.45],anchor='x2'),
    yaxis3=dict(domain=[0.55, 1],anchor='x3'),
    yaxis4=dict(domain=[0.55, 1],anchor='x4'),
    
    title = 'Research, citation, income and total score VS World Rank of Universities'
    )

fig = dict(data=data, layout=layout)
iplot(fig)

