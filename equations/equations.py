from manim import *

class MatchingEquationParts(Scene):
    def construct(self):
        variables = VGroup(MathTex("a"), MathTex("b"), MathTex("c")).arrange_submobjects().shift(UP)

        eq1 = MathTex("{{x}}^2", "+", "{{y}}^2", "=", "{{z}}^2")
        eq2 = MathTex("{{a}}^2", "+", "{{b}}^2", "=", "{{c}}^2")
        eq3 = MathTex("{{a}}^2", "=", "{{c}}^2", "-", "{{b}}^2")
        
        self.add(eq1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Group(eq1, variables), eq2))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(0.5)

class example3(Scene):
    def construct(self):
        variables = VGroup(MathTex("a"), MathTex("b"), MathTex("c")).arrange_submobjects().shift(UP)
        isolate_tex = ["a","b", "c"]
        isolate_tex2 = ["x", "y", "z"]
        eq1 = MathTex("x^2", "+", "y^2", "=", "z^2",substrings_to_isolate = isolate_tex2)
        eq2 = MathTex("a^2", "+", "b^2", "=", "c^2",substrings_to_isolate = isolate_tex)
        eq3 = MathTex("a^2", "=", "c^2", "-", "b^2",substrings_to_isolate = isolate_tex)
        eq4 = MathTex("a", "=","\\sqrt{ ","c^2-b^2}",substrings_to_isolate = isolate_tex2)
        
        self.add(eq1)
        self.wait(0.5)
        self.play(TransformMatchingTex(Group(eq1, variables), eq2))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq2, eq3))
        self.wait(0.5)
        self.play(TransformMatchingTex(eq3, eq4))
        self.wait(0.5)
        
class example(Scene):
    def construct(self):
        t1 = MathTex("{{x}}+{{y}}={{4}}")
        t2 = MathTex("{{x}}={{4}}-{{y}}")
        VGroup(t1,t2)\
            .scale(3)
        #t2.align_to(t1,LEFT)
        
        self.add(t1)
        self.wait()
        self.play(
            TransformMatchingTex(
                t1,t2,
                # Try removing this dictionary
                key_map={
                    "+":"-"
                }
            ),
            run_time=4
        )
        self.wait()
        
    
class chicharronera(Scene):
    def construct(self):

        isolate_tex  = ["a","x^2","x","b","c", "-","=","+","0"]
        isolate_tex2 = ["+","b","c","a","x^2","x","=", "\\over", "-"]
        isolate_tex3 = ["+","b","2a","\\left(","\\right)","b \\over 2a","^2", "\\over" ]
        isolate_tex4 = ["a","x^2","x","b","c","2a","=","\\left(","\\right)","-","+","b \\over 2a","c \\over a", "b \\over a","^2", "\\over"]
        
        eq4 = Group(MathTex(r"+\left( { b \over 2a } \right)^2",substrings_to_isolate=isolate_tex3),
                    MathTex(r"+\left( { b \over 2a } \right)^2",substrings_to_isolate=isolate_tex3)).arrange_submobjects().shift(2*UP)
        
        eq1 = MathTex("a x^2 + b x + c = 0",substrings_to_isolate=isolate_tex)
        eq2 = MathTex("a x^2 + b x = - c",substrings_to_isolate=isolate_tex)
        eq3 = MathTex(r"x^2 + { b \over a } x = - { c \over a }",substrings_to_isolate=isolate_tex2)
        eq5 = MathTex(r"x^2 + { b \over a } x +\left( { b \over 2a } \right)^2"
                      r"= - { c \over a } + \left( { b \over 2a } \right)^2", substrings_to_isolate=isolate_tex4)
        eq6 = MathTex(r"\left( x + {a \over b} \right)^2 = { -4 a c + b^2 \over 4 a^2}",substrings_to_isolate=isolate_tex4)
        #eq2.align_to(eq1,LEFT)
        self.add(eq1)
        self.wait(1)

        self.play(
            TransformMatchingTex(eq1,eq2),#key_map={"+":"-"},
            run_time = 3)
        
        self.play(
            TransformMatchingTex(eq2,eq3,
                                 path_arc=90*DEGREES),
            run_time = 3)

        self.play(TransformMatchingTex(Group(eq3,eq4),eq5),run_time = 3)
        self.play(TransformMatchingTex(eq5,eq6),run_time = 3)
