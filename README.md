# Find_Roots
Different methods to find roots of given equation.

Creeate object for different equations.

$ cd locations/to/Find_Roots  
$ python  
from find_roots.functions import *  
  
1. a*(x^n); a and n are constants    
  
axn(a,n,precision)  
eg:  
a=axn(1,3,12)  
> a.f(value of x) returns value of function  
>   
a.f(2)  
Decimal('8.00')  
> a.df(value of x) returns value of function's derivative  
>   
a.df(2)  
Decimal('12.000')  
  
2, a1*(x^n1)+a2*(x^n2)+...+a_N*(x^n_N)  
  
poly((a1,n1),(a2,n2),...,(a_N,n_N),pr=precision)  
eg:  
a=poly((2,2),(1,3),pr=16)  
a.f(1.5)  
Decimal('7.8750')  
a.df(1.5)  
Decimal('12.7500')  
