def str2float(s):
 
    mid = s.index('.')
    s= s[:mid+1] + '0' + s[mid+1:]
    num = float(reduce(lambda x,y:int(y)+10*int(x),s[:mid]))
    num += reduce(lambda x,y:float(x)/10+float(y),s[:mid:-1])
   
    return num
   
 
print('str2float(\'123.456\') =', str2float('123.456'))  