class example2(Scene):
    def construct(self):
        isolate_tex = ["a","b","c","="]
        t1 = MathTex("a \\times b = c",substrings_to_isolate=isolate_tex)
        t2 = MathTex("a = { c \\over b }",substrings_to_isolate=isolate_tex)
        #VGroup(t1,t2)\
        #    .scale(3)
        #t2.align_to(t1,LEFT)
        
        self.add(t1)
        self.wait()
        self.play(
            TransformMatchingTex(
                t1,t2#,
                # This not works
               # key_map={
               #     "\\times":"\\over"
               # }
            ),
            run_time=4
        )
        self.wait()

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
            MathTex("A^2", "+", "B^2", "=", "C^2"),
            # Likewise here
            MathTex("A^2", "=", "C^2", "-", "B^2"),
            # Alternatively, you can pass in the keyword argument
            # "isolate" with a list of strings that should be out as
            # their own submobject.  So the line below is equivalent
            # to the commented out line below it.
            MathTex("A^2 = (C + B)(C - B)", substrings_to_isolate=["A^2", *to_isolate]),
            # OldTex("A^2", "=", "(", "C", "+", "B", ")", "(", "C", "-", "B", ")"),
            MathTex("A = \\sqrt{(C + B)(C - B)}", substrings_to_isolate=["A", *to_isolate])
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
        new_line2 = MathTex("A^2 = (C + B)(C - B)", substrings_to_isolate=["A", *to_isolate])
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
        self.play(FadeOut(lines))

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
        
class hola(Scene):
    def construct(self):

        isolate1 = ["c","2a"]
        isolate2= ["x", "x^2+"]
        isolate3= ["-","=","\left(","\right)"]

        isolate = [*isolate1, *isolate2, *isolate3]
        
        add1 = MathTex(r"+\left( { b \over 2a } \right)^2",substrings_to_isolate = [*isolate]).to_edge(2*UP).set_color(YELLOW)

        eq1 = MathTex(r"x^2 + { b \over a }",r" = - { c \over a}",substrings_to_isolate = [*isolate])

        eq2 = MathTex(r" x^2 + { b \over a }","+",r"\left( { b \over 2a } \right)^2","=",r"\left( { b \over 2a } \right)^2",r" - { c \over a}",substrings_to_isolate = [*isolate])

        eq3 = MathTex(r"x^2 + { b \over a }","+",r"\left( { b \over 2a } \right)^2",r" = - { c \over a}","+",r" { b^2 \over 4a^2 }",substrings_to_isolate = ["b^2","4","a^2"])
        
        
        self.play(TransformMatchingTex(Group(add1,eq1.copy(),eq1),eq2),run_time = 3)
        #self.play(TransformMatchingTex(eq2,eq3,key_map={"4":"2","b":"b^2","a":"a^2"}),run_time = 3)
        ex1 = MathTex(r" x^2 +{b \over a}+ \left( { b \over 2a } \right)^2 = \left( { b \over 2a } \right)^2 - {c \over a}",substrings_to_isolate=["\left(","b","2","-","a","\right)","^2","=","0","x^2","+"])
        ex2 = MathTex(r" x^2 + { b \over a} + {b^2 \over 4 a^2 } = {b^2 \over 4 a^2 } - {c \over a} ",substrings_to_isolate=["b","4", "a","-","^2","=","x^2","+","2a","\left(","\right)"])
        ex3 = MathTex(r"x^2 + { b \over a} + {b^2 \over 4 a^2 } = {b^2 - 4 a c \over 4a^2}  ",substrings_to_isolate=["b","4", "a","^2","=","-","x^2","+","\over"])
        ex4 = MathTex(r" \left( x + {b \over 2 a }\right)^2 = {b^2 - 4 a c \over 4a^2} ",substrings_to_isolate=["b","4", "a","=","-","x","+","\over","\left(","\right)^2","^2"])
        self.clear()
        #self.play(TransformMatchingTex(eq2,ex1),run_time = 3)
        self.play(TransformMatchingTex(ex1,ex2,key_map={"b":"b^2","a":"a^2","2":"4"},transform_mimatches=True),run_time = 3)
        self.play(TransformMatchingTex(ex2,ex3),run_time = 3)
        self.play(TransformMatchingTex(ex3,ex4,key_map={"b^2":"b","a^2":"a","4":"2"}),run_time = 3)

        xxx = MathTex(r"\left( x + { b \over 2a }\right)^2 = {b^2 - 4 a c \over 4a^2}",substrings_to_isolate=["\left(", "x", "+","b", "\over","2a","\right)^2","=","b^2","-","4ac","4a^2"])
        yyy = MathTex(r"\left( x + { b \over 2a }\right) =\pm \sqrt{ {b^2 - 4 a c \over 4a^2}} ",substrings_to_isolate=["\left(","x","+","b","\over","2a"," \right)","=","\pm","b^2","-","4ac","4a^2","\sqrt"])
        self.play(TransformMatchingTex(ex4,xxx))
        self.play(TransformMatchingTex(xxx,yyy,transform_mismatches = True),run_time=3)


