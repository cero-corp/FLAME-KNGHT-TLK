class epeiste_mage () :
    
    #caractéristiques du joueurs
    def __init__(self, name, life, defense, swd_atk, stamina, mana_atk, atk = None):
        self.name = name
        self.life = life
        self.defense = defense
        self.swd_atk = swd_atk
        self.stamina = stamina
        self.mana_atk = mana_atk
        self.atk = atk
    
    def get_life(self) :
        return self.life
    
    def get_defense(self) :
        return self.get_defense
    
    def get_atk(self) :
        return self.atk
    
    def get_stamina(self) :
        return self.stamina
         
    def attack(self, ennemi):
        if self.atk == "sword" and self.stamina >= 2:
            self.attaque_epee(ennemi)
        elif self.atk == "mana" and self.stamina >= 3:
            self.attaque_magique(ennemi)   
        
    def attaque_epee(self, ennemi):
        # Dégâts de l'attaque à l'épée
        swd_dmg = self.swd_atk
        ennemi.get_dmg(swd_dmg)
        # Réduire l'endurance ou appliquer d'autres effets liés à l'attaque à l'épée
        self.stamina -= 2  #réduire l'endurance de 5 points
        
    def attaque_magique(self, ennemi):
        # Dégâts de l'attaque de mana    
        mana_dmg = self.mana_atk
        ennemi.get_dmg(mana_dmg)
        # Réduire l'endurance ou appliquer d'autres effets liés à l'attaque de mana
        self.stamina -= 3  #réduire l'endurance de 4 points
        
    def get_dmg(self, damage):
        # Réduit la vie du joueur
        self.life -= damage - self.defense
    