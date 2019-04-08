import sqlite3
import os.path
import csv

path = '''C:\\Users\\nick\\AppData\\Local\\Packages\\Microsoft.Windows.Photos_8wekyb3d8bbwe\\LocalState'''
database = '''MediaDb.v1.sqlite'''

dbpath = os.path.join(path,database)

#a naive implementation of the unicode collation for the database to be able to open
def collate_ncl(string1, string2):
    if string1 == string2:
        return 0
    elif string1 > string2:
        return 1
    else:
        return -1

db = sqlite3.connect(dbpath)
#unicode collation on the database
db.create_collation("NoCaseUnicode", collate_ncl)

albums_cursor = db.cursor()
albums_cursor.execute('''select Album_Name from Album''')
for row in albums_cursor:
    print(row[0])
db.close()

#the export function
#read albums
#for each album, output photos based on hash
#output csv with album and photo hash (& path, probably useful if you want it for later...)

#the import function
#create new albums in target system
#read csv export; for each line
    #create album if it doesn't exist
    #associate file with album (if found), updating the count of photos in the album

