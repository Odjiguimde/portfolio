# Odjiguimde-Projet-1-Analyse-Exploratoire-des-Donnes-(EDA)

# 🏦 Projet EDA — Détection de Fraude Bancaire

Ce dépôt contient une série de notebooks Jupyter dédiés à l'**Analyse Exploratoire des Données (EDA)** appliquée à la détection de fraude bancaire. Les notebooks suivent une progression pédagogique allant des statistiques univariées à l'analyse multivariée.

## 📋 Contenu

### Partie 1 — Statistique univariée
**Fichier :** `01_EDA_Fraude_Statistique_Univariee.ipynb`

- Mesures de tendance centrale (moyenne, médiane, mode) sur `Amount` et `Time`
- Mesures de dispersion (variance, écart-type, IQR, coefficient de variation)
- Détection des outliers via la règle de Tukey
- Analyse de la forme de la distribution (asymétrie, kurtosis)
- Analyse de la variable cible `Class` (effectifs, proportions, déséquilibre)
- Tests de normalité (Shapiro-Wilk, Kolmogorov-Smirnov, Q-Q plot)
- Analyse temporelle : patterns horaires des transactions frauduleuses

### Partie 2 — Distributions de probabilité
**Fichier :** `02_EDA_Fraude_Distributions_Probabilite.ipynb`

- Loi normale : vérification sur les composantes V1–V28 (issues de la PCA)
- Loi log-normale : ajustement sur `Amount`
- Loi exponentielle : modélisation des intervalles entre transactions
- Loi de Bernoulli : modélisation de `Class` (fraude/normal)
- Loi binomiale : nombre de fraudes attendu dans un lot de transactions

### Partie 3 — Échantillonnage & Biais
**Fichier :** `03_EDA_Fraude_Echantillonnage_Biais.ipynb`

- Échantillonnage aléatoire simple, stratifié, avec oversampling
- Biais de déséquilibre de classes (0.17% de fraudes) et ses implications
- Piège de l'accuracy — métriques adaptées (AUC-PR, F1, Rappel)
- Biais d'anonymisation (PCA) et de sélection temporelle
- Data leakage : split chronologique obligatoire via `Time`
- Analyse des valeurs manquantes et doublons

### Partie 4 — Statistique bivariée
**Fichier :** `04_EDA_Fraude_Statistique_Bivariee.ipynb`

- Relations QUANTI ↔ QUANTI : corrélations entre composantes PCA et `Amount`
- Relations QUALI ↔ QUANTI : `Class` → `Amount` (boxplot, violin, KDE)
- Calcul du Cohen's d pour identifier les composantes les plus discriminantes
- Scatter plots colorés par classe pour visualiser la séparation

### Partie 5 — Tests statistiques bivariés
**Fichier :** `05_EDA_Fraude_Tests_Statistiques.ipynb`

- Tests de normalité et d'homogénéité des variances (Shapiro, Levene)
- t-test de Welch et Mann-Whitney U : `Amount` selon `Class`
- Test Mann-Whitney systématique sur toutes les composantes V1–V28
- Corrélations point-bisérielles avec `Class`
- Forest plot des tailles d'effet (Cohen's d)

### Partie 6 — Statistique multivariée & PCA
**Fichier :** `06_EDA_Fraude_Multivariee_PCA.ipynb`

- Matrice de corrélation complète (V1–V28, Amount, Class)
- Heatmap de corrélation
- Application d'une PCA pour visualiser la séparation Normal/Fraude en 2D
- Scree plot et variance expliquée cumulée
- Biplot et loadings : contribution des variables aux composantes principales

---

## 🗂️ Structure du projet

```
EDA_Fraude_Bancaire/
├── README.md
├── creditcard.csv                                    ← à télécharger (voir ci-dessous)
├── 01_EDA_Fraude_Statistique_Univariee.ipynb
├── 02_EDA_Fraude_Distributions_Probabilite.ipynb
├── 03_EDA_Fraude_Echantillonnage_Biais.ipynb
├── 04_EDA_Fraude_Statistique_Bivariee.ipynb
├── 05_EDA_Fraude_Tests_Statistiques.ipynb
└── 06_EDA_Fraude_Multivariee_PCA.ipynb
```

---

## 📊 Dataset

**Source :** [Credit Card Fraud Detection — Kaggle](https://www.kaggle.com/datasets/mlgulb/creditcardfraud)

Le dataset contient **284 807 transactions bancaires** réalisées par des titulaires de cartes européennes en septembre 2013.

| Variable | Description |
|----------|-------------|
| `Time` | Secondes écoulées depuis la 1ère transaction du dataset |
| `V1`–`V28` | Composantes issues d'une PCA (anonymisation des données sensibles) |
| `Amount` | Montant de la transaction (en €) |
| `Class` | Variable cible : 0 = Normal, 1 = Fraude |

**Caractéristiques clés :**
- 284 315 transactions normales (99.83%)
- 492 transactions frauduleuses (0.17%)
- Aucune valeur manquante
- Variables V1–V28 déjà standardisées et décorrélées

---

## 🔧 Prérequis

- Python 3.8+
- Jupyter Notebook ou JupyterLab

## 📦 Installation

### 1. Cloner ou télécharger ce dépôt

### 2. Installer les dépendances

```bash
pip install numpy pandas matplotlib scipy seaborn scikit-learn jupyter
```

### 3. Télécharger le dataset

Rendez-vous sur [Kaggle](https://www.kaggle.com/datasets/mlgulb/creditcardfraud), téléchargez `creditcard.csv` et placez-le dans le même dossier que les notebooks.

### 4. Lancer Jupyter

```bash
jupyter notebook
# ou
jupyter lab
```

---

## 🚀 Utilisation

1. Placez `creditcard.csv` dans le dossier du projet
2. Ouvrez les notebooks dans l'**ordre numérique** pour suivre la progression
3. Exécutez les cellules dans l'ordre
4. Modifiez les variables analysées pour explorer d'autres composantes

---

## 🔍 Concepts couverts

- Statistiques descriptives univariées
- Distributions de probabilité et ajustement paramétrique
- Déséquilibre de classes et techniques d'échantillonnage
- Analyse bivariée et corrélations
- Tests d'hypothèses paramétriques et non paramétriques
- Analyse en composantes principales (PCA)
- Visualisation de données (histogrammes, boxplots, KDE, scatter, heatmap, biplot)

---

## ⚠️ Points d'attention spécifiques à ce dataset

| Problème | Impact | Solution recommandée |
|----------|--------|----------------------|
| Déséquilibre de classes | Accuracy trompeuse | SMOTE, class_weight, évaluer avec AUC-PR |
| `Amount` asymétrique | Dégradation des modèles | Transformation `log(1 + Amount)` |
| Variables anonymisées (PCA) | Non-interprétabilité métier | Accepter les Vi comme features |
| Data leakage temporel | Suroptimisme du modèle | Split chronologique via `Time` |

---

## 📚 Ressources supplémentaires

- [Documentation NumPy](https://numpy.org/doc/)
- [Documentation Pandas](https://pandas.pydata.org/docs/)
- [Documentation SciPy](https://scipy.org/)
- [Documentation Matplotlib](https://matplotlib.org/)
- [Documentation Seaborn](https://seaborn.pydata.org/)
- [Documentation Scikit-learn (PCA)](https://scikit-learn.org/stable/modules/decomposition.html#pca)
- [Article original du dataset (Dal Pozzolo et al., 2015)](https://www.researchgate.net/publication/283349138)

---

## 📄 Licence

Ce projet est destiné à des fins éducatives.
