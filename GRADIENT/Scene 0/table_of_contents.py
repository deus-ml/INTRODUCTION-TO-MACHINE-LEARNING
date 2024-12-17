from manim import *

class Table(Scene):
    def construct(self): 
        """SCENE 0 Time Constants"""
        REVEAL_CONTENTS_RUN_TIME = 1
        REVEAL_FIRST_AFTER_SECONDS = 2
        REVEAL_NEXT_AFTER_SECONDS = 1
        SHOW_CONTENTS_FOR_SECONDS = 5



        # Create the text objects
        a = Text("Definition Of A Gradient", t2c={'i': RED}, t2w={'Gradient': BOLD}, font_size=20, font='Book Antiqua')
        b = Text("Gradient Of A Straight Line", t2c={'a': YELLOW}, t2w={'Straight': BOLD}, font_size=20, font='Book Antiqua')
        c = Text("Gradient Of A Function", t2c={'n': GREEN}, t2w={'Function': BOLD}, font_size=20, font='Book Antiqua')
        d = Text("Gradient Of A Function With More Variables", t2c={'e': BLUE}, t2w={'More': BOLD}, font_size=20, font='Book Antiqua')

        # Create the number objects
        one = Tex(r"$1.$", font_size=50, color=RED)
        two = Tex(r"$2.$", font_size=50, color=YELLOW)
        three = Tex(r"$3.$", font_size=50, color=GREEN)
        four = Tex(r"$4.$", font_size=50, color=BLUE)

        # Position the text objects vertically
        b.next_to(a, DOWN, aligned_edge=LEFT)
        c.next_to(b, DOWN, aligned_edge=LEFT)
        d.next_to(c, DOWN, aligned_edge=LEFT)

        # Position the number objects
        one.next_to(a, LEFT)
        two.next_to(b, LEFT)
        three.next_to(c, LEFT)
        four.next_to(d, LEFT)

        # Group the text and number objects together
        group = VGroup(one, two, three, four, a, b, c, d)
        group.move_to(UL*1.5)

        # Animate the objects
        self.wait(REVEAL_FIRST_AFTER_SECONDS)
        self.play(FadeIn(one), Write(a), run_time=REVEAL_CONTENTS_RUN_TIME)
        self.wait(REVEAL_NEXT_AFTER_SECONDS)
        self.play(FadeIn(two), Write(b), run_time=REVEAL_CONTENTS_RUN_TIME)
        self.wait(REVEAL_NEXT_AFTER_SECONDS)
        self.play(FadeIn(three), Write(c), run_time=REVEAL_CONTENTS_RUN_TIME)
        self.wait(REVEAL_NEXT_AFTER_SECONDS)
        self.play(FadeIn(four), Write(d), run_time=REVEAL_CONTENTS_RUN_TIME)
        self.wait(SHOW_CONTENTS_FOR_SECONDS)
