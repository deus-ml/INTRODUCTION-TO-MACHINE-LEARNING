from manim import *

class GradientOfAFunction(Scene):
    def construct(self):

        gradient_of = Text('Gradient Of ', t2c={'[3:-2]': BLUE}).move_to(LEFT)
        a_function = Text('A Function',t2c={'ction':RED}).next_to(gradient_of, RIGHT)
        f = MathTex(r"(f)").next_to(a_function, RIGHT*0.5)
        aka = MathTex(r"\text{Denoted as } \nabla f", font_size=40).shift(DOWN*0.6)

        group = Group(gradient_of, a_function, f)
        aka.shift(ORIGIN)
        group.move_to(ORIGIN)

        self.play(FadeIn(gradient_of), FadeIn(a_function), FadeIn(f), FadeIn(aka), run_time=3)
        self.play(FadeOut(gradient_of), FadeOut(a_function),FadeOut(f), FadeOut(aka), run_time=3)
    

        