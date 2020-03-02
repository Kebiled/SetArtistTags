"""
The purpose of this script is to add the artist ID3 tags to mp3 files
The files should be in the format "trackNumber - artist - song.mp3"

Author: Kieran Meekan
Date: 20200303
"""

# TO DO:
# - Add a check for tags already existing

import os
import eyeD3

errorCount = 0
errorList = []
paths = [
    'H O U S E/',
    'dnb tunes/',
    'Spin me some 70s/'
]

def get_artist_name(fileName):
    artistName = fileName.split(" - ")[1]
    return unicode(artistName)

def set_artist_name(path, fileName):
    with open(path + fileName, 'r+') as file:
        if eyeD3.isMp3File(file):
            audioFile = eyeD3.Mp3AudioFile(file)
            tag = audioFile.getTag(audioFile)
            tag.setArtist(get_artist_name(fileName))
            tag.update()
            print(fileName + " - tag updated successfully")
        else:
            print("Error: " + fileName + " is not an mp3 file")
            errorList += [fileName]
            errorCount += 1 

def main():
    for path in paths:
        print("Processing files from " + path)
        files = os.listdir(path)
        for fileName in files:
            set_artist_name(path, fileName)
    if errorCount == 0:
        print("Finished without error, all tags updated")
    else:
        print("Finished. Errors with the following files:")
        for each fileName in errorList:
            print(fileName)

main()
