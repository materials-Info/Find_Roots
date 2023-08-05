from deciml import deciml, algbra as alg, Decimal, getpr

# a*x**n
# axn(a,n,precision)

class axn:
    
    def __init__(self,__f1:Decimal,__f2:Decimal,__pr=getpr())->None:
        try:
            self.__f=tuple(map(lambda x:deciml(x,__pr),(__f1,__f2)))
            if self.__f[1]!=0:self.__df=(alg.mul(*self.__f,pr=__pr),alg.sub(self.__f[1],'1',pr=__pr));
            else:self.__df=(Decimal('0'),Decimal('0'));
            del __f1,__f2,__pr;
            self.f=lambda __a,__pr=getpr():alg.mul(self.__f[0],alg.pwr(__a,self.__f[1],__pr),pr=__pr)
            self.df=lambda __a,__pr=getpr():alg.mul(self.__df[0],alg.pwr(__a,self.__df[1],__pr),pr=__pr)
        except Exception as e:print("Invalid command: axn\n",e);

    def getf(self)->tuple[Decimal,Decimal]:return self.__f;

    def getdf(self)->tuple[Decimal,Decimal]:return self.__df;

# a1*x**n1 + a2*x**n2 + a3*x**n3 +...
# poly((a1,n1),(a2,n2),(a3,n3),...,pr=precision)

class poly:
    
    def __init__(self,*__f:tuple[Decimal,Decimal]|list,pr=getpr())->None:
        try:
            self.__f=tuple(map(lambda x:axn(*x,pr),__f));del __f,pr;
            self.f=lambda __a,__pr=getpr():alg.add(*map(lambda i:i.f(__a,__pr),self.__f),pr=__pr)
            self.df=lambda __a,__pr=getpr():alg.add(*map(lambda i:i.df(__a,__pr),self.__f),pr=__pr)
        except Exception as e:print("Invalid command: poly\n",e);

    def getf(self)->tuple[tuple[Decimal,Decimal],...]:return tuple(map(lambda i:i.getf(),self.__f));

    def getdf(self)->tuple[tuple[Decimal,Decimal],...]:return tuple(map(lambda i:i.getdf(),self.__f));

# a*(a1*x**n1 + a2*x**n2 + a3*x**n3 +...)**n
# apolyn(a,n,(a1,n1),(a2,n2),(a3,n3),...,pr=precision)

class apolyn:
    
    def __init__(self,__a:Decimal,__n:Decimal,*__f:tuple[Decimal,Decimal]|list,pr=getpr())->None:
        try:
            self.__an=axn(__a,__n,pr);
            self.__f=poly(*__f,pr=pr);del __a,__n,__f,pr;
            self.f=lambda __a,__pr=getpr():self.__an.f(self.__f.f(__a,__pr),__pr)
            self.df=lambda __a,__pr=getpr():alg.mul(self.__an.df(self.__f.f(__a,__pr),__pr),self.__f.df(__a,__pr),pr=__pr)
        except Exception as e:print("Invalid command: apolyn\n",e);

    def getf(self)->tuple[tuple[Decimal,Decimal],tuple[tuple[Decimal,Decimal],...]]:return self.__an.getf(),self.__f.getf();

    def getdf(self)->tuple[tuple[Decimal,Decimal],tuple[tuple[Decimal,Decimal],...],tuple[tuple[Decimal,Decimal],...]]:return self.__an.getdf(),self.__f.getf(),self.__f.getdf();

class funcutils:
    
    @staticmethod
    def rearr(__a,__pos:int,__pr=getpr())->apolyn:
        try:
            ta = __a.__class__.__name__
            a=__a.getf()
            match ta:
                case 'poly':
                    p=(a:=list(a)).pop(__pos)
                    a=list(map(list,a))
#                     for i in range(len(a)):a[i]=list(a[i]);
                    for i in a:i[0]=alg.mul('-1',i[0],pr=__pr);
                    if p[1]==0:print(p[1],"is zero!");return None;
                    return apolyn(alg.pwr(alg.div('1',p[0],__pr),(pw:=alg.div('1',p[1],__pr)),__pr),pw,*a,pr=__pr);
                case _:return None;
        except Exception as e:print("Invalid command: funcutils.rerr\n",e);

    @staticmethod
    def ndpoly(__p:poly,__n:int,__pr=getpr()) -> poly | None:
        try:
            for _ in range(__n):__p=poly(*__p.getdf(),pr=__pr);
            return __p
        except Exception as e:print("Invalid command: funcutils.ndpoly\n",e);

# a=poly((2,1),(1,-2))
# b=funcutils.rearr(a,0)
# print(b.getdf())
# print(a.f(1),a.df(1),a.getdf())
# print(funcutils.ndpoly(a,3).getf())
# a=apolyn(2,1,(1,2),(2,1))
# print([a.f(1),a.df(1)],a.getf())
# print(a.getdf())