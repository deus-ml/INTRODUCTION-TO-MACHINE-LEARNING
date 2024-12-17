from manim import *
import numpy as np

class Gradient(Scene):

    def construct(self):



        # GRADIENT SCENE 2
        
        # SECTION ONE

        """SECTION ONE Timing Constants"""
        DRAW_POINT_A_AFTER = 2
        DRAW_POINT_B_AFTER = 2
        DRAW_AXES_AFTER = 2
        DRAW_DELTA_Y_AFTER = 1
        DRAW_DELTA_X_AFTER = 1
        INDICATE_AFTER = 1
        FADE_OUT_SCENE_AFTER = 3
        SHIFT_DURATION = 3
        WAIT_BEFORE_SHIFTING = 2
        ALTERNATIVE_WAIT_UNTIL = 1







        axes_one = Axes(
            x_range=[0, 6],
            y_range=[0, 6],

            x_length=8,
            y_length=6,
            tips=False
            )
        
        xy_labels = axes_one.get_axis_labels(
            Tex("x-axis").scale(0.7), Text("y-axis").scale(0.45)
        )

        self.wait(DRAW_AXES_AFTER)
        self.play(Write(axes_one), run_time=1.0)
        self.add(xy_labels)
        self.wait()

        # plotting The Line
        graph = axes_one.plot(lambda x: x, x_range=[2, 5], color=GREEN_B, use_smoothing=False)
        self.play(Write(graph), run_time=2)


        point_1 = axes_one.coords_to_point(2, 2)
        point_2 = axes_one.coords_to_point(5, 5)
        meeting_point = axes_one.coords_to_point(5, 2)

        line1 = DashedLine(point_1, meeting_point, color=RED)
        line2 = DashedLine(point_2, meeting_point, color=BLUE_B)

        dot1 = Dot(point_1, color=RED)
        dot1_label = MathTex(r"A","(","x_1", ",", " y_1",")").next_to(dot1, LEFT*0.1).scale(0.6)
        dot1_label[0].set_color(ORANGE)
        dot2 = Dot(point_2, color=BLUE_B)
        dot2_label = MathTex(r"B","(","x_2", ",", " y_2",")").next_to(dot2, LEFT*0.1).scale(0.6)
        dot2_label[0].set_color(BLUE_B)
        meeting_dot = Dot(meeting_point, color=YELLOW)

        self.wait(DRAW_POINT_A_AFTER)


        self.play(FadeIn(dot1), run_time=1)
        self.play(Write(dot1_label))


        self.wait(DRAW_POINT_B_AFTER)

    
        self.play(FadeIn(dot2), run_time=1)
        self.play(Write(dot2_label))
        self.wait(1)
        self.play(Create(line1), Create(line2), FadeIn(meeting_dot))

        self.wait(DRAW_DELTA_Y_AFTER)

        brace_y = BraceBetweenPoints(point_2, meeting_point, direction=RIGHT)
        self.play(GrowFromCenter(brace_y), run_time=1)
        delta_y = brace_y.get_text("$\Delta$y")
        y_1 = dot1_label[4]
        y_2 = dot2_label[4]
        self.play(Write(delta_y), Indicate(y_1), Indicate(y_2), run_time=2)

        self.wait(DRAW_DELTA_X_AFTER)

        brace_x = BraceBetweenPoints(point_1, meeting_point)
        self.play(GrowFromCenter(brace_x), run_time=1)
        delta_x = brace_x.get_text("$\Delta$x")
        x_1 = dot1_label[2]
        x_2 = dot2_label[2]
        self.play(Write(delta_x), Indicate(x_1), Indicate(x_2), run_time=2)


        self.wait(INDICATE_AFTER)
        self.play(Indicate(delta_y, scaling_factor=1.5), run_time=1)
        self.wait(INDICATE_AFTER)
        self.play(Indicate(delta_x, scaling_factor=1.5), run_time=1)

        definition_group = Group(dot1, dot2, meeting_dot, line1,
            line2, brace_x, brace_y, graph, axes_one, dot1_label,
            xy_labels, dot2_label, delta_x, delta_y)


        self.wait(WAIT_BEFORE_SHIFTING)
        self.play(definition_group.animate.scale(0.7).shift(RIGHT*2), run_time=SHIFT_DURATION)


        gd = MathTex(r"Gradient", r"&= \frac{\Delta y}{\Delta x}\\ &= \frac{y_2 - y_1}{x_2 - x_1}\\", r"\\&=\frac{y_1 - y_2}{x_1 - x_2}").move_to(LEFT*3.5)
        gd.scale(0.8)
        gd[0].set_color(YELLOW)
        self.play(DrawBorderThenFill(gd[0:2]), run_time=2)

        self.wait(ALTERNATIVE_WAIT_UNTIL)


        self.play(DrawBorderThenFill(gd[2]), run_time=2)


        # END OF SECTION ONE
        self.wait(FADE_OUT_SCENE_AFTER)
        self.play(
            AnimationGroup(FadeOut(dot1), FadeOut(dot2),
            FadeOut(meeting_dot), FadeOut(line1), FadeOut(line2),
            FadeOut(brace_x), FadeOut(delta_x),
            FadeOut(dot1_label), FadeOut(dot2_label),
            FadeOut(brace_y), FadeOut(delta_y),
            FadeOut(gd),
            FadeOut(graph), runtime=0.65

        ))








        # SECTION TWO BEGINS HERE

        """SECTION TWO Timing Constants"""
        DRAW_POINT_B_AFTER = 2
        DRAW_POINT_A_AFTER = 2
        WAIT_BEFORE_BRACE_Y = 2
        WAIT_BEFORE_BRACE_X = 2
        WAIT_BEFORE_MAKING_FORMULA = 5
        SHOW_DYNAMIC_GRAD_AFTER = 10




        # Second Smaller Graph Plot

        axes_two = Axes(
            x_range=[0, 7],
            y_range=[0, 9],

            x_length=8,
            y_length=8,
            tips=False,
            axis_config={'include_numbers': True}
            ).shift(LEFT * 3.7).scale(0.6)
            
        xy_labels_1 = axes_two.get_axis_labels(
            Tex("x").scale(0.4), Text("y").scale(0.4)
        )

        group_1 = Group(axes_one, xy_labels)
        self.play(ReplacementTransform(group_1, axes_two))
        
        # Line Value Tracker
        value_tracker = ValueTracker(1)
        # plotting The Line
        graph_1 = always_redraw(lambda: axes_two.plot(lambda x: value_tracker.get_value()*x + 2, x_range=[0, 5], color=GREEN_B, use_smoothing=False))
        self.add(xy_labels_1)
        self.play(Write(graph_1), run_time=1)
        
        self.wait(DRAW_POINT_B_AFTER)


        point_22 = axes_two.point_to_coords(graph_1.get_end())

        point_11 = axes_two.coords_to_point(0, 2)
        meeting_point_1 = axes_two.coords_to_point(5, 2)

        dot11 = Dot(point_11, color=RED)
        dot11_label = MathTex(r"A","(","0", ",", " 2",")").next_to(dot11, RIGHT*0.11+UP*0.05).scale(0.5)
        dot11_label[0].set_color(RED)

        meeting_dot_1 = Dot(meeting_point_1, color=BLUE_B)

    
        dot22 = always_redraw(lambda: Dot(axes_two.c2p(*axes_two.point_to_coords(graph_1.get_end())), color=YELLOW))
    

        dot22_label = MathTex(r"B","(","5", ",", " 7",")").next_to(dot22, LEFT*0.1).scale(0.5)
        dot22_label[0].set_color(YELLOW)

        line11 = DashedLine(point_11, meeting_point_1, color=RED)
        line22 = always_redraw(lambda: DashedLine(dot22.get_center(), meeting_point_1, color=YELLOW))




        self.play(FadeIn(dot22))
        self.play(Write(dot22_label), run_time=1)

        self.wait(DRAW_POINT_A_AFTER)

        self.play(FadeIn(dot11))
        self.play(Write(dot11_label), run_time=1)
        self.wait(2)
        self.play(Create(line11), Create(line22), FadeIn(meeting_dot_1))




        # Coordinate Points
        change_x = 5
        change_y = 5

        result = 1



        self.wait(WAIT_BEFORE_BRACE_Y)


        brace_yy = always_redraw(lambda: BraceBetweenPoints(dot22.get_center(), meeting_point_1, direction=RIGHT))
        self.play(GrowFromCenter(brace_yy), run_time=1)

        variable_y = Variable(change_y, Tex("$\Delta$y"), num_decimal_places=1).next_to(brace_yy, RIGHT*0.0001)
        variable_y.scale(0.5)
        self.play(Write(variable_y))

        self.wait(WAIT_BEFORE_BRACE_X)

        brace_xx = BraceBetweenPoints(point_11, meeting_point_1)
        self.play(GrowFromCenter(brace_xx), run_time=1)

        variable_x = Variable(change_x, Tex("$\Delta$x"), num_decimal_places=1).next_to(brace_xx, DOWN*0.1)
        variable_x.scale(0.5)
        self.play(Write(variable_x))




        self.wait(WAIT_BEFORE_MAKING_FORMULA)



        # Dynamic label for the y-axis brace showing the difference in y-values
        brace_yy_value = always_redraw(
            lambda: brace_yy.get_text(
                fr"= {round(axes_two.point_to_coords(graph_1.get_end())[1] - 2, 1)}"
            )
        )
        # Dynamic label for the y-axis brace showing the difference in y-values
        brace_xx_value = brace_xx.get_tex("5.0", buff=0.1)




        # Gradient
        # grad_word = Text("Gradient = ", t2c={'Gradient':PURPLE}, font_size=35)

        # Working Out A Gradient From The Formula
        formula = MathTex(r"Gradient = ", r"\frac{\Delta y}{\Delta x} &= \frac{7-2}{5-0}\\ &= \frac{5}{5}\\ &= 1").move_to(RIGHT*2.75+DOWN*0.2)
        formula[0].set_color(ORANGE)
        # Group The Delta_x And Delta_y Labels On the Plot
        # And Transform Them Into The Formula Of A Gradient Of A Line
        group_deltas_values = Group(variable_x, variable_y, dot11_label, dot22_label)
        self.play(
            AnimationGroup(TransformMatchingShapes(group_deltas_values, formula).set_run_time(3),
            FadeOut(brace_xx), FadeOut(brace_yy), Write(formula[0])
        ))

        self.wait(SHOW_DYNAMIC_GRAD_AFTER)
        
        # Transform Static Formula Into Dynamic Gradient Values
        self.play(
            # Transform Gradient Formula Into The Word Gradient
            TransformMatchingShapes(formula, formula[0]).set_run_time(2),
            FadeIn(dot11).set_run_time(0.001), runtime=0.65
        )
        self.wait(2)

        # Re-draw Braces And Their Labels
        self.play(GrowFromCenter(brace_yy), Write(brace_yy_value), 
            GrowFromCenter(brace_xx), Write(brace_xx_value), run_time=2)

        # The Updating Gradient Value Of The Line
        grad = always_redraw(lambda: DecimalNumber(value_tracker.get_value(), num_decimal_places=2))
        grad.add_updater(lambda m: m.set_value(value_tracker.get_value()).next_to(formula[0], RIGHT))
        self.add(grad)

        # Move The Line Around The Plot
        self.play(value_tracker.animate.set_value(1.38), rate_func=there_and_back, run_time=15)
        self.wait(3)
        self.play(value_tracker.animate.set_value(0.0), run_time=7.5)
        self.wait(3)
        self.play(value_tracker.animate.set_value(1.0), run_time=7.5)
        self.wait(2)















