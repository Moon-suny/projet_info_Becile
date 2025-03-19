# projet_info_Becile
Titre : Bécile Contre attaque

Thème : voyage à travers l’espace 

Histoire: un robot nain a perdu tous ses membres 
 à un jeu de cartes et se fait aider par une créature (nous) pour récupérer ces membres.
durant les trois mini-jeu.


Personnages:
tête robot nain appelé Bécile ( protagoniste )
créature végétale (Joueur)
Le Seigneur des Semelles ( méchant )


Fonctionnalité (suivie d’une parti classique du point de vu d’un joeur) :

intro (orange diagramme):
Le jeu commence avec un générique à la manière de la saga Star-wars dans laquelle on introduit un nain robot héroïque nommé Bécile, le nain Bécile. Bécile a fait fortune avec ses aventures mais celui-ci est addicte au jeu d’argent et il a tout perdu.
Le joueur tombe sur cette petite boite de conserve arrogante dans un sale état grignoté par des rats dans une ruelle sombre. (Le joueur est tu petite créature verte muette)


Une Boîte de dialogue s’ouvre proposant au joueur : “veux-tu l'aider ?“


		oui						            non
le rat sur sa tête s’en va et début du mini jeu		On recommence au début du jeu


le premier mini jeu (vert)


Dans ce mini-jeu, le joueur doit relier des câbles de la même couleur entre eux.
puis réussir à passer une carte dans un lecteur de carte.Et enfin on fait un jeu dans lequel on doit recopier le modèle de l’ordinateur sur un clavier de couleur.


fin du premier mini-jeu


Dialogue toujours dans la ruelle.

La tête nous dit:”haaaaa  j’ai plus de corps.pourquoi ma jambe se trouve à 2 années lumière. va chercher le reste maintenant!! “

joueur: *taper sa tête * ou *hmmmmm*

robot:” Aïe, VA CHERCHER MES MEMBRES ” ou “ ok je monte sur ton dos je te guide ”

Si première option : le robot continue de demander pour récupérer ces membres.
si deuxième option : animation black pearl qui voyages


2eme mini-jeu (violet) :

objectif : récupérer ces jambes face à un fétichiste qui a gardé ses pieds.

Le joueur doit  les récupérer et les deux doivent fuir le méchant.
pour cela le jeu se présente comme un subway surfer vu du-dessus (en 2D) 
avec des objectifs décroissants qui représentent la distance avec le bateau.

 fin 2ème mini-jeu. 

“au non j’ai oublié mes bras. allez on y retourne !”


3ème mini-jeu (bleu):
Notre créature doit esquiver les barils lancés par le méchant
jeux inspirer dans le style que “ mario contre don king kong “
récompense: les bras du robot nain.

fin du mini-jeu 3

le nain robot offre un sons dédicacer à la créature

générique de fin avec le son reçu par la créature dans les crédits.






Modélisation des donnée : 


Avancement dans les mini-jeux : 
Une liste principale qui sauvegarde l'avancée de différentes sauvegardes pour 3 joueurs différents. Les sauvegardes de chaque joueur sont implémentées en dictionnaire qui possède à ce jour 4 clés : Le nom de la sauvegarde choisi par le joueur ainsi qu’un booléen retraçant sont avancées pour chaque mini jeu.


High score mini jeu 3 : 
Le mini jeu 3 comme imaginer pour le moment aura un système de point permettant  un petit peu de compétition, afin de sauvegarder les meilleur score, un documents text est envisagé. Nous nous interrogeons sur le côté falsifiable de ce scoreboard mais n’étant qu’un ajout à notre jeu, cela ne nous paraît pas être important.
