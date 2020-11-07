# Rapport SMA Tri collectif multi-agents
## BRUNEAU Richard - VASLIN Pierre


## Introduction 

Nous avons décidé de lever la contrainte du sujet qui interdisait d'avoir un agent et un objet sur la même case afin de se placer dans le contexte de l'article. La représentation graphique dans ce genre de situation est explicité dans le README.md. 


## Réalisation 


### Question 1 

#### Implémentation

Dans un premier temps, nous avons suivi le sujet pour la prise et le dépôt d'un objet. Nous avons donc implémenté cette prise en se concentrant sur le voisinage de l'objet (cf. src/agent.py/proportionCalculationNeighborhood) en utilisant les formules indiquées dans le sujet.  

Après cette première implémentation, nous avons suivi l'article afin d'implémenter la prise et le dépôt en fonction de la mémoire uniquement. 

#### Outil d'analyse des résultats

Dans un premier temps, nous nous sommes aperçu visuellement que la prise de décision à l'aide de la mémoire était plus efficace que la méthode grâce à l'entourage. Afin de mesurer la différence entre les deux méthodes, nous avons calculé deux valeurs : 

- La première valeur est une valeur proche de la densité (cf. src/environnement.py/densityGlobal). Nous regardons autour de chaque objet si au sein de ses huit voisins il y a beaucoup d'objets. Cette valeur est importante si l'objet est entouré de huit autres objets. 

- Pierre : Dans un second temps nous avons utilisé le premier quartile afin de mesurer [TODO]

### Analyse des résultats

Nous avons lancé plusieurs executions afin de vérifier que les courbes de résultats ci-dessous ne sont pas des "accidents" et que les résultats reflètent bien le comportement des agents. 


[INSERTION DES IMAGES]


Comme vous pouvez le constater, 

brouillon : 
Avec la mémoire, meilleure résultat, mais le pic d'efficacité est plus lent à arriver

Sans mémoire, moins bon résultat, mais le seuil maximal est inférieur. 

Bien s'appuyer sur les graph et les valeurs pour analyser. 


### Question 2 

### Implémentation 

Dans cette deuxième partie du TP nous avons implémenté un pourcentage d'erreur (modifiable lors de l'appel de la fonction) afin de créer du bruit lors de la perception des objets. 

De plus, notre programme s'arrête quand un seuil de satisfaction est atteint ou, afin de limiter le temps d'exécution, au bout de 500 000 pas de temps, variable modifiable dans src/triCollectif.py/ variable stepDefault. Un pas de temps est un cycle perception/action de l'intégralité des agents. 


[TODO] : Analyser avec des bruits différents 

### Outils d'analyse des résultats

Comme lors de la question 1, nous nous sommes rapidement aperçu visuellement que les clusters étaient moins nombreux et donc plus gros. Afin de confirmer notre pensée nous avons utilisé les mêmes mesures que lors de la question précédente. En effet, avec des clusters plus important, notre densité est sensé augmenté car cela fait plus d'objet avec huit voisins. 

[TODO] Pierre : Justifier l'utilisation de la seconde mesure via le quartile. 

### Analyse des résultats

A nouveau, nous avons lancé plusieurs execution afin de s'assurer que les captures ci-dessous reflètent le comportement habituel des agents que nous avons implémenté. 

# TODO

Question 2 : Parler que les clusters sont plus gros, mais comporte un taux d'erreur important