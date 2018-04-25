# -*- coding: utf-8 -*-

"""
Assignment_5F_PIC16
Ashley Wu
ID 204612415
"""
from sympy import *
from IPython.display import display


init_printing(use_latex="mathjax")

#e11 is assumed to be 0
T, I_E, I_A, I_B, m_E, b, t= symbols('T I_E I_A I_B m_E b t')
w=Function('w')

#I_E=(I_A*(I_B+m_E*b**2))/(I_A+I_B+m_E*b**2)
#display(I_E)

e11=diff(w(t),t) - (T/I_E)
display (e11)

#T=e12=something, something assumes to be 0
T_0, P=symbols('T_0 P*')
e12=T_0*(1-(w(t)*T_0)/(4*P))
display (e12)
             
#e13=0
e13=expand(e11.subs(T,e12))
display (e13)

#solve for differential equation 
e14=dsolve(Eq(e13,0),w(t)).rhs
print "e14 rhs:"
display (e14)                       

C1,t_f=symbols('C1 t_f')
e14C= solve(e14.subs(t,0),C1)[0]

e14sol=expand(e14.subs(C1,e14C))
display(e14sol)

e15=simplify(integrate(e12.subs(w(t),e14sol),(t,0,t_f),conds='none'))
print "e15:"
display(e15)

e17=factor(diff(e15,T_0))
display(e17)

e18=solve(e17,T_0)[0]
display (e18)

