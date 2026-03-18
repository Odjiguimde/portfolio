#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur de Transactions en Temps Réel - Simulation Fintech
==============================================================

Simule un flux continu de transactions financières type Mobile Money
pour un pipeline de données temps réel.

Auteur: Oumaro Titans DJIGUIMDE
Date: Février 2026
"""

import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import time
import random

# Configuration
np.random.seed(42)
random.seed(42)

# ============================================================================
# CONFIGURATION DU CONTEXTE SÉNÉGALAIS
# ============================================================================

VILLES = ['Dakar', 'Thiès', 'Saint-Louis', 'Kaolack', 'Ziguinchor']

TRANSACTION_TYPES = {
    'transfer': 0.45,
    'payment': 0.30,
    'withdrawal': 0.20,
    'deposit': 0.05
}

OPERATEURS = ['Orange Money', 'Wave', 'Free Money', 'Wizall']

# Montants réalistes par type
MONTANT_RANGES = {
    'transfer': (1000, 100000),
    'payment': (500, 50000),
    'withdrawal': (5000, 200000),
    'deposit': (10000, 500000)
}

# ============================================================================
# GÉNÉRATION DE TRANSACTIONS
# ============================================================================

def generer_montant(transaction_type):
    """Génère un montant réaliste selon le type"""
    min_val, max_val = MONTANT_RANGES[transaction_type]
    # Distribution log-normale pour plus de réalisme
    montant = np.random.lognormal(
        mean=np.log(min_val + (max_val - min_val) / 3),
        sigma=0.8
    )
    return max(min_val, min(max_val, round(montant, 0)))

def generer_user_id():
    """Génère un user_id format téléphone sénégalais"""
    prefixes = ['77', '78', '76', '70', '75']
    prefix = random.choice(prefixes)
    numero = f"{prefix}{random.randint(1000000, 9999999)}"
    return f"user_{numero}"

def generer_transaction():
    """Génère une transaction unique"""
    # Type de transaction
    trans_type = np.random.choice(
        list(TRANSACTION_TYPES.keys()),
        p=list(TRANSACTION_TYPES.values())
    )
    
    # Montant
    amount = generer_montant(trans_type)
    
    # Ville
    city = random.choice(VILLES)
    
    # Opérateur
    operator = random.choice(OPERATEURS)
    
    # User
    user_id = generer_user_id()
    
    # Timestamp actuel
    timestamp = datetime.now()
    
    return {
        'transaction_id': f"TXN{int(time.time()*1000)}_{random.randint(1000,9999)}",
        'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        'user_id': user_id,
        'amount': amount,
        'city': city,
        'transaction_type': trans_type,
        'operator': operator,
        'status': 'completed'
    }

def generer_batch_transactions(n_transactions=1000):
    """
    Génère un batch de transactions pour simulation
    """
    print("="*70)
    print("🚀 GÉNÉRATION DE TRANSACTIONS - PIPELINE TEMPS RÉEL")
    print("="*70)
    print(f"\n📊 Nombre de transactions à générer : {n_transactions:,}")
    
    transactions = []
    
    # Date de base
    base_date = datetime.now() - timedelta(days=7)  # Derniers 7 jours
    
    for i in range(n_transactions):
        if (i + 1) % 200 == 0:
            print(f"   ✓ {i+1:,} / {n_transactions:,} transactions générées")
        
        # Génération transaction
        trans = generer_transaction()
        
        # Ajuster le timestamp pour simuler un historique
        offset_hours = random.randint(0, 7*24)  # 7 jours en heures
        timestamp = base_date + timedelta(hours=offset_hours)
        trans['timestamp'] = timestamp.strftime('%Y-%m-%d %H:%M:%S')
        
        transactions.append(trans)
    
    print(f"\n✅ {len(transactions):,} transactions générées avec succès")
    
    # Créer DataFrame
    df = pd.DataFrame(transactions)
    
    # Trier par timestamp
    df = df.sort_values('timestamp').reset_index(drop=True)
    
    return df

def afficher_statistiques(df):
    """Affiche les statistiques du dataset"""
    print("\n" + "="*70)
    print("📊 STATISTIQUES DU FLUX")
    print("="*70)
    
    print(f"\n📌 Transactions : {len(df):,}")
    print(f"📅 Période : {df['timestamp'].min()} → {df['timestamp'].max()}")
    
    print(f"\n💰 Montants :")
    print(f"   • Total : {df['amount'].sum():,.0f} FCFA")
    print(f"   • Moyenne : {df['amount'].mean():,.0f} FCFA")
    print(f"   • Médiane : {df['amount'].median():,.0f} FCFA")
    
    print(f"\n🏙️  Par ville :")
    for city, count in df['city'].value_counts().items():
        pct = (count / len(df)) * 100
        print(f"   • {city:15s} : {count:5,} ({pct:5.1f}%)")
    
    print(f"\n💳 Par type :")
    for ttype, count in df['transaction_type'].value_counts().items():
        pct = (count / len(df)) * 100
        print(f"   • {ttype:15s} : {count:5,} ({pct:5.1f}%)")
    
    print(f"\n📱 Par opérateur :")
    for op, count in df['operator'].value_counts().items():
        pct = (count / len(df)) * 100
        print(f"   • {op:20s} : {count:5,} ({pct:5.1f}%)")
    
    print("\n" + "="*70)

# ============================================================================
# EXÉCUTION
# ============================================================================

if __name__ == "__main__":
    # Génération
    df = generer_batch_transactions(n_transactions=10000)
    
    # Statistiques
    afficher_statistiques(df)
    
    # Sauvegarde
    output_path = 'data/transactions_stream.csv'
    df.to_csv(output_path, index=False, encoding='utf-8')
    
    print(f"\n✅ Flux sauvegardé : {output_path}")
    print(f"📊 Taille : {df.memory_usage(deep=True).sum() / 1024 / 1024:.2f} MB")
    print("\n" + "="*70 + "\n")
