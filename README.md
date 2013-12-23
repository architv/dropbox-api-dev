handlr
================================
handlr is an app which lets you download and upload content in your dropbox account.

first_app_1.0.py is the main file. Run it using the python interpreter and follow the instructions from there on.
The app uploads the text file 'file_to_be_uploaded' in your dropbox folder and downloads all the images from a specified folder on your system.


Changelog:
----------

1.  Now you have to only authenticate the app once. Subsequent usage doesn't require any authentication.

2.  The app now has the ability to upload the specified file in chunks, thus allowing uploads to resume on spotty connections.

3.  The app now allows you to download all the images in a specified folder of your dropbox directory. Only the files in that folder is downloaded and not the subfolders.

