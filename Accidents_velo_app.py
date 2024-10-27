import streamlit as st
import pandas as pd
import plotly.express as px

@st.cache_data

def load_data():
    data=pd.read_csv('AccidentsVelo3.csv')
    return data
data=load_data()

def display_projet1(): 
    st.title("Analyse des Accidents Corporels Impliquants des Cyclistes de 2005 à 2021")
    st.markdown("Les cyclistes représentent une part importante des usagers de la route, mais leur vulnérabilité dans un environnement où prédominent les véhicules motorisés pose un problème de sécurité. Entre 2005 et 2021, la France a enregistré de nombreux accidents corporels impliquant des cyclistes. La question centrale est : ")
    st.title('Comment les accidents de cyclistes évoluent-ils au fil du temps, et quelles sont les caractéristiques principales de ces accidents ?')

    if st.checkbox("Afficher les données"):
        st.write(data)

    # 1. Sélection de filtres

    année = st.selectbox("Choisir une année :", data['an'].unique())
    df_filtered = data[data['an'] == année]

    st.write(f"Accidents pour l'année {année}:")
    st.write(df_filtered)

    # 2. Carte interactive des accidents

    gravite_mapping = {
        1: "Indemne",
        2: "Blessé léger",
        3: "Blessé hospitalisé",
        4: "Tué"
    }
    data['Etat_gravite'] = data['gravite'].map(gravite_mapping)

    st.markdown("<h3 style='color:pink;'>1. Analyse géographique et gravité des accidents</h3>",unsafe_allow_html=True)
    st.markdown("La carte interactive offre un premier aperçu des accidents par gravité, répartis sur l’ensemble du territoire français. Chaque accident est représenté selon la gravité des blessures : indemne, blessé léger, blessé hospitalisé, ou tué.")


    gravites = list(gravite_mapping.values())
    selected_gravites = st.multiselect("Sélectionnez les niveaux de gravité à afficher :", gravites, gravites)
    filtered_data_gravite = data[data['Etat_gravite'].isin(selected_gravites)]


    def show_map(data):
        fig = px.scatter_mapbox(data,
                            lat='latitude',
                            lon='longitude',
                            color='Etat_gravite',  
                            size='nombreVehicules',
                            hover_name='Numero_accident',
                            mapbox_style='open-street-map',
                            zoom=5)
        st.plotly_chart(fig)
        st.write(
        """
        - La carte montre une concentration d'accidents dans les zones urbaines, particulièrement dans les grandes villes telles que Paris, Lyon et Marseille.
        - Les accidents les plus graves, avec des cyclistes blessés ou tués, sont souvent localisés dans des zones avec une forte densité de véhicules ou des infrastructures routières mal adaptées aux vélos.
        """
        )   

    if st.checkbox("Afficher la carte des accidents"):
        show_map(filtered_data_gravite)


    # 3. Histogramme des Accidents par Année

    st.markdown("<h3 style='color:pink;'>Histogramme des Accidents par Année</h3>",unsafe_allow_html=True)
    st.markdown("L'histogramme des accidents par année montre la fluctuation du nombre d'accidents cyclistes de 2005 à 2021, en fonction de leur gravité.")

    def show_histogram(data):
        fig = px.histogram(data, x='an', color='Etat_gravite', 
                       title='Nombre d\'accidents par année selon la gravité',
                       labels={'an': 'Année'})
        st.plotly_chart(fig)
        st.write(
            """
            - 2005 à 2016 : Le nombre total d'accidents reste assez stable, avec une légère tendance à la baisse après 2014.
            - 2020-2021 : Une chute nette est observée. Cela pourrait être attribué à la pandémie de COVID-19, qui a réduit la circulation routière en 2020 et début 2021 à travers les confinements et restrictions de déplacement liés à la pandémie, réduisant ainsi les risques d'accidents de la route.
            """
            )

    if st.checkbox("Afficher l'histogramme des accidents par année"):
        show_histogram(filtered_data_gravite)  

    # 4. l'histogramme des accidents par heure

    st.markdown("<h3 style='color:pink;'>l'histogramme des accidents par heure</h3>",unsafe_allow_html=True)

    def show_hisyogram2(data):
        fig = px.histogram(data, x='heure', color='Etat_gravite', 
                     title="l'histogramme des accidents par heure",
                     labels={'heure': 'Heure de l\'accident'})
        st.plotly_chart(fig)
        st.write('Les accidents surviennent principalement aux heures de pointe, entre 17h-19h, lorsque le trafic est le plus dense.Le nombre de véhicules impliqués dans les accidents à ces moments tend également à être plus élevé.')
        st.write('Des mesures de gestion de la circulation aux heures de pointe, comme la création de voies réservées aux cyclistes ou la régulation du trafic, peuvent aider à diminuer ces accidents.')

    if st.checkbox("Afficher l'histogramme des accidents par heures"):
        show_hisyogram2(filtered_data_gravite) 


    # 5. Histogramme de la Répartition des Accidents par Sexe

    st.markdown("<h3 style='color:pink;'>Histogramme de la Répartition des Accidents par Sexe</h3>",unsafe_allow_html=True)

    sexe_mapping = {
        1: "Homme",
        2: "Femme"
    }

    data['Etat_sexe'] = data['sexe'].map(sexe_mapping)

    def show_sex_histogram(data):
        fig = px.histogram(data, x='Etat_sexe', color='Etat_sexe', 
                       title='Répartition des accidents par sexe',
                       color_discrete_map={"Homme": "green", "Femme": "gray"},
                       labels={'Etat_sexe': 'Sexe'})
        st.plotly_chart(fig)

    if st.checkbox("Afficher l'histogramme des accidents par sexe"):
        show_sex_histogram(data) 

    # 6. Calendrier des Accidents par Jour et Mois

    st.markdown("<h3 style='color:pink;'>Calendrier des Accidents par Jour et Mois",unsafe_allow_html=True)
    st.write("Les mois d'été, en particulier juillet et août, voient une augmentation significative du nombre d'accidents, probablement en raison d'une hausse des déplacements à vélo pendant les vacances et le beau temps. Les jours en semaine présentent également plus d'accidents, en lien avec les déplacements domicile-travail.")
    st.write("<h3 style='color:pink;'>Proposition de solution :</h3>",unsafe_allow_html=True)
    st.markdown("Pendant les mois d'été, des mesures de sécurité accrues, telles que des pistes cyclables temporaires dans les zones touristiques, et des initiatives locales pour promouvoir la sécurité des cyclistes pourraient réduire les accidents.")

    data['date'] = pd.to_datetime(data['date'], errors='coerce')
    data['jour'] = data['date'].dt.day
    data['mois'] = data['date'].dt.month

    heatmap_data = data.groupby(['mois', 'jour']).size().reset_index(name='nombre_accidents')

    fig = px.density_heatmap(heatmap_data, 
                          x='jour', 
                          y='mois', 
                          z='nombre_accidents', 
                          color_continuous_scale='Viridis',
                          title='Calendrier des Accidents par Jour et Mois',
                          labels={'jour': 'Jour du mois', 'mois': 'Mois', 'nombre_accidents': 'Nombre d\'accidents'})

    fig.update_yaxes(tickvals=list(range(1, 13)), 
                 ticktext=['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Jun', 
                           'Juil', 'Août', 'Sep', 'Oct', 'Nov', 'Déc'])

    if st.checkbox("Afficher le calendrier des accidents par jour et mois"):
        st.plotly_chart(fig)


    # 7.les Courbes d'Évolution par Mois

    st.markdown("<h3 style='color:pink;'>les Courbes d'Évolution par Mois",unsafe_allow_html=True)

    def prepare_monthly_data(data):
        monthly_data = data.groupby([data['date'].dt.year, data['mois']]).size().reset_index(name='nombre_accidents')
        monthly_data.columns = ['annee', 'mois', 'nombre_accidents'] 
        return monthly_data

    def plot_accidents_trend(monthly_data):
        fig = px.line(monthly_data, 
                  x='mois', 
                  y='nombre_accidents', 
                  color='annee', 
                  title='Évolution du Nombre d\'Accidents par Mois (2005-2021)',
                  labels={'mois': 'Mois', 'nombre_accidents': 'Nombre d\'Accidents'},
                  markers=True)  

        fig.update_xaxes(
            tickvals=list(range(1, 13)), 
            ticktext=["Jan", "Fév", "Mar", "Avr", "Mai", "Juin", "Juil", "Août", "Sep", "Oct", "Nov", "Déc"]  # Noms des mois
        )
        fig.update_layout(yaxis_title='Nombre d\'Accidents')
    
        return fig

    monthly_data = prepare_monthly_data(data)

    if st.checkbox("Afficher l'évolution du nombre d'accidents par mois"):
        accidents_trend_fig = plot_accidents_trend(monthly_data)
        st.plotly_chart(accidents_trend_fig)


    st.title("L'aide à la Prise de décisions pour les infrastructures cyclables")
    st.markdown("Grâce à l'identification des zones et périodes à risque, ce projet fournit des informations clés pour l'aménagement des infrastructures. Les décideurs publics peuvent utiliser les données pour :")
    st.write(
            """
            - Promouvoir des mesures temporaires de sécurité, telles que des pistes cyclables supplémentaires pendant l'été.
            - Mettre en place des campagnes de sensibilisation ou des réglementations spécifiques pendant les heures de pointe.
            - Planifier des pistes cyclables sécurisées dans les zones à forte densité d'accidents.
            """
            )
    st.image("https://media3.giphy.com/media/26xBNwL69IM5ng3f2/source.gif", width=500)
    st.write(
            """
            - Améliorer l'infrastructure cycliste : Les zones urbaines à forte densité de véhicules devraient bénéficier d'une infrastructure dédiée aux cyclistes. La création de pistes cyclables continues et protégées pourrait grandement diminuer les accidents, notamment aux intersections où la majorité des accidents graves se produisent
            - Renforcer la sécurité en période estivale et aux heures de pointe : Pendant les mois d'été, des initiatives locales pour renforcer la sécurité, comme des pistes cyclables temporaires, ou des campagnes de sensibilisation pourraient réduire les accidents. De plus, une gestion du trafic aux heures de pointe (par exemple, des voies réservées aux cyclistes) pourrait également diminuer les risques d'accidents.
            - Promouvoir l'éducation routière pour tous les usagers : Sensibiliser les automobilistes et les cyclistes sur le partage de la route, et les informer sur les comportements dangereux à éviter, pourrait réduire le nombre d'accidents.
            """
            )
   
