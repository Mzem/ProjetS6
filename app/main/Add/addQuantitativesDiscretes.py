
"""
	Le module ``Analyse de données quantitatives discrètes``
	========================================================
	
	
	
"""

def moyenne(listeEffectifs):
	"""Calcule la moyenne."""
	
def quantileDiscret(ordre, listeFrequencesCumulees):
	"""Calcule le quantile d'ordre ``ordre``.
	
	:param ordre: Nombre flottant compris entre 0 et 1.
	:return: La première valeur telle que la fréquence cumulée correspondante soit supérieure ou égale à l'ordre
	
	.. note:: La médiane est le quantile d'ordre 1/2.
	"""
	
def variance(listeEffectifs):
	"""Calcule la variance."""
	
def ecartType(variance):
	"""Calcule l'écart-type."""
	return sqrt(variance)
	
def anomaliesTukey(listeEffectifs):
	"""Liste les valeurs aberrantes de la liste.
	
	Une valeur est dite aberrante selon la règle de Tukey si elle n'appartient pas à un intervalle I définit tel que :
	I = [Q1 - k * IQ ; Q3 + k * IQ  ] , k constante réelle Q1 et Q3 les quartiles, IQ l'écart inter-quartiles.
	
	La constante k est choisie arbitrairement égale à 1,5. La valeur 1.5 est selon Tukey une valeur pragmatique, qui a une raison probabiliste.
	Si une variable suit une distribution normale, alors la zone délimitée par la boîte et les moustaches devrait contenir 99,3 % des observations.
	
	:rtype: list
	:return: Collection contenant les données anormales pour la distribution des valeurs.
	
	"""

def symetrie(listeEffectifs):
	"""Calcule le coefficient de symétrie de Pearson.
	
	Si le coefficient est nul, la distribution est symétrique.
	Si le coefficient est positif, la distribution est étalée sur la droite.
	Si le coefficient est négatif, la distribution est étalée sur la gauche.
	
	
	:rtype: float
	:return: Valeur comprise entre -1 et 1.
	
	"""
	
def aplatissement(listeEffectifs):
	"""Calcule le coefficient d'aplatissement de Fisher.
	
	Si le coefficient est nul, la distribution suit une loi normale centrée réduite.
	Si le coefficient est inférieur à 3, la distribution est aplatie.
	Si le coefficient est supérieur à 3, les valeurs de la distribution est concentrée autour de la moyenne.
	
	:rtype: float
	
	"""
	

# A faire plus tard
def infoDistributionDiscrete(listeEffectifs):
def infoDistributionCumulativeDiscrete(listeEffectifsCumules):
def infoBoiteTukey(listeEffectifs):
def infoSerieTemporelle(listeSerieTemporelle):
