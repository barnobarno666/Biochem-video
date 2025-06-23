from manim import *

class PersonalisedMedicineScene(Scene):
    def construct(self):
        # Heading at the top
        heading = Text("Personalised Medicine", font_size=48).to_edge(UP)
        self.play(Write(heading))

        # Image on the left, smaller and further left
        image = ImageMobject("media/images/MANIM VIDEO/personalised_medicine.png")
        image.set_height(2.5)
        image.to_corner(UL, buff=1.2)
        self.play(FadeIn(image))

        # Description as a large, multiline text box
        description_text = (
            "Personalised medicine tailors medical treatment to the individual characteristics "
            "of each patient. By analyzing genetic, environmental, and lifestyle factors, "
            "doctors can design more effective and targeted therapies, improving outcomes "
            "and reducing side effects."
        )
        description = Text(description_text, font_size=36, line_spacing=1.2)
        description.set_width(7)  # Make sure it wraps and fits the screen
        description.next_to(image, RIGHT, buff=1)
        description.align_to(image, UP)
        self.play(Write(description))

        self.wait(3)
