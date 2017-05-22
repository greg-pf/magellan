import matplotlib.image as mpimg
import numpy as np
import tile
from sklearn.neighbors import KNeighborsClassifier as KNN

imgpath = './Notebooks/map.png'

class BaseTerrainClassifier(KNN):

    def fit(self):
        img = tile._rgb2rgba(mpimg.imread(imgpath))

        # set up training data and labels
        side_length = 100

        train_tiles = []
        np.random.seed(12345)
        for i in range(20):
            for j in range(6):
                rand_y = np.random.randint(0, img.shape[0]-side_length)
                rand_x = np.random.randint(0, img.shape[1]-side_length)
                t = tile.Tile(img, rand_x, rand_y, side_length)
                train_tiles.append(self.preprocess(t.get_image()))
        train_tiles = np.asarray(train_tiles, np.float32)

        train_labels = np.empty((len(train_tiles),), np.int32)
        train_labels[0:6] = [4, 4, 4, 4, 1, 4]
        train_labels[6:12] = [4, 4, 3, 4, 7, 4]
        train_labels[12:18] = [4, 4, 1, 4, 4, 2]
        train_labels[18:24] = [1, 2, 2, 4, 4, 1]
        train_labels[24:30] = [1, 4, 4, 2, 1, 4]
        train_labels[30:36] = [1, 2, 4, 4, 4, 4]
        train_labels[36:42] = [4, 2, 2, 6, 1, 2]
        train_labels[42:48] = [4, 4, 3, 4, 4, 4]
        train_labels[48:54] = [4, 4, 4, 3, 2, 1]
        train_labels[54:60] = [4, 6, 4, 4, 4, 4]
        train_labels[60:66] = [4, 4, 4, 4, 1, 6]
        train_labels[66:72] = [4, 6, 1, 2, 4, 4]
        train_labels[72:78] = [1, 4, 2, 6, 4, 4]
        train_labels[78:84] = [1, 4, 4, 1, 4, 4]
        train_labels[84:90] = [1, 4, 3, 4, 1, 4]
        train_labels[84:90] = [4, 4, 4, 4, 4, 1]
        train_labels[90:96] = [4, 4, 4, 4, 4, 1]
        train_labels[96:102] = [4, 4, 4, 4, 1, 1]
        train_labels[102:108] = [4, 6, 3, 4, 1, 4]
        train_labels[108:114] = [1, 3, 6, 1, 4, 4]
        train_labels[114:120] = [4, 4, 4, 4, 4, 4]

        # fit the model with the training data
        return super(BaseTerrainClassifier, self).fit(
                    self.preprocess(train_tiles), train_labels)

    def predict(self, tile_img):
        return super(BaseTerrainClassifier, self).predict(
                    self.preprocess(np.asarray([tile_img])))[0]

    def preprocess(self, tiles):
        return np.float32(np.average(np.delete(tiles.reshape((len(tiles), -1, 4)), 3, 2), axis=1))