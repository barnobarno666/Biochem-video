from manim import *

class PersonalisedMedicineScenegemini(Scene):
    def construct(self):
        # Heading
        heading = Text("Personalised Medicine", font_size=48).to_edge(UP)
        self.play(Write(heading))
        
        # Add underline to heading
        underline = Line(start=LEFT, end=RIGHT, color=WHITE).next_to(heading, DOWN, buff=0.1)
        underline.set_width(heading.width)
        self.play(Create(underline))        # Video/Animation on the left - positioned lower
        try:
            # Option 1: If you have video frames as images, you can animate through them
            # For now, I'll create an animated rectangle that simulates video content
            video_frame = Rectangle(height=3, width=4.5, color=BLUE, fill_opacity=0.7)
            video_frame.to_edge(LEFT, buff=1)
            video_frame.shift(DOWN * 0.5)
            
            # Add some animated elements to simulate video content
            dna_helix = Circle(radius=0.5, color=GREEN).move_to(video_frame.get_center())
            pulse_circle = Circle(radius=0.3, color=YELLOW, fill_opacity=0.3).move_to(video_frame.get_center())
            
            # Create video-like animation
            self.play(FadeIn(video_frame))
            self.play(FadeIn(dna_helix), FadeIn(pulse_circle))
            
            # Animate the elements to simulate video content
            self.play(
                Rotate(dna_helix, angle=2*PI, run_time=3),
                pulse_circle.animate.scale(2).set_opacity(0),
                run_time=3
            )
            
        except Exception as e:
            print(f"Video simulation failed: {e}. Using a placeholder rectangle.")
            video_frame = Rectangle(height=2.5, width=4.5, color=RED, fill_opacity=0.8)
            video_frame.to_edge(LEFT, buff=1)
            video_frame.shift(DOWN * 0.5)
            self.play(FadeIn(video_frame))

        self.wait(0.5)

        # Description text - using single Text object with newlines and better spacing
        description_text = """Personalised medicine tailors medical treatment
to the individual characteristics of each patient.

By analyzing genetic, environmental, and lifestyle
factors, doctors can design more effective and
targeted therapies, improving outcomes and
reducing side effects."""
        
        description = Text(description_text, font_size=24, line_spacing=2)
        description.scale(0.8)  # Scale down to prevent overlap while maintaining spacing
        description.set_width(4.5)  # Smaller width to ensure it fits
        description.to_edge(RIGHT, buff=1)  # Position from right edge with buffer
        description.align_to(video_frame, UP)
        # Animate the description slower
        self.play(Write(description), run_time=5)
        self.wait(3)    