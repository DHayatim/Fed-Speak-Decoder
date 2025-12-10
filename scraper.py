import requests
from bs4 import BeautifulSoup

# 1. CIBLE : On ne vise plus une réunion précise, mais la page SOMMAIRE de 2024
base_url = "https://www.federalreserve.gov"
year_url = "https://www.federalreserve.gov/monetarypolicy/fomcminutes2024.htm"

headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36"
}

print(f"--- Démarrage du Scraper V2 (Mode Automatique) ---")

# --- ÉTAPE A : Trouver le dernier lien ---
print(f"1. Recherche de la dernière réunion sur : {year_url}")
response_list = requests.get(year_url, headers=headers)

if response_list.status_code == 200:
    soup_list = BeautifulSoup(response_list.content, 'html.parser')
    
    # On cherche tous les liens (a) qui contiennent le mot "fomcminutes"
    # C'est l'astuce pour ne prendre que les minutes et pas les autres documents
    all_links = soup_list.find_all('a', href=True)
    minute_links = [link['href'] for link in all_links if 'fomcminutes' in link['href'] and '.htm' in link['href']]
    
    # On prend le DERNIER de la liste (c'est souvent le plus récent)
    # [-1] en Python veut dire "le dernier élément de la liste"
    last_meeting_suffix = minute_links[-1] 
    
    # On reconstruit l'URL complète
    final_url = base_url + last_meeting_suffix
    print(f"✅ Trouvé ! La réunion la plus récente est ici : {final_url}")
    
    # --- ÉTAPE B : Récupérer le texte (comme avant) ---
    print(f"2. Téléchargement du discours...")
    response_text = requests.get(final_url, headers=headers)
    
    if response_text.status_code == 200:
        soup_article = BeautifulSoup(response_text.content, 'html.parser')
        article = soup_article.find('div', id='article')
        
        if article:
            paragraphs = article.find_all('p')
            text_content = " ".join([p.get_text() for p in paragraphs])
            clean_text = " ".join(text_content.split())
            
            # On affiche un petit bout pour vérifier la date dans le texte
            print("\n--- DÉBUT DU TEXTE ---")
            print(clean_text[:300] + "...")
            print("----------------------\n")
            
            # Sauvegarde intelligente : on met la date ou l'url dans le nom du fichier pour ne pas écraser l'ancien
            # On extrait juste "fomcminutes2024xxxx" de l'url pour le nom
            file_suffix = last_meeting_suffix.split('/')[-1].replace('.htm', '')
            filename = f"minutes_{file_suffix}.txt"
            
            with open(filename, "w", encoding="utf-8") as f:
                f.write(clean_text)
            print(f"📁 Sauvegardé sous le nom : {filename}")
            
        else:
            print("Erreur : Impossible de trouver le texte sur la page finale.")
    else:
        print("Erreur lors de l'accès à la page finale.")

else:
    print("Erreur : Impossible d'accéder à la page sommaire.")