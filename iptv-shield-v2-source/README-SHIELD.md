# IPTV Player HA — Nvidia Shield TV (prototype v2)

## Build APK
1. Mettre les fichiers de ce dossier à la racine d’un dépôt GitHub.
2. Dans Actions, lancer **Build Nvidia Shield TV APK** via **Run workflow**.
3. Télécharger l’artefact `iptv-shield-debug-apk` puis installer `app-debug.apk` sur la Shield.

## Changements
- Navigation directionnelle au clavier / télécommande et focus visible.
- Retour ferme les fenêtres de lecture/configuration.
- Correctif de création des sources vidéo selon extension.
- Catégorie Android TV Leanback et autorisation des serveurs HTTP (à restreindre en production).

## Limites importantes
- APK non compilé ni testé sur une vraie Shield dans cet environnement.
- Lecteur WebView/Video.js conservé; MPEG-TS et certains codecs peuvent échouer.
- Séries Xtream, stockage sécurisé des identifiants et durcissement des données HTML restent à développer.
- Le chargement des CDN exige Internet.
- APK debug à usage de test; une version finale doit être signée.
- Utiliser uniquement des sources IPTV pour lesquelles vous disposez des droits.
