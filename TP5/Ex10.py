#!/usr/bin/env python
# coding: utf-8

# In[1]:


import csv


def ajouter_contact():
    nom = input("Entrez le nom du contact : ")
    telephone = input("Entrez le numéro de téléphone : ")
    email = input("Entrez l'adresse email : ")

    with open('/content/drive/MyDrive/contacts.csv', mode='a', newline='') as fichier:
        writer = csv.writer(fichier)
        writer.writerow([nom, telephone, email])
    print("Contact ajouté avec succès !")


def afficher_contacts():
    try:
        with open('/content/drive/MyDrive/contacts.csv', mode='r') as fichier:
            reader = csv.reader(fichier)
            for ligne in reader:
                print(f"Nom: {ligne[0]}, Téléphone: {ligne[1]}, Email: {ligne[2]}")
    except FileNotFoundError:
        print("Aucun contact trouvé.")


def rechercher_contact():
    nom_recherche = input("Entrez le nom du contact à rechercher : ")
    trouve = False

    with open('/content/drive/MyDrive/contacts.csv', mode='r') as fichier:
        reader = csv.reader(fichier)
        for ligne in reader:
            if ligne[0].lower() == nom_recherche.lower():
                print(f"Nom: {ligne[0]}, Téléphone: {ligne[1]},  {ligne[2]}")
                trouve = True
                break

    if not trouve:
        print("Contact non trouvé.")


def supprimer_contact():
    nom_suppression = input("Entrez le nom du contact à supprimer : ")
    contacts = []

    with open('/content/drive/MyDrive/contacts.csv', mode='r') as fichier:
        reader = csv.reader(fichier)
        for ligne in reader:
         if ligne[0].lower() != nom_suppression.lower():
          contacts.append(ligne)

    with open('/content/drive/MyDrive/contacts.csv', mode='w', newline='') as fichier:
        writer = csv.writer(fichier)
        writer.writerows(contacts)
    print("Contact supprimé avec succès !")


def menu():
    while True:
        print("\n--- Gestion des Contacts ---")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Quitter")
        choix = input("Choisissez une option : ")

        if choix == '1':
            ajouter_contact()
        elif choix == '2':
            afficher_contacts()
        elif choix == '3':
            rechercher_contact()
        elif choix == '4':
            supprimer_contact()
        elif choix == '5':
            print("Au revoir !")
            break
        else:
            print("Option invalide. Veuillez réessayer.")


if _name_ == "_main_":
    menu()

