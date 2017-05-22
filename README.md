# Identifying Major Features in Terrain Imagery

## About

The aim of this project is to convert sattellite and other overhead terrain imagery to a game board for use in Sid Meier's strategy game, Civilization. 

Images are divided into triangular, square, or hexagonal tiles. Each tile is then assigned lables identifying a single base terrain type and several terrain features. The table below labels these terrain types:

| | Base Terrains | Terrain Features |
|-|---------------|------------------|
|1| Grasslands | Hills |
|2| Plains | Forrest |
|3| Desert | Jungle |
|4| Ocean | Mountains |
|5| Lake | Coast |
|6| Tundra | Flood Plains |
|7| Snow | Oasis |
|8|       | Ice |
|9|        | Fallout |
|10|       | Atoll |
|11|      | Wonder |

In it's current state, the program uses KNN to determine the base terrain of tiles with over 70% accuracy. While this can be improved with more elaborate feature selection, it has proven much more successful than SVM.

Our research into a multilable variant of KNN has also shown promise for classifying secondary terrain features, and will likely come in the next iteration of the program.

## Usage
a command line tool that accepts a file and side length of tiles and
prints the serialized json of the now classified tiles to std out

`python main.py ./path/to/map.png 150`

a sample image file (map.png) is provided in the Notebooks directory

for more details, use:
`python main.py -h`