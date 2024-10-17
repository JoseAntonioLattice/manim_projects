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
    

class SizingAndSpacing(Scene):
    def construct(self):
        
        
        func = lambda pos: LEFT#np.sin(pos[0] / 2) * UR + np.cos(pos[1] / 2) * LEFT
        func2 = lambda pos: (pos[1]*RIGHT - pos[0]*UP)/np.sqrt(pos[0]**2+pos[1]**2+0.001)
        
        vf = ArrowVectorField(f, x_range=[-7, 7, 1])
        self.add(vf)
        self.wait()

        center = Dot(color=RED)
        length_func = lambda x: x/3
        vf2 = ArrowVectorField(func2, x_range=[-7, 7, 1], length_func=length_func)
        self.play(vf.animate.become(vf2))
        self.add(center)
        self.wait(3)
