
"""
	Le module ``intervalle``
	========================
	
	Ce module pour une manipulation réduite des intervalles dans R.
	
	:Example:
	
	>>>from add import intervalle
	>>>i = Intervalle(0, 1, true ,false)
	>>>i.contient(0.8)
	True
	
	L'intervalle i de l'exemple sert à représenter [0, 1[ en notation mathématiques.
	
	
"""

class Intervalle(object):
	"""Ensemble d'objets pour représenter les intervalles de R.
	
	Attributs:
		borneInf (float): borne inférieure de l'intervalle
		borneSup (float): borne supérieure de l'intervalle
		infInclus (boolean): indique si la borne inférieure est comprise ou non dans l'intervalle
		supInclus (boolean): indique si la borne supérieure est comprise ou non dans l'intervalle
		centre (float): centre de l'intervalle
		
	"""
	
	def __init__(self, borneInf, borneSup, infInclus, supInclus):
		"""Constructeur de la classe.
		
		Initialise les attributs des paramètres données.
		
		Calcule le centre de l'intervalle et initialise l'attribut ``centre`` avec cette valeur.
		
		"""
		self.borneInf = borneInf
		self.borneSup = borneSup
		self.infInclus = infInclus
		self.supInclus = supInclus
		self.centre = (borneInf + borneSup) / 2
		
	def contient(self, nombre):
		"""Retourne vrai si l'argument appartient à l'intervalle, faux sinon"""
		if nombre == borneInf:
			return infInclus
		elif nombre == borneSup:
			return supInclus
		else:
			return nombre > borneInf and nombre < borneSup

def rechercheIntervalle(intervalles, nombre):
	"""Retrouve l'intervalle contenant un nombre en parmaètre
	
	Les intervalles de la liste sont distincts.
	Les intervalles de la liste forment une partition de l'étendue qu'ils représentent et sont triés.
	Ainsi, le nombre (on suppose qu'il appartient à l'étendue) appartient à un unique intervalle de la liste.
	
	Exemple:
		etendue = [1, 3]
		l = { [0, 1[ ; [1, 2[ ; [2, 3] }
		
	On exploite la liste triée avec une recherche dichotomique.
		
	:return: retourne l'intervalle auquel ``nombre`` appartient.
	
	"""
	i = len(intervalles) / 2
	while len(intervalles) > 0:
		if intervalles[i].contient(nombre):
			break
		elif nombre < intervalles[i].borneInf:
			intervalles = intervalles[0 : i - 1]
			i = (i - 1) / 2
		else:# nombre > intervalles[i].borneSup
			intervalles = intervalles[i + 1 :] #de l'indice i + 1 à la fin de la liste
			i = ((i + 1) + (len(intervalles) - 1)) ∕ 2

	return intervalles[i]
