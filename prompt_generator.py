import random

class NeonGenerationPromptGenerator:
    def __init__(self):
        self.subjects = [
            "cyberpunk city street at night",
            "futuristic neon-lit robot",
            "glowing neon vampire with electric aura",
            "cyberpunk hacker with neon visor",
            "neon dragon with electric flames",
            "futuristic android with glowing circuits",
            "neon witch casting electric spells",
            "cyberpunk warrior with neon sword",
            "glowing neon demon with electric wings",
            "futuristic mecha with neon armor",
            "neon angel with electric halo",
            "cyberpunk monk with glowing tattoos",
            "neon phoenix with electric feathers",
            "futuristic vehicle with neon lights",
            "glowing neon sorcerer with electric staff"
        ]
        
        self.neon_colors = [
            "electric blue neon glowing",
            "vibrant pink neon radiating",
            "intense purple neon shimmering",
            "bright cyan neon pulsating",
            "glowing red neon flaming",
            "electric green neon sparking",
            "vivid orange neon burning",
            "luminous yellow neon blazing",
            "neon teal neon flowing",
            "electric magenta neon swirling"
        ]
        
        self.effects = [
            "electric sparks flying everywhere",
            "glowing particles floating around",
            "neon rain dripping down",
            "light beams shooting upward",
            "energy aura surrounding character",
            "plasma waves rippling through air",
            "laser beams cutting through darkness",
            "holographic screens flickering",
            "glowing circuits pulsing on surfaces",
            "electric arcs crackling around"
        ]
        
        self.backgrounds = [
            "dark cyberpunk cityscape with skyscrapers",
            "neon-lit alleyway with street vendors",
            "futuristic laboratory with glowing machines",
            "abandoned warehouse with neon signs",
            "space station with neon control panels",
            "underground club with neon dance floor",
            "digital virtual reality landscape",
            "corporate tower with neon windows",
            "mysterious temple with neon runes",
            "cybernetic dimension with neon grids"
        ]
        
        self.lighting = [
            "harsh neon lighting with deep shadows",
            "soft glowing ambient neon light",
            "dramatic backlighting with neon rim light",
            "volumetric neon light rays",
            "cinematic neon lighting with contrast",
            "moody neon atmosphere with haze",
            "intense neon spotlight effects",
            "ambient neon glow with reflections"
        ]
        
        self.art_qualities = [
            "ultra detailed, 8k resolution, photorealistic",
            "highly detailed, cinematic lighting, masterpiece",
            "professional digital art, sharp focus, vibrant",
            "hyper realistic, octane render, unreal engine 5",
            "award winning artwork, intricate details, stunning",
            "concept art quality, polished, professional grade",
            "CGI quality, ray tracing, hyperrealistic",
            "studio quality, refined, breathtaking visuals"
        ]
    
    def generate_prompt(self):
        subject = random.choice(self.subjects)
        color = random.choice(self.neon_colors)
        effect = random.choice(self.effects)
        background = random.choice(self.backgrounds)
        lighting = random.choice(self.lighting)
        quality = random.choice(self.art_qualities)
        
        prompt = f"""
Neon cyberpunk artwork of {subject}, {color} neon glowing effects, {effect}, {background}. 
{lighting}. {quality}.
Vibrant neon colors, electric atmosphere, futuristic aesthetic.
High contrast, glowing highlights, dark shadows, electronic energy.
"""
        return prompt.strip()


if __name__ == "__main__":
    generator = NeonGenerationPromptGenerator()
    print("=== NEON GENERATION PROMPT ===")
    print(generator.generate_prompt())
    print()
    print("=== ANOTHER PROMPT ===")
    print(generator.generate_prompt())
