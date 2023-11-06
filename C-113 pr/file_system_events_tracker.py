import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/Kuttimma/Downloads"

# Event Hanlder Class
class FileEventHandler(FileSystemEventHandler):
    def on_created(self, event):

        name, extension = os.path.splitext(event.src_path)
       
        time.sleep(1)

        for key, value in dir_tree.items():
            time.sleep(1)

            if extension in value:

                file_name = os.path.basename(event.src_path)
               
                print("Downloaded " + file_name)

                path1 = from_dir + '/' + file_name
                path2 = to_dir + '/' + key
                path3 = to_dir + '/' + key + '/' + file_name

                if os.path.exists(path2):
                    print("Directory Exists...") 
                    time.sleep(1)
                    if os.path.exists(path3):
                        print("File Already Exists in " + key + "....")
                        print("Renaming File" + file_name +"....")
                        new_file_name = os.path.splitext(file_name)[0] + str(random.randint(0, 999)) + os.path.splitext(file_name)[1]
                        path4 = to_dir + '/' + key + '/' + new_file_name
                        print("Moving "+ new_file_name + "...")
                        shutil.move(path1, path4)
                        time.sleep(1)
                    else:
                        print("Moving " + file_name + "....")
                        shutil.move(path1, path3)
                        time.sleep(1)

                else:
                    print("Making Directory...")
                    os.makedirs(path2)
                    print("Moving " + file_name + "....")
                    shutil.move(path1, path3)
                    time.sleep(1)

    
        


# Initialize Event Handler Class
event_handler = FileEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)


# Start the Observer
observer.start()


#5_Write a exception for keyboardInterrupt
try:
 while True:
    time.sleep(2)
    print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()







