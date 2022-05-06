from os import access
from tkinter import Frame
from unicodedata import name
from unittest import result
from uuid import NAMESPACE_X500
import cv2
from cv2 import VideoCapture
import dropbox
import time
import random 

from numpy import number, take

start_time = time.time()

def take_snapshot():
    number = random.randint(0,100)
    VideoCaptureobj = cv2.VideoCapture(0)
    result = True
    while (result):
        ret , frame = VideoCaptureobj.read()
        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name , frame)
        start_time = time.time()
        result = False

    return img_name 
    print("snapshot taken")
    VideoCaptureobj.release()
    cv2.destroyAllWindows()



def upload_file(img_name):
    access_token = "sl.BHDC2ibIuxMYzadyljlbt9fsocQSqtQNyTmJ_HHq6u3OP6Vt3mGkq5wYwYQf-YBA9kDlGftn4rSQUyx1VakKIP2NsV7HM4bdKjha4iw-kg4TZ1FikBQ1KbC9Nk3I387Zqt5xxPQzoMI"
    file = img_name
    file_from = file 
    file_to = "/testfolder/" + (img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from , 'rb') as f :
        dbx.files_upload(f.read(), file_to , mode=dropbox.files.WriteMode.overwrite)
        print("File Uploaded")


def main():
    while(True):
        if((time.time() - start_time)>=5):
            name = take_snapshot()
            upload_file(name)



main()
