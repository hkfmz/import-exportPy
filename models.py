from datetime import datetime

from django.conf import settings
from django.db import models

from profils.models import ProfilModel, Profession, TaxesModel, Nationnalite


# Create your models here.

class AttestationModel(models.Model):
    name = models.CharField(verbose_name="Nom du modèle",max_length=50,help_text="nom du modèle d'attestation")
    link = models.CharField(verbose_name="Lien vérification",max_length=255,help_text="lien utilisé pour vérification du model",default="http://dgrp.cg/dgtt/check_atp/")
    small = models.CharField(verbose_name="Code article",max_length=10,help_text="le petit nom du modèle d'attestation",blank=True,null=True)
    upload = models.FileField(verbose_name="Fichier", upload_to='Models/%Y/%m/%d/', )

    isActif = models.BooleanField(verbose_name="Actif", default=True)
    create = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    last_update = models.DateTimeField(verbose_name="Last update", auto_now=True)
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="Attestation_Model_createby")
    update_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="Attestation_Model_updateby")

    class Meta:
        ordering = ('-create',)
        verbose_name = 'Modèle Attestation'
        verbose_name_plural = 'Modèle Attestation'.upper()

    def __str__(self):
        return self.name

class Attesta_vente(models.Model):
    GENRE = (
        ("M.", "M."),
        ("Mme", "Mme"),
        ("Mlle", "Mlle"),
    )

    profil = models.ForeignKey(ProfilModel, verbose_name="Profil Utilisateur", on_delete=models.CASCADE, null=True,blank=True)
    model = models.ForeignKey(AttestationModel, verbose_name="Attestation", on_delete=models.SET_NULL, null=True,
                              blank=True)
    Montant = models.BooleanField(verbose_name="Montant Achat", help_text="Montant de la transaction", default=0)

    civilite_v = models.CharField(verbose_name="Civilité Vendeur", max_length=5,choices=GENRE, default="M.")
    dateDelivre_v = models.DateField(verbose_name="Delivré le (Vendeur)", null=True,blank=True)
    numPiece_v = models.CharField(verbose_name="Numéro CNI/Passeport Vendeur", max_length=50, null=True,blank=True)
    vendeur = models.CharField(verbose_name="Identité du Vendeur",help_text="le nom et prénom du Vendeur",max_length=100,null=True,blank=True)
    nationalite_v = models.CharField(verbose_name="Nationalité du vendeur",help_text="La nationaité du vendeur",max_length=50, null=True,blank=True)
    bp_v = models.CharField(verbose_name="BP vendeur",help_text="Boite Postale du vendeur",max_length=100, null=True,blank=True)
    tel_v = models.CharField(verbose_name="Téléphone du vendeur",help_text="Numero de téléphone du vendeur",max_length=20, null=True,blank=True)
    niu_v = models.CharField(verbose_name="NIU",help_text="Le numéro du NUI",max_length=50, null=True,blank=True)
    profession_v = models.CharField(verbose_name="Profession",max_length=50, null=True,blank=True)
    adresse_v = models.CharField(verbose_name="Adresse vendeur", help_text="Adresse du vendeur", max_length=100,
                                       null=True, blank=True)
    # ====== Vehicule

    immatricule = models.CharField(verbose_name="Immatriculation", help_text="Immatriculation du vendeur",
                                   max_length=50, null=True, blank=True)
    genre_vehicule = models.CharField(verbose_name="Genre véhicule", max_length=40, null=True, blank=True)
    marque = models.CharField(verbose_name="Genre véhicule", max_length=50, null=True, blank=True)
    type = models.CharField(verbose_name="Type véhicule",max_length=50, null=True,blank=True)
    num_serie = models.CharField(verbose_name="N° dans la série du type",max_length=100, null=True,blank=True)
    num_chassis = models.CharField(verbose_name="N° du châssis",max_length=100, null=True,blank=True)
    num_moteur = models.CharField(verbose_name="N° du Moteur",max_length=100, null=True,blank=True)
    carrosserie = models.CharField(verbose_name="Carrosserie",max_length=100, null=True,blank=True)
    energie = models.CharField(verbose_name="Energie",max_length=100, null=True,blank=True)
    puissance = models.CharField(verbose_name="Puissance",max_length=100, null=True,blank=True)
    nb_place_assises = models.IntegerField(verbose_name="Nombre de place assises",default=0)
    poid = models.IntegerField(verbose_name="Poids total en charge",default=0)
    firt_circus = models.IntegerField(verbose_name="Année de première mise en circulation",default=0)

    # ====== Acheteur
    civilite_a= models.CharField(verbose_name="Civilité Achetteur",max_length=5, default="M.")
    nationalite_a = models.CharField(verbose_name="Nationalité de Acheteur", help_text="La nationaité du Acheteur",
                                           max_length=50, null=True, blank=True)
    numPiece_a = models.CharField(verbose_name="Numéro CNI/Passeport Acheteur", max_length=50, null=True, blank=True)
    dateDelivre_a = models.DateField(verbose_name="Delivré le (Acheteur)", null=True, blank=True)
    acheteur = models.CharField(verbose_name="Identité Acheteur", help_text="le nom et prénom du Vendeur",
                               max_length=100, null=True, blank=True)
    niu_a = models.CharField(verbose_name="NIU acheteur", help_text="Le numéro du NUI", max_length=50, null=True,
                                   blank=True)
    bp_a = models.CharField(verbose_name="BP Acheteur", help_text="Boite Postale de l'acheteur", max_length=100,
                                  null=True, blank=True)
    tel_a = models.CharField(verbose_name="Téléphone Acheteur", help_text="Numero de téléphone de l'acheteur",
                                   max_length=20, null=True, blank=True)
    adresse_a = models.CharField(verbose_name="Adresse vendeur", help_text="Adresse du vendeur", max_length=100,
                                 null=True, blank=True)





    isActif = models.BooleanField(verbose_name="Actif", default=True)
    create = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    last_update = models.DateTimeField(verbose_name="Last update", auto_now=True)
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="Attesta_vente_createby")
    update_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="Attesta_vente_updateby")

    class Meta:
        ordering = ('-create',)
        verbose_name = 'Attestation de Vente'
        verbose_name_plural = 'Attestation de Vente'.upper()

    def __str__(self):
        return self.name

