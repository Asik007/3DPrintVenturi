from manim import *
import numpy as np

class VenturiTubeBernoulli(Scene):
    def construct(self):
        # Create the Venturi tube shape
        # Create the Venturi tube using polygons
        wide_left = Polygon([-4, 1, 0], [-4, -1, 0], [-2, -0.5, 0], [-2, 0.5, 0]).set_color(WHITE)
        narrow_middle = Polygon([-2, 0.5, 0], [-2, -0.5, 0], [2, -0.5, 0], [2, 0.5, 0]).set_color(WHITE)
        wide_right = Polygon([2, 0.5, 0], [2, -0.5, 0], [4, -1, 0], [4, 1, 0]).set_color(WHITE)

        venturi_tube = VGroup(wide_left, narrow_middle, wide_right)

        # Show the Venturi tube
        self.play(FadeIn(venturi_tube))

        # Labels for pressure and velocity at wide and narrow sections
        P1 = MathTex("P_1").move_to(venturi_tube.get_left() + UP * 0.5)
        v1 = MathTex("v_1").move_to(venturi_tube.get_left() + DOWN * 0.5)
        P2 = MathTex("P_2").move_to(venturi_tube.get_right() + UP * 0.5)
        v2 = MathTex("v_2").move_to(venturi_tube.get_right() + DOWN * 0.5)
        
        # Show the labels for the first part
        self.play(Write(P1), Write(v1), Write(P2), Write(v2))

        # Create arrows for fluid flow
        flow_arrows_wide = VGroup(*[Arrow(start=venturi_tube.get_left() + RIGHT * i * 0.2, 
                                          end=venturi_tube.get_left() + RIGHT * (i * 0.2 + 0.1), 
                                          buff=0, stroke_width=4).set_color(BLUE) 
                                    for i in range(5)])
        
        flow_arrows_narrow = VGroup(*[Arrow(start=venturi_tube.get_right() + LEFT * i * 0.2, 
                                            end=venturi_tube.get_right() + LEFT * (i * 0.2 + 0.1), 
                                            buff=0, stroke_width=4).set_color(BLUE) 
                                      for i in range(8)])
        
        # Animate fluid flow at wide section
        self.play(LaggedStartMap(GrowArrow, flow_arrows_wide, lag_ratio=0.1))

        # Animate fluid flow at narrow section
        self.play(LaggedStartMap(GrowArrow, flow_arrows_narrow, lag_ratio=0.05))

        # Bernoulli's equation
        bernoulli_eq = MathTex(
            "P_1", "+", r"\frac{1}{2} \rho v_1^2", "=", "P_2", "+", r"\frac{1}{2} \rho v_2^2"
        ).to_edge(UP)
        
        self.play(Write(bernoulli_eq))
        
        # Highlight pressure and velocity difference
        self.play(Indicate(P1), Indicate(v1), Indicate(P2), Indicate(v2))

        # Emphasize velocity increase in the narrow section
        v_increase = MathTex("v_2 > v_1").next_to(venturi_tube, DOWN)
        self.play(Write(v_increase))
        
        # Emphasize pressure drop in the narrow section
        p_drop = MathTex("P_2 < P_1").next_to(v_increase, DOWN)
        self.play(Write(p_drop))

        # Fade out everything at the end
        self.play(FadeOut(VGroup(venturi_tube, P1, v1, P2, v2, flow_arrows_wide, flow_arrows_narrow, bernoulli_eq, v_increase, p_drop)))

# Run the scene using Manim
