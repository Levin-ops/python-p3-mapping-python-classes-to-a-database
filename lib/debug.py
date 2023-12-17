#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song

import pytest; pytest.set_trace()

if __name__ == '__main__':
    import ipdb; ipdb.set_trace()

    Song.create_table()

    blinding_lights = Song("Blinding Lights", "After Hours")

 



