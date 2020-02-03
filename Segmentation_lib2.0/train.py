import tensorflow as tf
print(tf.__version__)
from Unet_model import UNet
from keras import optimizers
from keras.callbacks import ModelCheckpoint, Callback, EarlyStopping
from callback import ImageWriter
import keras.backend as K


def weighted_crossentropy_wrapper(class_weights, eps=1e-7):
    def weighted_cross_entropy(onehot_labels, output):
        output = K.clip(output, eps, 1.)
        loss = - tf.reduce_mean(class_weights * onehot_labels * tf.math.log(output))
        return loss

    return weighted_cross_entropy

def run(img_path, seg_path, learn_test, ans_test, imgs, segs, img_shape, weights, train_gen, steps_per_epoch, epochs, test_gen, validation_steps, weight_name, optimizer, batch_size):
    model = UNet(input_shape=img_shape, classes=2).build()
    model.compile(
        optimizer=optimizer,
        loss=weighted_crossentropy_wrapper(weights),
        metrics=['accuracy']
    )

    mc_cb = ModelCheckpoint('unet_pcb_weights.hdf5', monitor='val_loss', save_best_only=True, save_weights_only=True)
    im_cb = ImageWriter(img_path, seg_path, learn_test, ans_test, img_shape, batch_size)
    es_cb = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)
                        


    history = model.fit_generator(
        generator=train_gen,
        steps_per_epoch=steps_per_epoch,
        epochs=epochs,
        callbacks=[mc_cb, im_cb, es_cb],
        # callbacks = [es_cb],
        validation_data=test_gen,
        validation_steps=validation_steps,
        shuffle=True
    )
    model.save_weights(f'{weight_name}')
  