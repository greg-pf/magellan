import numpy as np
from skimage import color, transform

"""
	A class representation of an image tile
	Image data of the Tile is used to classify its base terrain type
"""
class Tile():
	def __init__(self, parent_image, x, y, side_length):
		self.parent = parent_image
		self.x = x
		self.y = y
		self.side_length = side_length
		self.base = None

	def get_image(self, resize=(100, 100)):
		img = self.parent[self.y:self.y+self.side_length,
						self.x:self.x+self.side_length]
		if resize is None:
			return img
		return transform.resize(img, resize)

# divide the image into Tiles with side_length
def img_to_tiles(img, side_length):
    img_rgba = _rgb2rgba(img)
    tiles = []
    for y in range(0, len(img)-side_length + 1, side_length):
        tiles.append([])
        for x in range(0, len(img[0])-side_length + 1, side_length):
                tiles[y/side_length].append(Tile(img_rgba, x, y, side_length))
    return np.asarray(tiles)

# convert an rgb image to rgba
def _rgb2rgba(img):
    if img.shape[2] == 3:
        return np.dstack((img, (color.rgb2gray(img) != -1)))
    if img.shape[2] == 4:
        return img
    raise ValueError("expected an rgb image, got img with shape " + str(img.shape))