class Cat_ATP(models.Model):
    name = models.CharField(verbose_name="Catégotie ATP",max_length=50)
    cout = models.BigIntegerField(verbose_name="Montant",default=0)
    T = models.IntegerField(verbose_name="Benéficière trésor",default=0)
    D = models.IntegerField(verbose_name="Benéficière DGTT",default=0)
    A = models.IntegerField(verbose_name="Benéficière ARPCE",default=0)
    M = models.IntegerField(verbose_name="Benéficière MAIRIE",default=0)
    C = models.IntegerField(verbose_name="Benéficière CODAMI",default=0)
    isActif = models.BooleanField(verbose_name="Actif", default=True)
    upload = models.FileField(verbose_name="copie Model", upload_to='ATP_Model/%Y/%m/%d/', null=True, blank=True)

    create = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    last_update = models.DateTimeField(verbose_name="Last update", auto_now=True)
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="cat_ATP_createby")
    update_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="cat_ATP_updateby")

    class Meta:
        ordering = ('-create',)
        verbose_name = 'Catégorie ATP'
        verbose_name_plural = 'Catégorie ATP'.upper()

    def __str__(self):
        return self.name

class ATP(models.Model):
    choix=[
        ("Petite entreprise","Petite entreprise"),
        ("Grande entreprise","Grande entreprise"),
        ("Entreprise artisanale","Entreprise artisanale"),
        ("Moyenne entreprise","Moyenne entreprise"),
           ]

    TYPE_ATP = (
        ("Voyageur","Voyageur"),
        ("Marchandise","Marchandise"),
    )
    zero = 0
    un = 1
    deux = 2
    trois = 3
    quatre = 4
    cinq = 5
    cent = 100
    cent_un = 101
    cent_deux = 102
    STATUT = (
        (zero, "Initial"),
        (un, "Etape 1"),
        (deux, "Etape 2"),
        (trois, "Etape 3"),
        (quatre, "Etape 4"),
        (cinq, "Terminée"),
        (cent_un, "Suspendue"),
        (cent_deux, "Echouée"),
    )

    profil = models.ForeignKey(ProfilModel, verbose_name="Profil Utilisateur", on_delete=models.SET_NULL, null=True,
                               blank=True)
    taxe = models.ForeignKey(TaxesModel, verbose_name="Taxe", on_delete=models.CASCADE)
    type_atp = models.CharField(verbose_name="Type ATP",choices=TYPE_ATP,default="Voyageur",max_length=20)
    # cat_apt = models.ForeignKey(Cat_ATP,verbose_name="Catégorie ATP",on_delete=models.SET_NULL,null=True,blank=True)
    nom = models.CharField(verbose_name='Nom du propriétaire', max_length=100, default="",)
    societe = models.CharField(verbose_name='Société', max_length=100, default="",blank=True, null=True)
    rccm = models.CharField(verbose_name='RCCM', max_length=100, default="",blank=True, null=True)
    niu = models.CharField(verbose_name='NIU', max_length=100, default="")
    cout = models.BigIntegerField(verbose_name='Coût', default=0)
    isPaid = models.BooleanField(verbose_name="Payée?", default=False)
    num_paid = models.CharField(verbose_name="Numéro Paiement",max_length=25,null=True,blank=True)
    adresse = models.CharField(verbose_name='Adresse', max_length=200, blank=True, null=True)
    adresse_complet = models.CharField(verbose_name='Adresse complète', max_length=200, blank=True, null=True)
    profession = models.ForeignKey(Profession, verbose_name="Profession", on_delete=models.SET_NULL,null=True)
    genre = models.CharField(verbose_name="Genre",max_length=50,null=True, blank=True)
    marque = models.CharField(verbose_name="Marque",max_length=30,null=True, blank=True)
    type = models.CharField(verbose_name="Type",max_length=30,null=True, blank=True)
    num_immatriculation = models.CharField(verbose_name="N° d’immatriculation ",max_length=100)
    zone_exploitation = models.CharField(verbose_name="Zone d’exploitation",max_length=100,null=True, blank=True)
    tv = models.BooleanField(verbose_name="TV",default=False)
    tvm = models.BooleanField(verbose_name="TVM",default=False)
    taxi = models.BooleanField(verbose_name="Taxi",default=False)
    tm = models.BooleanField(verbose_name="TM",default=False)
    date_expire = models.DateField(verbose_name="Date d'expiration",null=True,default=datetime(day=31,month=12,year=datetime.now().year).date())
    location_vehicule = models.BooleanField(verbose_name="Location de Véhicule",default=False)
    transport_commun = models.BooleanField(verbose_name="Transport en Commun",default=False)
    vehicule_demenagement = models.BooleanField(verbose_name="Véhicule de Déménagement",default=False)
    autres = models.BooleanField(verbose_name="Autres",default=False)
    type_entreprise = models.CharField(verbose_name="Type d'entreprise",max_length=30,choices=choix,default= "Petite entreprise")
    upload = models.FileField(verbose_name="Copie Electronique", upload_to='ATP/%Y/%m/%d/', null=True, blank=True)
    statut = models.IntegerField(verbose_name="Statut", choices=STATUT, default=0)

    isActif = models.BooleanField(verbose_name="Actif", default=True)

    id_transact = models.BigIntegerField(verbose_name="ID Transact Paid", default=0)
    create = models.DateTimeField(verbose_name="Created", auto_now_add=True)
    last_update = models.DateTimeField(verbose_name="Last update", auto_now=True)
    create_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="ATP_createby")
    update_by = models.ForeignKey(settings.AUTH_USER_MODEL,
                                  null=True, blank=True, on_delete=models.SET_NULL,
                                  related_name="ATP_updateby")
    class Meta:
        ordering = ('-create',)
        verbose_name = 'ATP'
        verbose_name_plural = 'ATP'.upper()

    def __str__(self):
        return self.taxe.name





