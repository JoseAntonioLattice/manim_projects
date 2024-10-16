from manim import *

#config.background_color = WHITE

class EinsteinQuote(Scene):
    def construct(self):
        #quote = Text("No me heches tus pedos caldosos \n"
        #             " que no tengo cuchara, mami.")#.to_edge(UP)
        quote = Paragraph("Tumba la casa, mami.",
                          "Y mueve la batidora, mami, mami.",
                          "Beibi beibi beibi oh...",
                     # omo una mujer va a se presidente?",
                     #"no mmn",
                     #     "anlo forever!!!."
                          color=BLUE,alignment="center")
        #einstein = ImageMobject("ein.png",invert=True).to_edge(DR)
        einstein = ImageMobject("/home/jose/Pictures/coloreinstein.jpg").scale(1)#.to_edge(0.1*DOWN)
        #einstein.set_color((0.8,0,0),alpha=1,family=True)
        author = Text("-Albert Einstein",color=YELLOW)#.to_edge(DOWN)

        mob = Group(quote,einstein,author).arrange(DOWN)
        self.play(Write(mob[0]),run_time = 5)
        self.play(Write(mob[2]), run_time = 2)
        self.play(FadeIn(mob[1]))
        self.wait(3)
