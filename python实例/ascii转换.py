'''
转换ascii码

'''



def reversea(arr):
    # 遍历数组,设置一个数组存放结果
    res = ''
    
    # 解密
    for i in arr:
        a = chr(i)
        res += ''.join(a)
    # 打印
    print(res)
    

   
    

if __name__ == '__main__':
    arr = [97,97,105,120,105,110]
    reversea(arr)