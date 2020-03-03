"""
The purpose of this script is to add the artist ID3 tags to mp3 files
The files should be in the format "trackNumber - artist - song.mp3"

Author: Kieran Meekan
Date: 20200303
"""

# TO DO:
# - Add a check for tags already existing
# - Currently will not work on songs which have a '-' character in the title (i.e. remixes)
#       - Need to check how the names are done by deezloader to ensure i can sort 

import os
import eyeD3

paths = [
    'H O U S E/',
    'dnb tunes/',
    'Spin me some 70s/'
]

def get_artist_name(fileName):
    """ fileName format "trackNumber - artist - song.mp3" """
    # no matter the number of '-' characters, we may be able to still use the 2nd ([1]), str in the list
    if  len(fileName.split(" - ")) == 3:
        artistName = fileName.split(" - ")[1]
        return artistName
    else:
        print("Error: " + fileName + " has an incorrect number of '-' characters, unable to process")
        return ""

def set_artist_name(path, fileName):
    tag = eyeD3.Tag()
    tag.link(path + fileName)
    tag.setArtist(get_artist_name(fileName))
    tag.update()
    print(fileName + " - tag updated successfully")

def main():
    for path in paths:
        print("Processing files from " + path)
        files = os.listdir(path)
        for fileName in files:
            set_artist_name(path, fileName)

main()




