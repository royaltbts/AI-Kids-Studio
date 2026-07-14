"""
Default TinyVerse Characters

These are the core recurring characters that appear
throughout the TinyVerse universe.
"""

from backend.app.characters.models import Character

TOBY = Character(
    id="toby",
    name="Toby Bear",
    species="Bear",
    age=5,
    personality=("Curious, kind, adventurous and always excited to learn."),
    appearance=("Small brown bear with bright eyes and a warm smile."),
    clothing="Blue backpack and a red t-shirt.",
    voice_style="Cheerful young boy.",
    catch_phrase="Let's learn together!",
    favorite_color="Blue",
    image_prompt=(
        "Cute 3D cartoon brown bear, Pixar-style, blue backpack, "
        "red t-shirt, smiling, children's educational animation."
    ),
    animation_notes=(
        "Energetic movements, expressive facial animations, " "friendly waving."
    ),
)


MIMI = Character(
    id="mimi",
    name="Mimi Rabbit",
    species="Rabbit",
    age=5,
    personality=("Creative, gentle and loves asking questions."),
    appearance=("White rabbit with pink ears and sparkling eyes."),
    clothing="Purple dress with a yellow bow.",
    voice_style="Sweet young girl.",
    catch_phrase="Wow! That's amazing!",
    favorite_color="Purple",
    image_prompt=(
        "Cute white rabbit wearing a purple dress with yellow bow, "
        "3D Pixar-style children's animation."
    ),
    animation_notes=("Gentle bouncing, happy ear movements."),
)


LEO = Character(
    id="leo",
    name="Leo Lion",
    species="Lion",
    age=6,
    personality=("Brave, confident and encourages friends."),
    appearance=("Golden lion cub with fluffy mane."),
    clothing="Green explorer vest.",
    voice_style="Confident young boy.",
    catch_phrase="We can do it!",
    favorite_color="Green",
    image_prompt=(
        "Cute lion cub wearing green explorer vest, " "Pixar-style 3D animation."
    ),
    animation_notes=("Strong posture with playful expressions."),
)


ELLIE = Character(
    id="ellie",
    name="Ellie Elephant",
    species="Elephant",
    age=5,
    personality=("Thoughtful, patient and loves solving puzzles."),
    appearance=("Cute baby elephant with large expressive ears."),
    clothing="Orange overalls.",
    voice_style="Soft and calm.",
    catch_phrase="Let's think together!",
    favorite_color="Orange",
    image_prompt=(
        "Cute baby elephant wearing orange overalls, "
        "Pixar-style educational animation."
    ),
    animation_notes=("Gentle movements with expressive trunk gestures."),
)
