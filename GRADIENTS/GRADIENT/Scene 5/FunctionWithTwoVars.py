from manim import *

class IntroTwoVariables(Scene):
    def construct(self):

        text = Text("Considering The Function:", font='Book Antiqua', color=PURPLE)
        equation = MathTex("f(", "x", ",", "b", ") =", "x","^2", "+", "b", color=RED).next_to(text, DOWN)

        text.scale(0.8)
        equation.scale(0.8)

        self.play(FadeIn(text), run_time=2)
        self.play(FadeIn(equation), run_time=2)
        self.play(FadeOut(text), run_time=2)
        self.play(equation.animate.shift(UP*3.5))
        self.wait(2)

        self.play(equation.animate.scale(1.5), run_time=2)

        # Indicate The Two Variables In The Equation
        self.play(Indicate(equation[1], color=ORANGE, scale_factor=1.3), Wiggle(equation[5], rotation_angle=0.05), run_time=2) 
        self.play(Indicate(equation[3], color=ORANGE, scale_factor=1.3), Wiggle(equation[8]), run_time=2)
        self.wait(2)


        gradient = MathTex(r"\text{Gradient, } \nabla f(x, b)").next_to(equation, DOWN*1.1)
        self.play(Write(gradient), run_time=2.5)
        self.play(gradient.animate.shift(DOWN*1.5, LEFT*2.27))
        self.wait(2)

       
        equal_sign = MathTex("=").next_to(gradient, RIGHT)
        self.play(FadeIn(equal_sign), run_time=1)

        gradient_vector = Matrix([[r"\frac{\delta f}{\delta x}"],
                                  [r"\frac{\delta f}{\delta b}"]], v_buff=1.25).next_to(equal_sign, RIGHT)
        gradient_vector.set_row_colors(YELLOW, GREEN)


        self.play(DrawBorderThenFill(gradient_vector), run_time=3)
        self.wait(2)



        row_index = 0  # Second row (0-based index)
        col_index = 0  # Third column (0-based index)

        row_index_1 = 1  # Second row (0-based index)
        col_index_1 = 0  # Third column (0-based index)


        self.play(Indicate(gradient_vector.get_entries()[row_index + col_index], scale_factor=1.3), run_time=2)
        self.play(Indicate(gradient_vector.get_entries()[row_index_1 + col_index_1], color=GREEN, scale_factor=1.3), run_time=2)

        self.wait(3)





        group_01 = Group(gradient, equal_sign, gradient_vector)
        self.play(group_01.animate.scale(0.65).shift(LEFT*2), run_time=3)

        derivative_wrt_x = MathTex(r"\nabla_x f(x,", "b", ")",  "=", r"\frac{\delta}{\delta x} (x^2 + b)").move_to(RIGHT*2.5)
        derivative_wrt_x.shift(UP)
        derivative_wrt_x.set_color_by_tex(r"\frac{\delta}{\delta x} (x^2 + b)", YELLOW)
        self.play(Write(derivative_wrt_x[0:3]), run_time=2)
        self.wait(2)
        # Equal_Sign
        derivative_wrt_x[3]
        self.play(Write(derivative_wrt_x[3]))
        # Equation
        self.play(Write(derivative_wrt_x[4]), run_time=2)

        self.wait(3)

        derivative_wrt_x_1 = MathTex(r"\frac{\delta}{\delta x} (x^2 +", "b",")",  "=", "x","^2", "+", "b").next_to(derivative_wrt_x, DOWN)
        self.play(Write(derivative_wrt_x_1), run_time=2)
        self.wait(3)

    
        derivative_wrt_x_10 = MathTex(r"\frac{\delta}{\delta x} (x^2 +", "b",")",  "=", "x","^2", "+", "0").next_to(derivative_wrt_x, DOWN)
        self.play(ReplacementTransform(derivative_wrt_x_1, derivative_wrt_x_10), run_time=3)

        self.wait(4)

        derivative_wrt_x_11 = MathTex(r"\frac{\delta}{\delta x} (x^2 +", "b",")",  "=", "x^2").next_to(derivative_wrt_x, DOWN)
        self.play(TransformMatchingShapes(derivative_wrt_x_10, derivative_wrt_x_11), run_time=3)
        derivative_wrt_x_12 = MathTex(r"\frac{\delta}{\delta x} (x^2 +", "b",")",  "=", "2x").next_to(derivative_wrt_x, DOWN)
        derivative_wrt_x_12.set_color_by_tex(r"2x", YELLOW)
        self.wait(1)
        self.play(TransformMatchingShapes(derivative_wrt_x_11, derivative_wrt_x_12), run_time=4)

        self.wait(3)

        row_index = 0  # Second row (0-based index)
        col_index = 0  # Third column (0-based index)
        element = gradient_vector.get_entries()[row_index * 1 + col_index]

        first_derivative = MathTex("2x")
        first_derivative.move_to(element.get_center())


        self.play(ReplacementTransform(gradient_vector.get_entries()[row_index + col_index], first_derivative.set_color(YELLOW)), run_time=3)

        self.wait(3)

        self.play(FadeOut(derivative_wrt_x_12), run_time=2)

        # Derivative wrt b
        derivative_wrt_b = MathTex(r"\nabla_b f(x,", "b", ")",  "=", r"\frac{\delta}{\delta b} (x^2 + b)").move_to(RIGHT*2.5)
        derivative_wrt_b.shift(UP)
        derivative_wrt_b.set_color_by_tex(r"\frac{\delta}{\delta b} (x^2 + b)", GREEN)
        self.play(TransformMatchingShapes(derivative_wrt_x, derivative_wrt_b), run_time=3)


        derivative_wrt_b_1 = MathTex(r"\frac{\delta}{\delta b} (x^2 + b) = x^2 + b").next_to(derivative_wrt_b, DOWN)
        self.play(Write(derivative_wrt_b_1), run_time=2)

        self.wait(3)

        derivative_wrt_b_10 = MathTex(r"\frac{\delta}{\delta b} (x^2 + b) = 0 + b").next_to(derivative_wrt_b, DOWN)
        self.play(TransformMatchingShapes(derivative_wrt_b_1, derivative_wrt_b_10), run_time=4)

        self.wait(4)

        derivative_wrt_b_11 = MathTex(r"\frac{\delta}{\delta b} (x^2 + b) = b").next_to(derivative_wrt_b, DOWN)
        self.play(TransformMatchingShapes(derivative_wrt_b_10, derivative_wrt_b_11), run_time=3)
        derivative_wrt_b_12 = MathTex(r"\frac{\delta}{\delta b} (x^2 + b ) = ","1").next_to(derivative_wrt_b, DOWN)
        derivative_wrt_b_12.set_color_by_tex(r"1", GREEN)
        self.play(TransformMatchingShapes(derivative_wrt_b_11, derivative_wrt_b_12), run_time=3)

        self.wait(3)

        row_index = 1  # Second row (0-based index)
        col_index = 0  # Third column (0-based index)
        element = gradient_vector.get_entries()[row_index * 1 + col_index]

        second_derivative = MathTex("1")
        second_derivative.move_to(element.get_center())

        self.play(ReplacementTransform(gradient_vector.get_entries()[row_index + col_index], second_derivative.set_color(GREEN)), run_time=3)

        self.wait(3)

        group_02 = Group(derivative_wrt_b_12, derivative_wrt_b)
        self.play(FadeOut(group_02), run_time=3)
        self.wait(2)

        new_gradient_vector = Matrix([["2x"],
                                      ["1"]], v_buff=1.25).next_to(equal_sign, RIGHT)
        new_gradient_vector.set_row_colors(YELLOW, GREEN)
        
        group_03 = VGroup(equal_sign, gradient, new_gradient_vector)

        ReplacementTransform(gradient_vector, group_03)
        self.remove(gradient_vector)
        self.play(group_03.animate.scale(1.1).shift(RIGHT*2.3), run_time=2)

        self.wait(2)




        row_index = 0  # Second row (0-based index)
        col_index = 0  # Third column (0-based index)

        row_index_1 = 1  # Second row (0-based index)
        col_index_1 = 0  # Third column (0-based index)



        self.play(Indicate(new_gradient_vector.get_entries()[row_index + col_index], scale_factor=1.5), run_time=2)
        self.play(Indicate(new_gradient_vector.get_entries()[row_index_1 + col_index_1], color=GREEN, scale_factor=1.5), run_time=2)

        self.wait(2)


        point_1 = 6
        point_2 = 3

        gradient_1 = MathTex(r"\text{Gradient, } \nabla f(6, 3)").next_to(new_gradient_vector, LEFT*1.1)
        gradient_1.scale(0.7)
        equal_sign = MathTex("=").next_to(gradient_1, RIGHT)

        new_gradient_vector_1 = Matrix([[fr"2({point_1})"],
                                        ["1"]], v_buff=1.25).next_to(equal_sign, RIGHT)
        new_gradient_vector_1.set_row_colors(YELLOW, GREEN)

        new_gradient_vector_2 = Matrix([["12"],
                                        ["1"]], v_buff=1.25).next_to(equal_sign, RIGHT)
        new_gradient_vector_2.set_row_colors(YELLOW, GREEN)


        group_04 = VGroup(gradient_1, equal_sign, new_gradient_vector_1)
        group_05 = VGroup(gradient_1, equal_sign, new_gradient_vector_2)

        self.wait(3)
        self.play(TransformMatchingShapes(group_03, group_04), run_time=2)
        self.wait(3)
        self.play(TransformMatchingShapes(group_04, group_05), run_time=2)
        self.wait(3)


        group_05 = VGroup(equation, group_05)
        self.play(FadeOut(group_05))


        self.wait(5)
    
        # Conclusion


        equation_n = MathTex(r"f(x_1, x_2, \cdots, x_n) = x_1 + x_2 + \cdots + x_n", color=RED).move_to(UP*3)

        gradient_2 = MathTex(r"\text{Gradient, } \nabla f(x_1, x_2, \cdots, x_n)")

        equal_sign_2 = MathTex("=").next_to(gradient_2, RIGHT)

        gradient_vector_3 = Matrix([[r"\frac{\delta f}{\delta x_1}"],
                                  [r"\frac{\delta f}{\delta x_2}"],
                                  [r"\vdots"],
                                  [r"\frac{\delta f}{\delta x_n}"]], v_buff=1.25).next_to(equal_sign_2, RIGHT)
        gradient_vector_3.scale(0.8)


        group_06 = VGroup(gradient_2, equal_sign_2, gradient_vector_3)



        self.play(Write(equation_n))
        self.wait(3)

        self.play(Write(gradient_2), run_time=2)
        self.wait(2)
        self.play(FadeIn(equal_sign_2), run_time=1)
        self.wait(2)
        self.play(Write(gradient_vector_3), run_time=3)

        self.play(group_06.animate.shift(LEFT*1.2), run_time=2)

        self.wait(16)


        self.play(FadeOut(group_06), FadeOut(equation_n), run_time=3)

        self.wait(1)

















