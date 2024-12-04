import os
import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
from dotenv import load_dotenv

load_dotenv()

# Texto y fuente personalizada
text = 'Get ready! Press "Q" to start capturing images'
font_path = './fonts/Roboto-Regular.ttf'  # Ruta a la fuente personalizada
font_size = 28  # Tamaño de la fuente

DATA_DIR = './data'
if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

number_of_classes = 3
dataset_size = 100

cap = cv2.VideoCapture(1)
if not cap.isOpened():
    print("Error: No se pudo abrir la cámara.")
    exit()

window_name = 'Capture images'  # Nombre de la ventana

for j in range(number_of_classes):
    class_dir = os.path.join(DATA_DIR, str(j))
    if not os.path.exists(class_dir):
        os.makedirs(class_dir)

    print(f'Collecting data for class {j}')

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: No se pudo capturar el cuadro. Verifica la cámara.")
            break

        # Convertir frame OpenCV a imagen PIL
        pil_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        draw = ImageDraw.Draw(pil_image)

        # Cargar fuente personalizada
        font = ImageFont.truetype(font_path, font_size)

        # Obtener tamaño del texto usando textbbox()
        text_bbox = draw.textbbox((0, 0), text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]

        # Posición del texto
        text_x, text_y = 20, 20  # Margen desde la esquina superior izquierda

        # Dimensiones del fondo
        padding = 10
        rect_x0 = text_x - padding
        rect_y0 = text_y - padding
        rect_x1 = text_x + text_width + padding
        rect_y1 = text_y + text_height + padding

        # Dibujar rectángulo de fondo opaco
        rect_color = (0, 0, 0, 150)  # Negro translúcido
        draw.rectangle([rect_x0, rect_y0, rect_x1, rect_y1], fill=rect_color)

        # Agregar contorno al texto
        outline_color = (0, 0, 0)  # Negro para el contorno
        outline_offset = 2
        for dx in [-outline_offset, 0, outline_offset]:
            for dy in [-outline_offset, 0, outline_offset]:
                if dx != 0 or dy != 0:  # Evitar el centro
                    draw.text((text_x + dx, text_y + dy), text, font=font, fill=outline_color)

        # Dibujar el texto principal
        text_color = (255, 255, 255)  # Blanco
        draw.text((text_x, text_y), text, font=font, fill=text_color)

        # Convertir imagen PIL de vuelta a OpenCV
        frame_with_text = cv2.cvtColor(np.array(pil_image), cv2.COLOR_RGB2BGR)

        # Mostrar frame con texto
        cv2.imshow(window_name, frame_with_text)

        # Cerrar con la tecla 'Q'
        if cv2.waitKey(25) == ord('q'):
            break

    counter = 0
    while counter < dataset_size:
        ret, frame = cap.read()
        if not ret:
            print("Error: No se pudo capturar el cuadro durante la colección de datos.")
            break

        cv2.imshow(window_name, frame)
        cv2.waitKey(25)
        cv2.imwrite(os.path.join(class_dir, f'{counter}.jpg'), frame)
        counter += 1

cap.release()
cv2.destroyAllWindows()
