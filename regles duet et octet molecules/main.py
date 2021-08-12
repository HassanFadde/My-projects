class Atome():
    def __init__(self,name_atome):
        self.atomes=["H","He","Li","Be","B","C","N","O","F","Ne","Na","Mg","Al","Si","P","S","Cl","Ar"]
        if name_atome not in self.atomes:
            raise NameError (f"cet atome ({name_atome}) ne subit pas au regle d'octet ou du duet !! ou il n'existe pas !!")
        self.name_atome=name_atome
        self.name=name_atome
        self.nombre_atomique=self.atomes.index(name_atome)+1
        self.peut_entrer_molecule=self.nombre_atomique in[1,6,7,8,9,14,15,16,17]
        self.regle= "duet" if self.nombre_atomique<6 else "octet"
        if self.peut_entrer_molecule:
            if self.regle=="octet":
                if self.nombre_atomique>10:
                    self.nombre_electrons_couche_externe=self.nombre_atomique-10
                else:
                    self.nombre_electrons_couche_externe=self.nombre_atomique-2
                self.nombre_doublets=4
                self.doublets_liants=8-self.nombre_electrons_couche_externe
                self.doublets_non_liants=(2*self.nombre_electrons_couche_externe-8)//2
            else:
                self.nombre_electrons_couche_externe=1
                self.nombre_doublets=1
                self.doublets_liants=1
                self.doublets_non_liants=0
            self.liaisons=[None]*self.doublets_liants
            self.len=0
    def couche_externe_saturee(self):
        return self.len==self.doublets_liants
    def creer_doublet(self,autre_atome):
        if not autre_atome.peut_entrer_molecule :
            raise NameError("cette atome est invalide")
        if self.couche_externe_saturee():
            raise KeyError("couche externe est saturee !!")
        self.liaisons[self.len]=f"{autre_atome.name_atome}"
        self.len+=1
    def sup_doublet(self):
        self.liaisons[self.len-1]=None
        self.len-=1
    def __str__(self):
        return f"(name : {self.name_atome} , liaisons : {self.liaisons})"
class Molecule():
    def __init__(self,formule_chimique:str):
        integer=list(map(str,range(0,10)))
        maj_chars=list("A Z E R T Y U I O P M L K J H G F D S Q W X C V B N".split())
        min_chars=list("a z e r t y u i o p m l k j h g f d s q w x c v b n".split())
        index=0
        self.index={}
        self.atomes=[]
        while index<len(formule_chimique):
            if formule_chimique[index] in maj_chars:
                if index+1<len(formule_chimique) and formule_chimique[index+1] in min_chars:
                    name_atome=formule_chimique[index:index+2]
                    index+=1
                else:
                     name_atome=formule_chimique[index]
                num=[]
                while index+1<len(formule_chimique) and formule_chimique[index+1] in integer:
                    num.append(formule_chimique[index+1])
                    index+=1
                if num:
                    num=int("".join(num))
                else:
                    num=0
                atome=Atome(name_atome)
                if not atome.peut_entrer_molecule:
                    raise ValueError(f"{atome.name_atome} ne peut pas former une molecule subit au regle du duet ou l'octet !!")
                atome.name_atome=f"{atome.name_atome}1"
                self.atomes.append(atome)
                self.index[atome.name_atome]=len(self.atomes)-1
                for i in range(1,num):
                    atome=Atome(name_atome)
                    atome.name_atome=f"{atome.name_atome}{i+1}"
                    self.atomes.append(atome)
                    self.index[atome.name_atome]=len(self.atomes)-1
            index+=1
        self.isomeries=[]
        self.creer_la_molecule(self.atomes,result=self.isomeries)
        

    def lier(self,atome_1:Atome,atome_2:Atome):
        if type(atome_1)!=type(atome_2)or type(atome_1)!=Atome or atome_1==atome_2 or atome_1.couche_externe_saturee() or atome_2.couche_externe_saturee():
            raise KeyError("les atomes sont saturees ou indefinies !!")
        atome_1.creer_doublet(atome_2)
        atome_2.creer_doublet(atome_1)
    def delier(self,atome_1,atome_2):
        atome_1.sup_doublet()
        atome_2.sup_doublet()
    def couches_saturees(self):
        for atome in self.atomes:
            if not atome.couche_externe_saturee():
                return False
        return True
    def nur(self,atome1:str,atome2:str,situation:list)->int:
        result=0
        for case in situation:
            if (case[0].name_atome,case[1].name_atome)==(atome1,atome2) or (case[0].name_atome,case[1].name_atome)==(atome2,atome1):
                result+=1
        return result
    def is_accepted(self,formule):
        pass
    def creer_la_molecule(self,atomes,situation=[],result=[]):
        for index in range(1,len(atomes)):
            if len(self.atomes)>2 and atomes[0].doublets_liants==atomes[index].doublets_liants and self.nur(atomes[0].name_atome,atomes[index].name_atome,situation)==atomes[0].doublets_liants-1:
                continue
            self.lier(atomes[0],atomes[index])
            situation.append((atomes[0],atomes[index]))
            new_atomes=[]
            for atome in atomes:
                if not atome.couche_externe_saturee():
                    new_atomes.append(atome)
            self.creer_la_molecule(new_atomes,situation,result)
        if self.couches_saturees() and situation:
            to_append=[]
            for case in situation:
                to_append.append((case[0].name_atome,case[1].name_atome))
            result.append(to_append)
        if situation:
          edge=situation.pop()
          self.delier(edge[0],edge[1])
ll=Molecule("C6H12O6")
print(ll.index)