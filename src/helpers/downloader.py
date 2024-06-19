import requests
from pathlib import Path

def download_to_local(url: str, out_path: Path, parent_mkdir: bool = True):
    """
    Télécharge un fichier à partir d'une URL et le sauvegarde à un chemin local spécifié.
    
    Args:
        url (str): L'URL du fichier à télécharger.
        out_path (Path): Le chemin local où le fichier doit être sauvegardé.
        parent_mkdir (bool): Si True, crée les répertoires parents du chemin de sortie s'ils n'existent pas.

    Returns:
        bool: True si le téléchargement et la sauvegarde sont réussis, sinon False.
    
    Raises:
        ValueError: Si out_path n'est pas une instance de pathlib.Path.
    """
    
    # Vérifie si out_path est bien une instance de pathlib.Path
    if not isinstance(out_path, Path):
        raise ValueError("chemin non valide")
    
    # Crée les répertoires parents si parent_mkdir est True
    if parent_mkdir:
        out_path.parent.mkdir(parents=True, exist_ok=True)
    
    try:
        # Effectue une requête GET pour télécharger le fichier à partir de l'URL
        response = requests.get(url)
        # Vérifie si la requête a réussi (code de statut HTTP 200)
        response.raise_for_status()
        
        # Écrit le contenu téléchargé dans le fichier en mode binaire
        # Le mode binaire empêche la conversion automatique des nouvelles lignes
        out_path.write_bytes(response.content)
        
        # Retourne True pour indiquer que le téléchargement et la sauvegarde ont réussi
        return True
    except requests.RequestException as e:
        # Affiche un message d'erreur en cas d'exception lors de la requête
        print(f'Erreur impossible de télécharger {url} : {e}')
        
        # Retourne False pour indiquer que le téléchargement ou la sauvegarde ont échoué
        return False
