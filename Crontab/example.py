from datetime import datetime
myFile = open('/home/khoa/Documents/Test/Crontab/append.txt', 'a')
myFile.write('\nAccessed on ' + str(datetime.now()))