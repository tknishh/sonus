import openai
from PIL import Image
from io import BytesIO

class ImageProcessor:
    def __init__(self, openai_api_key):
        self.openai_api_key = openai_api_key
        openai.api_key = self.openai_api_key

    def describe_image(self, image_path):
        """
        Generates a description of an image using OpenAI's API.
        
        Parameters:
            image_path (str): The path to the image file.
        
        Returns:
            str: A description of the image.
        """
        try:
            img = Image.open(image_path)
            img.save("/tmp/temp_image.jpg")  # Save image temporarily if needed
            with open("/tmp/temp_image.jpg", "rb") as image_file:
                image_data = image_file.read()

            response = openai.Image.create(
                image=image_data,
                model="gpt-4-turbo"  # This model name is hypothetical
            )
            description = response.choices[0].text.strip()
            return description
        except Exception as e:
            return f"Error describing image: {e}"

    def preprocess_image_for_api(self, image_path):
        """
        Converts an image file into a format suitable for submission to the OpenAI API.
        
        Parameters:
            image_path (str): The path to the image file.
        
        Returns:
            bytes: The image data in bytes, ready to be sent to the API.
        """
        try:
            img = Image.open(image_path)
            buffered = BytesIO()
            img.save(buffered, format="JPEG")
            img_byte = buffered.getvalue()
            return img_byte
        except Exception as e:
            return f"Error preparing image for API: {e}"
