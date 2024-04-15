from input_support import AudioProcessor
from input_support import ImageProcessor

def main():
    # Example usage of AudioProcessor
    print("Demonstrating AudioProcessor:")
    audio_proc = AudioProcessor(openai_api_key='your-openai-api-key')
    translated_text = audio_proc.capture_and_translate("path_to_audio_file.wav")
    print(f"Translated Text: {translated_text}\n")

    # Example usage of ImageProcessor
    print("Demonstrating ImageProcessor:")
    image_proc = ImageProcessor(openai_api_key='your-openai-api-key')
    image_description = image_proc.describe_image("url_to_image")
    print(f"Image Description: {image_description}\n")

if __name__ == "__main__":
    main()
