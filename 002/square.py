from manim import *

class MakeSquare(Scene):
    def construct(self):
        sq = VMobject()
        points = [
            [ 1, 1, 0],
            [ 1,-1, 0],
            [-1,-1, 0],
            [-1, 1, 0],
         #   [ 1, 1, 0],
        ]

        dots = VGroup(*[Dot(p) for p in points])
        self.add(dots)

        sq.set_points_as_corners(points)
        
        #sq.add_points_as_corners([1, 1, 0])
        self.play(Create(sq), run_time=2)

        sq.make_smooth()



class SimpleAnimation(Scene):
    def construct(self):
        triangle = Triangle()
        self.play(Create(triangle))
        self.wait(2)


class TexTransformExample(Scene):
    def construct(self):
        to_isolate = ["B", "C", "=", "(", ")"]
        lines = VGroup(
            # Passing in muliple arguments to Tex will result
            # in the same expression as if those arguments had
            # been joined together, except that the submobject
            # hierarchy of the resulting mobject ensure that the
            # Tex mobject has a subject corresponding to
            # each of these strings.  For example, the Tex mobject
            # below will have 5 subjects, corresponding to the
            # expressions [A^2, +, B^2, =, C^2]
            Tex("A^2", "+", "B^2", "=", "C^2"),
            # Likewise here
            Tex("A^2", "=", "C^2", "-", "B^2"),
            # Alternatively, you can pass in the keyword argument
            # "isolate" with a list of strings that should be out as
            # their own submobject.  So the line below is equivalent
            # to the commented out line below it.
            Tex("A^2 = (C + B)(C - B)", isolate=["A^2", *to_isolate]),
            # OldTex("A^2", "=", "(", "C", "+", "B", ")", "(", "C", "-", "B", ")"),
            Tex("A = \\sqrt{(C + B)(C - B)}", isolate=["A", *to_isolate])
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        for line in lines:
            line.set_color_by_tex_to_color_map({
                "A": BLUE,
                "B": TEAL,
                "C": GREEN,
            })

        play_kw = {"run_time": 2}
        self.add(lines[0])
        # The animation TransformMatchingTex will line up parts
        # of the source and target which have matching tex strings.
        # Here, giving it a little path_arc makes each part sort of
        # rotate into their final positions, which feels appropriate
        # for the idea of rearranging an equation
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()

        # Now, we could try this again on the next line...
        self.play(
            TransformMatchingTex(lines[1].copy(), lines[2]),
            **play_kw
        )
        self.wait()
        # ...and this looks nice enough, but since there's no tex
        # in lines[2] which matches "C^2" or "B^2", those terms fade
        # out to nothing while the C and B terms fade in from nothing.
        # If, however, we want the C^2 to go to C, and B^2 to go to B,
        # we can specify that with a key map.
        self.play(FadeOut(lines[2]))
        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[2],
                key_map={
                    "C^2": "C",
                    "B^2": "B",
                }
            ),
            **play_kw
        )
        self.wait()

        # And to finish off, a simple TransformMatchingShapes would work
        # just fine.  But perhaps we want that exponent on A^2 to transform into
        # the square root symbol.  At the moment, lines[2] treats the expression
        # A^2 as a unit, so we might create a new version of the same line which
        # separates out just the A.  This way, when TransformMatchingTex lines up
        # all matching parts, the only mismatch will be between the "^2" from
        # new_line2 and the "\sqrt" from the final line.  By passing in,
        # transform_mismatches=True, it will transform this "^2" part into
        # the "\sqrt" part.
        new_line2 = OldTex("A^2 = (C + B)(C - B)", isolate=["A", *to_isolate])
        new_line2.replace(lines[2])
        new_line2.match_style(lines[2])

        self.play(
            TransformMatchingTex(
                new_line2, lines[3],
                transform_mismatches=True,
            ),
            **play_kw
        )
        self.wait(3)
        self.play(FadeOut(lines, RIGHT))

        # Alternatively, if you don't want to think about breaking up
        # the tex strings deliberately, you can TransformMatchingShapes,
        # which will try to line up all pieces of a source mobject with
        # those of a target, regardless of the submobject hierarchy in
        # each one, according to whether those pieces have the same
        # shape (as best it can).
        source = Text("the morse code", height=1)
        target = Text("here come dots", height=1)

        self.play(Write(source))
        self.wait()
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait()
        self.play(TransformMatchingShapes(target, source, **kw))
        self.wait()


