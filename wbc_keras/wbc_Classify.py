import tensorflow as tf
import numpy as np
import keras_cv
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow import keras
from keras.models import load_model
from tensorflow.keras import layers
from tensorflow.python.client import device_lib
import matplotlib.pyplot as plt

#-----------------------------------------------------------------------------------

def make_model(input_shape, num_classes):
    inputs = keras.Input(shape=input_shape)
    # Image augmentation block
    x = data_augmentation(inputs)

    # Entry block
    x = layers.experimental.preprocessing.Rescaling(1.0 / 255)(x)
    x = layers.Conv2D(32, 3, strides=2, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    x = layers.Conv2D(64, 3, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    previous_block_activation = x  # Set aside residual

    for size in [128, 256, 512, 728]:
        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(size, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.Activation("relu")(x)
        x = layers.SeparableConv2D(size, 3, padding="same")(x)
        x = layers.BatchNormalization()(x)

        x = layers.MaxPooling2D(3, strides=2, padding="same")(x)

        # Project residual
        residual = layers.Conv2D(size, 1, strides=2, padding="same")(
            previous_block_activation
        )
        x = layers.add([x, residual])  # Add back residual
        previous_block_activation = x  # Set aside next residual

    x = layers.SeparableConv2D(1024, 3, padding="same")(x)
    x = layers.BatchNormalization()(x)
    x = layers.Activation("relu")(x)

    x = layers.GlobalAveragePooling2D()(x)
    if num_classes == 2:
        activation = "sigmoid"
        units = 1
    else:
        activation = "softmax"
        units = num_classes

    x = layers.Dropout(0.5)(x)
    outputs = layers.Dense(units, activation=activation)(x)
    return keras.Model(inputs, outputs)


#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------

image_size = (512, 512)
batch_size = 90

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "/wbc/training/",
    validation_split=0.2,
    subset="training",
    seed=4252374731,
    image_size=image_size,
    batch_size=batch_size,
)
val_ds = tf.keras.preprocessing.image_dataset_from_directory(
    "/wbc/training/",
    validation_split=0.2,
    subset="validation",
    seed=4252374731,
    image_size=image_size,
    batch_size=batch_size,
)

data_augmentation = keras.Sequential(
    [
        layers.experimental.preprocessing.RandomFlip("horizontal"),
        layers.experimental.preprocessing.RandomFlip("vertical"),
        layers.experimental.preprocessing.RandomRotation(
            factor=(-0.15,0.15),
            fill_mode="reflect",
            seed=31333947,
        ),
        layers.experimental.preprocessing.RandomZoom(
            height_factor=(0,-0.10),
            width_factor=None,
            fill_mode="reflect",
            interpolation="bilinear",
            seed=86777615,
            fill_value=0.0,
        ),
        keras_cv.layers.RandomSaturation((0.480,0.520), seed=6032258),
        keras_cv.layers.RandomHue((0.000,0.100), [0, 255], seed=4575532),
        keras_cv.layers.RandomSharpness((0.000,0.050), [0, 255], seed=982543),
    ]
)

plt.figure(figsize=(10, 10))
for images, _ in train_ds.take(1):
    for i in range(9):
        augmented_images = data_augmentation(images)
        ax = plt.subplot(3, 3, i + 1)
        plt.imshow(augmented_images[0].numpy().astype("uint8"))
        plt.axis("off")

##plt.show()

#-----------------------------------------------------------------------------------

strategy = tf.distribute.MirroredStrategy()
print('Number of devices: {}'.format(strategy.num_replicas_in_sync))

val_ds = val_ds.prefetch(buffer_size=batch_size)

with strategy.scope():
   #model = make_model(input_shape=image_size + (3,), num_classes=11)
   model = load_model('leukoRight.h5')
   keras.utils.plot_model(model, show_shapes=True)
   
epochs = 1000
   
callbacks = [
    keras.callbacks.ModelCheckpoint("leukoRight_model_{epoch}.h5"),
]
   
#loss_fn = keras.losses.SparseCategoricalCrossentropy()
       
model.compile(
    optimizer = keras.optimizers.Adam(learning_rate=1e-10),
    loss = "sparse_categorical_crossentropy",
    metrics = ["accuracy"],
)

model.fit(
    train_ds, epochs=epochs, callbacks=callbacks, validation_data=val_ds,
)
