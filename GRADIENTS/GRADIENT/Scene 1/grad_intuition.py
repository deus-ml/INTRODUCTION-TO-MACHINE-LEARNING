from manim import *

class GradIntuition(Scene):
    def construct(self):

        """SCENE 1 Time Constants"""
        SHOW_FOR_SECONDS = 5
        DISP_ANSWER_1_AFTER = 3
        DISP_ANSWER_2_AFTER = 3
        






        line = Line(start=LEFT*7, end=RIGHT*7)
        line.shift(DOWN*2.3)
        self.play(Write(line))

        axes_1 = Axes(
            x_range=[-5, 20],
            y_range=[0, 10, 1]
        )
        # Hide Axes
        axes_1.set_opacity(0)

        mount_1 = axes_1.plot(lambda x: 5 + 4*x - x**2, x_range=[-1, 5])
        # Define the points
        point_A = Dot(axes_1.coords_to_point(-0.98, 0), color=RED)
        label_A = Text("A", color=RED).next_to(point_A, UP+LEFT*0.5)
        
        point_B = Dot(axes_1.coords_to_point(0.5, 7), color=GREEN)
        label_B = Text("B", color=RED).next_to(point_B, UP+LEFT*0.5)

        brace = BraceBetweenPoints(point_A.get_center(), point_B.get_center(), direction=RIGHT)
        brace_text = brace.get_text("50m", buff=0.1)

        horizontal_brace = Brace(
        Line(
            axes_1.coords_to_point(-1, 0),
            axes_1.coords_to_point(1, 0)
        ),
        direction=DOWN,
        color=BLUE)
        hill_one = Text("Hill 1").next_to(mount_1, UP*2)
        hill_one.shift(LEFT*2.2)

        horizontal_brace_text = horizontal_brace.get_text("5m", buff=0.1)
        horizontal_brace_text.move_to(horizontal_brace.get_center() + DOWN * 0.5)

        # Group the axes and the graph
        group = VGroup(axes_1, mount_1, point_A, label_A, point_B, label_B, brace, brace_text, horizontal_brace, horizontal_brace_text)
        group.scale(0.7)
        group.shift(LEFT*3)

        self.play(FadeIn(hill_one))
        self.play(Write(axes_1), run_time=0.1)
        self.play(Create(mount_1))
        self.play(FadeIn(point_A), Write(label_A))
        self.play(FadeIn(point_B), Write(label_B))
        self.play(GrowFromCenter(brace), Write(brace_text))
        self.play(GrowFromCenter(horizontal_brace), Write(horizontal_brace_text))



        # Second Illustration


        axes_2 = Axes(
            x_range=[-5, 10],
            y_range=[0, 10, 1]
        )
        axes_2.set_opacity(0)

        mount_2 = axes_2.plot(lambda x: 5 + 4*x - x**2, x_range=[-1, 5])


        hill_two = Text("Hill 2").next_to(mount_2, UP*2)
        hill_two.shift(RIGHT*2.5)

        # Define the points
        point_A2 = Dot(axes_2.coords_to_point(-0.98, 0), color=RED)
        label_A2 = Text("A", color=RED).next_to(point_A2, UP+LEFT*0.5)
        
        point_B2 = Dot(axes_2.coords_to_point(0.5, 7), color=GREEN)
        label_B2 = Text("B", color=RED).next_to(point_B2, UP+LEFT*0.5)

        brace_2 = BraceBetweenPoints(point_A2.get_center(), point_B2.get_center(), direction=RIGHT)
        brace_text_2 = brace_2.get_text("50m", buff=0.1)

        horizontal_brace_2 = Brace(
        Line(
            axes_2.coords_to_point(-1, 0),
            axes_2.coords_to_point(1, 0)
        ),
        direction=DOWN,
        color=YELLOW)

        horizontal_brace_text_2 = horizontal_brace_2.get_text("10m", buff=0.1)
        horizontal_brace_text_2.move_to(horizontal_brace_2.get_center() + DOWN * 0.5)

        # Group the axes and the graph
        group_2 = VGroup(axes_2, mount_2, point_A2, label_A2, point_B2, label_B2, brace_2, brace_text_2, horizontal_brace_2, horizontal_brace_text_2)
        group_2.scale(0.7)
        group_2.shift(RIGHT*3.8)

        self.play(FadeIn(hill_two))
        self.play(Write(axes_2), run_time=0.1)
        self.play(Create(mount_2))
        self.play(FadeIn(point_A2), Write(label_A2))
        self.play(FadeIn(point_B2), Write(label_B2))
        self.play(GrowFromCenter(brace_2), Write(brace_text_2))
        self.play(GrowFromCenter(horizontal_brace_2), Write(horizontal_brace_text_2))


        self.wait(DISP_ANSWER_1_AFTER)

        div_1 = MathTex(r'gradient(hill 1) = ', r'\frac{50}{5}').move_to(UP*2+LEFT)
        div_1.scale(0.7)
        div_11 = MathTex(r'10', color=BLUE).next_to(div_1[0], RIGHT)
        div_11.scale(0.7)
        self.play(Write(div_1), run_time=1)
        self.play(TransformMatchingShapes(div_1[1], div_11), run_time=2)


        self.wait(DISP_ANSWER_2_AFTER)

        div_2 = MathTex(r'gradient(hill 2) = ', r'\frac{50}{10}').move_to(UP*0.9+LEFT)
        div_2.scale(0.7)
        div_22 = MathTex(r'5', color=YELLOW).next_to(div_2[0], RIGHT)
        div_22.scale(0.7)
        self.play(Write(div_2), run_time=1)
        self.play(TransformMatchingShapes(div_2[1], div_22), run_time=2)


        self.wait(SHOW_FOR_SECONDS)