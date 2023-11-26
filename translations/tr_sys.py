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
            "menu.play.return.tooltip": "Return to home menu"
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
            "menu.play.return.tooltip": "Retourner à l'accueil"
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