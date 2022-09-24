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

# Simple, remove the spaces from the string, 
# then return the resultant string. 
def no_space(x):
    #your code here
    res = ''
    s = x.split() 
    res += ''.join(s)
    print(res)
    

   
    

if __name__ == '__main__':
    # arr = [97,97,105,120,105,110]
    # reversea(arr)
    s = '8 j 8   mBliB8g  imjB8B8  jl  B'
    no_space(s)
    