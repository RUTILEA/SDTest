from keras.callbacks import Callback
import data_generator
import matplotlib.pyplot as plt

class ImageWriter(Callback):
    def __init__(self, img_path, seg_path, learn_test, ans_test, img_shape, batch_size):
        super().__init__()
        self.batch_size = batch_size
        test_gen = data_generator.get_datagen(img_path, seg_path, learn_test, ans_test, img_shape, batch_size, train=False)
        self.x, self.y = test_gen.__next__()
        self.y_shape = (self.x.shape[1], self.x.shape[2], 2)
        self.img = data_generator.decode_img(self.x)
        self.gth = data_generator.decode_prob(self.y)
        self.preds = []

    def on_epoch_end(self, epoch, logs={}):
        self.p = self.model.predict_on_batch(self.x)
        self.pre = data_generator.decode_prob(self.p)
        self.preds.append(self.pre)

        figsize = (
            (self.x.shape[2]  * (len(self.preds) + 1)) / 100,
            (self.x.shape[1]  * (self.batch_size + 1)) / 100
        )

        fig, axes = plt.subplots(self.batch_size, 2 + len(self.preds), figsize=figsize)
        # Set title
        axes[0, 0].set_title('X')
        axes[0, 1].set_title('GT')
        for i in range(len(self.preds)):
            axes[0, i + 2].set_title(str(i))
        # Set images
        for i in range(self.batch_size):
            axes[i, 0].imshow(self.img[i], vmin=0, vmax=255)
            axes[i, 0].axis('off')
            axes[i, 1].imshow(self.gth[i], vmin=0, vmax=255)
            axes[i, 1].axis('off')
            for j in range(len(self.preds)):
                axes[i, j + 2].imshow(self.preds[j][i], vmin=0, vmax=255)
                axes[i, j + 2].axis('off')
        plt.savefig('history.jpg'.format(epoch))
        plt.close()  # This line stops matplotlib display image
      