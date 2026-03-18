# 🚀 Realtime Data Pipeline for Financial Transactions
## (Ingénierie de Données – Simulation Fintech)

---

## 📌 Présentation

Ce projet simule un **pipeline de données en temps réel** appliqué à des transactions financières (type Mobile Money / Fintech).

Il démontre la capacité à :
* Générer des flux de données simulés
* Structurer un pipeline d'ingestion
* Transformer et agréger les données
* Produire des indicateurs analytiques
* Organiser un projet data de manière professionnelle

**Ce projet met l'accent sur l'ingénierie de données**, plus que sur la modélisation IA.

---

## 🎯 Objectif

Construire un pipeline capable de :

1. **Simuler** des transactions financières
2. Les **ingérer** automatiquement
3. Les **transformer** et enrichir
4. Produire des **indicateurs analytiques** exploitables

Ce type d'architecture est utilisé dans :
* 🏦 Fintechs
* 💳 Banques
* 📱 Opérateurs Mobile Money
* 🚀 Startups data

---

## 🧠 Contexte métier

Les plateformes de paiement doivent traiter en continu :
* Des **milliers de transactions**
* Des **volumes financiers importants**
* Des données **multi-villes**
* Des indicateurs en **quasi temps réel**

Ce projet simule un environnement réaliste inspiré du **contexte sénégalais** (Dakar, Thiès, Saint-Louis, Kaolack, Ziguinchor).

---

## 🗂 Structure du projet

```
realtime-data-pipeline/
│
├── data/
│   └── transactions_stream.csv     # Flux de transactions simulé
│
├── notebooks/
│   ├── 01_stream_simulation.ipynb  # Simulation du flux
│   ├── 02_transformation.ipynb     # Transformation des données
│   └── 03_analysis_dashboard.ipynb # Analyse et visualisation
│
├── scripts/
│   └── transaction_generator.py    # Générateur de transactions
│
├── README.md                       # Documentation (ce fichier)
└── requirements.txt                # Dépendances Python
```

---

## 📦 Description des données

### Structure du flux

Chaque transaction contient :

| Colonne | Description |
|---------|-------------|
| `transaction_id` | Identifiant unique |
| `timestamp` | Date et heure de la transaction |
| `user_id` | Identifiant utilisateur (format téléphone sénégalais) |
| `amount` | Montant (FCFA) |
| `city` | Ville (Dakar, Thiès, Saint-Louis, Kaolack, Ziguinchor) |
| `transaction_type` | Type (transfer, payment, withdrawal, deposit) |
| `operator` | Opérateur (Orange Money, Wave, Free Money, Wizall) |
| `status` | Statut (completed) |

### Volume des données

- **10 000 transactions** simulées
- Période : **7 derniers jours**
- Volume financier : **~530 millions FCFA**
- Montant moyen : **~53 000 FCFA**

---

## 🔄 Architecture du pipeline

### 1️⃣ Simulation de flux
Un script génère dynamiquement des transactions simulées avec des patterns réalistes :
- Distribution géographique équilibrée
- Types de transactions pondérés (45% transfers, 30% payments, etc.)
- Montants réalistes selon le type
- Timestamps sur 7 jours glissants

### 2️⃣ Stockage
Les transactions sont enregistrées dans un fichier CSV (simulant une ingestion continue).

**Note** : En production, cela serait remplacé par :
- Base de données (PostgreSQL, MongoDB)
- Queue de messages (Kafka, RabbitMQ)
- Data Lake (S3, Azure Data Lake)

### 3️⃣ Transformation
- Conversion des dates en format datetime
- Extraction des heures, jours, périodes
- Nettoyage et validation
- Création de métriques dérivées

### 4️⃣ Analyse
- Volume total par ville
- Moyenne horaire
- Répartition des types de transactions
- Tendances temporelles
- Indicateurs de performance

---

## 🛠 Technologies utilisées

- **Python 3.12**
- **Pandas** - Manipulation de données
- **NumPy** - Calculs numériques
- **Matplotlib** / **Seaborn** - Visualisation
- **Jupyter Notebook** - Analyses interactives
- **Git & GitHub** - Versioning

---

## 📊 Exemples d'analyses réalisées

