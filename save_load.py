import pickle
import os

SAVE_DIR = "saves"

def _ensure_save_dir():
    """Ensures the save directory exists."""
    if not os.path.exists(SAVE_DIR):
        os.makedirs(SAVE_DIR)

def save_character(character, slot):
    """Saves a character object to a specific slot."""
    _ensure_save_dir()
    filepath = os.path.join(SAVE_DIR, f"save_{slot}.pkl")
    try:
        with open(filepath, 'wb') as f:
            pickle.dump(character, f)
        print(f"\nGame saved successfully to slot {slot}.")
        return True
    except Exception as e:
        print(f"\nAn error occurred while saving: {e}")
        return False

def load_character(slot):
    """Loads a character object from a specific slot."""
    filepath = os.path.join(SAVE_DIR, f"save_{slot}.pkl")
    if not os.path.exists(filepath):
        return None
    try:
        with open(filepath, 'rb') as f:
            return pickle.load(f)
    except Exception as e:
        print(f"\nAn error occurred while loading the save file: {e}")
        return None

def get_save_slots():
    """Lists available save slots with character summaries."""
    _ensure_save_dir()
    saves = []
    for filename in sorted(os.listdir(SAVE_DIR)):
        if filename.startswith("save_") and filename.endswith(".pkl"):
            try:
                slot = int(filename.split('_')[1].split('.')[0])
                character = load_character(slot)
                if character:
                    saves.append((slot, f"{character.c_fullname}, Age {character.c_age}"))
            except (ValueError, IndexError, pickle.UnpicklingError):
                continue  # Ignore malformed or corrupted save files
    return saves