from functions import funcutils
from functions import poly
from deciml import algbra as alg, abs, deciml, getpr, Decimal


class SolveFn:
    
    # rootrearr(function, list of points, max x, precision)

    @staticmethod
    def rootrearr(__a,__x:list[Decimal]|tuple[Decimal,...],__p=0.01,__pr=getpr())->dict:
        try:
            pr1=__pr+1;x=tuple(map(lambda x:Decimal(str(x)),__x));del __x;l=list();__p=Decimal(str(__p));
            for i in range(len(__a.getf())):
                f=funcutils.rearr(__a,i,pr1);l1=list();
                if f is None:continue;
                for j in x:
                    a=abs(f.df(j,pr1))
                    if a is None:continue;
                    if a<=1:l1.append(j)
                if len(l1)>0:l.append((f,tuple(l1),i));
            l1=list()
            for i in l:
                f=i[0];l2=list();
                for j in i[1]:
                    f1=j;c=0;p=Decimal('Inf');
                    while p>__p:
                        f1=f.f(f1,pr1);c+=1;p=abs(__a.f(f1,pr1));
                        if p is None:break;
                    if p is not None:
                        l2.append({'rearrange pos':i[2],'iterations':c,'start value':j,'value':(deciml(f1,__pr),deciml(__a.f(f1,pr1),__pr))})
                l1.append(tuple(l2))
            return tuple(l1)
        except Exception as e:print("Invalid command: SolveFn.rootrearr\n",e);
             
    # lininter(function, list of points, max x, precision)

    @staticmethod
    def lininter(__a,__x:list[Decimal]|tuple[Decimal,...],__p=0.01,__pr=getpr())->dict:
        try:
            pr1=__pr+1;x=tuple(map(lambda x:Decimal(str(x)),__x));del __x;__p=Decimal(str(__p));fv=tuple(map(lambda x:__a.f(x,pr1),x));ln=list();lp=list();l=list();
            for i in range(len(x)):
                if fv[i]<0:ln.append(x[i]);
                else:lp.append(x[i]);
            del fv
            for i in ln:
                a=i;fa=__a.f(a,pr1);l1=list();
                for j in lp:
                    b=j;fb=__a.f(b,pr1);c=0;p=Decimal('Inf');
                    while p>__p:
                        x=alg.div(alg.sub(alg.mul(a,fb,pr=pr1),alg.mul(b,fa,pr=pr1),pr=pr1),alg.sub(fb,fa,pr=pr1),pr1);c+=1;p=__a.f(x,pr1);
                        if p<0:a=x;fa=p;
                        else:b=x;fb=p;
                        p=abs(p)
                        if p is None:break;
                    if p is not None:
                        l1.append({'iterations':c,'start value':(i,j),'value':(deciml(x,__pr),deciml(__a.f(x,pr1),__pr))})
                l.append(tuple(l1))
            return tuple(l)
        except Exception as e:print("Invalid command: SolveFn.lininter\n",e);

    # bchop(function, list of points, max x, precision)

    @staticmethod
    def bchop(__a,__x:list[Decimal]|tuple[Decimal,...],__p=0.01,__pr=getpr())->dict:
        try:
            pr1=__pr+1;x=tuple(map(lambda x:Decimal(str(x)),__x));del __x;__p=Decimal(str(__p));fv=tuple(map(lambda x:__a.f(x,pr1),x));ln=list();lp=list();l=list();
            for i in range(len(x)):
                if fv[i]<0:ln.append(x[i]);
                else:lp.append(x[i]);
            del fv
            for i in ln:
                a=i;l1=list();
                for j in lp:
                    b=j;c=0;p=Decimal('Inf');
                    while p>__p:
                        x=alg.div(alg.add(a,b,pr=pr1),'2',pr1);c+=1;p=__a.f(x,pr1);
                        if p<0:a=x;
                        else:b=x;
                        p=abs(p)
                        if p is None:break;
                    if p is not None:
                        l1.append({'iterations':c,'start value':(i,j),'value':(deciml(x,__pr),deciml(__a.f(x,pr1),__pr))})
                l.append(tuple(l1))
            return tuple(l)
        except Exception as e:print("Invalid command: SolveFn.bchop\n",e);

    # nriter(function, list of points, max x, precision)
    
    @staticmethod
    def nriter(__a,__x:list[Decimal]|tuple[Decimal,...],__p=0.01,__pr=getpr())->dict:
        try:
            pr1=__pr+1;x=tuple(map(lambda x:Decimal(str(x)),__x));del __x;__p=Decimal(str(__p));l=list();
            for i in x:
                c=0;p=Decimal('Inf');a=i;
                while p>__p:
                    x=alg.sub(a,alg.div(__a.f(a,pr1),__a.df(a,pr1),pr1),pr=pr1);c+=1;p=abs(__a.f(x,pr1));a=x;
                    if p is None:break;
                if p is not None:
                    l.append({'iterations':c,'start value':i,'value':(deciml(x,__pr),deciml(__a.f(x,pr1),__pr))})
            return tuple(l)
        except Exception as e:print("Invalid command: SolveFn.nriter\n",e);


# for j in range(1):
#     d = {'Al_LowCutoff': {'parameters': [16.058881741715595, -8.955601539113559, 1.0939627709012711],
#                           'r^2': 0.9983192621607382, 'r^2_adj': 0.9978390513495206},
#         'Al_HighCutoff': {'parameters': [15.811508555198088, -8.971596025396138, 1.1032308384019416],
#                            'r^2': 0.998828056926424, 'r^2_adj': 0.9984932160482594},
#         'Al_MedCutoff': {'parameters': [15.946995875099674, -9.0157831403194, 1.107305156358052],
#                           'r^2': 0.9988916677797752, 'r^2_adj': 0.9985750014311395}}
#     p = dict()
#     for i in d.items():
#         p[i[0]] = poly(*tuple(zip(i[1]["parameters"],[0, 1, 2])))
#     for i in p.items():
#         p[i[0]] = funcutils.ndpoly(i[1], 1)
#     for i in p.items():
#         p[i[0]] = SolveFn.nriter(i[1], [-10, 0, 10], 0.001)
#     for i in p.items():
#         print(i,'\n\n')
# p = SolveFn.rootrearr(poly((1,5), (-2,2), (-3,0)), [1.7,], 0.00001)
# print(p)
# p=SolveFn.rootrearr(poly((4,0), (-4,1), (1,2),), [i - 5 for i in range(10)],0.001)
# print(p)
# p = SolveFn.bchop(poly((1,5), (-2,2), (-3,0)),[1.7,1,-1], 0.00001)
# print(p)
# p = SolveFn.lininter(poly((1,5), (-2,2), (-3,0)),[1.7,1,-1], 0.00001)
# print(p)
# p = SolveFn.nriter(poly((1,5), (-2,2), (-3,0)),[1.7,1,-1], 0.00001)
# print(p)