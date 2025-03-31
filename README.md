# Raspberry Pi - Projet Fil Rouge 1A SRI 2023/2024
![Python](https://img.shields.io/badge/python-blue)
![Status](https://img.shields.io/badge/status-terminé-green)

Ce dépôt contient le code exécuté sur le **Raspberry Pi** embarqué sur le robot explorateur, dans le cadre du **projet fil rouge 1A SRI (2023–2025)** à l’UPSSITECH Toulouse.  
Il agit comme un serveur local, transmettant le flux vidéo de la caméra ainsi que les données **LiDAR RPLIDAR A1** vers le backend Flask.

---

## 🎯 Objectif

- Capturer et transmettre en temps réel :
  - le **flux vidéo MJPEG** via HTTP
  - les **données LiDAR** via un serveur socket
- Offrir une API simple que le backend Flask peut consommer.

---

## ⚙️ Fonctionnalités principales

- Serveur **Flask** minimal pour le flux vidéo : `/video_feed`
- Serveur **TCP Socket** pour la diffusion des données LiDAR en JSON
- Gestion multi-thread : Flask + socket tournent en parallèle
- Compatible avec la détection et les modes de navigation côté backend

---

## 🧰 Stack technique

- **Langage** : Python 3.10
- **Librairies** :
  - `opencv-python` : capture et encodage vidéo
  - `flask`, `flask-cors` : serveur web léger
  - `socket`, `threading`, `json` : communication réseau
  - `rplidar` : acquisition depuis le capteur LiDAR

---

## 🔗 Dépendances

```bash
pip install flask flask-cors opencv-python rplidar
```

---

## 🚀 Lancer le projet sur le Raspberry Pi

1. **Connecter le LiDAR** au port `/dev/ttyUSB0`
2. Lancer le script `stream.py` :

```bash
python3 stream.py
```
Un script `launch_video_stream.sh` est fourni pour lancer automatiquement le stream au démarrage.

3. Le serveur :
   - exposera la **caméra** sur : `http://<raspberry_ip>:31000/video_feed`
   - ouvrira un port `12345` pour les **données LiDAR**

📅 Il est conçu pour fonctionner avec :
- [Interface Angular du robot](https://github.com/Bebel19/interface_robot_explorateur)
- [Backend Flask du robot](https://github.com/MaelaViguier/mobile_robot_backend)

---

## 🔧 Script d’automatisation (optionnel)

Un script `launch_video_stream.sh` est fourni pour lancer automatiquement le stream au démarrage.

```bash
chmod +x launch_video_stream.sh
./launch_video_stream.sh
```

---

**Projet universitaire ✨** — UPSSITECH Toulouse
