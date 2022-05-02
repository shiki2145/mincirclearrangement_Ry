

def calR(r1,r2):    # 计算相邻两个圆心的横坐标距离
    r = ((r1+r2)**2-(r1-r2)**2)**0.5
    return r

def calLong(CList):     # 计算当前排列的长度
    if (len(CList)==1):  # 排列中只有一个圆的时候长度为其直径
        long = 2*CList[0]
    else:
        x=0
        for i in range(len(CList)-1):
            x=x+calR(CList[i],CList[i+1])
        long = CList[0] + x + CList[-1]
    return long

'''输入的参数解释
RList,表示圆半径的列表
fList,表示最终输出的列表
CList,用来记录过程当前圆排列的列表，
i,记录层数，这里最大层数就是圆的个数
long,用于记录当前排列长度
LongList,记录每个排列长度的列表
minlong，记录最小排列长度
'''
def Backtrack(RList,fList,CList,i,long,LongList,minlong):
    if i >= len(RList)+len(CList):#超出圆的个数时，停止递归，输出结果
        if long <= min(LongList):
            if(len(fList)==0):
                for x in range(len(CList)):
                    fList.append(CList[x])
            else:
                for x in range(len(CList)):
                    fList[x]=CList[x]
        LongList.append(long)  # 在长度列表中添加新长度

    else:#递归的调用函数达到自动回溯的效果
        for n in range(len(RList)):#开始循环
            CList.append(RList[n]) # 在当前列表中添加新的圆
            long = calLong(CList) #计算当前排列的长度,得到新的长度
            RList.pop(n) #将已经用过的圆移除列表
            if (long <= min(LongList)):#只有数值小于当前最优值时，进入下一层
                Backtrack(RList,fList,CList,i+1,long,LongList,minlong)
            RList.insert(n,CList[-1])
            CList.pop(-1)#将圆返回列表，后续进行其他分支
    return fList,minlong

if __name__ == '__main__':
    rList = [2,9,4,1,1,3,6]  # 表示圆半径的列表
    cList = []  # 表示当前列表
    fList = []  # 表示最终的最优排列列表
    LongList = [2*sum(rList)]  # 先规定一个上界，后续进行迭代
    Backtrack(rList, fList, cList, 0, 0, LongList, 2*sum(rList))
    print("最小圆排列(半径):",fList)
    print("全部圆排列的长度:",LongList)
    print("MinLong:",min(LongList))


