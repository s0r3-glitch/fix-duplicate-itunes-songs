Fix Duplicate Songs - iTunes
----
This solution provides a Python script that will allow the user to select a folder to remove duplicate files from (the intended use case is songs from the iTunes folder, though it will work for any) and then a solution to resolving dead links in iTunes after deleting the duplicates.

DESCRIPTION:
----
Hello everyone, I recently had a problem where I had numerous duplicates in my iTunes library (~500 songs). This proved to be a far greater headache than I imagined. Hence, with a lot of googling and some medicore programming, I hacked up a solution to:

Deleting all of the duplicate files
Telling iTunes that I deleted all of the files

DISCLAIMER:
----
*ENSURE THAT YOU HAVE BACKUPS OF ALL YOUR SONGS*

There are some minor issues with my code, but the end result will be what you expect. It is certainly faster than manually deleting these files, as some of you may have thousands and thousands of duplicates. The only thing this code does that I would change is that it deletes the non-copy version of the song. So instead of Song.mp3 and Song 1.mp3, it will delete Song.mp3 and keep Song 1.mp3. While this bothers me greatly (OCD, anyone?), it WILL NOT be reflected in your iTunes library. Only the song files themselves will appear this way. If this is truly bothersome to some, I will look into appending a script that will clean up the filenames afterward, as it should be a quick fix.

Edit: It seems like my file names went from being copies (i.e. Song 1.mp3) to simply being named as the non-copies (i.e. Song.mp3). I don't know if this issue resolved itself or if it will do so for everyone, but be sure to let me know so I can fix this if it does still occur!

TO USE:
----
1. Simply clone this repo or copy the remove_dupes.py file.
2. Run remove_duplicates.py in the terminal, follow the on-screen instructions.
3. Once the script has finished, open up iTunes and follow this guide: http://paulmayne.org/blog/2007/11/how-to-remove-broken-or-dead-tracks-from-itunes/
4. Duplicates should be removed! I'll be working on a fix for the raw file names, but this should be sufficient for now.

ACKNOWLEDGMENTS:
----
I would like to extend a very grateful thank you to everyone on the Stack Overflow thread for the ideas and specifically user zalew for the baseline of my code.

Additonally, I'd like to thank Paul Mayne and contributors for providing the steps to identify and remove dead links.

SOURCES:
----
http://stackoverflow.com/questions/748675/finding-duplicate-files-and-removing-them

http://paulmayne.org/blog/2007/11/how-to-remove-broken-or-dead-tracks-from-itunes/

Additionally, the raw HTML of Paul Mayne's solution is included in the repository.

s0r3-glitch section:
----
The paul mayne blog post is no longer available through the links, the direct html file is in this project so thank you to fiveohh for grabbing the pages html well it was still available. With out that the iTunes portion of this project would not have happened. As for 10/5/2020 the steps in paul mayne guide still work.

If fiveohh is reading this thank you for making this it saved me so much time cleaning out my over 4000 duplicate songs. If at any point in time you would like me to make this into a branch and make a murge request please contanct me and I will do it as soon as I see it. 

I ran this on my 11000 song library and experienced no problems with it. I have not gone and checked to see if any files were false positives but do not take this as a garentee that it wont make anything always back up your data.

Thanks to LXNN#4932 in the python discord for helping me fix the md5 hashing (line 64 and 65 in the project)

The origional project can be found here https://github.com/fiveohh/fix-duplicate-itunes-songs origional project written in python 2

I do not own any of this code and all parts of this code go to the respective owners.
