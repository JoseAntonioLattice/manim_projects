from manim import *


class RomanticText(Scene):
    def construct(self):
        text = Text("Hola Beibi, TE AMO <3")
        #circle = Circle()  # create a circle
        #circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Write(text, run_time=3))  # show the circle on screen
        text = Text("Esto esta shido siono")
        text.to_edge(DOWN)
        self.play(Write(text, run_time=5))


class HelloWorld(Scene):
    def construct(self):
        circle = Circle()
        square = Square()

        text = Tex("Oye, me dijiste que me ibas a llevar a comer", font_size=72)
        text.scale(0.9)
        #text.to_edge(UP)
        text2 = Tex("TQM?")
        text3 = Tex("Tons Que Monserrat?")

        #text2.move_to([2,-0.1,0])
        #text3.move_to([-2,0,0])
        self.play(
            Write(text, run_time=3)
        )
        self.clear()
        self.play(
            Write(text2, run_time=3)
        )
        self.clear()
        self.play(
            Write(text3, run_time=3)
        )
        #self.clear()

        
        '''
        self.play(
            Transform(text[12][0], text2[0][0]),
            Transform(text[13][0], text2[1][0]),
            Transform(text[6][0], text3[0][0]),
            Transform(text[2][0], text3[1][0]),
            run_time=5,
            rate_func=linear
        )
        '''
        #self.wait(3)

        
class Irlanda(Scene):
    def construct(self):
        text = Tex("Oye...").scale(2)
        text2 = Tex("Te invito a tomar"," té").scale(2)
        text3 = Tex("Y a comer"," galletas").scale(2)
        text4 = Tex("...y a hablar de algebras de Lie $\mathfrak{su}(N)$ obvio...")
        text5 = Tex("si",font_size=120).scale(3)
        text6 = Tex("ne",font_size=120)

        text2[1].set_color(GREEN)
        text3[1].set_color(RED)
        text5.to_edge(DL)
        text5.set_color(GREEN)
        text6.to_edge(DR)
        text6.set_color(BLUE)
        
        self.play(Write(text,run_time=1))
        self.wait(2)
        self.clear()
        self.play(Write(text2,run_time=3))
        self.play(Wiggle(text2[1]))
        self.wait(1)
        self.clear()
        self.play(Write(text3,run_time=3))
        self.play(ApplyWave(text3[1]))
        self.wait(3)
        self.clear()
        
        self.play(Write(text4,run_time=3))
        self.play(ApplyWave(text4))
        self.wait(2)
        self.play(Transform(text4[0][26],text5[0][0]),
                  Transform(text4[0][24],text5[0][1]),
                  Transform(text4[0][29],text6[0][0]),
                  Transform(text4[0][25],text6[0][1]),
                  run_time=2)
        self.play(Indicate(text5))
        self.play(Circumscribe(text5))
        self.wait(3)

