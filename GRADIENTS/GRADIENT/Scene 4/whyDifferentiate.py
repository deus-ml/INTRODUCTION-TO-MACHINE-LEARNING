from manim import *

class WhyDiff(Scene):
    def construct(self):
        # Function Defined by Equation
        func_definition = MathTex(r"f(x) := 0.1x^3 - 1.4x^2 + 5.9x", color=YELLOW).scale(0.7)
        func_definition.shift(UP*3.2)

        
        axes = Axes(
            x_range=[0, 10, 1],
            x_length=9,
            y_range=[0, 20, 5],
            y_length=6,
            tips=False,
            axis_config={'include_numbers': False}
        ).scale(0.7)
        xy_labels = axes.get_axis_labels(
            Tex("x").scale(0.7), Text("y").scale(0.45)
        )
        self.play(Write(axes), run_time=2)
        self.add(xy_labels)

        # Graph
        graph = axes.plot(lambda x: 0.1 * (x-2) * (x-5) * (x-7) + 7 , x_range=[0, 10], color=BLUE)
        self.play(Write(graph), DrawBorderThenFill(func_definition), run_time=3)

        # Dynamic Values
        x = ValueTracker(7)
        dx = ValueTracker(2.5)

        # The secant
        secant = always_redraw(lambda: axes.get_secant_slope_group(
            x = x.get_value(),
            dx = dx.get_value(),
            graph=graph,
            secant_line_length=6,
            secant_line_color=RED,
            dx_line_color=YELLOW,
            dy_line_color=YELLOW,
            dx_label='\delta x',
            dy_label='\delta y'
        ))
        dot_1 = always_redraw(
            lambda: Dot().move_to(axes.c2p(x.get_value(), 
            graph.underlying_function(x.get_value())))
        )
        label_1 = MathTex(r'f(x_0)').next_to(dot_1, LEFT*0.3+UP).scale(0.5)
        label_1.shift(RIGHT*0.2)
        
        dot_2 = always_redraw(
            lambda: Dot().move_to(axes.c2p(x.get_value() + dx.get_value(),
            graph.underlying_function(x.get_value() + dx.get_value())))
        )
        label_2 = always_redraw(lambda: MathTex(r'f(x_0 + \delta x)').next_to(dot_2.get_center(), RIGHT*0.3).scale(0.5))


        x0 = MathTex(r"x_0").next_to(axes.c2p(7, 0), DOWN).scale(0.4)
        x1 = MathTex(r"x_0 + \delta x").next_to(axes.c2p(9.5, 0), DOWN).scale(0.4)

        line_1 = axes.get_vertical_line(dot_1.get_center(), line_config={"dashed_ratio": 0.5}, color=YELLOW)
        line_2 = always_redraw(lambda: axes.get_vertical_line(dot_2.get_center(), line_config={"dashed_ratio": 0.5}, color=YELLOW))
    
        self.play(Write(secant), FadeIn(dot_1), FadeIn(dot_2), FadeIn(x0), FadeIn(x1), FadeIn(line_1), FadeIn(line_2), run_time=3)
        self.play(Write(label_1), Write(label_2), run_time=2)
        
        self.wait(3)


        ###################################################################
        ###################################################################
        group_1 = VGroup(axes, xy_labels, graph, secant, dot_1, dot_2, label_1, label_2, line_1, line_2, x0, x1, func_definition)
        self.play(group_1.animate.shift(RIGHT*2))

        gradient = MathTex(r'\frac{\delta y}{\delta x} &:= \frac{f(x_0 + \delta x) - f(x_0)}{x_0 + \delta x - x_0}',
            r'\\ \\ &= \frac{f(x_0 + \delta x) - f(x_0)}{\delta x}').scale(0.6)
    
        gradient.next_to(group_1, LEFT*5)
        gradient[1].set_color(BLUE)

        self.play(Write(gradient[0]), run_time=2)
        self.play(Write(gradient[1]), run_time=2)
        
        self.wait(3)

        self.play(Indicate(dot_1, scale_factor=1.5), run_time=2)
        
        self.wait(3)

        self.play(gradient.animate.shift(UP*1.5), run_time=2)
        
        self.wait(3)    

        # The Limit Concept
        lim_concept = MathTex(r'limit:',  r'\lim_{\delta x \to 0}').next_to(gradient, DOWN*2)
        lim_concept.shift(DOWN)
        lim_concept[1].set_color(YELLOW)
        self.play(DrawBorderThenFill(lim_concept), run_time=2)

        self.wait(3)    

        # # Draw Rectangle On The Limit As Small Change In x tends To Zero
        # rect_1 = SurroundingRectangle(lim_concept[1], color=RED, buff=0.1)
        # self.play(Create(rect_1), run_time=1)
        # self.play(FadeOut(rect_1), run_time=1)

        # self.wait(3)    

        # FadeOut The Labels On The X_axis
        self.play(FadeOut(x0), FadeOut(x1), run_time=2)

        # Draw A Brace On The X-axis
        dot = always_redraw(
            lambda: Dot().move_to(axes.c2p(x.get_value() + dx.get_value()))
        )

        brace_x = always_redraw(lambda: BraceBetweenPoints(dot_1.get_center(), dot.get_center(), direction=DOWN))
        
        # Dynamic Brace Values
        brace_x_value = always_redraw(
            lambda: brace_x.get_text(
                fr"$\delta x$ = {round(dx.get_value(), 5)}"
            )
        )


        self.play(GrowFromCenter(brace_x), run_time=2)
        self.add(dot)
        self.add(brace_x_value)
        self.play(Indicate(lim_concept[1], scale_factor=1.5), run_time=2)
        self.play(dx.animate.set_value(0.0001), run_time=8)
        
        
        # transform Into A Derivative Of A Function
        diff_eqn = MathTex(r"\frac{dy}{dx} &:= ", r"\lim_{\delta x \to 0}", r"\left[ \frac{f(x + \delta x) - f(x)}{\delta x} \right]").next_to(gradient[0], DOWN)
        diff_eqn.set_color(BLUE)
        diff_eqn[1].set_color(YELLOW)
        diff_eqn.scale(0.6)
        group_2 = VGroup(gradient[1], lim_concept[1])
        self.play(TransformMatchingShapes(group_2, diff_eqn), FadeOut(lim_concept[0]), run_time=2)

        brace = Brace(diff_eqn, direction=DOWN, color=ORANGE)
        brace_label = Text(r"Definition Of A Derivative").next_to(brace, DOWN).scale(0.5)
        self.play(FadeIn(brace), FadeIn(brace_label), run_time=2)

        self.wait()


        # So this becomes the gradient of arbitrary function at point x_0
        # And this secant becomes a tangent at point x_0
        x0 = always_redraw(lambda: MathTex(r"x_0", color=YELLOW).next_to(axes.c2p(x.get_value(), 0), DOWN).scale(0.5))
        self.play(FadeIn(x0))

        intuition = MathTex(r"f'(x_0) = 0.3x_0^2 - 2.8x_0 + 5.9", color=YELLOW).scale(0.7).next_to(axes, UP*2)
        intuition.shift(UP*0.4)
        self.play(TransformMatchingShapes(func_definition, intuition), FadeOut(brace_x_value), FadeOut(label_1), FadeOut(label_2), run_time=3)
        self.wait(2)
    
        self.remove(line_1)
        self.remove(brace_x)
        self.play(x.animate.set_value(9.5), run_time=5)
        self.wait()
        self.play(x.animate.set_value(0.5), run_time=5)
        self.wait()
        self.play(x.animate.set_value(7), run_time=5)
        self.wait()






        



