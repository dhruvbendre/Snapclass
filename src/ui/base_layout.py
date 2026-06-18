import streamlit as st

def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: #4A56D2 !important;
            }

            .stApp div[data-testid="stColumn"] {
                background-color: #EEF0FF !important;
                padding: 2.5rem !important;
                border-radius: 2rem !important;
                box-shadow: 0 8px 32px rgba(26, 26, 46, 0.15) !important;
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

        h1, h1 span, h1 div {
            font-family: 'Climate Crisis', sans-serif !important;
            font-size: 3.5rem !important;
            line-height: 1.1 !important;
            color: #1a1a2e !important;
            margin-bottom: 0rem !important;
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

        /* --- Primary button (default) --- */
        button[kind="primary"],
        button:not([kind]) {
            font-family: 'Outfit', sans-serif !important;
            font-weight: 500 !important;
            border-radius: 999px !important;
            background-color: #4A56D2 !important;
            color: #ffffff !important;
            padding: 10px 24px !important;
            border: none !important;
            box-shadow: 0 2px 10px rgba(74, 86, 210, 0.30) !important;
            letter-spacing: 0.01em !important;
            transition:
                transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1),
                box-shadow 0.2s ease !important;
        }

        /* --- Secondary button (pink/accent) --- */
        button[kind="secondary"] {
            font-family: 'Outfit', sans-serif !important;
            font-weight: 500 !important;
            border-radius: 999px !important;
            background-color: #D63384 !important;
            color: #ffffff !important;
            padding: 10px 24px !important;
            border: none !important;
            box-shadow: 0 2px 10px rgba(214, 51, 132, 0.28) !important;
            letter-spacing: 0.01em !important;
            transition:
                transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1),
                box-shadow 0.2s ease !important;
        }

        /* --- Tertiary button (dark) --- */
        button[kind="tertiary"] {
            font-family: 'Outfit', sans-serif !important;
            font-weight: 500 !important;
            border-radius: 999px !important;
            background-color: #1a1a2e !important;
            color: #ffffff !important;
            padding: 10px 24px !important;
            border: none !important;
            box-shadow: 0 2px 10px rgba(26, 26, 46, 0.22) !important;
            letter-spacing: 0.01em !important;
            transition:
                transform 0.2s cubic-bezier(0.34, 1.56, 0.64, 1),
                box-shadow 0.2s ease !important;
        }

        /* --- Hover: lift + deeper shadow --- */
        button:hover {
            transform: translateY(-2px) scale(1.03) !important;
            box-shadow: 0 8px 24px rgba(0, 0, 0, 0.18) !important;
        }

        /* --- Active: press-down feel --- */
        button:active {
            transform: scale(0.97) !important;
            box-shadow: none !important;
        }
        </style>
    """, unsafe_allow_html=True)