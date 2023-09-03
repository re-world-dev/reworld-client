import os
import threading
import time
from libs import console
.
# Global variable to signal threads to stop
stop_threads = False

def error_log(text):
    console.error(text)

def execute_file(file_path, mod_directory):
    console.info(text=f"RML : Loading {file_path} in {mod_directory}")
    try:
        with open(file_path, "r") as file:
            file_content = file.read()
            exec(file_content, {'__file__': file_path, '__name__': '__main__', 'os': os, 'console': console})
    except FileNotFoundError:
        console.alert(text=f"RML : The file {file_path} does not exist.")
    except Exception as e:
        console.alert(text=f"RML : Error while executing the file {file_path}: {e}")
def process_list_file(list_file_path, mod_directory):
    try:
        with open(list_file_path, "r") as list_file:
            for line in list_file:
                if stop_threads:
                    break

                line = line.strip()  # Supprime les espaces et les sauts de ligne
                if not line.startswith("#"):  # Ignore les lignes commençant par "#"
                    file_to_execute = line
                    if file_to_execute.endswith(".py"):
                        execute_file(os.path.join(mod_directory, file_to_execute), mod_directory)
                    else:
                        console.alert(text=f"Skipping non-Python file: {file_to_execute}")
    except FileNotFoundError:
        console.alert(text=f"RML : The file {list_file_path} does not exist.")
    except Exception as e:
        console.alert(text=f"RML : Error while processing {list_file_path}: {e}")


def scan_and_execute_mods(mods_directory):
    try:
        mods = os.listdir(mods_directory)
        for mod in mods:
            mod_path = os.path.join(mods_directory, mod)
            list_txt_path = os.path.join(mod_path, "list.txt")
            if os.path.isfile(list_txt_path):
                thread_mod = threading.Thread(target=process_list_file, args=(list_txt_path, mod_path))
                thread_mod.start()
    except Exception as e:
        console.alert(text=f"RML : An error occurred: {e}")

def stop_mods():
    global stop_threads
    stop_threads = True
    console.alert("RML : Stopping all mod threads...")
    console.info(text="RML : if you are difficult to close the game taskkill the game with taskmanager ! ")
    for thread in threading.enumerate():
        if thread != threading.current_thread():
            thread.join()
    console.alert("RML : All mod threads stopped.")

def init():
    console.info("RML : Starting loading...")
    mods_directory = "mods"
    scan_and_execute_mods(mods_directory)
    console.info("RML : Loaded")

# Example usage:
# To stop all mod threads, call stop_mods()
# stop_mods()


