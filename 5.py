from PIL import Image, ImageFilter, ImageEnhance
import os


image_directory = r'C:\Users\vovam\OneDrive\Зображення'
output_directory = r'C:\Users\vovam\OneDrive\Зображення\Processed'
os.makedirs(output_directory, exist_ok=True)

if os.path.exists(image_directory):
    images = [f for f in os.listdir(image_directory) if f.endswith(('.jpg', '.png', '.jpeg'))]
    if images:
        print("Доступні зображення:")
        for idx, image in enumerate(images, 1):
            print(f"{idx}. {image}")
        
        selected_indexes = input("Введіть номери зображень через кому (наприклад, 1, 3, 5): ")
        selected_indexes = [int(idx.strip()) - 1 for idx in selected_indexes.split(',')]
        selected_images = [images[idx] for idx in selected_indexes if 0 <= idx < len(images)]

        class ImageFacade:
            def __init__(self, image_path):
                self.image = Image.open(image_path)

            def get_image(self):
                return self.image

        class ImageDecorator:
            def __init__(self, image_facade):
                self.image_facade = image_facade

            def get_image(self):
                return self.image_facade.get_image()

        class BlurDecorator(ImageDecorator):
            def get_image(self):
                return self.image_facade.get_image().filter(ImageFilter.GaussianBlur(5))

        class SharpnessDecorator(ImageDecorator):
            def get_image(self):
                enhancer = ImageEnhance.Sharpness(self.image_facade.get_image())
                return enhancer.enhance(2.0)

        class SaturationDecorator(ImageDecorator):
            def get_image(self):
                enhancer = ImageEnhance.Color(self.image_facade.get_image())
                return enhancer.enhance(1.5)

        class ResizeDecorator(ImageDecorator):
            def get_image(self):
                return self.image_facade.get_image().resize((400, 400), Image.LANCZOS)

        for img in selected_images:
            img_path = os.path.join(image_directory, img)
            facade = ImageFacade(img_path)

            print(f"\nОбробка зображення: {img}")

            filters = {
                "blur": BlurDecorator(facade).get_image(),
                "sharp": SharpnessDecorator(facade).get_image(),
                "saturated": SaturationDecorator(facade).get_image(),
                "resized": ResizeDecorator(facade).get_image()
            }

            for filter_name, processed_image in filters.items():
                output_path = os.path.join(output_directory, f"{filter_name}_{img}")
                processed_image.save(output_path)
                print(f"Збережено: {output_path}")
    else:
        print("У цій папці немає зображень.")
else:
    print(f"Шлях {image_directory} не існує.")
