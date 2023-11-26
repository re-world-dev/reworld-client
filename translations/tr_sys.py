"""RE:WORLD translation system"""

class Translation(object):
    # the tr key must be : <system/class>.<subpart/method>.<element>.<(sub-element)>
    EN_EN = {
            "menu.home.play.button": "Play", 
            "menu.home.play.tooltip": "Start a new journey",
            "menu.home.exit.button": "Exit",
            "menu.home.exit.tooltip": "See you soon !",
            "menu.home.credits.button": "Credits",
            "menu.home.credits.tooltip": "Show credits", 

            "menu.play.title": "Select a game mode", 
            "menu.play.solo.button": "Solo",
            "menu.play.solo.tooltip": "Singleplayer", 
            "menu.play.multi.button": "Multiplayer",
            "menu.play.multi.tooltip": "Multiplayer mode",
            "menu.play.return.button": "Return",
            "menu.play.return.tooltip": "Return to home menu", 

            "menu.serverlist.title": "SERVER LIST", 
            "menu.serverlist.add.button": "Add a server", 
            "menu.serverlist.add.tooltip": "Add a new online game area !", 
            "menu.serverlist.return.button": "Return", 
            "menu.serverlist.return.tooltip": "Return to play menu", 

            "menu.connection.label.working": "Connecting...\nPlease wait.",
            "menu.connection.stop.button": "CANCEL", 

            "menu.connection.failed.label": "Failed to connect to the server:\n{0}", 
            "menu.connection.failed.button": "Return to serverlist", 

            "menu.servercreation.title": "ADD A SERVER",
            "menu.servercreation.add.button": "Add",
            "menu.servercreation.add.tooltip": "Add the server to your server list",
            "menu.servercreation.exit.button": "Return",
            "menu.servercreation.exit.tooltip": "Return to server list",

            "menu.credits.title.all": "CREDITS", 
            "menu.credits.title.dev": "Developpers : ",
            "menu.credits.title.music": "Music by : ", 
            "menu.credits.exit.button": "Return"
             }

    FR_FR = {
            "menu.home.play.button": "Jouer", 
            "menu.home.play.tooltip": "Commencer un nouveau voyage",
            "menu.home.exit.button": "Quitter",
            "menu.home.exit.tooltip": "A bientôt !",
            "menu.home.credits.button": "Crédits",
            "menu.home.credits.tooltip": "Montrer les crédits", 

            "menu.play.title": "Sélectionnez un mode de jeu", 
            "menu.play.solo.button": "Solo",
            "menu.play.solo.tooltip": "Un joueur", 
            "menu.play.multi.button": "Multijoueur",
            "menu.play.multi.tooltip": "Mode multijoueur",
            "menu.play.return.button": "Retour",
            "menu.play.return.tooltip": "Retourner à l'accueil", 

            "menu.serverlist.title": "LISTE DES SERVEURS", 
            "menu.serverlist.add.button": "Ajouter un serveur", 
            "menu.serverlist.add.tooltip": "Ajouter un nouvel espace de jeu en ligne !", 
            "menu.serverlist.return.button": "Retour", 
            "menu.serverlist.return.tooltip": "Retourner au menu de jeu", 

            "menu.connection.label.working": "Connexion en cour...\nVeuillez patienter.",
            "menu.connection.stop.button": "ANNULER", 

            "menu.connection.failed.label": "Echec de la connexion au server :\n{0}", 
            "menu.connection.failed.button": "Retour à la liste des serveurs", 

            "menu.servercreation.title": "AJOUTER UN SERVEUR",
            "menu.servercreation.add.button": "Ajouter",
            "menu.servercreation.add.tooltip": "Ajouter le serveur à votre liste des serveurs",
            "menu.servercreation.exit.button": "Retour",
            "menu.servercreation.exit.tooltip": "Retour à la liste des serveurs",

            "menu.credits.title.all": "CRÉDITS", 
            "menu.credits.title.dev": "Developpeurs : ",
            "menu.credits.title.music": "Musique de : ", 
            "menu.credits.exit.button": "Retour"
             }


    def __init__(self, lang="en_en"):
        self.lang = lang

    def gv_tr_dic(self):
        if self.lang == "en_en":
             return self.EN_EN
        elif self.lang == "fr_fr":
            return self.FR_FR
        else:
            raise TranslationException("An unknow language was gived.")

class TranslationException(Exception):
    pass