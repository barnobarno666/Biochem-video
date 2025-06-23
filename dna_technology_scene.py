from manim import *

class DNATechnologyScene(Scene):
    def construct(self):
        # Title text at the top
        title = Text("DNA TECHNOLOGY", font_size=48).to_edge(UP)
        self.play(Write(title))

        # List of state-of-the-art DNA technologies
        technologies = [
            "CRISPR-Cas9",
            "Gene Therapy",
            "Synthetic Biology",
            "DNA Sequencing",
            "Epigenetic Editing",
            "RNA Interference",
        ]

        descriptions = {
            "CRISPR-Cas9": "Precise genome editing tool.",
            "Gene Therapy": "Treats genetic disorders by altering genes.",
            "Synthetic Biology": "Design and construct new biological parts.",
            "DNA Sequencing": "Determines the order of DNA nucleotides.",
            "Epigenetic Editing": "Modifies gene expression without altering DNA.",
            "RNA Interference": "Silences specific gene expressions.",
        }

        # Create a VGroup for the list and position it on the left
        tech_list = VGroup(
            *[Text(tech, font_size=36) for tech in technologies]
        ).arrange(DOWN, aligned_edge=LEFT).to_edge(LEFT, buff=1)

        # Animate the list and add arrows with descriptions
        for i, tech in enumerate(tech_list):
            self.play(FadeIn(tech, shift=UP))
            arrow = Arrow(
                start=tech.get_right(), 
                end=tech.get_right() + RIGHT * 2, 
                color=rgb_to_color([1, 1, 0])  # RGB color for customization
            )
            self.play(Create(arrow))

            # Move description to the right side of the screen
            description_box = Text(
                descriptions[tech.text], 
                font_size=28, 
                t2c={"Precise": YELLOW, "Silences": RED}  # Optional text coloring
            ).scale(0.8).next_to(arrow, RIGHT, buff=0.5)
            self.play(Write(description_box))
            self.wait(3)  # Pause for voiceover

        # Add some design elements (optional)
        underline = Line(start=LEFT, end=RIGHT, color=BLUE).next_to(title, DOWN)
        underline.set_width(title.width)
        self.play(Create(underline))

        # Keep the scene for a few seconds
        self.wait(3)
