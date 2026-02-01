# A-MAZE-ING

*par wehan et eberling*

![Demo](https://filedn.eu/lqAABNUSgVkfRyevTm4sSpR/NEVER_DELETE_ALWAYS_ADD/Screencast%20from%2001-31-2026%2003_56_06%20PM.gif)

## Description

A-MAZE-ING est une application interactive de génération et de résolution de labyrinthes développée en Python. Le projet permet de créer des labyrinthes aléatoires de différentes tailles, de visualiser le chemin le plus court entre l'entrée et la sortie, et d'interagir avec le labyrinthe via un menu interactif.

L'application génère des labyrinthes parfaits (sans cycles) ou imparfaits (avec cycles), avec la possibilité d'inclure un motif "42" visible dans les labyrinthes suffisamment grands. Le système utilise un encodage hexadécimal pour représenter les murs des cellules et sauvegarde automatiquement le labyrinthe généré ainsi que le chemin de résolution dans un fichier de sortie.

## Features

- Generate random mazes using DFS algorithm
- Visualize the shortest path using BFS
- Interactive menu system
- Color customization options
- Real-time maze display
- Support for perfect and imperfect mazes
- Automatic 42 pattern integration (for mazes ≥14×10)
- Hex-encoded wall representation
- Automatic file output with maze, entry/exit, and solution path

## Requirements

- Python 3
- Linux/Unix system (uses termios for input handling)

## Instructions

### Installation

1. Clonez le dépôt ou téléchargez les fichiers du projet.

2. Installez les dépendances (optionnel, pour le linting) :
```bash
make install
```

Les dépendances incluent `flake8` et `mypy` pour le linting et la vérification de types.

### Utilisation de base

Lancez l'application avec un fichier de configuration :

```bash
python3 a_maze_ing.py <config_file>
```

Exemple :
```bash
python3 a_maze_ing.py config.txt
```

### Utilisation avec Makefile

Vous pouvez également utiliser le Makefile :

```bash
make run config.txt
```

### Menu interactif

Une fois l'application lancée, vous disposez d'un menu interactif :

- **[1] Generate maze** : Génère un nouveau labyrinthe avec les paramètres du fichier de configuration
- **[2] Show / Hide shortest path** : Affiche ou masque le chemin le plus court (ON/OFF)
- **[3] Change colors** : Change la couleur d'affichage du labyrinthe
  - Default (pas de couleur)
  - Red
  - Green
  - Yellow
- **[Q] Quit** : Quitte l'application (ou appuyez sur ESC)

### Fichier de configuration

Le fichier de configuration doit respecter la structure suivante :

```
# mandatory
WIDTH=50
HEIGHT=20
ENTRY=0,1
EXIT=10,14
OUTPUT_FILE=maze.txt
PERFECT=True
#SEED=42
```

#### Structure complète du fichier config

- **WIDTH** (obligatoire) : Largeur du labyrinthe en nombre de cellules (entier positif)
- **HEIGHT** (obligatoire) : Hauteur du labyrinthe en nombre de cellules (entier positif)
- **ENTRY** (obligatoire) : Coordonnées de l'entrée au format `ligne,colonne` (tuple d'entiers)
- **EXIT** (obligatoire) : Coordonnées de la sortie au format `ligne,colonne` (tuple d'entiers)
- **OUTPUT_FILE** (obligatoire) : Nom du fichier de sortie où sera sauvegardé le labyrinthe
- **PERFECT** (obligatoire) : `True` pour un labyrinthe parfait (sans cycles), `False` pour un labyrinthe imparfait (avec cycles)
- **SEED** (optionnel) : Graine pour la génération aléatoire (entier). Si omis ou commenté, la génération sera non-déterministe
- **COLOR** (optionnel, géré par l'interface) : Couleur d'affichage (Default, Red, Green, Yellow)

**Notes importantes :**
- Les lignes commençant par `#` sont des commentaires
- Les coordonnées ENTRY et EXIT doivent être valides (dans les limites du labyrinthe)
- ENTRY et EXIT ne peuvent pas être identiques
- Les coordonnées sont indexées à partir de 0

### Format de sortie

Le fichier de sortie contient :
1. **Grille du labyrinthe** : Chaque ligne représente une rangée de cellules, chaque caractère hexadécimal représente les murs d'une cellule
   - `0` = aucun mur ouvert
   - `1` = mur nord ouvert
   - `2` = mur est ouvert
   - `3` = murs nord et est ouverts
   - `4` = mur sud ouvert
   - `5` = murs nord et sud ouverts
   - `6` = murs est et sud ouverts
   - `7` = murs nord, est et sud ouverts
   - `8` = mur ouest ouvert
   - `9` = murs nord et ouest ouverts
   - `a` = murs est et ouest ouverts
   - `b` = murs nord, est et ouest ouverts
   - `c` = murs sud et ouest ouverts
   - `d` = murs nord, sud et ouest ouverts
   - `e` = murs est, sud et ouest ouverts
   - `f` = tous les murs ouverts
2. **Ligne vide**
3. **ENTRY** : Coordonnées de l'entrée au format `ligne,colonne`
4. **EXIT** : Coordonnées de la sortie au format `ligne,colonne`
5. **Chemin de résolution** : Séquence de directions (N, E, S, W) représentant le chemin le plus court

### Commandes Makefile

- `make install` : Crée un environnement virtuel et installe les dépendances
- `make run <config_file>` : Lance l'application avec le fichier de configuration spécifié
- `make lint` : Exécute flake8 et mypy pour vérifier le code
- `make lint-strict` : Exécute mypy en mode strict et flake8
- `make debug <config_file>` : Lance l'application en mode débogage avec pdb
- `make clean` : Supprime les fichiers de cache et l'environnement virtuel
- `make re` : Nettoie et réinstalle l'environnement

## Algorithme de génération

### Algorithme choisi : Depth-First Search (DFS)

Le projet utilise l'algorithme **Depth-First Search (DFS)** avec backtracking pour générer les labyrinthes.

#### Justification du choix

1. **Simplicité et efficacité** : DFS est un algorithme simple à implémenter et très efficace pour générer des labyrinthes parfaits (sans cycles).

2. **Garantie de connexité** : DFS garantit qu'il existe un chemin unique entre n'importe quelle paire de cellules dans un labyrinthe parfait, ce qui est une propriété souhaitable.

3. **Contrôle de la structure** : L'utilisation d'une pile (stack) permet un contrôle précis sur le processus de génération et facilite l'implémentation du backtracking.

4. **Performance** : La complexité temporelle est O(n) où n est le nombre de cellules, ce qui est optimal pour ce type de problème.

5. **Flexibilité** : L'algorithme peut facilement être étendu pour créer des labyrinthes imparfaits en ajoutant des ouvertures supplémentaires après la génération initiale.

#### Fonctionnement

1. **Initialisation** : Toutes les cellules sont initialement fermées (tous les murs sont présents).

2. **Point de départ** : Un point de départ aléatoire est choisi dans le labyrinthe.

3. **Exploration DFS** :
   - La cellule courante est marquée comme visitée
   - Les voisins non visités sont identifiés
   - Un voisin aléatoire est choisi
   - Le mur entre la cellule courante et le voisin choisi est supprimé
   - Le voisin devient la nouvelle cellule courante et est ajouté à la pile
   - Si aucun voisin n'est disponible, on fait un backtrack (retour en arrière) en dépilant

4. **Labyrinthe imparfait** : Si `PERFECT=False`, des ouvertures supplémentaires sont ajoutées aux impasses (cellules avec 3 murs) pour créer des cycles.

5. **Motif 42** : Si le labyrinthe est suffisamment grand (≥14×10), un motif "42" est intégré en marquant certaines cellules comme non accessibles.

### Algorithme de résolution : Breadth-First Search (BFS)

Pour trouver le chemin le plus court, le projet utilise **Breadth-First Search (BFS)**.

#### Justification

- BFS garantit de trouver le chemin le plus court dans un graphe non pondéré
- L'utilisation d'une file (queue) assure que tous les chemins de longueur k sont explorés avant ceux de longueur k+1
- Complexité O(n) où n est le nombre de cellules

## Partie réutilisable

### Module `mazegen`

Le package `mazegen` est conçu pour être réutilisable dans d'autres projets. Il contient :

- **`MazeManager`** (`mazegen/main.py`) : Classe principale pour gérer la génération et la manipulation de labyrinthes
- **`MazeCell`** (`mazegen/models.py`) : Modèle de données pour représenter une cellule de labyrinthe
- **`BFS`** (`mazegen/shortest_path.py`) : Classe pour calculer le chemin le plus court
- **`MazeRender`** (`mazegen/render.py`) : Classe pour le rendu et l'affichage des labyrinthes

### Comment utiliser le module dans un autre projet

1. **Importation** :
```python
from mazegen import MazeManager, BFS
from mazegen.models import MazeCell
from mazegen.render import MazeRender
```

2. **Création d'un labyrinthe** :
```python
config = {
    "WIDTH": 20,
    "HEIGHT": 10,
    "ENTRY": (0, 1),
    "EXIT": (9, 18),
    "OUTPUT_FILE": "my_maze.txt",
    "PERFECT": True,
    "SEED": 42,
    "COLOR": "Default"
}

mm = MazeManager(config)
mm.generate_maze_dfs()
```

3. **Calcul du chemin le plus court** :
```python
bfs = BFS()
path = bfs.shortest_path(
    maze=mm.maze,
    height=mm.height,
    width=mm.width,
    start=mm.entry,
    end=mm.exit
)
```

4. **Affichage du labyrinthe** :
```python
mm.print_maze(path)
```

5. **Accès aux données** :
```python
# Accéder à une cellule spécifique
cell = mm.get_maze_cell_from_coordinate((5, 5))

# Obtenir tous les voisins disponibles d'une cellule
neighbors = mm.get_neighbor_cells(cell, available_coords)
```

### Exemple d'utilisation autonome

```python
from config_loader import get_config
from mazegen import MazeManager, BFS

# Charger la configuration
config = get_config("config.txt")

# Créer et générer le labyrinthe
maze_manager = MazeManager(config)
maze_manager.generate_maze_dfs()

# Calculer le chemin
bfs = BFS()
path = bfs.shortest_path(
    maze=maze_manager.maze,
    height=maze_manager.height,
    width=maze_manager.width,
    start=maze_manager.entry,
    end=maze_manager.exit
)

# Afficher
maze_manager.print_maze(path)
```

## Resources

### Références utilisées

- **Algorithmes de génération de labyrinthes** : Documentation sur DFS et backtracking pour la génération de labyrinthes
- **Breadth-First Search** : Algorithmes de parcours de graphes pour la résolution de labyrinthes
- **Encodage hexadécimal** : Système de représentation des murs des cellules (4 bits : nord, est, sud, ouest)
- **Termios (Python)** : Documentation pour la gestion de l'entrée clavier non-bloquante sur Linux/Unix

### Usage de l'IA

L'IA a été utilisée pour :
- **Assistance au développement** : Aide à la structuration du code et à la résolution de bugs
- **Documentation** : Génération de docstrings et commentaires explicatifs
- **Tests et validation** : Vérification de la logique des algorithmes
- **Optimisation** : Suggestions d'amélioration de la performance et de la lisibilité du code

## Gestion d'équipe et planification

### Répartition des tâches

- **wehan** :
  - Implémentation de l'algorithme DFS de génération de labyrinthes
  - Gestion du motif 42 et des labyrinthes imparfaits
  - Système de rendu et affichage du labyrinthe
  - Encodage hexadécimal et sauvegarde dans le fichier de sortie

- **eberling** :
  - Implémentation de l'algorithme BFS pour le chemin le plus court
  - Système de menu interactif et gestion des entrées utilisateur
  - Chargement et validation du fichier de configuration
  - Intégration des couleurs et personnalisation de l'affichage

### Planification du projet

1. **Phase 1 - Structure de base** :
   - Définition de la structure du projet et des modèles de données
   - Implémentation de `MazeCell` et structure de base du labyrinthe

2. **Phase 2 - Génération** :
   - Implémentation de l'algorithme DFS
   - Gestion des labyrinthes parfaits et imparfaits
   - Intégration du motif 42

3. **Phase 3 - Résolution** :
   - Implémentation de BFS pour trouver le chemin le plus court
   - Conversion du chemin en directions (N, E, S, W)

4. **Phase 4 - Interface utilisateur** :
   - Développement du menu interactif
   - Gestion des entrées clavier non-bloquantes
   - Système de couleurs et personnalisation

5. **Phase 5 - Configuration et sortie** :
   - Parser de fichier de configuration
   - Validation des paramètres
   - Encodage hexadécimal et sauvegarde du fichier de sortie

6. **Phase 6 - Finalisation** :
   - Tests et débogage
   - Documentation et README
   - Optimisation et nettoyage du code

### Outils de développement

- **Version control** : Git pour la gestion des versions
- **Linting** : flake8 pour la vérification du style de code
- **Type checking** : mypy pour la vérification des types
- **Environnement virtuel** : venv pour l'isolation des dépendances
- **Makefile** : Automatisation des tâches courantes

## Authors

by wehan and eberling
