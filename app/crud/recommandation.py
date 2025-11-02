from enum import Enum
from typing import List, Tuple


class Region(str, Enum):
    SAHEL = "sahel"
    SAVANE = "savane"
    GUINEEN = "guineen"
    FORET = "foret"

class RecommendationEngine:
    """Moteur d'analyse et de recommandation basé sur les composants du sol et région"""
    
    # Référence pour les cultures par région
    CULTURES_PAR_REGION = {
        Region.SAHEL: ["mil", "sorgho", "arachide", "nielle", "gousses"],
        Region.SAVANE: ["mais", "sorgho", "niebe", "arachide", "riz pluvial"],
        Region.GUINEEN: ["mais", "riz", "manioc", "igname", "soja"],
        Region.FORET: ["cacao", "cafe", "kola", "palmier à huile", "manioc"]
    }
    
    # Paramètres optimaux par culture
    OPTIMA_CULTURES = {
        "mil": {"pH": (5.5, 7.5), "N": (20, 60), "P": (8, 25), "K": (40, 150), "MO": (1, 3)},
        "sorgho": {"pH": (5.5, 8.0), "N": (20, 60), "P": (8, 25), "K": (40, 150), "MO": (1, 3)},
        "mais": {"pH": (6.0, 7.5), "N": (30, 80), "P": (12, 35), "K": (80, 200), "MO": (2, 4)},
        "riz": {"pH": (6.0, 7.5), "N": (40, 100), "P": (15, 40), "K": (100, 250), "MO": (2.5, 5)},
        "arachide": {"pH": (6.0, 7.5), "N": (15, 40), "P": (10, 30), "K": (60, 180), "MO": (1.5, 3.5)},
        "niebe": {"pH": (6.0, 7.5), "N": (10, 35), "P": (8, 25), "K": (50, 150), "MO": (1, 3)},
        "riz pluvial": {"pH": (6.0, 7.5), "N": (35, 90), "P": (12, 35), "K": (80, 220), "MO": (2, 4.5)},
        "manioc": {"pH": (5.5, 7.5), "N": (15, 50), "P": (8, 25), "K": (70, 200), "MO": (1.5, 4)},
        "igname": {"pH": (6.0, 7.5), "N": (25, 70), "P": (12, 35), "K": (100, 250), "MO": (2, 4)},
        "soja": {"pH": (6.0, 7.5), "N": (20, 50), "P": (12, 35), "K": (80, 200), "MO": (2, 4)},
        "cacao": {"pH": (6.0, 7.0), "N": (30, 80), "P": (15, 40), "K": (100, 250), "MO": (3, 6)},
        "cafe": {"pH": (5.5, 7.0), "N": (25, 70), "P": (12, 35), "K": (80, 220), "MO": (2.5, 5)},
        "kola": {"pH": (6.0, 7.5), "N": (25, 65), "P": (12, 35), "K": (90, 230), "MO": (2.5, 5)},
        "palmier à huile": {"pH": (5.5, 7.5), "N": (35, 85), "P": (15, 40), "K": (110, 260), "MO": (3, 6)},
        "gousses": {"pH": (6.0, 7.5), "N": (10, 40), "P": (8, 25), "K": (50, 150), "MO": (1, 2.5)},
        "nielle": {"pH": (6.0, 7.5), "N": (15, 45), "P": (8, 25), "K": (60, 170), "MO": (1, 2.5)},
        "haricots": {"pH": (6.0, 7.5), "N": (15, 45), "P": (10, 30), "K": (70, 180), "MO": (1, 3)},
        "sesame": {"pH": (5.5, 7.5), "N": (10, 35), "P": (8, 25), "K": (50, 150), "MO": (1, 2.5)},
    }
    
    @staticmethod
    def calculer_score_aptitude(culture: str, ph: float, n: float, p: float, k: float) -> Tuple[float, List[str]]:
        """Calcule le score d'aptitude (0-100) et retourne les raisons"""
        if culture not in RecommendationEngine.OPTIMA_CULTURES:
            return 0, ["Culture non documentée"]
        
        optima = RecommendationEngine.OPTIMA_CULTURES[culture]
        raisons = []
        score = 100
        
        # Évaluation du pH
        pH_min, pH_max = optima["pH"]
        if ph < pH_min or ph > pH_max:
            deviation = min(abs(ph - pH_min), abs(ph - pH_max))
            score -= deviation * 10
            raisons.append(f"pH non optimal (optimum: {pH_min}-{pH_max}, actuel: {ph})")
        
        # Évaluation de l'azote
        N_min, N_max = optima["N"]
        if n < N_min:
            score -= (N_min - n) * 0.5
            raisons.append(f"Azote insuffisant (optimum: {N_min}-{N_max} mg/kg, actuel: {n})")
        elif n > N_max:
            score -= (n - N_max) * 0.3
            raisons.append(f"Azote en excès")
        
        # Évaluation du phosphore
        P_min, P_max = optima["P"]
        if p < P_min:
            score -= (P_min - p) * 0.5
            raisons.append(f"Phosphore insuffisant (optimum: {P_min}-{P_max} mg/kg, actuel: {p})")
        elif p > P_max:
            score -= (p - P_max) * 0.2
        
        # Évaluation du potassium
        K_min, K_max = optima["K"]
        if k < K_min:
            score -= (K_min - k) * 0.3
            raisons.append(f"Potassium insuffisant (optimum: {K_min}-{K_max} mg/kg, actuel: {k})")
        
        score = max(0, min(100, score))
        return score, raisons
    
    @staticmethod
    def obtenir_aptitude_label(score: float) -> str:
        """Convertit le score en label d'aptitude"""
        if score >= 80:
            return "excellente"
        elif score >= 60:
            return "bonne"
        elif score >= 40:
            return "moyenne"
        else:
            return "faible"
    
    @staticmethod
    def obtenir_rendement_estime(culture: str, score: float) -> str:
        """Estime le rendement potentiel en kg/ha"""
        rendements_reference = {
            "mil": (800, "800-1200"),
            "sorgho": (1000, "1000-1500"),
            "mais": (2000, "2000-4000"),
            "riz": (2500, "2500-5000"),
            "riz pluvial": (1500, "1500-3000"),
            "arachide": (1200, "1200-2000"),
            "niebe": (800, "800-1500"),
            "manioc": (5000, "5000-10000"),
            "igname": (3000, "3000-8000"),
            "soja": (1500, "1500-2500"),
            "cacao": (400, "400-1000"),
            "cafe": (800, "800-1200"),
            "kola": (600, "600-1000"),
            "palmier à huile": (3500, "3500-6000"),
            "gousses": (1000, "1000-1800"),
            "nielle": (1200, "1200-2000"),
        }
        
        if culture not in rendements_reference:
            return "Non disponible"
        
        base, plage = rendements_reference[culture]
        rendement_ajuste = int(base * (score / 100))
        return f"{rendement_ajuste} kg/ha (cible: {plage})"
    
    @staticmethod
    def obtenir_pratiques_recommandees(culture: str, ph: float, humidite: float) -> List[str]:
        """Retourne les pratiques agricoles recommandées"""
        pratiques = []
        
        # Pratiques selon la culture
        if culture in ["riz", "riz pluvial"]:
            pratiques.append("Préparer les rizières 3-4 semaines avant le repiquage")
            pratiques.append("Assurer une submersion régulière pour le riz")
        elif culture in ["mil", "sorgho"]:
            pratiques.append("Utiliser des variétés résistantes à la sécheresse")
            pratiques.append("Pratiquer le zaï ou des demi-lunes pour la rétention d'eau")
        elif culture in ["arachide"]:
            pratiques.append("Utiliser des graines traitées")
            pratiques.append("Écarter les plants à 40-50 cm")
        elif culture in ["mais"]:
            pratiques.append("Densité: 20-25 plants/m²")
            pratiques.append("Appliquer l'engrais au stade 4-6 feuilles")
        elif culture in ["manioc"]:
            pratiques.append("Utiliser des boutures saines")
            pratiques.append("Écarter les plants à 1m x 1m")
        elif culture in ["cacao", "cafe"]:
            pratiques.append("Assurer l'ombrage partiel")
            pratiques.append("Pratiquer l'élagage régulier")
        
        # Pratiques selon la qualité du sol
        if ph < 6.0:
            pratiques.append("Envisager l'application de chaux pour corriger l'acidité")
        
        if humidite < 30:
            pratiques.append("Mettre en place un système d'irrigation goutte-à-goutte")
            pratiques.append("Appliquer un mulch pour conserver l'humidité")
        elif humidite > 70:
            pratiques.append("Améliorer le drainage du sol")
            pratiques.append("Pratiquer des billons surélevés")
        
        return pratiques
    
    @staticmethod
    def analyser_sol(ph: float, n: float, p: float, k: float, humidite: float) -> dict:
        """Analyse générale du sol"""
        analyse = {
            "pH": {
                "valeur": ph,
                "interpretation": "acide" if ph < 6.5 else "neutre" if ph < 7.5 else "alcalin"
            },
            "fertilite": {
                "azote": "faible" if n < 20 else "moyen" if n < 60 else "élevé",
                "phosphore": "faible" if p < 8 else "moyen" if p < 25 else "élevé",
                "potassium": "faible" if k < 40 else "moyen" if k < 150 else "élevé",
            },
            "humidite": "faible" if humidite < 20 else "moyen" if humidite < 60 else "élevée",
            "indice_fertilite_globale": "faible" if (n + p + k) / 3 < 30 else "moyen" if (n + p + k) / 3 < 100 else "bon"
        }
        return analyse
    
    @staticmethod
    def generer_amendements(ph: float, n: float, p: float, k: float) -> List[str]:
        """Recommande les amendements nécessaires"""
        amendements = []
        
        if n < 30:
            amendements.append("Engrais azoté (urée): 50-100 kg/ha")
        
        if p < 10:
            amendements.append("Engrais phosphaté (superphosphate): 30-50 kg/ha")
        
        if k < 80:
            amendements.append("Engrais potassique: 40-60 kg/ha")
        
        if ph < 6.0:
            amendements.append("Chaux agricole: 1-3 tonnes/ha selon le pH")
        
        if ph > 8.0:
            amendements.append("Soufre élémentaire: 0.5-2 tonnes/ha pour diminuer le pH")
        
        return amendements if amendements else None