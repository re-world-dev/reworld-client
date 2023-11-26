
client_id = "1166066458644713563"  # Replace this with your own client id
stategame = "Playing"
detail = "Join RE:WORLD now !"
try:
    from discordrp import Presence
    import time
    import threading
    from libs import console
    def start_presence():
        try:
            with Presence(client_id) as presence:
                print("Connected")
                presence.set(
                    {
                        "state": stategame,
                        "details": detail,
                        "timestamps": {"start": int(time.time())},
                    }
                )
                print("Presence updated")

                while True:
                    time.sleep(15)
        except Exception as e:
            console.alert(f"An error occured in richpresence.py : {e}")
    def richpresence_set(state,details):
        stategame = state
        detail = details
 
    def start():
        thread_rich_presence = threading.Thread(target=start_presence)
        thread_rich_presence.start()

except Exception as e:
     console.alert(f"A error occured in richpresence.py : {e}")