from sysexpert import Fait, BaseDeRegles, BaseDeFaits, AnalyseurSyntaxique, MoteurDInferance

def lire_regles(basederegles):
	basedefaits = BaseDeFaits()
	AnalyseurSyntaxique.analyse_fichier('regle_confex.txt', basedefaits, basederegles)

def lire_faits(dict_faits, basedefaits):
	for cle in dict_faits:
		basedefaits.ajouter(Fait(dict_faits[cle], True))

def recuperer_liste_metiers(dict_faits):
	basederegles = BaseDeRegles()
	basedefaits = BaseDeFaits()

	lire_regles(basederegles)
	lire_faits(dict_faits, basedefaits)

	liste_metiers = []
	moteur_d_inference = MoteurDInferance()
	
	# Pannes de la RAM
	valide = moteur_d_inference.chainage_avant(basedefaits, basederegles, Fait("PRA", True))
	if valide:
		liste_metiers.append(
			"Problème au niveau de la Ram : nous vous suggerons de remplacé une à une ou de la changer")

	# Pannes de la carte graphique
	valide = moteur_d_inference.chainage_avant(basedefaits, basederegles, Fait("PCG", True))
	if valide:
		liste_metiers.append(
			"Problème au niveau de carte graphique  : nous vous suggerons de la rechauffer votre carte ou de la changer")

	# Pannes du processeur
	valide = moteur_d_inference.chainage_avant(basedefaits, basederegles, Fait("PP", True))
	if valide:
		liste_metiers.append(
			"Problème au niveau du processeur : nous vous suggerons de bien connecter votre processeur ou de le changer")

	# Pannes de l'écran
	valide = moteur_d_inference.chainage_avant(basedefaits, basederegles, Fait("PE", True))
	if valide:
		liste_metiers.append(
			"Problème au niveau de l'écran' : nous vous suggerons de changer votre écran")

	# Pannes de la souris
	valide = moteur_d_inference.chainage_avant(basedefaits, basederegles, Fait("PS", True))
	if valide:
		liste_metiers.append(
			"Problème de souris  : nous vous suggerons de changer de souris")

	# Pannes du clavier
	valide = moteur_d_inference.chainage_avant(basedefaits, basederegles, Fait("PC", True))
	if valide:
		liste_metiers.append(
			"Problème de clavier : nous vous suggerons de changer de clavier")

	# Pannes du ventilateur
	valide = moteur_d_inference.chainage_avant(basedefaits, basederegles, Fait("PV", True))
	if valide:
		liste_metiers.append(
			"Problème au niveau du ventilateur : nous vous suggerons de la nettoyer ou de bien le connecter ou de le changer")

	# Pannes du disque dur
	valide = moteur_d_inference.chainage_avant(basedefaits, basederegles, Fait("PD", True))
	if valide:
		liste_metiers.append(
			"Problème au niveau du disque dur: nous vous suggerons de faire la formation en Sciences Infirmières à la FSS")

	# Pannes du chargeur
	valide = moteur_d_inference.chainage_avant(basedefaits, basederegles, Fait("PCH", True))
	if valide:
		liste_metiers.append(
			"Les métiers de la santé : nous vous suggerons de changer de disque dur")

	# Pannes de la ROM
	valide = moteur_d_inference.chainage_avant(basedefaits, basederegles, Fait("PRO", True))
	if valide:
		liste_metiers.append(
			"Problème de ROM : nous vous suggerons de changer votre mémoire")

	# Pannes du boitier d'alimentation
	valide = moteur_d_inference.chainage_avant(basedefaits, basederegles, Fait("PBA", True))
	if valide:
		liste_metiers.append(
			"Problème au niveau du boitier d'alimentation : nous vous suggerons de vérifier votre boitier d'alimentation ou de le changer")

	# Pannes du chipset
	valide = moteur_d_inference.chainage_avant(basedefaits, basederegles, Fait("PCH", True))
	if valide:
		liste_metiers.append(
			"Problème au niveau de chipset : nous vous suggerons de vérifier votre chipset")

	# Pannes de l'imprimante
	valide = moteur_d_inference.chainage_avant(basedefaits, basederegles, Fait("PIM", True))
	if valide:
		liste_metiers.append(
			"Problème au niveau de l'imprimante : nous vous suggerons de vérifier si vous etes connectés")

	# Pannes du bouton d'allumage
	valide = moteur_d_inference.chainage_avant(basedefaits, basederegles, Fait("PBa", True))
	if valide:
		liste_metiers.append(
			"Problème au niveau du bouton d'allumage : nous vous suggerons de changer de bouton d'allumage")

	# Pannes de la pile
	valide = moteur_d_inference.chainage_avant(basedefaits, basederegles, Fait("PPI", True))
	if valide:
		liste_metiers.append(
			"Problème au niveau de la pile : nous vous suggerons de changer votre pile ou de changer de machine")

	# Pannes de cablage
	valide = moteur_d_inference.chainage_avant(basedefaits, basederegles, Fait("PCA", True))
	if valide:
		liste_metiers.append(
		  "Problème de cablage : nous vous suggerons de vérifier votre cablage")
	return liste_metiers