class MatchingEquationParts(Scene):
    def construct(self):
        variables = VGroup(MathTex("a"), MathTex("b"), MathTex("c")).arrange_submobjects().shift(UP)

        eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
        eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
        eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")
        eq4 = MathTex("{{a}}", "=", "\\sqrt{{{c}}^2 - {{b}}^2}")
        self.add(eq1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Group(eq1, variables), eq2))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(0.5)

class FormulaColor3(Scene): 
    def construct(self):
        text = MathTex("\\sqrt{","\\int_{","a}^","{b}","\\left(","\\frac{x}{y}","\\right)","dx}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        self.play(Write(text))
        self.wait(2)

class FormulaColor3Fixed2(Scene): 
    def construct(self): 
        text = MathTex("\\sqrt{","\\int_","{a}^","{b}","{\\left(","{x","\\over","y}","\\right)}","d","x",".}")
        text[0].set_color(RED)
        text[1].set_color(BLUE)
        text[2].set_color(GREEN)
        text[3].set_color(YELLOW)
        text[4].set_color(PINK)
        text[5].set_color(ORANGE)
        text[6].set_color(PURPLE)
        text[7].set_color(MAROON)
        text[8].set_color(TEAL)
        text[9].set_color(GOLD)
        self.play(Write(text))
        self.wait(3)

class chicharronera(Scene):
    def construct(self):

        text1 = Tex("Derivación de la Chicharronera")

        self.play(FadeIn(text1))
        self.wait(1)
        
        self.play(FadeOut(text1))
        eq1 = MathTex("a","x^2","+","b", "x", "+", "c", "=", "0")
        eq2 = MathTex("a","x^2","+","b", "x", "=", "-","c")
        eq3 = MathTex("x^2","+","{","b", "\\over","a","}", "x", "=", r"{","c","\\over","a"," }")
        eq4 = MathTex("x^2","+","{","b", "\\over","a","}", "x" ,"+", r"\left(","{","b","\\over","2","a","}",r"\right)^2",
                                "=", "{", "c","\\over","a", "}","+", r"\left(","{","b","\\over","2","a","}",r"\right)^2")
        eq5 = MathTex(r"\left(","x","+","{","b","\\over", "2","a","}","\\right)","^2", "=", "{","b","^2", "-","4","a","c","\\over","4","a","^2","}")
        eq6 = MathTex("x", "+","{","b","\\over","2","a","}", "=", "\\sqrt{" , "{","b","^2", "-","4","a","c","\\over","4","a","^2","}", "}")
        eq7 = MathTex("x", "=","-","{","b","\\over","2","a","}", "+", "\\sqrt{" , "{","b","^2", "-","4","a","c","\\over","4","a","^2","}", "}")
        eq8 = MathTex("x", "=","-","{","b","\\over","2","a","}", "+", "{","\\sqrt{" ,"b","^2", "-","4","a","c","}","\\over","2","a","}")
        
        self.add(eq1)
        self.wait(1)
        self.play(TransformMatchingTex(eq1,eq2,path_arc=90*DEGREES))
        self.wait(1)
        self.play(TransformMatchingTex(eq2,eq3))
        self.wait(1)
        self.play(TransformMatchingTex(eq3,eq4))
        self.wait(1)
        self.play(TransformMatchingTex(eq4,eq5))
        self.wait(1)
        self.play(TransformMatchingTex(eq5,eq6))
        self.wait(1)
        self.play(TransformMatchingTex(eq6,eq7))
        self.wait(1)
        self.play(TransformMatchingTex(eq7,eq8))
        self.wait(1)

class Anagram(Scene):
    def construct(self):
        src = Text("the morse code")
        tar = Text("here come dots")
        self.play(Write(src))
        self.wait(0.5)
        self.play(TransformMatchingShapes(src, tar, path_arc=PI/2))
        self.wait(0.5)



class TexTransformExample(Scene):
    def construct(self):
        to_isolate = ["B", "C", "=", "(", ")"]
        lines = VGroup(
            # Passing in muliple arguments to Tex will result
            # in the same expression as if those arguments had
            # been joined together, except that the submobject
            # hierarchy of the resulting mobject ensure that the
            # Tex mobject has a subject corresponding to
            # each of these strings.  For example, the Tex mobject
            # below will have 5 subjects, corresponding to the
            # expressions [A^2, +, B^2, =, C^2]
            MathTex(r"A^2", "+", r"B^2", "=", r"C^2"),
            # Likewise here
            MathTex(r"A^2", "=", r"C^2", "-", r"B^2"),
            # Alternatively, you can pass in the keyword argument
            # "isolate" with a list of strings that should be out as
            # their own submobject.  So the line below is equivalent
            # to the commented out line below it.
            #MathTex("A^2 = (C + B)(C - B)", isolate=["A^2", *to_isolate]),
            MathTex("A^2", "=", "(", "C", "+", "B", ")", "(", "C", "-", "B", ")"),
            MathTex(r"A = \sqrt{(C + B)(C - B)}")
        )
        lines.arrange(DOWN, buff=LARGE_BUFF)
        for line in lines:
            line.set_color_by_tex_to_color_map({
                "A": BLUE,
                "B": TEAL,
                "C": GREEN,
            })

        play_kw = {"run_time": 2}
        self.add(lines[0])
        # The animation TransformMatchingTex will line up parts
        # of the source and target which have matching tex strings.
        # Here, giving it a little path_arc makes each part sort of
        # rotate into their final positions, which feels appropriate
        # for the idea of rearranging an equation
        self.play(
            TransformMatchingTex(
                lines[0].copy(), lines[1],
                path_arc=90 * DEGREES,
            ),
            **play_kw
        )
        self.wait()

        # Now, we could try this again on the next line...
        self.play(
            TransformMatchingTex(lines[1].copy(), lines[2]),
            **play_kw
        )
        self.wait()
        # ...and this looks nice enough, but since there's no tex
        # in lines[2] which matches "C^2" or "B^2", those terms fade
        # out to nothing while the C and B terms fade in from nothing.
        # If, however, we want the C^2 to go to C, and B^2 to go to B,
        # we can specify that with a key map.
        self.play(FadeOut(lines[2]))
        self.play(
            TransformMatchingTex(
                lines[1].copy(), lines[2],
                key_map={
                    "C^2": "C",
                    "B^2": "B",
                }
            ),
            **play_kw
        )
        self.wait()

        # And to finish off, a simple TransformMatchingShapes would work
        # just fine.  But perhaps we want that exponent on A^2 to transform into
        # the square root symbol.  At the moment, lines[2] treats the expression
        # A^2 as a unit, so we might create a new version of the same line which
        # separates out just the A.  This way, when TransformMatchingTex lines up
        # all matching parts, the only mismatch will be between the "^2" from
        # new_line2 and the "\sqrt" from the final line.  By passing in,
        # transform_mismatches=True, it will transform this "^2" part into
        # the "\sqrt" part.

        '''
        new_line2 = MathTex(r"A^2"," =", "(", "C"," +"," B",")","(","C"," -"," B",")")#, isolate=["A", *to_isolate])
        new_line2.replace(lines[2])
        new_line2.match_style(lines[2])

        self.play(
            TransformMatchingTex(
                new_line2, lines[3],
               # transform_mismatches=True,
            ),
            #**play_kw
        )
        self.wait(3)
        self.play(FadeOut(lines, RIGHT))
        '''
        # Alternatively, if you don't want to think about breaking up
        # the tex strings deliberately, you can TransformMatchingShapes,
        # which will try to line up all pieces of a source mobject with
        # those of a target, regardless of the submobject hierarchy in
        # each one, according to whether those pieces have the same
        # shape (as best it can).
        '''
        source = Text("the morse code", height=1)
        target = Text("here come dots", height=1)

        self.play(Write(source))
        self.wait()
        kw = {"run_time": 3, "path_arc": PI / 2}
        self.play(TransformMatchingShapes(source, target, **kw))
        self.wait()
        self.play(TransformMatchingShapes(target, source, **kw))
        self.wait()
        '''
