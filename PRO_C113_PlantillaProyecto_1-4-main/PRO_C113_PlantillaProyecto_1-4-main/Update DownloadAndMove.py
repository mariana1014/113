import sys
import time
import random

import os
import shutil
import logging

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "/Users/Kuttimma/Downloads"

# Clase Event Hanlder 
class FileEventHandler(FileSystemEventHandler):

    def on_created(self, event):
        print(f"¡Hola, {event.src_path} ha sido creado!")

    def on_deleted(self, event):
        print(f"¡Alguien borró {event.src_path}!")

    def on_modified(self, event):
        print(f"¡{event.src_path} ha sido modificado!")

    def on_moved(self, event):
        print(f"¡Alguien movió {event.src_path} a {event.dest_path}!")

        


# Inicia clase Event Handler 
event_handler = FileEventHandler()

# Inicia Observer
observer = Observer()

# Programa the Observer
observer.schedule(event_handler, from_dir, recursive=True)


#Comienza el Observer
observer.start()


#5 Escribe una excepción para keyboardInterrupt

while True:
    time.sleep(2)
    print("ejecutando...")
except keyboardInterrupt:
    print("¡detenido!")
    observer.stop()


