import re
from collections import Counter
import glob

print("--- Démarrage du Nettoyeur ---")

# 1. TROUVER LE FICHIER AUTOMATIQUEMENT
# On cherche n'importe quel fichier qui commence par "minutes_" et finit par ".txt"
# C'est pratique : pas besoin de copier-coller le nom compliqué avec la date !
files = glob.glob("minutes_*.txt")

if not files:
    print("❌ Erreur : Je ne trouve pas de fichier texte !")
    print("Piste : As-tu bien lancé scraper.py avant ?")
    exit()

# On prend le premier fichier trouvé
filename = files[0]
print(f"📖 Lecture du fichier : {filename}")

# 2. CHARGER LE TEXTE
with open(filename, 'r', encoding='utf-8') as f:
    text = f.read()

# 3. LE GRAND NETTOYAGE
def clean_text(raw_text):
    # A. Tout mettre en minuscule
    # Pour l'ordinateur, "Inflation" et "inflation" sont deux mots différents. On uniformise.
    text_lower = raw_text.lower()
    
    # B. Supprimer la ponctuation et les chiffres
    # On utilise une "Expression Régulière" (regex) : [^\w\s] veut dire "tout sauf les lettres et espaces"
    text_clean = re.sub(r'[^\w\s]', '', text_lower)
    text_clean = re.sub(r'\d+', '', text_clean) # Enlève les chiffres
    
    # C. Couper le texte en liste de mots (Tokenization)
    words = text_clean.split()
    
    return words

all_words = clean_text(text)
print(f"📊 Mots bruts trouvés : {len(all_words)}")

# 4. LE TAMIS (Filtrer les Stop Words)
# Voici une liste manuelle des mots inutiles en anglais + mots administratifs de la FED
stop_words = {
    "the", "of", "and", "to", "in", "a", "is", "that", "for", "it", "as", "was", "with", "on", 
    "at", "by", "be", "this", "which", "from", "but", "not", "are", "have", "an", "or", "has", 
    "would", "could", "been", "their", "its", "about", "some", "participants", "committee", "meeting", "members"
}

# On ne garde que les mots qui NE SONT PAS dans la liste des stop_words
keywords = [word for word in all_words if word not in stop_words and len(word) > 2]

print(f"💎 Mots utiles restants (Pépites) : {len(keywords)}")

# 5. PREMIÈRE ANALYSE : Quels sont les mots les plus utilisés ?
word_counts = Counter(keywords)

print("\n--- TOP 20 DES MOTS CLÉS DE CETTE RÉUNION ---")
for word, count in word_counts.most_common(20):
    print(f"{word}: {count} fois")
print("---------------------------------------------")