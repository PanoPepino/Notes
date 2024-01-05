from manim import *
from manim_mobject_svg import *
from manim_theoretical import *




class Class_Cosmo_Notes(Scene):
    def construct(self):
        Tex.set_default(font_size=20)
        Dot.set_default(radius=0.04)
        Line.set_default(stroke_width = 0.5)
        Line.set_default(color = BLACK)
        Arrow.set_default(color = BLACK)
        Arrow.set_default(stroke_width = 0.5)
        Arrow.set_default(max_tip_length_to_length_ratio=0.1)
        self.camera.background_color = "#FFFFFF"
        
        
        # Light cone
        line_1 = Line(start=[-2,0,0], end=[2,0,0]).rotate(PI/4)
        line_2 = line_1.copy().rotate(PI/2)
        event = Dot(color = GREEN_E)
        disconnect_event = Dot(color= DARK_BLUE).move_to([1.2,0.45,0])
        event_text = Tex("Event", color = GREEN_E).next_to(event, LEFT)
        p_text = Tex("P", color = GREEN_E).next_to(event, DOWN)
        #disconnect_text = Tex("disconnected", color = DARK_BLUE).next_to(disconnect_event, RIGHT, buff =0.1)
        q = Tex("Q", color = DARK_BLUE).next_to(disconnect_event, UP, buff =0.1)
        f= Tex("Future Light Cone", color = RED_E).shift(1.1*UP)
        p= Tex("Past Light Cone", color = RED_E).shift(1.1*DOWN)
        arrow_t = Arrow(start = [0,0,0], end = [0,1,0]).next_to(event,UP)
        arrow_x = Arrow(start = [0,0,0], end = [1,0,0]).next_to(event, RIGHT)
        t = Tex("t", color = BLACK).next_to(arrow_t, RIGHT, buff = 0.1)
        x = Tex("x", color = BLACK).next_to(arrow_x, RIGHT, buff = 0.1)
        light_cone = VGroup(line_1,line_2,event, disconnect_event, event_text,p_text, f,p,q, arrow_x, arrow_t ,t, x)
        
        light_cone.to_svg("Svgs/light_cone.svg", crop = False)
        #Observe that I wrote the path to the folder I want this to be crafted at.
        
        # Potential Cosmo
        ax_cosmo= NumberPlane(
                x_range=[0.01, 5, 1],
                y_range=[-3, 1, 1],
                tips=False,
                background_line_style={"stroke_opacity":0}).set_color(BLACK)
        rp = ax_cosmo.coords_to_point(1, 1)
        rpb = ax_cosmo.coords_to_point(1, -3)
        split_regions = ax_cosmo.get_vertical_line(rp, stroke_width = 0.5).set_color(BLACK)
        split_regions_bis = ax_cosmo.get_vertical_line(rpb,stroke_width = 0.5).set_color(BLACK)
        sr = VGroup(split_regions, split_regions_bis)
        sr_2 = sr.copy().shift(2*RIGHT)
        lab_ax_q_cosmo = ax_cosmo.get_axis_labels(x_label=Tex("a",font_size=25, color = BLACK), y_label=Tex("V(a)",font_size=25, color = BLACK))
        regions= MathTex("A", "B", "C", font_size=30, color = BLACK)
        regions[0].move_to(ax_cosmo.coords_to_point(0.5, 0.5)).set(color = RED_E)
        regions[1].move_to(ax_cosmo.coords_to_point(2, 0.5)).set(color = GREEN_E)
        regions[-1].move_to(ax_cosmo.coords_to_point(4, 0.5))

        #Potential
        pot_q_cosmo = ax_cosmo.plot(
                    lambda x: -(0.05/x + 0.5/x**2 + 0.1* x**2) ,
                    color=DARK_BLUE,
                    x_range=[0.42,5.1],
                    stroke_width=2,
                    use_smoothing=True)
        
        pot= VGroup(ax_cosmo, pot_q_cosmo, lab_ax_q_cosmo, sr,sr_2, regions)
        pot.to_svg("Svgs/classical_cosmo_pot.svg", crop = False)
        
        # Density distribution
        
class Dark_Bubbles(Scene):
    def construct(self):
        Tex.set_default(font_size=20)
        Text.set_default(color=BLACK)
        Tex.set_default(color=BLACK)
        MathTex.set_default(color = BLACK)
        Dot.set_default(radius=0.04)
        Line.set_default(stroke_width = 0.5)
        Line.set_default(color = BLACK)
        #Arrow.set_default(color = BLACK)
        #Arrow.set_default(stroke_width = 0.5)
        #Arrow.set_default(max_tip_length_to_length_ratio=0.1)
        self.camera.background_color = "#FFFFFF"  

        bub_1 = Bubble(color = "#9b0508")[2:]
        bub_2 = Bubble(color = "#9b0508")
        bub_2[0].scale(2)
        bub_2[1].scale(1.5)
        bub_1[-1].scale(1.5)
        bub_2[-1].scale(1.5)
    

        ar = Arrow(max_tip_length_to_length_ratio=1, color= BLACK, start = LEFT, end= [0.3,0,0], stroke_color = "#9b0508")
        all = VGroup(bub_1, ar, bub_2).arrange(RIGHT, buff = 0.5).scale(0.8)
        self.add(all)
        all.to_svg("Svgs/bubble_nuc.svg", crop = True)
        
        
        
        
        
        