class pipo(Scene):
    def construct(self):

        eq1 = MathTex(
            "\\frac{d}{dx}", #0
            "(", #1
            "u", #2
            "+", #3
            "v", #4
            ")", #5
            "=", #6
            "\\frac{d}{dx}", #7
            "u", #8
            "+", #9
            "\\frac{d}{dx}", #10
            "v" #11
        )

        self.play(Write(eq1[0:7]))
        self.wait(2)
        self.play(ReplacementTransform(eq1[2].copy(),eq1[8]),
                  ReplacementTransform(eq1[3].copy(),eq1[9]),
                  ReplacementTransform(eq1[4].copy(),eq1[11])
                  )
        self.wait(2)
        self.play(ReplacementTransform(eq1[0].copy(),eq1[7]),
                  ReplacementTransform(eq1[0].copy(),eq1[10]),
                  )


class quadratic(Scene):
    def construct(self):

        isolate = ["x^2","x","a","c","-","=","b"]

        add = MathTex("+","\\left(","{ b \\over 2a }","\\right)^2",
                     # substrings_to_isolate = ["b","2a","\\left(","\\right)"]
                      ).to_edge(2*UP).set_color(YELLOW)
        
        eq1 = MathTex("a","x^2","+","b","x","+","c","=","0",
                      substrings_to_isolate = [*isolate,"0"]
                      )
        eq1copy = MathTex("ax^2 + bx + c = 0")[0]
        eq2 = MathTex("a","x^2","+","b","x","=","-","c",
                      substrings_to_isolate = [*isolate])
        eq2copy = MathTex("ax^2+bx=-c")[0]
        eq3 = MathTex("x^2","+","{ b \\over a }","x", #0 1 2 3
                      "=", # 4
                      "-","{ c \\over a }") # 5 6
        eq3b = MathTex("x^2","+","{ b \\over a }","x", # 0 1 2 3
                       "=", # 4
                       "-","{ c \\over a }", # 5 6
                       substrings_to_isolate=isolate)
        eq4 = MathTex("x^2","+","{ b \\over a }","x","+", #0 1 2 3 4
                      "\\left(","{ b \\over 2a }","\\right)^2", # 5 6 7  
                      "=", # 8
                      "\\left(","{ b \\over 2a }","\\right)^2", # 9 10 11
                      "-","{ c \\over a }", # 12 13
                      #substrings_to_isolate=[*isolate,
                      #                       "\\left(","\right)","2a"]
                      )
        eq5 = MathTex("\\left(","x", "+", "{ b \\over 2a }","\\right)^2", # 0 1 2 3 4
                      "=", # 5
                      "\\left(","{ b \\over 2a }","\\right)^2", # 6 7 8
                      "-","{ c \\over a }" # 9 10
                      )
        eq5b=MathTex("\\left(","x", "+", "{ b \\over 2a }","\\right)^2", # 0 1 2 3 4
                      "=", # 5
                      "\\left(","{ b \\over 2a }","\\right)^2", # 6 7 8
                      "-","{ c \\over a }", # 9 10
                      substrings_to_isolate=[])
        eq6 = MathTex("\\left(","x", "+", "{ b \\over 2a }","\\right)^2", # 0 1 2 3 4
                      "=", # 5
                      "{ b^2 \\over 4a^2 }", # 6 
                      "-","{ c \\over a }"#, # 7 8
                      #substrings_to_isolate=isolate
                      )
     
        self.play(Write(eq1))
        self.wait()
        self.play(TransformMatchingTex(eq1,eq2))
        self.wait()
        self.play(TransformMatchingTex(eq2,eq3b))
        self.wait()
        self.clear()

        self.play(ReplacementTransform(eq3[0:4],eq4[0:4]),
                  ReplacementTransform(eq3[4],eq4[8]),
                  ReplacementTransform(eq3[5:7],eq4[12:14])
                  )
        self.wait()
        
        self.play(FadeIn(add))
        self.wait()
        self.play(ReplacementTransform(add[0],eq4[4]),
                  ReplacementTransform(add[1].copy(),eq4[5]),
                  ReplacementTransform(add[2].copy(),eq4[6]),
                  ReplacementTransform(add[3].copy(),eq4[7]),
                  ReplacementTransform(add[1],eq4[9]),
                  ReplacementTransform(add[2],eq4[10]),
                  ReplacementTransform(add[3],eq4[11])
                
                  )
        self.wait()

        nothing = MathTex(".")
        self.play(TransformMatchingTex(eq4,eq5))
        self.wait()
        self.play(ReplacementTransform(eq5[8][1],eq6[6][1]),ReplacementTransform(eq5[6][0],nothing[0]))
        self.play(ReplacementTransform(eq5,eq6))
        self.wait()
        #self.clear()
        
