import glob
import re

print("--- Démarrage de l'Analyseur Financier ---")

# 1. CHARGEMENT DU FICHIER (Comme avant)
files = glob.glob("minutes_*.txt")
if not files:
    print("❌ Pas de fichier trouvé.")
    exit()

filename = files[0]
with open(filename, 'r', encoding='utf-8') as f:
    text = f.read().lower() # On met tout en minuscule

# 2. LE DICTIONNAIRE FINANCIER (Version Mini)
# +1 = Mot Positif (Croissance, Stabilité)
# -1 = Mot Négatif (Risque, Inflation, Baisse)
financial_lexicon = {
    # Mots Négatifs (Risques)
    "loss": -1, "losses": -1, "decline": -1, "declined": -1, "sluggish": -1,
    "inflation": -1, "risk": -1, "risks": -1, "uncertainty": -1, "adverse": -1,
    "shortfall": -1, "weak": -1, "weakness": -1, "difficult": -1, "volatility": -1,
    "concern": -1, "concerns": -1, "fears": -1, "pressure": -1, "drag": -1,
    "contract": -1, "contraction": -1, "unemployment": -1, "recession": -1,
    
    # Mots Positifs (Croissance)
    "gain": 1, "gains": 1, "growth": 1, "strong": 1, "strengthen": 1,
    "recovery": 1, "improve": 1, "improved": 1, "improvement": 1, "positive": 1,
    "stable": 1, "stability": 1, "confident": 1, "expansion": 1, "robust": 1,
    "rise": 1, "rose": 1, "solid": 1, "higher": 1, "advance": 1
}

# 3. LE MOTEUR DE CALCUL
print(f"🧠 Analyse du sentiment pour : {filename}")

words = re.sub(r'[^\w\s]', '', text).split() # Nettoyage rapide

score = 0
positive_count = 0
negative_count = 0

matched_words = []

for word in words:
    if word in financial_lexicon:
        # On ajoute le score du mot (-1 ou +1) au score total
        valeur = financial_lexicon[word]
        score += valeur
        
        # Pour les statistiques
        if valeur > 0:
            positive_count += 1
        else:
            negative_count += 1
            
        matched_words.append(word)

# 4. LE RAPPORT FINAL
total_significant_words = positive_count + negative_count

print("\n" + "="*40)
print(" RÉSULTATS DE L'ANALYSE")
print("="*40)
print(f"Nombre de mots financiers détectés : {total_significant_words}")
print(f"Mots Positifs : {positive_count}")
print(f"Mots Négatifs : {negative_count}")
print("-" * 40)
print(f"SCORE FINAL DE SENTIMENT : {score}")
print("-" * 40)

if score > 5:
    print("📈 CONCLUSION : Discours OPTIMISTE (Bullish)")
elif score < -5:
    print("📉 CONCLUSION : Discours PESSIMISTE/RISQUÉ (Bearish)")
else:
    print("⚖️ CONCLUSION : Discours NEUTRE")

print("\nNote : Un score négatif signifie que la FED est focalisée sur les risques (Inflation, etc).")