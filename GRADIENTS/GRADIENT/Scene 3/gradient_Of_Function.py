from manim import *

class GradientCurve(Scene):
    def construct(self):

        # SECTION ONE TIME CONSTANTS
        WAIT_BEFORE_REVERSE = 2



        # Beginning Quote
        quote = Text("Tangent at any point can be viewed as the local approximation to the curve itself \n for an infinitesimally small neighborhood around the point", font='Bell MT', color=PURPLE)
        quote_source = Text("-- Math and Architectures of Deep Learning", font='Book Antiqua').next_to(quote, DOWN*0.5)

        quote.scale(0.5)
        quote_source.scale(0.5)
        self.play(FadeIn(quote), FadeIn(quote_source), run_time=2)
        self.wait(5)
        self.play(FadeOut(quote), FadeOut(quote_source), run_time=2)

        self.wait(3)

        
        #Introduction

        axes_intro = Axes(
            x_range=[-7, 10, 1],
            y_range=[-5, 10, 1],

            x_length=8,
            y_length=6,
            tips=False,
            axis_config={'include_numbers': False}
            ).scale(0.8).move_to(UP)

        self.play(FadeIn(axes_intro), run_time=2)

        eqn_line = axes_intro.plot(lambda x: x + 2, x_range=[0, 7], color=BLUE)
        eqn_poly_1 = axes_intro.plot(lambda x: (x - 2)**2, x_range=[-1.3, 5], color=BLUE)
        eqn_poly_2 = axes_intro.plot(lambda x: (2 - 3*x)/(x**2 + 3*x + 3), x_range=[-7, 7], color=BLUE)
        eqn_poly_3 = axes_intro.plot(lambda x: (x**3 + 3*x**2 - 6*x - 8), x_range=[-4, 2], color=BLUE)

        self.play(DrawBorderThenFill(eqn_line), run_time=2)
        self.wait(1)
        self.play(ReplacementTransform(eqn_line, eqn_poly_1), run_time=2)
        self.wait(1)
        self.play(ReplacementTransform(eqn_poly_1, eqn_poly_2), run_time=2)
        self.wait(1)
        self.play(ReplacementTransform(eqn_poly_2, eqn_poly_3), run_time=2)

        # Unwind The Graph Animations
        self.wait(WAIT_BEFORE_REVERSE)
        eqn_poly_2 = axes_intro.plot(lambda x: (2 - 3*x)/(x**2 + 3*x + 3), x_range=[-7, 7], color=BLUE)
        self.play(ReplacementTransform(eqn_poly_3, eqn_poly_2), run_time=1)
        eqn_poly_1 = axes_intro.plot(lambda x: (x - 2)**2, x_range=[-1.3, 5], color=BLUE)
        self.play(ReplacementTransform(eqn_poly_2, eqn_poly_1), run_time=1)
        self.play(Indicate(eqn_poly_1, scale_factor=1.05), run_time=1)
        self.wait(3)

        first_graph = VGroup(axes_intro, eqn_poly_1)







        # Create The Coordinate System
        axes = Axes(
            x_range=[-6, 10, 1],
            y_range=[0, 70, 10],

            x_length=8,
            y_length=6,
            tips=False,
            axis_config={'include_numbers': False}
            ).scale(0.8)
        xy_labels = axes.get_axis_labels(
            Tex("x").scale(0.7), Text("y").scale(0.45)
        )
  
        
        # Plot The Curve
        curve = always_redraw(lambda: axes.plot(lambda x: 
            (x - 2)**2, x_range=[-6, 8], color=BLUE, use_smoothing=False))
        equation = MathTex(r"Function", r":", r"f(x) = (x - 2)^2").next_to(axes, UP*2)
        equation[2].set_color(BLUE)
        equation.shift(LEFT*4.3)
        equation.scale(0.6)

        # Replace The Curves and Axes With The Actual, Bigger One (axes)
        second_graph = VGroup(axes, curve)
        self.play(ReplacementTransform(first_graph, second_graph), Write(equation), run_time=2)
        self.add(xy_labels)
        self.wait(2)

        # Shift The Plot To The Left, And Shrick It Abit
        group_1 = VGroup(axes, curve, xy_labels)
        self.play(group_1.animate.shift(LEFT*4).scale(0.75))
        self.wait()

        grad_curve = Text("Gradient Of The Function", font_size=20, font='Book Antiqua').shift(UR*2.5)
        nabla = MathTex(r'\nabla f(x)', color=BLUE).next_to(grad_curve, DOWN)

        group_2 = Group(grad_curve, nabla)

        self.play(Write(grad_curve), Write(nabla), run_time=2)
        self.play(group_2.animate.shift(LEFT * 2.2))
        self.wait()
    
        equal_sign = Tex(r"=").next_to(group_2, RIGHT)
        self.play(FadeIn(equal_sign))
        
        deri = Text("Derivative Of The Function", font_size=20, font='Book Antiqua')
        derivative = MathTex(r'f^\prime(x)', color=BLUE).next_to(deri, DOWN)

        group_3 = Group(deri, derivative).next_to(group_2, RIGHT*3.3)

        self.play(FadeIn(deri), Write(derivative), run_time=2)

        self.wait(4)

        # Tranform Words To Derivative And Its Sign Word
        self.play(TransformMatchingShapes(group_2, deri), FadeOut(equal_sign), FadeOut(derivative), run_time=1)
        self.play(deri.animate.shift(DOWN, LEFT*2))
        self.wait()


        derivative = MathTex(r'f^\prime(x)', r'&=', r"(x - 2)^2", r"\\&= 2(x - 2)", r"\\&= 2x - 4").next_to(deri, DOWN)
        self.play(Write(derivative[0]), run_time=1)
        # self.play(derivative[0].animate.shift(LEFT*1.19))

        equal_sign = derivative[1].next_to(derivative[0], RIGHT)
        self.play(FadeIn(equal_sign))

        equation = derivative[2].next_to(equal_sign, RIGHT)
        self.play(DrawBorderThenFill(equation))

        self.wait(2)

        # Display Calculated Derivative
        function_derivative = derivative[3]
        self.play(DrawBorderThenFill(function_derivative))
        function_derivative_opened = derivative[4]
        self.play(DrawBorderThenFill(function_derivative_opened))


        # Shift The Differenciated Equation Up
        self.play(deri.animate.shift(UP*1.65), derivative.animate.shift(UP*1.9).scale(0.5), run_time=2)


        # Differentiating Using First Principles
        or_word = Text('Or', font_size=20, font='Book Antiqua', color=YELLOW).next_to(derivative, DOWN*1.1)
        self.play(FadeIn(or_word), run_time=1)
        self.wait()

        first_principle_diff_eqn = MathTex(r"\frac{dy}{dx} &= \lim_{\delta x \to 0} \left[ \frac{f(x + \delta x) - f(x)}{\delta x} \right]",
            r"\\&= \lim_{\delta x \to 0} \left[ \frac{(x + \delta x - 2)^2 - (x - 2)^2}{\delta x} \right]",
            r"\\&= \lim_{\delta x \to 0} \left[ \frac{(x + \delta x - 2 - x + 2)(x + \delta x - 2 + x - 2)}{\delta x} \right]",
            r"\\&= \lim_{\delta x \to 0} \left[ \frac{\delta x(2x + \delta x - 4)}{\delta x} \right]",
            r"\\&= \lim_{\delta x \to 0} \left[(2x + \delta x - 4)\right]",
            r"\\&= 2x + 0 - 4",
            r"\\&= 2x - 4").next_to(deri, DOWN*1.4).scale(0.5)
        first_principle_diff_eqn.shift(RIGHT)

        self.play(Write(first_principle_diff_eqn[0]), run_time=2)
        self.wait(3)
    
        self.play(Write(first_principle_diff_eqn[1]), run_time=3)
        self.wait(2)
   
        self.play(Write(first_principle_diff_eqn[2]), run_time=3)
        self.wait(2)


        self.play(Write(first_principle_diff_eqn[3]), run_time=3)
        self.wait(2)
        self.play(Write(first_principle_diff_eqn[4]), run_time=3)
        self.wait(2)
        self.play(Write(first_principle_diff_eqn[5]), run_time=3)
        self.wait(2)
        self.play(Write(first_principle_diff_eqn[6]), run_time=3)
        self.wait(2)



        # Surrounding rectangles
        rect_1 = SurroundingRectangle(derivative[4], color=RED, buff=0.1)
        rect_2 = SurroundingRectangle(first_principle_diff_eqn[6], color=RED, buff=0.1)
        self.play(Create(rect_1), Create(rect_2), run_time=1)
        self.play(FadeOut(rect_1), FadeOut(rect_2), run_time=1)
        self.wait(2)

        derivative_ = MathTex(r"f^\prime(x) = 2x - 4").next_to(deri, DOWN).scale(0.7)

        # Remove The Steps After
        self.play(AnimationGroup(TransformMatchingShapes(derivative, derivative_),
            FadeOut(first_principle_diff_eqn),
            FadeOut(or_word)),
            run_time = 3) 
        self.wait(3)


        # # ###################################################################################
        # # ###################################################################################
        # # ###################################################################################



        # The Tangent To The Curve 2(x - 2)^2
        point = ValueTracker(3)


        tangent = always_redraw(lambda: axes.get_secant_slope_group(
            x = point.get_value(),
            dx = 0.00005,
            graph=curve,
            secant_line_length=4.5,
            secant_line_color=ORANGE
        ))
        self.play(AnimationGroup(FadeOut(derivative_), 
            FadeOut(deri).set_run_time(1)))
        self.wait(4)
        
        # Moving dot between curve and the tangent
        moving_dot = always_redraw(lambda: Dot(color=RED).move_to(axes.c2p(point.get_value(),
            curve.underlying_function(point.get_value()))))

        # Add the dotted line
        # Add the vertical dotted line
        vertical_dashed_line = always_redraw(lambda: DashedLine(
            start=axes.c2p(point.get_value(), 0),  # Start on x-axis
            end=moving_dot.get_center(),  # End at the moving dot
            color=ORANGE
        ))

        self.add(vertical_dashed_line)  # Adding the dotted line to the scene
        self.add(moving_dot)
        self.add(tangent)
        self.wait(3)



        # Derivative Of The Function At A Point, x = -2 {Dummy Example}
        x_value_1 = -2

        at_point = Text(fr'Gradient Of The Function f(x) At Point, x = {x_value_1}', 
            color=PURPLE, font='Book Antiqua', font_size=31).shift(UR*2).scale(0.7)
        self.play(Write(at_point), run_time=2)

        # f^(x) next_to = next_to 2x - 4
        derivative = MathTex(r'f^\prime(x)').next_to(at_point, DOWN*1.7) # f^(x)
        derivative.shift(LEFT)
        self.play(Write(derivative), run_time=1)
        equal_sign = Tex(r"=").next_to(derivative, RIGHT*1.4)
        self.play(Write(equal_sign), run_time=1)
        function_derivative_opened = MathTex("2x - 4", color=ORANGE).next_to(equal_sign, RIGHT) # Opened Brackets
        self.play(Write(function_derivative_opened), run_time=1)

        group_01 = Group(derivative, equal_sign, function_derivative_opened)
    
        # Samething But With value Of x (-2) Substituted In
        # f^(-2) next_to = next_to 2(-2) - 4
        derivative_02 = MathTex(fr'f^\prime({x_value_1})').next_to(at_point, DOWN*1.7)
        derivative_02.shift(LEFT)
        equal_sign_02 = Tex(r"=").next_to(derivative_02, RIGHT*1.4)
        function_derivative_opened_02 = MathTex(fr"2({x_value_1}) - 4", color=ORANGE).next_to(equal_sign_02, RIGHT)

        group_02 = Group(derivative_02, equal_sign_02, function_derivative_opened_02)

        self.wait(2)

        # Transform From Unsubstituted Value To Substituted Value Form (x = -2)
        self.play(TransformMatchingShapes(group_01, group_02), run_time=2)
        # Gradient Answer After Substituting The x Value
        ans = MathTex(fr'{2*x_value_1-4}', color=ORANGE).next_to(equal_sign_02, RIGHT)
        # Transform To The Final Answer Which Is (Gradient f^(x) = -6)
        self.play(Transform(function_derivative_opened_02, ans), run_time=2)
        # Shift The Tangent To Point x = 2 On The Graph
        self.play(point.animate.set_value(-2), run_time=5)
        self.wait(3)


        grad_at_points_word = Text("Gradient At Different Values Of x",
            color=PURPLE, font='Book Antiqua', font_size=31).shift(UR*2)
        # Calculate The Gradient At Different Values Of point.get_value()

        point = ValueTracker(-2)

        equation_01 = always_redraw(lambda:
            MathTex(fr'f^\prime({point.get_value():.2f})')).next_to(grad_at_points_word, DOWN*1.7).shift(LEFT)

        equal_sign_03 = Tex(r"=").next_to(equation_01, RIGHT*1.4)

        gradient = always_redraw(lambda: DecimalNumber(
            axes.slope_of_tangent(x=point.get_value(), graph=curve),
            color=PURE_RED, num_decimal_places=2)).next_to(equal_sign_03, RIGHT*1.4)

        # A group of f^(changing-values), equal_sign(=), and changing calclulated gradient
        group_03 = always_redraw(lambda: VGroup(
        MathTex(fr'f^\prime({point.get_value():.2f})').next_to(grad_at_points_word, DOWN*1.7).shift(LEFT),
        Tex(r"=").next_to(equation_01, RIGHT*1.4),
        DecimalNumber(
            axes.slope_of_tangent(x=point.get_value(), graph=curve), color=ORANGE, num_decimal_places=2
        ).next_to(equal_sign_03, RIGHT*1.4)
        ))
    

        self.play(TransformMatchingShapes(at_point, grad_at_points_word),
                TransformMatchingShapes(group_02, group_03), run_time=2.5)

        # Set To Different Values Of Variable, point
        # While Simultaneously Calculating Their Respective Gradients

        self.play(point.animate.set_value(5),
                rate_func=there_and_back, run_time=15)
        self.wait(3)
        self.play(point.animate.set_value(-5), 
                rate_func=there_and_back, run_time=15)
        self.wait(3)
    

    














        






