def get_sub_indexes(tex):
    ni = VGroup()
    colors = [RED,TEAL,GREEN,BLUE,PURPLE]
    for i in range(len(tex)):
        n = Text(f"{i}",color=colors[i%len(colors)]).scale(0.5)
        n.next_to(tex[i].set_color(colors[i%len(colors)]),DOWN,buff=0.01)
        ni.add(n)
    return ni
        
class trans1(Scene):
    def construct(self):
        #                           Why this?    |
        #
        source = MathTex("\\sqrt{\\frac{1}{8}}")[0]
        target = MathTex("\\frac{1}{2\\sqrt{2}}")[0]
        # If you ask yourself this, go back to "Tex as array"
        # section in the "Text and Tex" chapter
        
        VGroup(source,target).scale(4).arrange(RIGHT,buff=2)
        source_ind = get_sub_indexes(source)
        target_ind = get_sub_indexes(target)
        
        self.add(
            source, source_ind,
            target, target_ind
        )


class trans2(Scene):
    def construct(self):
        source = MathTex("\\sqrt{\\frac{1}{8}}")[0]
        target = MathTex("\\frac{1}{2\\sqrt{2}}")[0]
        
        VGroup(source,target).scale(4)
        self.add(source)
        transform_index = [
            [0,1,2,3,4,"r4"],
            # | | | | |  |
            # v v v v v  v
            [3,4,0,1,2, 5]
        ]
        self.play(
            *[
                # Try replacing "ReplacementTransform" with "FadeTransform"
                ReplacementTransform(source[i],target[j])
                if type(i) is int else
                ReplacementTransform(source[int(i[1:])].copy(),target[j])
                for i,j in zip(*transform_index)
            ],
            run_time=3
        )
        self.wait()

