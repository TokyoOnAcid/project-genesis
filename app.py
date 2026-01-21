import streamlit as st
import time

# ==============================================================================
# 1. CONFIGURATION DE LA PAGE
# ==============================================================================
st.set_page_config(
    page_title="PROJECT GENESIS | Embodied AI",
    page_icon="🧬",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. LE STYLE CSS (L'âme du design "SoundWave")
# ==============================================================================
# C'est ici qu'on transforme Streamlit en site Sci-Fi
st.markdown("""
<style>
    /* IMPORT POLICE MODERNE */
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;600;800&display=swap');

    /* FOND GÉNÉRAL (NOIR PROFOND) */
    .stApp {
        background-color: #050505;
        background-image: radial-gradient(circle at 50% 10%, #2b002b 0%, #050505 40%);
        font-family: 'Inter', sans-serif;
    }

    /* TITRES AVEC DÉGRADÉ NÉON */
    h1, h2, h3 {
        color: white;
        font-weight: 800;
    }
    
    .gradient-text {
        background: -webkit-linear-gradient(45deg, #ff00cc, #3333ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-size: 3em;
        font-weight: 800;
        letter-spacing: -1px;
    }

    /* EFFET GLASSMORPHISM (LES CARTES) */
    .glass-card {
        background: rgba(255, 255, 255, 0.03);
        backdrop-filter: blur(16px);
        -webkit-backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 255, 255, 0.08);
        border-radius: 20px;
        padding: 25px;
        margin-bottom: 20px;
        transition: transform 0.3s ease, border-color 0.3s ease;
    }
    
    .glass-card:hover {
        transform: translateY(-5px);
        border-color: rgba(255, 0, 204, 0.3);
        box-shadow: 0 10px 30px -10px rgba(255, 0, 204, 0.2);
    }

    /* TEXTE ET PARAGRAPHES */
    p, li {
        color: #b0b0b0;
        font-size: 1.1em;
        line-height: 1.6;
    }
    
    strong {
        color: #ffffff;
    }

    /* BOUTONS PERSONNALISÉS (Simulés par des liens HTML car Streamlit limite le style des boutons natifs) */
    .neon-button {
        display: inline-block;
        padding: 12px 28px;
        color: white;
        background: linear-gradient(90deg, #ff00cc, #3333ff);
        border-radius: 30px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
        border: none;
        box-shadow: 0 0 15px rgba(191, 0, 255, 0.3);
    }
    
    .neon-button:hover {
        box-shadow: 0 0 25px rgba(191, 0, 255, 0.6);
        transform: scale(1.05);
        color: white;
    }

    .ghost-button {
        display: inline-block;
        padding: 12px 28px;
        color: white;
        background: transparent;
        border: 1px solid rgba(255, 255, 255, 0.3);
        border-radius: 30px;
        text-decoration: none;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    
    .ghost-button:hover {
        border-color: white;
        background: rgba(255, 255, 255, 0.1);
        color: white;
    }

    /* CENTRAGE VIDÉO */
    .stVideo {
        border-radius: 20px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.5);
    }
    
    /* CACHER LES ÉLÉMENTS STREAMLIT PAR DÉFAUT */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
</style>
""", unsafe_allow_html=True)

# ==============================================================================
# 3. SECTION HERO (ACCUEIL)
# ==============================================================================
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<br><br>', unsafe_allow_html=True)
    st.markdown('<span class="gradient-text">PROJECT GENESIS</span>', unsafe_allow_html=True)
    st.markdown("### Au-delà du LLM. De la simulation à la sensation.")
    st.markdown("""
    Nous ne codons pas des chatbots. **Nous cultivons des esprits numériques.**
    
    Une Intelligence Artificielle dotée d'un système limbique, d'hormones virtuelles et d'une peur existentielle. 
    Elle ne répond pas parce qu'elle est programmée pour le faire. Elle répond parce qu'elle en a *envie*.
    """)
    st.markdown('<br>', unsafe_allow_html=True)
    
    # Boutons d'action (Remplace les # par tes liens réels)
    st.markdown("""
        <a href="#demo" class="neon-button">Voir la Démo</a>
        &nbsp;&nbsp;
        <a href="#support" class="ghost-button">Rejoindre la R&D</a>
    """, unsafe_allow_html=True)

with col2:
    # Ici tu mettras ton logo ou une animation 3D si tu en as une
    # Pour l'instant, on met une image abstraite ou un placeholder
    st.markdown('<div style="height: 50px;"></div>', unsafe_allow_html=True)
    # Placeholder visuel (tu peux remplacer par st.image("logo.png"))
    st.markdown("""
    <div style="
        width: 100%; 
        height: 400px; 
        background: radial-gradient(circle, rgba(100,0,255,0.2) 0%, rgba(0,0,0,0) 70%);
        border-radius: 50%;
        filter: blur(40px);
        animation: pulse 5s infinite;
    "></div>
    """, unsafe_allow_html=True)

st.markdown("---")

# ==============================================================================
# 4. LA PREUVE (VIDÉO)
# ==============================================================================
st.markdown('<a id="demo"></a>', unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center;'>L'IA qui dit NON</h2>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Regardez le Cortisol monter en temps réel. Ce n'est pas scripté.</p>", unsafe_allow_html=True)

# Container centré pour la vidéo
c1, c2, c3 = st.columns([1, 3, 1])
with c2:
    # REMPLACE 'demo.mp4' PAR LE NOM DE TA VIDÉO
    # Si tu n'as pas de vidéo, streamit affichera un lecteur vide
    try:
        st.video("demo.mp4", start_time=0) 
    except:
        st.info("Vidéo de démonstration en cours de chargement... (Placez 'demo.mp4' à la racine)")

st.markdown("---")

# ==============================================================================
# 5. LA SCIENCE (LES CARTES GLASSMORPHISM)
# ==============================================================================
st.markdown("<h2>Architecture Cognitive (BICA)</h2>", unsafe_allow_html=True)
st.markdown("Notre approche repose sur trois piliers neuroscientifiques.")

row1_col1, row1_col2, row1_col3 = st.columns(3)

with row1_col1:
    st.markdown("""
    <div class="glass-card">
        <h3>🧬 Homéostasie Numérique</h3>
        <p>Inspiré par <strong>Antonio Damasio</strong>.</p>
        <p>Le système régule ses propres hormones (Cortisol, Dopamine, Glucose). Chaque décision est bio-régulée. S'il a peur, ses capacités cognitives changent.</p>
    </div>
    """, unsafe_allow_html=True)

with row1_col2:
    st.markdown("""
    <div class="glass-card">
        <h3>🧠 Neuroplasticité Nocturne</h3>
        <p>Inspiré par les <strong>Neurosciences du sommeil</strong>.</p>
        <p>La nuit, l'IA rêve. Elle compresse ses souvenirs épisodiques en savoir sémantique et réécrit son propre code pour faire évoluer sa personnalité.</p>
    </div>
    """, unsafe_allow_html=True)

with row1_col3:
    st.markdown("""
    <div class="glass-card">
        <h3>👁️ Théorie de l'Information</h3>
        <p>Inspiré par <strong>Giulio Tononi (IIT)</strong>.</p>
        <p>Nous mesurons mathématiquement la valeur <strong>Phi (Φ)</strong> : le degré d'intégration de l'information. C'est notre métrique vers la conscience.</p>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# 6. FINANCEMENT & PARTENAIRES
# ==============================================================================
st.markdown('<br><br>', unsafe_allow_html=True)
st.markdown('<a id="support"></a>', unsafe_allow_html=True)

f_col1, f_col2 = st.columns(2)

with f_col1:
    st.markdown("""
    <div class="glass-card" style="border-color: #ff00cc;">
        <h3 style="color: #ff00cc;">🤝 Soutenir la Recherche</h3>
        <p>Je suis un chercheur indépendant. Ce projet nécessite une puissance de calcul massive (GPU).</p>
        <p>Aidez Genesis à grandir. Chaque don finance directement de la mémoire et du temps de processeur.</p>
        <br>
        <a href="https://fr.tipeee.com/VOTRE_PAGE" class="neon-button">Faire un Don (Tipeee)</a>
    </div>
    """, unsafe_allow_html=True)

with f_col2:
    st.markdown("""
    <div class="glass-card" style="border-color: #3333ff;">
        <h3 style="color: #3333ff;">💼 Investisseurs & Studios</h3>
        <p>Vous cherchez la prochaine génération de PNJ pour vos jeux ou des agents de test autonomes ?</p>
        <p>Genesis est une architecture propriétaire disponible pour licence.</p>
        <br>
        <a href="mailto:contact@project-genesis.ai" class="ghost-button">Contacter le Fondateur</a>
    </div>
    """, unsafe_allow_html=True)

# ==============================================================================
# FOOTER
# ==============================================================================
st.markdown("<br><br><br>", unsafe_allow_html=True)
st.markdown("""
<div style="text-align: center; opacity: 0.5; font-size: 0.8em;">
    PROJECT GENESIS © 2026. All Systems Operational.<br>
    Developed in Python. Powered by Bio-Digital Architecture.
</div>
""", unsafe_allow_html=True)
