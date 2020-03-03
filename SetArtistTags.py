"""
The purpose of this script is to add the artist ID3 tags to mp3 files
The files should be in the format "trackNumber - artist - song.mp3"

Author: Kieran Meekan
Date: 20200303
"""

import os
import eyeD3

def get_artist_name(fileName):
    """ fileName format "trackNumber - artist - song.mp3" """
    artistName = fileName.split(" - ")[1]
    return artistName

def check_for_tag(path, fileName):
    tag = eyeD3.Tag()
    tag.link(path + fileName)
    print(tag.getArtist())
    # this needs to be finished for the code to work
    return True

def set_artist_name(path, fileName):
    tag = eyeD3.Tag()
    tag.link(path + fileName)
    tag.setArtist(get_artist_name(fileName))
    tag.update()
    print(fileName + " - tag updated successfully")

def main():
    paths = os.listdir()
    for path in paths:
        if '.' not in path:
            path += '/'
            print("Processing files from " + path)
            files = os.listdir(path)
            for fileName in files:
                if not check_for_tag(path, fileName):
                    set_artist_name(path, fileName)

main()




