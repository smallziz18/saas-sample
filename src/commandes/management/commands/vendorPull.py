import helpers
from typing import Any
from django.core.management.base import BaseCommand
from django.conf import settings

import helpers.downloader

# Récupère le répertoire des fichiers statiques des vendors depuis les settings
STATICFILES_VENDOR_DIR = getattr(settings, 'STATICFILES_VENDOR_DIR')

# Dictionnaire contenant les noms des fichiers et leurs URLs de téléchargement
VENDOR_STATICFILES = {
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
    "flowbite.min.js.map": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js.map"
}

class Command(BaseCommand):
    help = "Télécharge les fichiers statiques des vendors."

    def handle(self, *args: Any, **options: Any):
        self.stdout.write("Téléchargement des fichiers vendors")
        completed_urls = []

        for name, url in VENDOR_STATICFILES.items():
            # Définit le chemin de sortie pour chaque fichier
            out_path = STATICFILES_VENDOR_DIR / name
            # Tente de télécharger le fichier
            dl_success = helpers.downloader.download_to_local(url, out_path)
            if dl_success:
                completed_urls.append(url)
                self.stdout.write(self.style.SUCCESS(f"Téléchargement réussi: {url}"))
            else:
                self.stdout.write(self.style.ERROR(f"Échec du téléchargement du fichier {url}"))


