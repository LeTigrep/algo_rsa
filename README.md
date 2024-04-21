# Algorithme rsa 

## Présentation

Ce projet a été réalisé lors de mon M1 informatique en Sécurité et Théorie de l'information avec deux autre de mes camarades. 
Le but ici est de manipuler les clés RSA en créant une paire à l’aide de la
commande genrsa d’OpenSSL. Les opérations liées à ces clés seront exécutées via
des commandes terminal, englobant des fonctionnalités telles que la signature, le
chiffrement de données, et la création d’empreintes. Une seconde partie du projet
consiste à développer un code dans le langage de notre choix pour accomplir les
actions suivantes : génération et exportation des clés, chiffrement des messages, et
déchiffrement des messages (il n'y aura que la partie code visible dans ce dépôt git)

## Compilation

`rsa.py`

`rsa_bonus.py`

## Nos réalisations

Nous avons développé un code Python
pour encrypter un message avec une clé RSA. Les trois fonctions principales incluent la génération et l’exportation d’une paire de clés RSA, le chiffrement du
message avec la clé publique, et le déchiffrement du message avec la clé privée.
Ce code a passé avec succès des tests rigoureux, démontrant son efficacité et sa
fiabilité dans la génération de clés, le chiffrement et le déchiffrement des messages,
et confirmant ainsi sa conformité aux exigences du projet.

En bonus, nous avons ajouté une troisième partie à notre projet.
Ce code prend en entrée les entiers p, q, et e, génère
les clés privée et publique, et propose une fonction d’encryption. Cette fonction
calcule le ciphertext en élevant le message à la puissance de e et en prenant le
modulo n. De plus, une fonction de déchiffrement a été implémentée pour déchiffrer les messages encryptés. Cette extension renforce la polyvalence du projet en
offrant la possibilité de générer des clés personnalisées et de chiffrer/déchiffrer des
messages en utilisant ces clés.

## Difficultés Rencontrées

La partie la plus complexe du code a résidé dans l’implémentation de l’algorithme euclidien inverse, essentiel pour trouver la clé privée dans le bonus. Bien
que la résolution manuelle avec papier et stylo soit relativement simple, la transposition de la forme mathématique directe vers le code a exigé un effort considérable.
Trouver une relation cohérente entre les équations obtenues a été un défi, nécessitant une manipulation approfondie des formules. Après une période d’exploration,
nous avons réussi à établir une relation basée sur l’idée d’utiliser des couples (u,
v), où u représente le coefficient de phi et v le coefficient de e, pour parvenir à une
formulation adaptée au code.