### Analyses géographiques
- Volume financier par ville
- Distribution des transactions par localisation
- Comparaison inter-villes

### Analyses temporelles
- Activité transactionnelle par heure
- Tendances par jour de la semaine
- Patterns horaires

### Analyses opérationnelles
- Distribution des types de transactions
- Performance par opérateur
- Indicateurs agrégés pour reporting

---

## 🚀 Compétences démontrées

✔️ **Simulation de données** : Génération de flux réalistes  
✔️ **Structuration d'un pipeline** : Architecture claire et maintenable  
✔️ **Transformation de données** : Nettoyage, enrichissement, agrégation  
✔️ **Analyse analytique** : Extraction d'insights métier  
✔️ **Organisation professionnelle** : Code propre, documenté, reproductible  

---

## 🌍 Applicabilité au Sénégal

Ce pipeline peut être adapté à :
* 📱 **Mobile Money** (Wave, Orange Money, Free Money)
* 💳 **Paiements digitaux** (marchands, e-commerce)
* 🏦 **Surveillance transactionnelle** (conformité, AML)
* 📊 **Reporting bancaire** (KPIs, tableaux de bord)

Il illustre une capacité à **comprendre les besoins des entreprises locales** tout en appliquant des **standards internationaux**.

---

## 🔮 Améliorations futures

### Infrastructure
- [ ] Intégration d'une **base de données** (PostgreSQL / SQLite)
- [ ] Orchestration avec **Apache Airflow**
- [ ] Streaming réel avec **Apache Kafka**
- [ ] Déploiement sur **cloud** (AWS, Azure, GCP)

### Fonctionnalités
- [ ] Système d'**alertes** en temps réel
- [ ] **Dashboard interactif** (Streamlit, Dash)
- [ ] **API REST** pour consommation des données
- [ ] **Monitoring** et logs

### Analytics
- [ ] Détection d'**anomalies**
- [ ] Prédiction de **volumes**
- [ ] Segmentation **client**
- [ ] Analyse de **tendances**

---

## ⚙️ Installation

### Prérequis
- Python 3.8+
- pip

### Installation des dépendances

```bash
pip install -r requirements.txt
```

### Génération des données

```bash
python scripts/transaction_generator.py
```

**Résultat attendu :**
```
✅ Flux sauvegardé : data/transactions_stream.csv
📊 Taille : 4.43 MB
```

### Exécution des analyses

Ouvrir les notebooks dans l'ordre :

```bash
jupyter notebook notebooks/
```

1. `01_stream_simulation.ipynb` - Simulation et génération
2. `02_transformation.ipynb` - Transformation et enrichissement
3. `03_analysis_dashboard.ipynb` - Analyse et visualisation

---

## 📈 Résultats

### Indicateurs produits

- **Volume transactionnel** par ville, heure, type
- **Montants moyens** par segment
- **Taux d'activité** temporels
- **Parts de marché** par opérateur
- **Tendances** journalières et hebdomadaires

### Visualisations

- Graphiques temporels (lignes, aires)
- Distributions (histogrammes, boxplots)
- Comparaisons (barres, pie charts)
- Heatmaps d'activité

---

## 👤 Auteur

**Oumaro Titans DJIGUIMDE**  
Étudiant en Ingénierie de Données & Intelligence Artificielle  
📍 Sénégal  

---

## 📚 Concepts clés illustrés

### Ingénierie de données
- Pipeline ETL (Extract-Transform-Load)
- Data quality & validation
- Agrégations et métriques

### Architecture
- Séparation des responsabilités (scripts, notebooks)
- Organisation modulaire
- Reproductibilité

### Business Intelligence
- KPIs transactionnels
- Reporting analytique
- Insights métier

---

## 📣 Conclusion

Ce projet démontre une **compréhension des concepts fondamentaux de l'ingénierie de données moderne** et la capacité à construire un **pipeline structuré** inspiré de cas réels fintech.

Il constitue un excellent support pour des **candidatures en stage ou premier emploi** en ingénierie de données, data engineering, ou analytics.

---
⭐ **Si ce projet vous intéresse, n'hésitez pas à le cloner et l'adapter !**

**#DataEngineering #Pipeline #RealTime #Fintech #MobileMoney #Senegal**
