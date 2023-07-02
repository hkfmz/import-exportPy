import resources

class Base_locale_vehiculeResource(resources.ModelResource):

    class Meta:
        model = Base_locale_vehicule

class Agrements_modelsResource(resources.ModelResource):

    class Meta:
        model = Agrements_models

class Def_AgrementsResource(resources.ModelResource):

    class Meta:
        model = Def_Agrements

class ActiviteTaxeResource(resources.ModelResource):

    class Meta:
        model = ActiviteTaxe

class Benefiere_tagResource(resources.ModelResource):

    class Meta:
        model = Benefiere_tag

class Def_ActiviteTaxeResource(resources.ModelResource):

    class Meta:
        model = Def_ActiviteTaxe

class GroupeTaxesResource(resources.ModelResource):

    class Meta:
        model = GroupeTaxes

class Groupes_TaxesResource(resources.ModelResource):

    class Meta:
        model = Groupes_Taxes

class Actions_TaxeAgentResource(resources.ModelResource):

    class Meta:
        model = Actions_TaxeAgent

class Taxes_modelsResource(resources.ModelResource):

    class Meta:
        model = Taxes_models

class CodificationResource(resources.ModelResource):

    class Meta:
        model = Codification

class Model_DocumentsResource(resources.ModelResource):

    class Meta:
        model = Model_Documents

class Document_ProfilResource(resources.ModelResource):

    class Meta:
        model = Document_Profil

class CouleursResource(resources.ModelResource):

    class Meta:
        model = Couleurs

class ResourcesResource(resources.ModelResource):

    class Meta:
        model = Resources

class Type_VehiculeResource(resources.ModelResource):

    class Meta:
        model = Type_Vehicule

class Marque_vehiculeResource(resources.ModelResource):

    class Meta:
        model = Marque_vehicule

class Modele_vehiculeResource(resources.ModelResource):

    class Meta:
        model = Modele_vehicule

class Genre_vehiculeResource(resources.ModelResource):

    class Meta:
        model = Genre_vehicule

class VehiculeResource(resources.ModelResource):

    class Meta:
        model = Vehicule

class Num_ImmatriculationResource(resources.ModelResource):

    class Meta:
        model = Num_Immatriculation

class ImmatriculationsResource(resources.ModelResource):

    class Meta:
        model = Immatriculations

class Changement_couleurResource(resources.ModelResource):

    class Meta:
        model = Changement_couleur

class Taxes_qualification_vehiculeResource(resources.ModelResource):

    class Meta:
        model = Taxes_qualification_vehicule

class Taxes_qualification_profilResource(resources.ModelResource):

    class Meta:
        model = Taxes_qualification_profil

class Agrement_qualification_profilResource(resources.ModelResource):

    class Meta:
        model = Agrement_qualification_profil

class Taxes_paidResource(resources.ModelResource):

    class Meta:
        model = Taxes_paid

class Agrement_paidResource(resources.ModelResource):

    class Meta:
        model = Agrement_paid

