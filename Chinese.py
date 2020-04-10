import random
data = []#诗词数据库 存储诗词内容
#Sdata = {}#诗词暂存库 打包诗词内容并添加到数据库
def Load( str ):#加载诗词
    Sdata={}
    f = open(str,'r', encoding='UTF-8')

    #count=0    
    #while True:  
    #buffer=f.read(1024*8192)  
    #if not buffer:  
    #    break  
    #count+=buffer.count('\n')
   # Line = f.readline()
    j=1
    IsLoadstart = False
    while True:
        Line = f.readline()
        if Line:
            if Line.startswith("-") == True:#读取诗名
                if IsLoadstart == True:
                    Sdata["Line"]= word
                    data.append(Sdata.copy())
                    sdata = {}
                    word = 0
                    Isloadstart = False
                word = 0#初始化行数，因为没有读取诗词内容
                Wname = Line[1:]
                Sdata["Name"] = Wname#存储诗名到系统
                #print(Sdata)
                IsLoadstart = True
            elif Line.startswith("@") == True:
                author = Line[1:]
                word = 0#初始化行数
                Sdata["author"] = author#存储作者到系统
            elif Line.startswith("=") == True:
                word = word + 1#行数加一
                Sdata[word]=Line[1:]
               # nextline = f.readline()#读取下一行内容，检查是否还有诗词
                #if nextline.startswith("=") == False:
                 #   Sdata["Line"] = word
                  #  data.append(Sdata.copy())
                   # print(Sdata.copy())
                    #Sdata = {}#清空缓存
                    #ord = 0#清空行数
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
    W = open("c:\\GWZKJWORK\\out.txt",'w', encoding='UTF-8')
    i= 0
    q = []
    wordlab = 0

    count = len(data)
    while i<count:
        #print (data)
        create = data[i]
        allLine = create["Line"]
        scname = create["Name"]
        scauthor = create["author"]
        W.write("<<" + scname[:len(scname) - 1 ]+ ">>" + "\n")
        W.write("作者" + scauthor)
        wl = 1
        i += 1
        #print(create)
        #print(allLine)
        while wl < allLine + 1:
        #    print(wl)
            shici = create[wl]
        #    print(shici)
            douhaolo = 0#逗号的位置
            wordlabjs = 0
            question = 0#填空问题的数量
            js=0
            IsFinish = False
            while IsFinish != True :
                js+=1
                #douhaolo 和 nd 若为-1则代表没有逗号
                douhaolo = shici.find("，")#查询第一个逗号的位置，下文将清除这些文段
                wordlab += 1#小段数量
                wordlabjs +=1
                if wordlabjs == 1:
                    other = shici[douhaolo + 1:] #把逗号后所有的字符都给Other

                if  wordlabjs== 1:#第一题默认提供题面
                    q.insert(wordlab, shici[:douhaolo + 1])#第一题默认提供题面
                else:
                    qm = random.randint(0,1)#随机题面代码 0为题目 1为题面
                    if other.find("，") == -1 and question == 0:#r如果下文查询无逗号（最后一个分段）且没有一个问题，强制此题为题目
                        qm = 0
                    if qm == 0 :
                        if other.find("，") == -1:#如果这个为最后一段
                            linenumber =len(other)#查询填空线数
                            q.insert(wordlab,"_" *linenumber*3 + "\n")#输出填空线
                            IsFinish = True
                        else:#若不是
                            nd = other.find("，")#下一个逗号的位置
                            linenumber = len(other[:nd])#取本题线数
                            q.insert(wordlab,"_" *linenumber*3+'，')
                            other = other[nd+1:]#去除本题在other中
                        question += 1
                    else:
                        if other.find("，") == -1:#若为最后一段
                            q.insert(wordlab,other + "\n")#直接到结尾
                            IsFinish= True#宣布该文章该句出题结束
                        else:
                            nd = other.find("，")#查询下一个逗号的位置
                            q.insert(wordlab,other[:nd+1])#明文输出
                            other = other[nd + 1 :]
                    printline = 0
            while printline < js:
                if printline == js-1:
                    W.write(q[printline] + "\n")
                    q=[]
                else:
                    W.write(q[printline])
                printline += 1
            wl+=1

    W.write("使用由鬼未族科技开发的「Python语文默写生成器1.0」生成")
    print("题目生成完成")

                        
print("DEBUG MODE")
print("未完工，暂时是演示模式，完工后会在视频底下放Github下载链接")
print("LOADING")
print("""
-------------------
BILIBILI 鬼未族科技
语文默写生成系统
Ver 1.0
该系统逻辑如下：
全文导入后 将随机抽取一些文段进行抽取默写。
每句第一句恒为题干。题目量的多少全看欧气
每句至少为2小段，如“床前明月光，疑是地上霜”
每一个小段以逗号分隔，不要有句号
每一句以换行分隔，可以看看Example.md
系统已经完成了很多的工作 剩下的只需要导入Word并排版即可
------------------
""")
Load("C:\\GWZKJWORK\\in.txt")
make()
