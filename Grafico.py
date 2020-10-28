from sympy import symbols
from sympy.plotting import plot
from sympy import plot_implicit, Eq, And

x, y = symbols('x, y')
p = plot_implicit(And(y < x+2, y > x+1, x <= 5, x > -2),(x,-10,10),(y,-10,10))
p2 = plot_implicit(And(y=5))
p2 = plot_implicit(And(y>0.5*x+1))
p2 = plot_implicit(And(y>3-2*x, y>0.5*, y>=x))
p2 = plot_implicit(And(y>=20-15*x,x>0,Y>0),(y,-100,100),(x,-100,100))
p2 = plot_implicit(And(y<100-2*x,y<=80-0.5*x,Y<100-x),(y,-100,100),(x,-100,100))
p2 = plot_implicit(And(y>=2*x,y<3*x+1,Y>0,x>0))
p2 = plot_implicit(And(y<=x+2,y>x+1,x<=5,x>-2))