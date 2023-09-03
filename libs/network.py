authenfication_serverip = "pasdefini"



def ipcheck(ip): # Permet de verifier l'ip si elle est bans
    try:
        x = requests.get(f"http://127.0.0.1:5000/check_ip?ip={ip}")
       
        if x.text == "ok":
            return("ok")
        elif x.text == "banned":
            return("banned")
    except requests.exceptions.RequestException as e:
        alert(text=f"RE:Network request failed : {e}")
        pass