# class PermisConduireModel(models.Model):
#     GENRE = (
#         ("Mr", "Mr"),
#         ("Mme", "Mme"),
#         ("Mlle", "Mlle"),
#     )
#     TYPE_PIECE = (
#         ("Carte Nationale d'identité", "Carte Nationale d'identité"),
#         ("Passeport", "Passeport"),
#         ("Carte de Résident", "Carte de Résident"),
#         ("Permis de conduire", "Permis de conduire"),
#     )
#     CAT_PERMIS =(
#         ("A","A"),
#         ("B","B"),
#         ("C","C"),
#         ("D","D"),
#         ("E","E"),
#         ("F","F"),
#         ("G","G"),
#     )
#     profil = models.ForeignKey(ProfilModel, verbose_name="Profil Utilisateur", on_delete=models.SET_NULL, null=True,
#                                blank=True)
#     categorie_permis = models.CharField(verbose_name="Catégorie Permis",max_length=2,choices=CAT_PERMIS,default="B")
#     nom = models.CharField(verbose_name="Nom",max_length=50,)
#     prenom = models.CharField(verbose_name="Prénom",max_length=50,null=True,blank=True)
#     genre = models.CharField(verbose_name='Civilité', max_length=5, choices=GENRE, default="Mr")
#     naissance = models.DateField(verbose_name="Date de Naissance", null=True, blank=True)
#     nationnalite = models.ForeignKey(Nationnalite, verbose_name="Nationnalité",on_delete=models.SET_NULL,null=True)
#     lieu_naissance = models.CharField(verbose_name="Lieu de Naissance",max_length=50,null=True,blank=True)
#     type_PI = models.CharField(verbose_name="Type Pièce d'identité",choices=TYPE_PIECE,max_length=30,default="Carte Nationale d'identité")
#
#     num_piece = models.CharField(verbose_name="Numéro de la Pièce", max_length=100, default="")
#     niu = models.CharField(verbose_name='NIU', max_length=100, default="", null=True)
#     date_expiration = models.DateField(verbose_name="Date d'Expiration PI", null=True, blank=True)
#
#     profession = models.ForeignKey(Profession, verbose_name="Profession", on_delete=models.SET_NULL, null=True)
#     adresse = models.CharField(verbose_name='Adresse', max_length=200, blank=True, null=True)
#     but_vise = models.CharField(verbose_name="But Visé",max_length=50,null=True,blank=True)
#     nature_candidature = models.CharField(verbose_name="Nature Condidature", max_length=50,null=True,blank=True)
#     libre = models.CharField(verbose_name="Nature Condidature", max_length=50,null=True,blank=True)
#     officielle = models.CharField(verbose_name="Officielle", max_length=50,null=True,blank=True)









