import random
data = []#单词数据库 存储诗词内容
Sdata = {}#单词暂存库 打包诗词内容并添加到数据库
def Load( str ):#加载单词
    Sdata={}
    f = open(str,'r', encoding='UTF-8')
    j=1
    IsLoadstart = False
    word = 0
    while True:
        Line = f.readline()
        if Line:
            if Line.startswith("-") == True:#读取单词组明
                if IsLoadstart == True:
                    Sdata["Line"]= word
                    data.append(Sdata.copy())
                    sdata = {}
                    word = 0
                    Isloadstart = False
                word = 0#初始化行数，因为没有读取诗词内容
                Wname = Line[1:]
                Sdata["Name"] = Wname#存储单词组名到系统
                IsLoadstart = True
            else:
                word = word + 1#行数加一
                Sdata[word]=Line
        else:
            Sdata["Line"] = word
            data.append(Sdata.copy())
            Sdata = {}
            word = 0
            break
    print("读取完成")
    #print(Sdata)
    #print(data)
    

def make():
    W = open("c:\\GWZKJWORK\\Eout.txt",'w', encoding='UTF-8')
    i= 0
    q = []
    wordlab = 0#外部行数 即在大库中的行数

    count = len(data)
    while i<count:
        #print (data)
        create = data[i]
        allLine = create["Line"]
        scname = create["Name"]#单词组名
      #  scauthor = create["author"]
        W.write("<<" + scname[:len(scname) - 1 ]+ ">>" + "\n")
     #   W.write("作者" + scauthor)
        wl = 1
        i += 1
        #print(create)
        #print(allLine)
        while wl < allLine + 1:
        #    print(wl)
            shici = create[wl]
        #    print(shici)
            douhaolo = 0#分隔号$的位置
            #wordlabjs = 0
            #question = 0#填空问题的数量
            js=0
            IsFinish = False
            while IsFinish != True :
                js+=1
                #douhaolo 和 nd 若为-1则代表没有逗号
                douhaolo = shici.find("：")#查询第一个逗号的位置，下文将清除这些文段
                wordlab += 2#小段数量 为2是指释义和单词总共为2段 所以一次加两段
                #wordlabjs +=1#因为每一行只能有一道题 所以此参数作废
                
                other = shici[douhaolo + 1:] #把分隔符号后面的字符全部给Other 即释义
                qm = random.randint(0,1)#随机题面代码 0为题目 1为题面
                #if other.find("，") == -1 and question == 0:#r如果下文查询无逗号（最后一个分段）且没有一个问题，强制此题为题目
                #    qm = 0
                #此部分作废 因为每行只有一个单词一个释义
                if qm == 0:
                    linenumber =len(other)#查询填空线数
                    q.insert(wordlab-1,shici[:douhaolo])
                    q.insert(wordlab,"_" *linenumber*3 + "\n")#输出填空线
                    IsFinish = True
                else:
                            IsFinish= True#宣布该文章该句出题结束
                            q.insert(wordlab-1,"_" * len(shici[:douhaolo])*3)
                            q.insert(wordlab,other+ "\n")#明文输出
                            #other = other[nd + 1 :]
            printline = 0
            while printline < js+1:#printline代表的是走过的行数 从0开始是代表q项中从0开始
                if printline == js:
                    W.write(q[printline] + "\n")
                    q=[]
                else:
                    W.write(q[printline])
                printline += 1
            wl+=1

    W.write("使用由鬼未族科技和cyx125共同开发的「Python英语默写生成器1.1」生成")
    print("题目生成完成")

                        
print("DEBUG MODE")
print("未完工，暂时是演示模式，完工后会在视频底下放Github下载链接")
print("LOADING")
print("""
-------------------
BILIBILI 鬼未族科技 cyx125
英语默写生成系统
Ver 1.1
#没错 语文默写系统完工的第二天英语默写系统也写完了
更新了以下：
取消前置符 分隔符改为中文冒号： 效率大幅增加
-------------------
该系统逻辑如下：
单词导入后 将随机决定题目。
每个单词可能为中译英也可能为英译中
中文和英文间使用$分隔 单词在前
支持词组
请不要在一行内放置多个要考的单词 $符号后默认全部为释义
每一句以换行分隔，可以看看Example.md
系统已经完成了很多的工作 剩下的只需要导入Word并排版即可
------------------
""")
print("请按下任意键继续")
input()
print("""
=====================
注意事项
=====================
由于还是测试版本 无法自动配置
请在C盘根目录建好一个文件夹
并命名为：
GWZKJWORK
（全大写）
创建一个Ein.txt 输入样本
创建一个Eout.txt 无需输入任何文本
然后按下任意键继续 显示读取完成和生成完成后打开Eout.txt
=====================
""")
Load("C:\\GWZKJWORK\\Ein.txt")
make()
input()