class trans3(Scene):
    def construct(self):
        source = MathTex("\\sqrt{\\frac{1}{8}}")[0]
        target = MathTex("\\frac{1}{2\\sqrt{2}}")[0]
        
        VGroup(source,target).scale(4)
        self.add(source)
        transform_index = [
            ["f0","f1",2,3,4,"r4"],
            #  |    |   | | |  |
            #  v    v   v v v  v
            [ 3,   4,  0,1,2, 5]
        ]
        self.play(
            *[
                ReplacementTransform(source[i],target[j])
                if type(i) is int else
                ReplacementTransform(source[int(i[1:])].copy(),target[j])
                if i[0]=="r" else
                FadeTransform(source[int(i[1:])],target[j])
                for i,j in zip(*transform_index)
            ],
            run_time=3
        )
        self.wait()


class eqs(Scene):
    def construct(self):

        eq1 = MathTex("ax^2 + bx + c = 0")[0]
        eq2 = MathTex("ax^2 + bx = -c ")[0]
        eq3 = MathTex("x^2 + \\frac{b}{a}x  = -\\frac{c}{a}")[0]
        eq4 = MathTex("x^2 + \\frac{b}{a}x + \\left(\\frac{b}{2a}\\right)^2 =  \\left(\\frac{b}{2a}\\right)^2 -\\frac{c}{a}")[0]
        eq5a = MathTex("\\left(x + \\frac{b}{2a}\\right)^2 = \\left( \\frac{b}{2a} \\right)^2 - \\frac{c}{a}")[0]
        eq5b = MathTex("\\left(x + \\frac{b}{2a}\\right)^2 = \\frac{b^2}{4a^2} - \\frac{c}{a}")[0]
        
        
        all1 = VGroup(eq1,eq2).scale(2.5).arrange(DOWN,buff=1)
        all2 = VGroup(eq3,eq4).scale(1.5).arrange(DOWN,buff=1)
        #eqs5 = VGroup(eq5a,eq5b).scale(1.5).arrange(DOWN,buff=1)
        eq1_ind = get_sub_indexes(eq1)
        eq2_ind = get_sub_indexes(eq2)
        eq3_ind = get_sub_indexes(eq3)
        eq4_ind = get_sub_indexes(eq4)
        eq5a_ind = get_sub_indexes(eq5a)
        eq5b_ind = get_sub_indexes(eq5b)
        
        '''self.add(eq1, eq1_ind,
                 eq2, eq2_ind)
        self.wait(2)
        self.clear()
        
        self.add(eq3, eq3_ind,
                 eq4, eq4_ind)
        self.wait(2)
        '''
        #self.add(eq5a,eq5a_ind,eq5b,eq5b_ind)
        self.add(eq5a)
        transform_index = [[0,1,2,3,4,5,6,7,8,9,11,12,13,14,16,"r16","r16",17,18,19,20,"v10","v15"],
                           [0,1,2,3,4,5,6,7,8,9,10,12,13,14,11,15   ,13   ,16,17,18,19,10   , 15  ]]

        self.wait(2)
        
        self.play(
            *[
                ReplacementTransform(eq5a[i],eq5b[j])
                if type(i) is int else
                ReplacementTransform(eq5a[int(i[1:])].copy(),eq5b[j])
                if i[0]=="r" else
                FadeTransform(eq5a[int(i[1:])],eq5b[j])
                #if i[0]=="v" else
                #FadeOut(eq5a[int(i[1:])])
                for i,j in zip(*transform_index)
            ],
            run_time=3
        )
        #self.play(Transform(eq5a,eq5b))
