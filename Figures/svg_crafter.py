from manim import *
from manim_mobject_svg import *
from matplotlib.pyplot import disconnect
from numpy import size
from pyrsistent import discard


class Light_Cone(Scene):
    def construct(self):
        Tex.set_default(font_size=20)
        Dot.set_default(radius=0.04)
        Line.set_default(stroke_width = 0.5)
        Line.set_default(color = BLACK)
        Arrow.set_default(color = BLACK)
        Arrow.set_default(stroke_width = 0.5)
        Arrow.set_default(max_tip_length_to_length_ratio=0.1)
        self.camera.background_color = "#CCEFEC"
        
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
        
        
        
        