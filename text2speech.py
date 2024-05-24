import uuid
import os
from dotenv import load_dotenv

from deepgram import (
    DeepgramClient,
    SpeakOptions,
)

load_dotenv()
# num = random.randint(0,100)
api_key = os.getenv("DG_API_KEY")


def text2speech(text):
    sound_dir = "./sounds"
    for f in os.listdir(sound_dir):
        if f.endswith(".wav"):
          os.remove(os.path.join(sound_dir, f))
    SPEAK_OPTIONS = {"text": text}
    try:
        # STEP 1: Create a Deepgram client using the API key from environment variables
        deepgram = DeepgramClient(api_key=api_key)

        # STEP 2: Configure the options (such as model choice, audio configuration, etc.)
        options = SpeakOptions(
            model="aura-arcas-en",
            encoding="linear16",
            container="wav"
        )
        unique_id = str(uuid.uuid4())
        filename = f"./sounds/output_{unique_id}.wav"
        # STEP 3: Call the save method on the speak property
        deepgram.speak.v("1").save(filename, SPEAK_OPTIONS, options)
        return filename

    except Exception as e:
        print(f"Exception: {e}")


if __name__ == "__main__":
    text2speech("this is a test")