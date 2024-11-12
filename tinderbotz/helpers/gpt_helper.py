import os
from openai import OpenAI
from dotenv import load_dotenv
import emoji
from tinderbotz.helpers.env_parser import env_vars
class GPTHelper:
    def __init__(self):
        self.api_key = self.load_api_key()
        self.openai = OpenAI(api_key=self.api_key)
        self.model = "gpt-4o-mini"
        self.system_prompt = "tu parle uniquement français. Tu es un seducteur agueri. Tu n'utilise pas d'émoticones ou de caracteres speciaux"

    def load_api_key(self):
        api_key = env_vars.get("OPENAI_API_KEY")
        if not api_key:
            api_key = input("Please enter your OpenAI API Key: ").strip()
            env_vars.set("OPENAI_API_KEY", api_key)
        return api_key

    def generate_pickup_line(self, name, bio):
        try:
            completion = self.openai.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "system", "content": self.system_prompt},
                    {
                    "role": "user",
                    "content": "tu vas generer une phrase d'accorche pour aborder une femme sur tinder, elle doit être un peu flirteuse et pas trop aggressive tout en étant viril, la femme s'appelle " + name + " et tu dois utiliser le prénom de la personne, de plus, elle a indiqué dans son profil la bio suivante : [debut de bio]" + bio + "[fin de bio], essaie de t'en inspirer si c'est possible, la phrase doit être courte et impactante. aucun emoji ou caractere special ne doit être utilisé. tu dois flirter un peu et pourquoi pas tenter d'etre entreprenant"
                    }
                ])
        except Exception as e:
            print(f"Error generating pickup line: {str(e)}")
            return None
        message = completion.choices[0].message.content.strip('"').strip("'").format(name)
        return message