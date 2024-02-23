# helena_haffner_chess_tournament_P4_24112023

## Lancement du programme (environnement virtuel activé)
```shell
python3 main.py
```

## Description du programme
Script permettant d'instancier des tournois d'échecs.
Par défaut, le nombre de round est fixé à 4.

Dans le fichier settings/settings.py il est possible de mettre AUTOCOMPLETE = True pour tester le programme sans avoir
à entrer chaque résultat à la main.
Dans ce même fichier ,il est également possible d'indiquer si on souhaite que les parties du premier tour soient 
déterminées aléatoirement ou en se basant sur les points globaux.

Le script utilise un système de base de données sous forme de json afin de conserver les informations de chaque tournoi
-- avec possibilité d'arrêter le script et de reprendre le tournoi un autre jour par exemple.

Le nombre de points accumulés au fil des tournoi par chaque joueur est compatibilisé dans le dossier global_players_list.
Le fichier s'y trouvant répertorie tous les joueurs ayant participés à au moins un tournoi.
Si, lors de l'enregistrement des joueurs participants au tournoi, l'un d'eux est déjà présent dans global_players_list,
alors les informations le concernant (nom de famille, prénom, date de naissance) seront automatiquement ajoutés dans 
les données du tournoi.

Le script gère le cas où le nombre de participants à un tournoi est impair et fait en sorte que chacun saute un tour à
tour de rôle.

## Flake8
Afin de vérifier que le projet respecte bien la PEP8, il est possible d'utiliser la commande ci-dessous:
```shell
flake8
```


Bien que Poetry soit l'environnement virtuel utilisé pour le développement, un fichier **requirements.txt** est présent
dans les fichiers pour ceux ne souhaitant pas utiliser Poetry.


## Environnement Virtuel
Environnement Virtuel utilisé : Poetry

Installation:
```shell
curl -sSL https://install.python-poetry.org | python3 - 
```

Activer l'environnement virtuel : 
```shell
poetry shell
```
Installer les dépendances (les fichiers pyproject.toml ou poetry.lock doivent être présents dans le dossier et qui sont
l'équivalent de requirements.txt): 
```shell
poetry install 
```
Sortir de l'environnement virtuel : 
```shell
exit
```

## Lancer le programme sans activer l'environnement virtuel (mais celui-ci doit être installé)
Dans le terminal, à la racine du projet :
```shell
poetry run python3 main.py
```
