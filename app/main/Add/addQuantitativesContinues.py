
"""
	Le module ``Analyse de données quantitatives continues``
	========================================================
	
	
"""

def discretisation(nombreClasses, donneesContinues):
	"""Discrétise des données continues du paramètre.
	
	La fonction se charge de décomposer l’étendue [min ; max] de l’ensemble de données en ``nombreClasses`` intervalles de même étendue.
	Ensuite de remplacer les occurrences des données par l’intervalle auquel la donnée appartient.
	
	:param donneesContinues: liste de nombres flottants
	:return: liste d'intervalles
	
	"""
	
def calculNombreClasses(donneesContinues):
	"""Calcule le nombre de classes nécessaire à une discrétisation selon la règle de Sturges.
	
	:rtype: int
	
	.. warning:: Si la distribution n'est pas symétrique, le nombre de classes ne sera pas optimal.
	
	"""
	
def preparationIntervallesAnalyse(listeIntervalles):
	"""Prépare les données pour l’utilisation des éléments de calcul du module ADD quantitatives discrètes.
	
	Pour effectuer les analyses descriptives dans le cas continu, la démarche est la même (sauf quantiles) que pour le cas discret.
	On utilisera cependant comme données les centres des intervalles.
	
	:param listeIntervalles: liste issue de la discrétisation des valeurs.
	:return: liste de flottants.
	
	"""
	
def quantileContinu(ordre, listeFrequencesCumulees):
	"""Calcule les quantiles d'ordre ``ordre`` pour une analyse de données conitnues.
	
	Le quantile discret nous permet de retrouver le centre de l'intervalle qui contient le vrai quantile.
	Ensuite, à partir de l'intervalle et de l'ordre, on en déduit une valeur plus précise par interpolation linéaire.
	
	La fonction linéaire est définie à l'aide des bornes de l'intervalle, on  a besoin de deux points :
	L'ordonnée de la borne supérieure est la fréquence cumulée du centre de l'intervalle ( 1 si borne = max )
	L'ordonnée de la borne supérieure est la fréquence cumulée du centre de l'intervalle précédent ( 0 si borne = min )
	
	:return: le quantile d'ordre ``ordre``
	
	"""
	
def interpolationLineaire(p1, p2, y):
	"""Calcule l’abscisse par interpolation linéaire
	
	Les points ``p1``, ``p2`` nous permettent de définir une fonction linéaire.
	On retrouve ensuite l’abscisse du point d’ordonnée ``y`` se trouvant sur la courbe de la fonction.
	
	:return: abscisse de l'ordonnée ``y`` par rapport à la droite (``p1``, ``p2``)
	:rtype: float
	
	"""

# A faire plus tard
def infoDistributionContinue(listeEffectifs):
def infoDistributionCumulativeContinue(listeEffectifsCumulees):
