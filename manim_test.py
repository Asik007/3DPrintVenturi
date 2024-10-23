from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class VenturiTubeBernoulli(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        width = 100
        self.camera.frame_width = width  # width of the frame
        self.camera.frame_height = (9/16) * width # height of the frame

        text_fmt = {"font_size": 72, "color": BLUE}

        # Create the Venturi tube shape
        # Create the Venturi tube using polygons
        # Define variables for the dimensions of the Venturi tube
        wide_section_length = 30
        narrow_section_length = 20
        wide_section_height = 5
        narrow_section_height = 2.5
        total_length = 100

        middle_1 = [(-total_length / 2) + (wide_section_length / 2), (wide_section_height / 2) + 5, 0]
        middle_2 = [0, (narrow_section_height / 2) + 5, 0]
        middle_3 = [(total_length / 2) - (wide_section_length / 2), (wide_section_height / 2) + 5, 0]

        middle_1_bot = [(-total_length / 2) + (wide_section_length / 2), -(wide_section_height / 2) - 5, 0]
        middle_2_bot = [0, -(narrow_section_height / 2) - 5, 0]
        middle_3_bot = [(total_length / 2) - (wide_section_length / 2), -(wide_section_height / 2) - 5, 0]



        # Create the Venturi tube using polygons
        tube = Polygon(
            [-total_length/2, wide_section_height, 0],
            [-total_length/2 + wide_section_length, wide_section_height, 0],
            [-total_length/2 + wide_section_length + narrow_section_length/2, narrow_section_height, 0],
            [total_length/2 - wide_section_length - narrow_section_length/2, narrow_section_height, 0], 
            [total_length/2 - wide_section_length, wide_section_height, 0],
            [total_length/2, wide_section_height, 0],
            [total_length/2, -wide_section_height, 0],
            [total_length/2 - wide_section_length, -wide_section_height, 0],
            [total_length/2 - wide_section_length - narrow_section_length/2, -narrow_section_height, 0],
            [-total_length/2 + wide_section_length + narrow_section_length/2, -narrow_section_height, 0],
            [-total_length/2 + wide_section_length, -wide_section_height, 0],
            [-total_length/2, -wide_section_height, 0],
        ).set_color(WHITE).set_stroke(width=10)

        # Show the Venturi tube
        Title = Text("Venturimeter", font_size=256).move_to([0,20,0])
        
        image = ImageMobject("Venturi.png")
        image.scale(5)


        with self.voiceover(text="Hello! Today, we’ll be exploring how a Venturimeter works.") as track:
            self.play(Write(Title), FadeIn(image))
            self.wait(2)
            self.play(FadeOut(image))

        

        self.wait(.2)
        self.play(Write(tube), run_time=4)
        
        # Labels for pressure and velocity at wide and narrow sections
        Q1 = MathTex("\dot{Q}_{In}").move_to(middle_1)
        Q2 = MathTex("\dot{Q}_{Middle}").move_to(middle_2)
        Q3 = MathTex("\dot{Q}_{Out}").move_to(middle_3)
        Qin1 = MathTex("\dot{Q}_{In}").move_to(middle_1)
        Qout = MathTex("\dot{Q}_{Out}").move_to(middle_3)
        ConvMass = Text("Conservation of Mass", font_size=256).move_to([0,20,0])
        BernEq = Text("Bernoulli's Equation", font_size=256).move_to([0,20,0])
        Takeaway = Text("Takeaways", font_size=256).move_to([0,20,0])
        V_take = MathTex(r"v_{Middle} \geq v_{In}").move_to(UP * 15).scale(8)
        P_take = MathTex(r"P_{Middle} \leq P_{In}").move_to(UP * 15).scale(8)
        
        BernoulliEquation = MathTex(r"P_{In} + \frac{1}{2} \rho v_{In}^2 +",r"\rho gh_{In}",r"=",r"P_{mid} + \frac{1}{2} \rho v_{Middle}^2 + ",r"\rho gh_{Middle}").move_to(DOWN * 0)
        Av1 = MathTex("A_{In}v_{In}").move_to(middle_1_bot)
        Av2 = MathTex("A_{Middle}v_{Middle}").move_to(middle_2_bot)
        Av3 = MathTex("A_{Out}v_{Out}").move_to(middle_3_bot)
        Qin = MathTex("\dot{Q}_{In} = \dot{Q}_{Out}").move_to(DOWN * 10)
        Qeq = MathTex(r"\dot{Q}_{In}"," = ",r"\dot{Q}_{Middle}"," = ",r"\dot{Q}_{Out}").move_to(DOWN * 17.5)
        Aveq = MathTex(r"A_{In}v_{In}"," = ",r"A_{Middle}v_{Middle}"," = ",r"A_{Out}v_{Out}").move_to(DOWN * 15)
        Ain = MathTex(r"A_{In}", r"= \pi \left(\frac{d_{In}}{2}\right)^2").move_to(DOWN * 15 + LEFT * 20)
        Amid = MathTex(r"A_{Middle}", r"= \pi \left(\frac{d_{Middle}}{2}\right)^2").move_to(DOWN * 15 + RIGHT * 20)
        Ain_solve = MathTex(r"A_{In}", r"= 0.00025\pi m^2").move_to(DOWN * 15 + LEFT * 20)
        Amid_solve = MathTex(r"A_{Middle}", r"= 0.00000625\pi m^2").move_to(DOWN * 15 + RIGHT * 20)
        Vin = MathTex(r"v_{In}", "=", r"\frac{\dot{Q}_{In}}{A_{In}}").move_to(DOWN * 17.5 + LEFT * 20)
        Vmid = MathTex(r"v_{Middle}", "=", r"\frac{\dot{Q}_{In}}{A_{Middle}}").move_to(DOWN * 17.5 + RIGHT * 20)
        Vin2 = MathTex(r"v_{In}", "=", r"\frac{\dot{Q}_{In}}{0.00025\pi} m^2").move_to(DOWN * 17.5 + LEFT * 20)
        Vmid2 = MathTex(r"v_{Middle}", "=", r"\frac{\dot{Q}_{In}}{0.00000625\pi} m^2}").move_to(DOWN * 17.5 + RIGHT * 20)
        rho = MathTex(r"\rho = 1000 \frac{kg}{L}").move_to(DOWN * 17.5 + LEFT * 20)
        Q_in = MathTex(r"\dot{Q}_{In} = 0.00025 \frac{L}{min}").move_to(DOWN * 17.5 + RIGHT * 20)

        # Ain_solve = MathTex("").move_to(DOWN * 15 + LEFT * 20)


        Din = Line([-total_length/2 + wide_section_length, wide_section_height, 0],
                   [-total_length/2 + wide_section_length, -wide_section_height, 0],
                   )
        Dmid = Line(
            [total_length/2 - wide_section_length - narrow_section_length/2, narrow_section_height, 0],
            [total_length/2 - wide_section_length - narrow_section_length/2, -narrow_section_height, 0],
            )
        
        Dout = Line(
            [total_length/2 - wide_section_length, wide_section_height, 0],
            [total_length/2 - wide_section_length, -wide_section_height, 0],
            )
        Din_brace = Brace(Din,[1,0,0], stroke_width=25, sharpness=1)
        Din_text = Text(".01m").next_to(Din_brace, RIGHT*15)
        Din_text.scale(5)
        Dmid_brace = Brace(Dmid, [1,0,0], stroke_width=25, sharpness=1)
        Dmid_text = Text(".005m").next_to(Dmid_brace, RIGHT*17)
        Dmid_text.scale(5)

        # Dout_brace = Brace(Dout, [1,0,0], stroke_width=100)

        ArrowIn = VGroup(*[Arrow(start=[-50, 4 - i, 0], 
                                  end=[-20, 4 - i, 0], 
                                  buff=1, stroke_width=10).set_color(BLUE) 
                            for i in range(9)])
        ArrowOut = VGroup(*[Arrow(start=[20, 4 - i, 0], 
                                  end=[50, 4 - i, 0], 
                                  buff=1, stroke_width=10).set_color(BLUE) 
                            for i in range(9)])
        ArrowMid = VGroup(*[Arrow(start=[-narrow_section_length / 2, 2 - i, 0], 
                                  end=[narrow_section_length / 2, 2 - i, 0], 
                                  buff=1, stroke_width=10).set_color(BLUE) 
                            for i in range(5)])

        Q1.scale(8)
        rho.scale(8)
        Q_in.scale(8)
        BernoulliEquation.scale(8)
        ConvMass.scale(1)
        Qin1.scale(8)
        Qout.scale(8)

        Ain.scale(8)
        Vin.scale(8)
        Vin[0].set_color(RED)
        Vin2.scale(8)
        Vin2[0].set_color(RED)
        Ain[0].set_color(RED)
        Ain_solve.scale(8)
        Ain_solve[0].set_color(RED)
        Av1.scale(8)
        Q1.set_color(RED)
        Av1.set_color(RED)
        Qeq[0].set_color(RED)
        Aveq[0].set_color(RED)

        Q2.scale(8)
        Av2.scale(8)

        Amid.scale(8)
        Amid[0].set_color(BLUE)
        Vmid2.scale(8)
        Vmid2[0].set_color(BLUE)
        Amid_solve.scale(8)
        Amid_solve[0].set_color(BLUE)
        Vmid.scale(8)
        Vmid[0].set_color(BLUE)
        
        Q2.set_color(BLUE)
        Av2.set_color(BLUE)
        Qeq[2].set_color(BLUE)
        Aveq[2].set_color(BLUE)

        Q3.scale(8)
        Av3.scale(8)

        Q3.set_color(GREEN)
        Av3.set_color(GREEN)
        Qeq[4].set_color(GREEN)
        Aveq[4].set_color(GREEN)
        Qin.scale(8)
        Aveq.scale(10)
        Qeq.scale(10)
        Qeq2 = Qeq.copy()




        self.play(*[GrowArrow(arrow) for arrow in ArrowIn], duration=1.5)
        self.wait(.5)
        self.play(Write(Qin1), duration=.75)
        self.play(*[GrowArrow(arrow) for arrow in ArrowOut], duration = 1.5)
        self.wait(.5)
        self.play(Write(Qout), duration=.75)
        self.wait()
        self.play(
            Transform(Qin1, Qin),
            Transform(Qout, Qin), FadeOut(Title)
            )

        self.wait(1)
        self.play(Write(ConvMass))
        self.wait(1)
        self.play(*[GrowArrow(arrow) for arrow in ArrowMid])
        

        # Show the labels for the first part

        self.wait(1)
        self.play(Transform(Qin,Qeq), FadeOut(Qin1), FadeOut(Qout))


        self.wait(1)
        self.play(
            Transform(Qeq[0], Q1),
            Transform(Qeq[1], Q2),
            Transform(Qeq[2], Q3),
            FadeOut(Qin)
            )
        
        self.wait(1)
        self.play(
            Transform(Q1,Av1),
            Transform(Q2,Av2),
            Transform(Q3,Av3),
        )

        self.wait(1)
        self.play(
            Transform(Av1, Aveq),
            Transform(Av2, Aveq),
            Transform(Av3, Aveq),
            Write(Din_brace),Write(Din_text),
            Write(Dmid_brace),Write(Dmid_text),
            # Write(Dout_brace),
        )
        self.wait(1)
        self.play(
            FadeOut(Av1),
            FadeOut(Av2),
            FadeOut(Av3),
        )

        self.wait(1)
        self.play(Write(Ain), Write(Amid))
        self.wait(1)
        self.play(Transform(Ain, Ain_solve),Transform(Amid, Amid_solve))
        self.wait(1)
        self.play(Ain.animate.shift(27.5*UP), Amid.animate.shift(27.5*UP))
        self.wait(1)
        self.play(FadeIn(Qeq2))
        self.wait(1)
        self.play(Transform(Qeq2[0],Vin), Transform(Qeq2[2],Vmid), 
                  FadeOut(Qeq2[1]), FadeOut(Qeq2[3]), FadeOut(Qeq2[4]))
        self.wait(1)
        self.play(FadeOut(Qeq2[0]),FadeOut(Qeq2[2]),Transform(Ain, Vin2),Transform(Amid, Vmid2))
        self.wait(1)
        self.play(Write(V_take))
        self.wait(1)
        self.play(FadeOut(V_take), FadeOut(tube),FadeOut(Din_brace), FadeOut(Dmid_brace),
                  FadeOut(Din_text), FadeOut(Dmid_text), 
                  FadeOut(ArrowIn),FadeOut(ArrowMid),FadeOut(ArrowOut),
                  FadeOut(Qeq),FadeOut(ConvMass), FadeOut(Q1), FadeOut(Q2), FadeOut(Q3))
        self.wait(1)
        self.play(Write(BernEq), Write(BernoulliEquation))
        
        line_b = Line(BernoulliEquation[1].get_left() + UP * 0.1, BernoulliEquation[1].get_right() + DOWN * 0.1, color=RED)
        line_b.set_stroke(10)
        line_d = Line(BernoulliEquation[4].get_left() + UP * 0.1, BernoulliEquation[4].get_right() + DOWN * 0.1, color=RED)
        line_d.set_stroke(10)
        self.wait(1)
        self.play(Create(line_b), Create(line_d))
        self.wait(1)
        self.play(FadeOut(BernoulliEquation[1]), FadeOut(BernoulliEquation[4]))
        BernoulliEquation2 = MathTex(r"P_{In} + \frac{1}{2} \rho v_{In}^2 = P_{Middle} + \frac{1}{2} \rho v_{Middle}^2 ").move_to(DOWN * 0).scale(8)
        BernoulliEquation3 = MathTex(r"P_{In} - P_{Middle}  = \frac{1}{2} \rho v_{Middle}^2 - \frac{1}{2} \rho v_{In}^2 ").move_to(DOWN * 0).scale(8)
        BernoulliEquation4 = MathTex(r"P_{In} - P_{Middle}  = \frac{1}{2} \rho (v_{Middle}^2 - v_{In}^2 )").move_to(DOWN * 0).scale(8)
        BernoulliEquation5 = MathTex(r"\Delta  P= \frac{1}{2} \rho (v_{Middle}^2 - v_{In}^2 )").move_to(DOWN * 0).scale(8)
        BernoulliEquation6 = MathTex(r"\Delta  P= \frac{1}{2} \rho ((\frac{\dot{Q}_{In}}{0.00025\pi})^2 - (\frac{\dot{Q}_{In}}{0.00000625\pi})^2)").move_to(DOWN * 0).scale(8)
        BernoulliEquation7 = MathTex(r"\Delta P = \frac{1}{2} 1000 ((\frac{.00025}{0.00025\pi})^2 - (\frac{.00025}{0.00000625\pi})^2)").move_to(DOWN * 0).scale(8)
        BernFin = MathTex(r"\Delta P = \frac{1}{2} 1000 ((\frac{.00025}{0.00025\pi})^2 - (\frac{.00025}{0.00000625\pi})^2)").move_to(DOWN * 0).scale(8)
        sol = MathTex(r"\Delta P  = 21.11 Pa").move_to(DOWN * 0).scale(8)
        
        self.wait(1)
        self.play(FadeOut(BernoulliEquation[0]),FadeOut(BernoulliEquation[2]),FadeOut(BernoulliEquation[3]), FadeIn(BernoulliEquation2))
        self.wait(1)
        self.play(FadeOut(BernoulliEquation2), FadeIn(BernoulliEquation3))
        self.wait(1)
        self.play(FadeOut(BernoulliEquation3), FadeIn(BernoulliEquation4))
        self.wait(1)
        self.play(FadeOut(BernoulliEquation4), FadeIn(BernoulliEquation5))
        self.wait(1)
        self.play(Write(P_take))
        self.wait(1)
        self.play(FadeOut(P_take),FadeOut(BernoulliEquation5), FadeIn(BernoulliEquation6),FadeOut(Ain),FadeOut(Amid))
        self.wait(1)
        self.play(FadeIn(rho),FadeIn(Q_in))
        self.wait(1)
        self.play(FadeOut(BernoulliEquation6), FadeIn(BernFin))
        self.wait(1)
        self.play(FadeOut(BernFin), FadeIn(sol), FadeOut(rho), FadeOut(Q_in))
        self.wait(1)
        P_take = MathTex(r"P_{Middle} \leq P_{In}").move_to(DOWN * 15).scale(8)
        self.play(FadeOut(BernEq),
                   FadeIn(Takeaway), FadeIn(P_take), FadeIn(V_take)) 
        
        h_diff = MathTex(r"\Delta h = \frac{\Delta P}{g \cdot \rho}").move_to(DOWN * 0).scale(8)
        h_diff2 = MathTex(r"\Delta h = \frac{21.11}{9.81 \cdot 1000}").move_to(DOWN * 0).scale(8)
        h_diff3 = MathTex(r"\Delta h = 0.0021517 \, \text{m}").move_to(DOWN * 0).scale(8)
        grav = MathTex(r"g = 9.81 \frac{m}{s^2}").move_to(DOWN * 17.5 + RIGHT * 20).scale(8)
        self.wait(1)
        self.play(FadeOut(P_take), FadeOut(V_take))
        self.wait(1)
        self.play(FadeIn(grav), FadeIn(rho), sol.animate.shift(DOWN * 15), FadeIn(h_diff))
        self.wait(1)
        self.play(FadeIn(h_diff2), FadeOut(h_diff))
        self.wait(1)
        self.play(FadeIn(h_diff3), FadeOut(h_diff2))