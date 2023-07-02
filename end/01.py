import resources

class IntegerRangeFieldResource(resources.ModelResource):

    class Meta:
        model = IntegerRangeField

class Secteur_activiteResource(resources.ModelResource):

    class Meta:
        model = Secteur_activite

class NationnaliteResource(resources.ModelResource):

    class Meta:
        model = Nationnalite

class ProfessionResource(resources.ModelResource):

    class Meta:
        model = Profession

class PaysResource(resources.ModelResource):

    class Meta:
        model = Pays

class RegionResource(resources.ModelResource):

    class Meta:
        model = Region

class ArrondissementResource(resources.ModelResource):

    class Meta:
        model = Arrondissement

class DirectionsModelResource(resources.ModelResource):

    class Meta:
        model = DirectionsModel

class type_entrepriseResource(resources.ModelResource):

    class Meta:
        model = type_entreprise

class ProfilModelResource(resources.ModelResource):

    class Meta:
        model = ProfilModel

class Verificateur_DOCResource(resources.ModelResource):

    class Meta:
        model = Verificateur_DOC

class ProfilMembreResource(resources.ModelResource):

    class Meta:
        model = ProfilMembre

class Pre_ProfileResource(resources.ModelResource):

    class Meta:
        model = Pre_Profile

class CategorieModelResource(resources.ModelResource):

    class Meta:
        model = CategorieModel

class TaxesModelResource(resources.ModelResource):

    class Meta:
        model = TaxesModel

class Profil_TaxeResource(resources.ModelResource):

    class Meta:
        model = Profil_Taxe

class Profil_CategorieResource(resources.ModelResource):

    class Meta:
        model = Profil_Categorie

class Categorie_TaxeResource(resources.ModelResource):

    class Meta:
        model = Categorie_Taxe

class Profil_ExonerationResource(resources.ModelResource):

    class Meta:
        model = Profil_Exoneration

class Type_partenaireResource(resources.ModelResource):

    class Meta:
        model = Type_partenaire

class PartenairesResource(resources.ModelResource):

    class Meta:
        model = Partenaires

class Partenaire_ExonerationResource(resources.ModelResource):

    class Meta:
        model = Partenaire_Exoneration

class Profil_NIUResource(resources.ModelResource):

    class Meta:
        model = Profil_NIU

class Profil_RCCMResource(resources.ModelResource):

    class Meta:
        model = Profil_RCCM

class Profil_PieceIdentiteResource(resources.ModelResource):

    class Meta:
        model = Profil_PieceIdentite

class Image_PUBLoginResource(resources.ModelResource):

    class Meta:
        model = Image_PUBLogin

class FonctionsResource(resources.ModelResource):

    class Meta:
        model = Fonctions

class AgentInterneResource(resources.ModelResource):

    class Meta:
        model = AgentInterne

class Managers_AgentResource(resources.ModelResource):

    class Meta:
        model = Managers_Agent

class Admin_AgentResource(resources.ModelResource):

    class Meta:
        model = Admin_Agent

class Historique_AgentResource(resources.ModelResource):

    class Meta:
        model = Historique_Agent

class ValideurDocResource(resources.ModelResource):

    class Meta:
        model = ValideurDoc

