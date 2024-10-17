from manim import *
from math import *
from random import *
class sinplot(Scene):
    def construct(self):
        plane = NumberPlane()

        sinp = FunctionGraph( lambda  x : np.sin(x))
        cosp = FunctionGraph( lambda  x : np.cos(x),color = RED)

        dsin = Dot().set_color(ORANGE)
        dcos = Dot().set_color(GREEN)

        #alpha = ValueTracker(0)
        #tangent = TangentLine(sinp, alpha = alpha.get_value(), length = 4, color = ORANGE)
        
        
        self.add(plane, sinp, cosp)
        self.play(MoveAlongPath(dsin,sinp), MoveAlongPath(dcos,cosp), rate_func = linear, run_time = 5)



class sinplot2(Scene):
    def construct(self):
        plane = NumberPlane()

        sinp = FunctionGraph( lambda  x : np.sin(x))
        #cosp = FunctionGraph( lambda  x : np.cos(x),color = RED)

        alpha = ValueTracker(0)
        dsin = always_redraw( lambda : Dot( sinp.point_from_proportion(alpha.get_value()), color = RED) )
        tangent = always_redraw(
            lambda : TangentLine(sinp, alpha = alpha.get_value(), length = 4, color = ORANGE)
            )
        
        self.add(plane, sinp, dsin, tangent)
        self.play(alpha.animate.set_value(1), rate_func = linear, run_time = 5)

def f(x):
    a = -0.7
    b = 0.7
    if x[0]<0:
        if x[1] >= 0:
            return UP + UP*np.random.uniform(a,b) + RIGHT*np.random.uniform(a,b)
        elif x[1] < 0:
            return LEFT + UP*np.random.uniform(a,b) + RIGHT*np.random.uniform(a,b)
    elif x[0] >= 0:
        if x[1] > 0:
            return RIGHT + UP*np.random.uniform(a,b) + RIGHT*np.random.uniform(a,b)
        elif x[1] <= 0:
            return DOWN + UP*np.random.uniform(a,b) + RIGHT*np.random.uniform(a,b)

def f1(x):
    a = -0.7
    b = 0.7
    if x[0] < 0:
        if x[1] >= 0:
            return UP + UP*np.random.uniform(a,b) + RIGHT*np.random.uniform(a,b)
    else:
        return 0*UP

def f2(x):
    a = -0.7
    b = 0.7
    if x[0] >= 0:
        if x[1] >= 0:
            return RIGHT + UP*np.random.uniform(a,b) + RIGHT*np.random.uniform(a,b)
    else:
        return 0*DOWN

def f3(x):
    a = -0.7
    b = 0.7
    if x[0] >= 0:
        if x[1] < 0:
            return DOWN + UP*np.random.uniform(a,b) + RIGHT*np.random.uniform(a,b)
    else:
        return 0*DOWN
    
def f4(x):
    a = -0.7
    b = 0.7
    if x[0] < 0:
        if x[1] < 0:
            return LEFT + UP*np.random.uniform(a,b) + RIGHT*np.random.uniform(a,b)
    else:
        return 0*DOWN


def g(x):
    return 0*UP

    
class SizingAndSpacing(Scene):
    def construct(self):
        
        
        func = lambda pos: LEFT#np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        func2 = lambda pos: (pos[1]*RIGHT - pos[0]*UP)/np.sqrt(pos[0]**2+pos[1]**2+0.001)

        vf = ArrowVectorField(f, x_range=[-7, 7, 1], y_range = [-4,4,1])
        vf1 = ArrowVectorField(f, x_range=[-7, -1, 1], y_range = [0,4,1])
        vf2 = ArrowVectorField(f, x_range=[0, 7, 1]  , y_range = [0,4,1])
        vf3 = ArrowVectorField(f, x_range=[0, 7, 1]  , y_range = [-4,-1,1])
        vf4 = ArrowVectorField(f, x_range=[-7, -1, 1], y_range = [-4,-1,1])

        c1 = Circle(radius = 3, color = RED, fill_opacity=0 ).shift(LEFT*4 + 2*UP)
        c2 = Circle(radius = 3, color = BLUE,fill_opacity = 1).shift(RIGHT*4 + 2*UP)
        c3 = Circle(radius = 3, color = GREEN,fill_opacity = 1).shift(RIGHT*4 + 2*DOWN)
        c4 = Circle(radius = 3, color = YELLOW,fill_opacity = 1).shift(LEFT*4 + 2*DOWN)

        op11 = Intersection(c1,vf,fill_opacity = 0)
        op12 = Union(c1,vf,fill_opacity = 0)
        op13 = Difference(c1,vf,fill_opacity = 0)
        op14 = Exclusion(c1,vf,fill_opacity = 0)
        vf = vf1+vf2+vf3+vf4
        
        #self.add(vf)
        
        #self.play(GrowFromCenter(c1),GrowFromCenter(c2),GrowFromCenter(c3),GrowFromCenter(c4), run_time = 5)
        self.play(GrowFromCenter(vf1),GrowFromCenter(vf2), GrowFromCenter(vf3), GrowFromCenter(vf4),run_time = 5)
        #self.remove(c1,c2,c3,c4)
        # self.wait(2)
        #self.clear()
        #self.add(vf)
        self.wait(1)
        center = Dot(color=RED)
        length_func = lambda x: x/3

        vf1_top = ArrowVectorField(func2, x_range=[-7, -1, 1], y_range=[0, 4, 1]  , length_func=length_func)
        vf2_top = ArrowVectorField(func2, x_range=[0, 7, 1]  , y_range=[0, 4, 1]  , length_func=length_func)
        vf3_top = ArrowVectorField(func2, x_range=[0, 7, 1]  , y_range=[-4, -1, 1], length_func=length_func)
        vf4_top = ArrowVectorField(func2, x_range=[-7, -1, 1], y_range=[-4, -1, 1], length_func=length_func)

        self.play(vf1.animate.become(vf1_top), vf2.animate.become(vf2_top), vf3.animate.become(vf3_top), vf4.animate.become(vf4_top))
        self.add(center)
        self.wait(3)
        
