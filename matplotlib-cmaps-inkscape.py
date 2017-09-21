#!/usr/bin/env python3

from matplotlib import cm
from matplotlib.colors import rgb2hex
from matplotlib import __version__ as mplVersion


def main():
    pallettes = [
        PaletteInfo(name='Viridis', cmap=cm.viridis),
        PaletteInfo(name='Magma', cmap=cm.magma),
        PaletteInfo(name='Inferno', cmap=cm.inferno),
        PaletteInfo(name='Plasma', cmap=cm.plasma)
    ]  # yapf: disable

    for each in pallettes:
        make_palette(each)


def make_palette(palette):
    with open(palette.filename, 'w') as f:
        f.write('GIMP Palette\n')
        f.write('Name: ' + palette.name + '\n')
        f.write('# From matplotlib ' + mplVersion + '\n')
        for color in palette.cmap.colors:
            R, G, B = [int(round(x * 255)) for x in color]
            f.write('{0:3d} {1:3d} {2:3d}  {3:s}\n'.format(R, G, B,
                                                           rgb2hex(color)))


class PaletteInfo:

    def __init__(self, name, cmap, filename='', description=''):
        self.cmap = cmap
        self.name = name
        if filename != '':
            self.filename = filename
        else:
            self.filename = 'palettes/' + name + '.gpl'
        self.description = description


if __name__ == '__main__':
    main()
