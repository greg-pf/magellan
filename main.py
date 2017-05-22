#!/usr/bin/env python
import matplotlib.image as mpimg
import json
import os.path
import tile

from argparse import ArgumentParser, ArgumentTypeError
from classifiers import BaseTerrainClassifier
from civ_encoder import CivVEncoder

# determine if the path given is a valid file with .png extension
def is_valid_png(arg):
    if not os.path.exists(arg):
        raise ArgumentTypeError("{0} does not exist".format(arg))
    _, ext = os.path.splitext(arg)
    if ext != '.png':
        raise ArgumentTypeError("expected a .png, got {0} instead".format(arg))
    return arg

def main():
    parser = ArgumentParser(
        description="Divide the image into square tiles with the given side " +
                    "length and classify the major terrain features in each tile")
    parser.add_argument("filename", type=lambda x: is_valid_png(x),
                        help="input image file (must be a .png)", metavar="FILE")
    parser.add_argument("length", type=int,
                        help="the side length of the tiles to create")
    # parser.add_argument(dest="shape", type=str,
    #                     help="the shape of the tiles to be used " +
    #                         "(one of: 'square', 'hex', or 'tri')")
    args = parser.parse_args()

    # read image file and convert to Tiles
    img = mpimg.imread(args.filename)
    tiles = tile.img_to_tiles(img, args.length)

    # build the classifier
    btc = BaseTerrainClassifier()
    btc.fit()

    # classify the base terrain of each Tile
    for t in tiles.reshape(-1):
        # this is where we will use our classifier
        t.base = btc.predict(t.get_image())

    print type(tiles[0][0].base)
    print json.dumps(tiles, cls=CivVEncoder)


if __name__ == '__main__':
    main()