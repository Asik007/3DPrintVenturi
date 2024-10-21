from manim import *


class VenturiTubeBernoulli3D(ThreeDScene):
    def construct(self):
        # Set up the 3D axes and camera
        self.set_camera_orientation(phi=60 * DEGREES, theta=45 * DEGREES)
        axes = ThreeDAxes()

        # Define the Venturi tube shape using parametric surfaces
        def venturi_tube(u, v):
            radius = 0.5 + 0.5 * (1 - np.abs(u))  # Radius decreases towards the center
            x = u * 4  # Length along the tube
            y = radius * np.cos(v * TAU)
            z = radius * np.sin(v * TAU)
            return np.array([x, y, z])

        # Create the Venturi tube surface
        tube = Surface(
            venturi_tube,
            u_range=[-1, 1],  # u determines the length (from -1 to 1)
            v_range=[0, 1],  # v determines the circular shape
            resolution=(30, 30),
        ).set_color(WHITE).set_opacity(0.6)

        # Fluid flow arrows in the wide section (left)
        arrows_wide = VGroup(
            *[Arrow3D(start=[-3.5, 0, 0], end=[-1.5, 0, 0], color=BLUE, stroke_width=2).shift(UP * i)
              for i in np.linspace(-0.6, 0.6, 4)]
        )

        # Fluid flow arrows in the narrow section (middle)
        arrows_narrow = VGroup(
            *[Arrow3D(start=[1.5, 0, 0], end=[3.5, 0, 0], color=BLUE, stroke_width=2).shift(UP * i)
              for i in np.linspace(-0.3, 0.3, 4)]
        )

        # Add the objects to the scene
        self.add(axes, tube)
        self.play(Create(tube))

        # Animate fluid flow in the wide and narrow sections
        self.play(LaggedStartMap(GrowArrow, arrows_wide, lag_ratio=0.1))
        self.play(LaggedStartMap(GrowArrow, arrows_narrow, lag_ratio=0.1))

        # Add labels for velocity and pressure
        v1_label = MathTex("v_1").move_to([-3.5, 1.5, 0])
        P1_label = MathTex("P_1").move_to([-3.5, -1.5, 0])
        v2_label = MathTex("v_2").move_to([3.5, 1.5, 0])
        P2_label = MathTex("P_2").move_to([3.5, -1.5, 0])

        self.play(Write(v1_label), Write(P1_label), Write(v2_label), Write(P2_label))

        # Show Bernoulli's equation
        bernoulli_eq = MathTex(
            "P_1", "+", r"\frac{1}{2} \rho v_1^2", "=", "P_2", "+", r"\frac{1}{2} \rho v_2^2"
        ).to_edge(UP)

        self.play(Write(bernoulli_eq))

        # Highlight the increase in velocity and decrease in pressure
        velocity_increase = MathTex("v_2 > v_1").next_to(v2_label, DOWN)
        pressure_decrease = MathTex("P_2 < P_1").next_to(P2_label, DOWN)

        self.play(Write(velocity_increase), Write(pressure_decrease))

        # End the animation
        self.wait(2)