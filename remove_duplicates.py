#!/usr/bin/python

'''
DESCRIPTION:
Hello everyone, I recently had a problem where I had numerous duplicates
in my iTunes library (~500 songs). This proved to be a far greater headache than I imagined.
Hence, with a lot of googling and some medicore programming, I hacked
up a solution to:
   1) Deleting all of the duplicate files
   2) Telling iTunes that I deleted all of the files
There are some minor issues with my code, but the end result will be what
you expect. It is certainly faster than manually deleting these
files, as some of you may have thousands and thousands of duplicates.
The only thing this code does that I would change is that it deletes
the non-copy version of the song. So instead of Song.mp3 and Song 1.mp3,
it will delete Song.mp3 and keep Song 1.mp3. While this bothers me
greatly, it *WILL NOT* be reflected in your iTunes library.
Only the song files themselves will appear this way. If this is truly
bothersome to some, I will look into appending a script that will clean
up the filenames afterward, as it should be a quick fix.
ACKNOWLEDGMENTS:
   1*) I would like to extend a very grateful thank you to everyone on the
      Stack Overflow thread for the ideas and specifically user zalew for
      the baseline of my code.
   2*) Additonally, I'd like to thank Paul Mayne and contributors for
      providing the steps to identify and remove dead links.
SOURCES:
   1*) http://stackoverflow.com/questions/748675/finding-duplicate-files-and-removing-them
   2*) http://paulmayne.org/blog/2007/11/how-to-remove-broken-or-dead-tracks-from-itunes/
'''

import sys
import os
import _md5 as md5

user_name = os.getlogin()
music_dir = "/Users/" + user_name + "/Music/iTunes/iTunes Media/Music"
cont = False

print("This utility is to remove duplicate music from your iTunes\n"
      + "library, though it will remove duplicates from any folder\n"
      + "that you enter.\n")
print("The default folder for iTunes is located at:\n"
      + "\t" + music_dir)

while (not cont):
    temp = input("\nEnter the name of your folder to remove duplicates\n"
                     + "from or hit enter to use the suggested location\n> ")

    if (not temp):
        temp = music_dir

    check = input("\nIs this correct? (y/n)\n\t" + temp + "\n> ")

    if (check == 'y'):
        music_dir = temp
        cont = True

def remove_duplicates(dir):
    unique = []
    for filename in os.listdir(dir):
        filename = dir + '/' + filename
        if os.path.isfile(filename):
            with open(filename, 'rb') as file:
                filehash = md5.md5(file.read()).hexdigest()
            if filehash not in unique:
                unique.append(filehash)
            else:
                print("Removing " + filename + "...")
                os.remove(filename)
        elif os.path.isdir(filename):
            remove_duplicates(filename)
        else:
            print("Unable to find file/directory " + filename + ", please try again")


print("\nIt's working I promise, give it a minute or two...\n")
remove_duplicates(music_dir)
