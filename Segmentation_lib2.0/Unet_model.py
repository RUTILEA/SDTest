from keras.layers import Input, Concatenate,MaxPooling2D, Dropout, Conv2DTranspose
from keras.layers.convolutional import Conv2D
from keras.models import Model
from keras import initializers, regularizers

class UNet:
    def __init__(self, input_shape, classes, l2reg=0.0001):
        self.input_shape = input_shape
        self.classes = classes
        self.l2reg = l2reg

    def build(self):
        x = Input(shape=self.input_shape)
        h = Conv2D(64, kernel_size=3, padding='same', kernel_initializer='he_normal', activation='relu', kernel_regularizer=regularizers.l2(self.l2reg))(x)
        h = Conv2D(64, kernel_size=3, padding='same', kernel_initializer='he_normal', activation='relu', kernel_regularizer=regularizers.l2(self.l2reg))(h)
        d1 = h
        h = MaxPooling2D(2)(h)
        h = Conv2D(128, kernel_size=3, padding='same', kernel_initializer='he_normal', activation='relu')(h)
        h = Conv2D(128, kernel_size=3, padding='same', kernel_initializer='he_normal', activation='relu', kernel_regularizer=regularizers.l2(self.l2reg))(h)
        d2 = h
        h = MaxPooling2D(2)(h)
        h = Conv2D(256, kernel_size=3, padding='same', kernel_initializer='he_normal', activation='relu', kernel_regularizer=regularizers.l2(self.l2reg))(h)
        h = Conv2D(256, kernel_size=3, padding='same', kernel_initializer='he_normal', activation='relu', kernel_regularizer=regularizers.l2(self.l2reg))(h)
        d3 = h
        h = MaxPooling2D(2)(h)
        h = Conv2D(512, kernel_size=3, padding='same', kernel_initializer='he_normal', activation='relu', kernel_regularizer=regularizers.l2(self.l2reg))(h)
        h = Conv2D(512, kernel_size=3, padding='same', kernel_initializer='he_normal', activation='relu', kernel_regularizer=regularizers.l2(self.l2reg))(h)
        d4 = h
        h = Dropout(0.5)(h)
        h = MaxPooling2D(2)(h)

        h = Conv2D(1024, kernel_size=3, padding='same', kernel_initializer='he_normal', activation='relu', kernel_regularizer=regularizers.l2(self.l2reg))(h)
        h = Conv2D(1024, kernel_size=3, padding='same', kernel_initializer='he_normal', activation='relu', kernel_regularizer=regularizers.l2(self.l2reg))(h)
        h = Dropout(0.5)(h)
        
        h = Conv2DTranspose(512, 2, strides=2, padding='valid', kernel_initializer='he_normal', activation='relu', kernel_regularizer=regularizers.l2(self.l2reg))(h)
        h = Concatenate(axis=-1)([h, d4])
        h = Conv2D(512, kernel_size=3, padding='same', kernel_initializer='he_normal')(h)
        h = Conv2D(512, kernel_size=3, padding='same', kernel_initializer='he_normal')(h)
        h = Conv2DTranspose(256, 2, strides=2, padding='valid', kernel_initializer='he_normal', activation='relu', kernel_regularizer=regularizers.l2(self.l2reg))(h)
        h = Concatenate(axis=-1)([h, d3])
        h = Conv2D(256, kernel_size=3, padding='same', kernel_initializer='he_normal')(h)
        h = Conv2D(256, kernel_size=3, padding='same', kernel_initializer='he_normal')(h)
        h = Conv2DTranspose(128, 2, strides=2, padding='valid', kernel_initializer='he_normal', activation='relu', kernel_regularizer=regularizers.l2(self.l2reg))(h)
        h = Concatenate(axis=-1)([h, d2])
        h = Conv2D(128, kernel_size=3, padding='same', kernel_initializer='he_normal')(h)
        h = Conv2D(128, kernel_size=3, padding='same', kernel_initializer='he_normal')(h)
        h = Conv2DTranspose(64, 2, strides=2, padding='valid', kernel_initializer='he_normal', activation='relu', kernel_regularizer=regularizers.l2(self.l2reg))(h)
        h = Concatenate(axis=-1)([h, d1])
        h = Conv2D(64, kernel_size=3, padding='same', kernel_initializer='he_normal')(h)
        h = Conv2D(64, kernel_size=3, padding='same', kernel_initializer='he_normal')(h)
        prob = Conv2D(self.classes, kernel_size=1, padding='same', kernel_initializer='he_normal', activation='softmax')(h)

        model = Model(x, prob)
        return model