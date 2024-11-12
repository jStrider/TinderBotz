from dotenv import load_dotenv, set_key, find_dotenv
import os

dotenv_path = find_dotenv()
if not dotenv_path:
    with open('.env', 'w') as f:
        dotenv_path = f.name

load_dotenv(dotenv_path)

class EnvVars:
    def __init__(self):
        self.env_vars = {
            key: os.getenv(key) for key in os.environ
        }

    def get(self, key):
        return self.env_vars.get(key)

    def set(self, key, value):
        os.environ[key] = value
        self.env_vars[key] = value
        set_key(dotenv_path, key, value)

env_vars = EnvVars()