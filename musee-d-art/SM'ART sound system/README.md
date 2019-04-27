# SM'ART SOUND SYSTEM

- Partenaire : Musée d'Art de Nantes

- Etudiants : 

	- Cuadros Nicolas
	- Marjault Antoine
	- Montagné Clara
	- Manoury Jules
	- Sannequin Violette
	- Graff Guillaume


- Technologie d'entrée : Capteurs de téléphone

- Technologie de sortie : Son spatialisé

  

# Peinture non morte

## Description

### Introduction et contexte

Ce projet vise à créer une escape room composée de quelques énigmes en utilisant uniquement un téléphone en entrée et des enceintes 5.1 en sortie afin de produire du son spatialisé.
Le Musée d'Art de Nantes nous a confié ce projet en nous proposant de répondre à la problématique suivante :

*Comment attirer et motiver les enfants et les adolescent à venir au musée pendant leur temps libre tout en leur permettant d'apprendre des choses sur l'art ?*

Ce projet a vu le jour lors du [ICreate 2019](https://projetICreate2019-1.wixsite.com/icreate19?fbclid=IwAR3sZtT69xuDUp60zoIqp_Ut2Em7cNhtB9y3uWBsRF6w7pOj3tiniH10_LM), une compétition de créativité et de développement rassemblant des élèves de l'école Polytechnique de l'Université de Nantes, de L'école de Design Nantes Atlantique ainsi qu'Audencia SciencesCom.

### Objectifs et énigmes proposés

Les énigmes sont centrées autour du tableau [L'Oiseleur accordant sa guitare (1757) de Jean-Baptiste Greuze](https://fr.wikipedia.org/wiki/Jean-Baptiste_Greuze).
Chaque énigme permet d'en apprendre plus sur le tableau afin d'en déceler le sens caché.

Les programmes qui composent ce projet permettent de mettre en place 5 énigmes :
- Sortir le téléphone d'un endroit sombre (boîte au centre d'une pièce)
- Scanner un tag NFC posé de préférence sur une guitare puis agiter le téléphone afin de jouer un son de guitare.
- Scanner 4 tags NFCs répartis sur divers objets (avec des tags piégés)
- Recomposer un code de cadenas diffusé de façon séquentielle via des sons spatialisés
- Retrouver l'auteur du tableau en *swapant* de gauche à droite des portraits et en reposant le téléphone dans un endroit sombre pour valider et terminer le jeu.

Chaque énigme est entrecoupée de séquences narratives audio permettant de faire avancer l'histoire.
Il y a également divers sons d'ambiance lors de la résolution d'énigme en lien avec l'énigme et l'histoire du tableau.
On peut participer à l'escape game seul ou en groupe jusqu'à 5 personnes (dans la limite de la place disponible dans la pièce).

Si vous souhaitez avoir un aperçu des vues de l'application vous pouvez consulter le [README de l'application](./SM_ART/README.md)

## Guide de réalisation et d’installation du projet

### Matériel nécessaire

- 1 smartphone sous Android
- 1 ordinateur Windows
- 7 tags NFC ou n'importe quel autre objet disposant d'une puce NFC

### Serveur de gestion du son

Pour cette partie rendez-vous dans le dossier ```SM_ART_SERVER/```.

#### Configuration des enceintes

Le serveur a été conçu pour fonctionner avec des enceintes 5.1 (Creative T6300 pour nos tests). Normalement les enceintes sont automatiquement détectées et utilisées en 5.1.

Si ce n'est pas le cas ou si les enceintes fonctionnent seulement en stéréo, rendez-vous sur ce [site](https://kcat.strangesoft.net/openal.html) afin de télécharger l'archive nommée *openal-soft-1.19.1-bin*.
Extraire les fichiers de l'archive et lancez dans une invite de commande Windows l'exécutable *openal-info64.exe*. Celui-ci va lister les périphériques audio disponibles, repérez alors vos enceintes. La ligne correspondante aux enceintes est de la forme ```OpenAL Soft on Haut-parleurs (USB Sound Device        )```.
Copiez la ligne associée et dans le fichier ```server.py``` effectuez les changements suivants :

```python
oalInit()
#Remplacer la ligne ci-dessus par la ligne suivante
oalInit(b"OpenAL Soft on Haut-parleurs (USB Sound Device        )")
```

#### Installation du serveur
Executez la commande suivante pour installer les packages nécessaires au fonctionnement du serveur.

```bash
pip3 install -r requirements.txt
```

#### Lancement du serveur
Pour lancer le serveur, executez la commande suivante.
```bash
python3 server.py
```
L'adresse IP et le port sur lequel écoute le serveur vont s'afficher, utilisez ces informations pour configurer le client (l'application mobile).

### Application android

#### Installation directe

L'application peut être retrouvée sous ce [dossier](./SM_ART/).
*L'application n'a été testé que sur des appareils android*.
##### Si vous êtes sur un ordinateur

Afin d'installer l'application vous pouvez utiliser directement l'APK fourni dans le [dossier correspondant](./SM_ART/apk), ensuite vous pouvez suivre le tutoriel [suivant](https://www.wondershare.com/fr/mobile-phone/installer-android-application.html) pour l'installer sur un téléphone.

##### Si vous êtes sur votre smartphone

Vous pouvez directement télécharger et installer l'application via ce [lien](https://github.com/CuadrosNicolas/ICreate2019-1/raw/master/SM_ART/apk/app-release.apk).

Attention, votre téléphone doit être muni de la technologie NFC.

#### Installation à partir des sources

Si vous souhaitez construire l'application par vous même il vous faut d'abord vous procurer [node js](https://nodejs.org/en/).

Ensuite dans le [dossier de l'application](./SM_ART), lancer la commande suivante :
```bash
npm install
```

Après cette étape il vous faudra également compiler le code en utilisant react-native, pour cela vous pouvez suivre le [tutoriel suivant](https://facebook.github.io/react-native/docs/running-on-device) afin de compiler le code.

Et finalement si vous souhaitez produire une version signée de l'application vous pouvez suivre [ce tutoriel](https://facebook.github.io/react-native/docs/signed-apk-android).

### Scène

![Alt text](img/inventaire_materiel.jpg?raw=true "Inventaire matériel")
![Alt text](img/ameublement_et_installation_technique.jpg?raw=true "Ameublement et installation technique")
![Alt text](img/placement_des_objets.jpg?raw=true "Placement des objets")

### Utilisation

Après avoir installé les programmes nécessaires et mis en place la scène, suivez les étapes suivantes afin de démarrer l'escape game :
- Lancez le serveur  via la commande ```python3 server.py``` sur un ordinateur puis relevez l'adresse IP affichée dans la console.
- Lancez l'application et utilisez le menu de configuration pour entrer l'adresse IP du serveur, vous devez aussi reconfigurer les IDs des tags NFC liés aux énimges via le menu *Tags*.
- Ensuite vous pouvez lancer directement la partie via le bouton "lancer la partie", attention , une fois lancé vous avez 3 secondes pour placer le téléphone dans l'endroit sombre de la première étape.
- Le jeu boucle sur lui même, une fois la dernière étape réalisée, le jeu retournera à la première étape.
