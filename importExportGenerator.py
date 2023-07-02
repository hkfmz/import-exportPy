import ast

def extract_class_names(file_path):
    class_names = []

    with open(file_path, "r") as file:
        tree = ast.parse(file.read())

        for node in ast.walk(tree):
            if isinstance(node, ast.ClassDef):
                if node.name != "Meta":
                    class_names.append(node.name)

    return class_names


def generate_import_exports_file(class_names):
    file_name = "import_exports.py"
    
    with open(file_name, "w") as file:
        file.write("import resources\n\n")
        
        for class_name in class_names:
            resource_class_name = class_name + "Resource"
            file.write(f"class {resource_class_name}(resources.ModelResource):\n\n")
            file.write(f"    class Meta:\n")
            file.write(f"        model = {class_name}\n\n")
    
    print(f"Le fichier {file_name} a été généré avec succès.")

# Demande le nom du fichier models.py
nom_fichier = input("Entrez le nom du fichier models.py : ")

# Récupère les noms de classe depuis le fichier models.py
class_names = extract_class_names(nom_fichier)

generate_import_exports_file(class_names)

