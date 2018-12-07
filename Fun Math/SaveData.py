import os
class SaveDa(object):
    OncePrint = False
    
    def __init__(self):
        self.abspath = self.GetAbspath() + '\\Saves.txt'
    
    def Run_Test(self):
        print('SaveDatas 1.0 class could be Runing!')	
        
    def PrintRes(func):
        def wrapper(*arg,**kw):
            if arg[0].OncePrint:
                arg[0].OncePrint = False
                Res = func(*arg,**kw)
                arg[0].OncePrint = True
                print('func name: %s\tRes:'%func.__name__,Res)
            else:
                Res = func(*arg,**kw)
            return Res
        return wrapper
        
    def GetAbspath(self):
        return os.path.abspath('.')
    
    @PrintRes
    def str_Rd(self):
        strs = ''
        if os.path.exists(self.abspath):
            fp = open(self.abspath,'r')
            strs = fp.read()
            fp.close()
        return strs
    
    def str_Wd(self,strs):
        fp = open(self.abspath,'w')
        fp.write(strs)
        fp.close
        
    @PrintRes
    def int_Rd(self):
        return int(self.str_Rd())
    
    def int_Wd(self,x):
        strx = str(x)
        self.str_Wd(strx)
        
    @PrintRes
    def Lint_Rd(self):
        strx = self.str_Rd()
        Lx = strx.split(',')
        Intx = []
        for sx in Lx:
            Intx.append(int(sx))
        return Intx
    
    def Lint_Wd(self,Lx):
        strx = ''
        for x in Lx:
            strx += str(x)
            if x != Lx[-1]:
                strx += ','
        self.str_Wd(strx)