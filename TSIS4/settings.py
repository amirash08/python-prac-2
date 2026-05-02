import json
import os


SETTINGS_FILE = "settings.json"


default_settings = {
    "snake_color": "green",
    "grid": True,
    "sound": True
}


def load_settings():
    if not os.path.exists(SETTINGS_FILE):
        save_settings(default_settings)
        return default_settings

    with open(SETTINGS_FILE, "r") as file:
        return json.load(file)


def save_settings(settings):
    with open(SETTINGS_FILE, "w") as file:
        json.dump(settings, file, indent=4)