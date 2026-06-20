import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            /* Import Meta Variable Font */
            @font-face {
                src: url("https://www.axis-praxis.org/fonts/webfonts/MetaVariableDemo-Set.woff2") format("woff2");
                font-family: "Meta";
                font-style: normal;
                font-weight: normal;
            }

            .stApp {
                background: #4A56D2 !important;
            }

            .stApp div[data-testid="stColumn"] {
                background-color: #EEF0FF !important;
                padding: 2.5rem !important;
                border-radius: 2rem !important;
                box-shadow: 0 8px 32px rgba(26, 26, 46, 0.15) !important;
            }

            /* ========================================================
               HERO HEADER (H1) ANIMATION & STYLES (HOME ONLY)
               ======================================================== */
            .stApp h1, .stApp h1 span, .stApp h1 div {
                font-family: "Meta", sans-serif !important;
                font-size: 5rem !important; /* Scaled down slightly from 15rem to fit app layouts better */
                line-height: 1.1 !important;
                text-align: center !important;
                color: transparent !important;
                -webkit-text-stroke: 3px #d6f4f4 !important;
                font-variation-settings: "wght" 900, "ital" 1 !important;
                transition: all 0.5s ease-in-out !important;
                cursor: pointer;
                
                /* Multi-layered Retro Shadow Stack */
                text-shadow: 6px 6px 0px #07bccc,
                             11px 11px 0px #e601c0,
                             16px 16px 0px #e9019a,
                             21px 21px 0px #f40468,
                             35px 35px 10px rgba(72, 40, 150, 0.6) !important;
            }

            /* Hover Animation State: Shifts axes to thin & straight, drops shadow */
            .stApp h1:hover, .stApp h1:hover span, .stApp h1:hover div {
                font-variation-settings: "wght" 100, "ital" 0 !important;
                text-shadow: none !important;
                color: #d6f4f4 !important; /* Fills text with the stroke color on hover for extra pop */
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #EEF0FF !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_base_layout():
    st.markdown("""
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Climate+Crisis:YEAR@1979&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@100..900&display=swap');
        @import url('https://fonts.googleapis.com/css?family=Poppins:900i');

        /* Global fallback for H1 if not on home page */
        h1, h1 span, h1 div {
            font-family: 'Climate Crisis', sans-serif;
            font-size: 3.5rem;
            line-height: 1.1;
            color: #1a1a2e;
            margin-bottom: 0rem;
        }

        h2, h2 span, h2 div {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 2rem !important;
            line-height: 0.9 !important;
            color: #1a1a2e !important;
            margin-bottom: 0rem !important;
        }

        h3, h4, p, h3 span, h4 span, p span {
            font-family: 'Outfit', sans-serif !important;
            color: #4a4a6a !important;
        }
                
        #mainmenu, footer, header {
            visibility: hidden !important;
        }

        /* ========================================================
           GLOBAL BUTTON OVERRIDES (Retro, Skewed Style)
           ======================================================== */
        button[kind="primary"],
        button[kind="secondary"],
        button[kind="tertiary"],
        button:not([kind]) {
            font-family: 'Poppins', sans-serif !important;
            font-weight: 900 !important;
            font-style: italic !important;
            font-size: 24px !important;
            color: white !important;
            padding: 10px 45px !important;
            border: none !important;
            border-radius: 0px !important;
            transform: skewX(-15deg) !important;
            box-shadow: 6px 6px 0 black !important;
            transition: 0.5s cubic-bezier(0.25, 1, 0.5, 1) !important;
            height: auto !important;
        }

        button[kind="primary"] div p,
        button[kind="secondary"] div p,
        button[kind="tertiary"] div p,
        button:not([kind]) div p {
            font-family: 'Poppins', sans-serif !important;
            color: white !important;
            transform: skewX(15deg) !important;
        }

        button:focus {
            outline: none !important;
            box-shadow: 6px 6px 0 black !important;
        }

        button:hover {
            box-shadow: 10px 10px 0 #FBC638 !important;
            transform: skewX(-15deg) translateY(-2px) !important;
        }

        button:active {
            transform: skewX(-15deg) translate(4px, 4px) !important;
            box-shadow: 2px 2px 0 black !important;
        }
        
        /* Button Colors */
        button[kind="primary"], button:not([kind]) { background-color: #6225E6 !important; }
        button[kind="secondary"] { background-color: #D63384 !important; }
        button[kind="tertiary"] { background-color: #1a1a2e !important; }

        </style>
    """, unsafe_allow_html=True)