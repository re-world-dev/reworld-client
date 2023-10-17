# LIBRARIES AND VAR CODE
#==============================================================================================================================
import os
import threading
import time
import yaml  # Importer la bibliothèque PyYAML
from libs import console
from libs import assetsconf

skypath = assetsconf.SKY_NORMAL_PATH

stop_threads = False
#==============================================================================================================================

# MODDING API CODE
#==============================================================================================================================
def error_log(text):
    console.error(text)

def sky_setsky(path):
    global skypath
    console.info(f"[RML] : Sky changed to {path}")
    skypath = path
def sky_getskypath():
    return skypath
#==============================================================================================================================

#==============================================================================================================================
# INJECTOR CODE
def execute_file(file_path, mod_directory):
    console.info(text=f"[RML] : Loading {file_path} in {mod_directory}")
    try:
        with open(file_path, "r") as file:
            file_content = file.read()
            exec(file_content, {'__file__': file_path, '__name__': '__main__', 'os': os, 'console': console})
    except FileNotFoundError:
        console.alert(text=f"[RML] : The file {file_path} does not exist.")
    except Exception as e:
        console.alert(text=f"[RML] : Error while executing the file {file_path}: {e}")

def process_list_file(yaml_file_path, mod_directory):
    try:
        with open(yaml_file_path, "r") as yaml_file:
            mod_data = yaml.load(yaml_file, Loader=yaml.FullLoader)

            # Vous pouvez maintenant accéder aux champs du fichier YAML comme ceci
            name = mod_data.get("Name")
            description = mod_data.get("Description")
            main_file = mod_data.get("main_file")

            # Utilisez les données comme vous le souhaitez
            console.info(f"Name: {name}")
            console.info(f"Description: {description}")
            console.info(f"Main File: {main_file}")

            # Ensuite, vous pouvez exécuter le fichier principal (main.py par exemple)
            execute_file(os.path.join(mod_directory, main_file), mod_directory)

    except FileNotFoundError:
        console.alert(text=f"[RML] : The file {yaml_file_path} does not exist.")
    except Exception as e:
        console.alert(text=f"[RML] : Error while processing {yaml_file_path}: {e}")
    console.info("[RML] : Loaded")
def scan_and_execute_mods(mods_directory):
    try:
        mods = os.listdir(mods_directory)
        for mod in mods:
            mod_path = os.path.join(mods_directory, mod)
            yaml_file_path = os.path.join(mod_path, "mod.yaml")  # Remplacez "mod.yaml" par le nom de votre fichier YAML
            if os.path.isfile(yaml_file_path):
                thread_mod = threading.Thread(target=process_list_file, args=(yaml_file_path, mod_path))
                thread_mod.start()
    except Exception as e:
        console.alert(text=f"[RML] : An error occurred: {e}")

def stop_mods():
    global stop_threads
    stop_threads = True
    console.alert("[RML] : Stopping all mod threads...")
    console.info(text="[RML] : if you are difficult to close the game taskkill the game with taskmanager ! ")
    for thread in threading.enumerate():
        if thread != threading.current_thread():
            thread.join()
    console.alert("[RML] : All mod threads stopped.")

def init():
    console.info("[RML] : Starting loading...")
    mods_directory = "mods"
    scan_and_execute_mods(mods_directory)
    
#==============================================================================================================================

