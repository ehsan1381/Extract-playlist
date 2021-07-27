# IMPORTING LIBRARIES
import re
import os

# SOURCE FILE WITH .ZPL FORMAT
source_playlist_name = '.zpl'

# OPENING SOURCE PLAYLIST
source_playlist = open(source_playlist_name, 'r')

# OPENING A FILE TO SAVE FILE DIRECTORIES
target_directories_file = open('extracted_playlist', 'w+')

# DEFINING OBJ READLINE
lines = source_playlist.readlines()

for temp_line in lines :
    directory = re.search('<media src=(.+?).mp3', temp_line)
    if directory:
        found = directory.group(1)
        found = found.replace('"', '')
        found = '"%s.mp3"'% found
        print('found : %s' % found)
        print('copying : %s' % found)

        # MAKE SURE OUTPUT DIRECTORY EXISTS
        os.system('copy %s Output'%found)
