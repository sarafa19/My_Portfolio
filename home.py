import streamlit as st

st.set_page_config(page_title="Mon Portfolio", layout="wide")

# CSS pour changer la couleur de fond
page_bg = '''
<style>
body {
    background-color: #ADD8E6; /* Couleur bleu clair */
}
</style>
'''

# Appliquer le CSS
st.markdown(page_bg, unsafe_allow_html=True)

def main():

    # Barre de navigation
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Aller à", ["🌝Welcome !!!", "🚴‍♂️Cyclo-Paris", "📖Multi-label patent classification",'🛒Amazon BeReal','🚌EfreiCar - Datacamp','🩸Diabetes prediction','essai'])
    
    if page == "🌝Welcome !!!":
        import Accueil
        Accueil.display_home()
    elif page == "🚴‍♂️Cyclo-Paris":
        import Accidents_velo_app  
        Accidents_velo_app.display_projet1() 

if __name__ == "__main__":
    main()
