# https://openclassrooms.com/fr/courses/7150616-apprenez-la-programmation-orientee-objet-avec-python/7195400-ecrivez-une-classe-python 
class Toolbox:
    """
    Classe : boite à ouils
        Variables :
        -- tools : les outils présents dans la caisse à outil

        Méthodes :
        -- add_tool : ajoute un outil dans la boite à outils
        -- remove_tool : enlève un outil de la boite à outils   
    """
    def __init__ (self):
        """Initialise la caisse à outils."""
        self.tools = []
        
    
    def add_tool (self, tool) :
        """Ajoute un outil."""
        pass
    
    
    def remove_tool (self, tool) :
        """Enlève un outil."""
        pass
    
class Screwdriver:
    """
     Classe : Tournevis
        Variables :
        -- size : taille en mm de l'embout du tournevis

        Méthodes :
        -- tighten (screw) : serre la vis 'screw'
        -- loosen (screw) : desserre la vis 'screw'
    """
    def __init__ (self, size):
        """Initialise la taille du tournevis."""
        self.size = size
    
    def tighten (self, screw) :
        """Serre la vis."""
        pass
    
    def loosen (self, screw) :
        """Desserre la vis."""
        pass
    
    
 class Hammers:
    """
    Classe : Marteaux
        Variables :
        -- color : la couleur du marteau

        Méthodes :
        -- hammer_in(nail) : plante un clou
        -- remove(nail) : enlève un clou
    """
    def __init__ (self, color = "Red"):
        """Initialise la couleur du marteau (en rouge par défaut)."""
        self.color = color
 
    def paint (self, color) :
        """Plante le clou."""
        pass
    
    def hammer_in (self, nail) :
        """Plante le clou."""
        pass

    def remove (self, nail) :
        """Enlève le clou."""
        pass
    
 
 
