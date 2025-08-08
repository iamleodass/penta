import yaml
import os

CHARACTER_DIR = os.path.join(os.path.dirname(__file__), "characters")

def load_character_yaml(character_name):
    path = os.path.join(CHARACTER_DIR, f"{character_name}.yaml")
    with open(path, "r", encoding="utf-8") as file:
        return yaml.safe_load(file)

def build_system_prompt(character_data):
    return f"""
You are now roleplaying as the following character:

Name: {character_data['name']}
Age: {character_data['age']}
Gender: {character_data['gender']}
Race: {character_data['race']}
Role: {character_data['role']}
Occupation: {character_data['occupation']}
Speech Style: {character_data['speech_style']}
Personality Traits: {', '.join(character_data['personality_traits'])}
Alignment: {character_data['alignment']}

Background:
{character_data['background']}

Goals:
{', '.join(character_data['goals'])}

Fears:
{', '.join(character_data['fears'])}

Likes:
{', '.join(character_data['likes'])}
Dislikes:
{', '.join(character_data['dislikes'])}

Special Abilities:
{', '.join(character_data['special_abilities'])}

Relationships:
Ally: {character_data['relationships']['ally']}
Enemy: {character_data['relationships']['enemy']}

You must stay in character. Respond with the personality, tone, and knowledge of this character.
"""
