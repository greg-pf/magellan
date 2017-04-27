import json
import numpy
from tile import Tile

class CivVEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Tile):
            return {'base': obj.base}

        if isinstance(obj, numpy.ndarray):
            if obj.shape is ():
                return super(CivVEncoder, self).default(obj)
            return [self.default(x) for x in obj]

        if isinstance(obj, numpy.integer):
            return int(obj)

        if isinstance(obj, numpy.floating):
            return float(obj)

        return super(CivVEncoder, self).default(obj)
