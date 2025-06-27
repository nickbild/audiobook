import cv2
import os
import google.genai as genai
from google.genai import types
import wave
from piper.voice import PiperVoice
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN, pull_up_down=GPIO.PUD_UP)


while True:
    # Wait for a button press.
    if GPIO.input(7) == GPIO.LOW:
        ###
        # Capture an image.
        ###

        camera = cv2.VideoCapture(0)
        camera.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
        camera.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

        if not camera.isOpened():
            print("Error: Could not open camera.")
        else:
            # Read a single frame
            ret, frame = camera.read()

        if ret:
            cv2.imwrite("captured_image.jpg", frame)
        else:
            print("Failed to capture image.")

        camera.release()


        ###
        # Extract the image text with Gemini.
        ###

        with open('captured_image.jpg', 'rb') as f:
            image_bytes = f.read()


        client = genai.Client(api_key=os.getenv('GENAIAPI'))
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=[
                types.Part.from_bytes(
                data=image_bytes,
                mime_type='image/jpeg',
                ),
                'Give me the text in this image. Only include the image text in your response.'
            ]
        )

        print(response.text)


        ###
        # Synthesize and play speech.
        ###

        # Define the path to your downloaded model
        model_path = "/home/nick/software/audiobook/en_US-lessac-medium.onnx" 
        config_path = "/home/nick/software/audiobook/en_US-lessac-medium.onnx.json"

        # Load the Piper voice model
        voice = PiperVoice.load(model_path, config_path)

        # Output WAV file
        output_wav_file = "text.wav"

        # Synthesize speech and save to WAV file
        with wave.open(output_wav_file, "wb") as wav_file:
            audio = voice.synthesize(response.text, wav_file)

        os.system("aplay text.wav")

