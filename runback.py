from manim import *

class VelocityThroughPipe(Scene):
    def construct(self):
        # Create the pipe structure
        pipe_left = Rectangle(width=1, height=4, color=BLUE).shift(LEFT * 3)
        pipe_middle = Rectangle(width=0.5, height=3, color=BLUE)
        pipe_right = Rectangle(width=0.25, height=2, color=BLUE).shift(RIGHT * 3)

        # Draw the pipes
        self.play(Create(pipe_left), Create(pipe_middle), Create(pipe_right))

        # Function to generate particle arrows with given positions and velocities
        def create_particle(position, velocity, color=YELLOW):
            arrow = Arrow(position, position + velocity, buff=0, color=color)
            return arrow

        # Left pipe particles (low velocity)
        particles_left = VGroup(
            create_particle(LEFT * 3 + UP * 1.5, RIGHT * 0.75),
            create_particle(LEFT * 3, RIGHT * 0.75),
            create_particle(LEFT * 3 + DOWN * 1.5, RIGHT * 0.75)
        )

        # Middle pipe particles (medium velocity)
        particles_middle = VGroup(
            create_particle(UP * 1.25, RIGHT * 1.5),
            create_particle(DOWN * 1.25, RIGHT * 1.5)
        )

        # Right pipe particles (high velocity)
        particles_right = VGroup(
            create_particle(RIGHT * 3 + UP * 1, RIGHT * 2.25),
            create_particle(RIGHT * 3 + DOWN * 1, RIGHT * 2.25)
        )

        # Animate particles entering and increasing in velocity
        self.play(FadeIn(particles_left))
        self.wait(1)
        self.play(Transform(particles_left, particles_middle.shift(RIGHT * 3)))
        self.wait(1)
        self.play(Transform(particles_left, particles_right.shift(RIGHT * 6)))
        self.wait(1)

        # Display labels for velocity changes
        velocity_label_low = Text("Low Velocity", color=YELLOW).scale(0.5).next_to(pipe_left, UP)
        velocity_label_medium = Text("Medium Velocity", color=YELLOW).scale(0.5).next_to(pipe_middle, UP)
        velocity_label_high = Text("High Velocity", color=YELLOW).scale(0.5).next_to(pipe_right, UP)

        self.play(Write(velocity_label_low))
        self.wait(1)
        self.play(Write(velocity_label_medium))
        self.wait(1)
        self.play(Write(velocity_label_high))
        self.wait(1)

        # End the animation
        self.wait(2)
