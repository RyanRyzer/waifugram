import tensorflow as tf
import numpy as np

labels = [
    "Maid",
    "Cat Girl",
    "Elf",
    "Furry",
    "Loli",
    "Game",
    "Teen",
    "Milf"
]

interpreter = tf.lite.Interpreter(
    model_path="model.tflite"
)

interpreter.allocate_tensors()

input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()


def predict_image(image):

    input_shape = input_details[0]['shape']

    height = input_shape[1]
    width = input_shape[2]

    image = image.resize((width, height))

    image_array = np.array(image)

    input_data = np.expand_dims(
        image_array,
        axis=0
    ).astype(np.float32)

    input_data = input_data / 255.0

    interpreter.set_tensor(
        input_details[0]['index'],
        input_data
    )

    interpreter.invoke()

    output_data = interpreter.get_tensor(
        output_details[0]['index']
    )[0]

    predicted_index = np.argmax(output_data)

    predicted_label = labels[predicted_index]

    confidence = float(
        output_data[predicted_index]
    ) * 100

    return predicted_label, confidence, output_data
