import streamlit as st


def display_home():
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
    hero()
    social_media()
    show_experiences()
    show_projects()


def hero():
    # --- HERO SECTION ---
    st.title("ABOUT ME", anchor=False)
    col1, col2 = st.columns(2, gap="small", vertical_alignment="center")
    with col1:
        st.image("./images/profile.png", width=300)

    with col2:
        st.title("Aminata Sarah Fatim DIOMANDE", anchor=False)
        st.write(
        "Engineering student in Data science and Artificial Intelligence")
        resume_file = "CV_Sarah_Diomande_Data_English_2.pdf"
        with open(resume_file, "rb") as pdf_file:
            PDFbyte = pdf_file.read()
        st.download_button(
            label="📄 Download Resume",
            data=PDFbyte,
            file_name="CV_Sarah_Diomande_Data_English_2.pdf",
            mime="application/pdf"
        )
        st.write("📫 diomandasf@gmail.com")


def social_media():
    SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/",
    "LinkedIn": "www.linkedin.com/in/aminata-sarah-fatim-diomande",
    "GitHub": "https://github.com/sarafa19",
    "Twitter": "https://twitter.com",
}
    st.write('\n')
    cols = st.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")



def show_projects():
    st.write("")
    st.write("")
    st.header("Some of the projects I worked on 🗂️")
    st.write("")
    st.write("")

    projects = [
        {"title": "Multi-label patent classification",
         "description": "Response to a request for proposals from LIPSTIP for the development of an NLP prediction model to classify texts based on multiple CPC labels ",
         "tools": "Python, Tensorflow, Scikit-learn, MLP",
         "width": 270, 
         "image": "https://cdn.dribbble.com/users/2851002/screenshots/7151143/media/ceb737f35e10415cd3ce2379040be8a4.gif"},
        {"title": "Sarah Shop architecture based on restful APIs",
         "description": "Development of an e-commerce platform performing all CRUD operations with implementation of state and transaction management ",
         "tools": "MySQL, JavaScript, CSS, Node.js",
         "width": 270, 
         "image": "https://img.pikbest.com/png-images/20191028/push-shopping-cart-to-woman-gif_2515298.png!bw700"},
        {"title": "Diabetes prediction",
         "description": "The Pima Indian Diabetes dataset consists of medical records for Pima Indians, indicating whether each patient has a likelihood of developing diabetes within the next few years",
         "tools": "Python, Jupyter Notebook, Pandas, Sklearn, Matplotlib",
         "width": 270, 
         "image": "https://c.tenor.com/-ByTb1L5m2EAAAAj/virus.gif"},
        {"title": "EfreiCar - Datacamp",
         "description": "EfreiCar is a website that allows you to find cars based on a location you enter. It uses the Google places API and is a low-code website using Bubble.",
         "tools": "Bubble, Goodle Cloud Platform",
         "width": 270, 
         "image": "https://th.bing.com/th/id/R.9ec47ab984e936ac2fc55dec45c51d22?rik=ccDh76ujX8Da6w&pid=ImgRaw&r=0"},
        {"title": "Amazon BeReal",
         "description": "Advanced Analysis of Real-Time Web-Scraped Data from Amazon. In today's data-driven environment, vast amounts of information are available on the internet across various domains such as news outlets, blogs, forums, and public datasets. Analyzing this data in real-time can uncover valuable insights, trends, and patterns beneficial to businesses, researchers, and policymakers.",
         "tools": "Python, WebScraping, Apache Kafka, Spark Streaming, Hadoop HDFS",
         "width": 270, 
         "image": "https://i.pinimg.com/originals/71/3a/45/713a458f915977f6599326cf699cd37f.gif"},
        {"title": "Cyclo-Paris",
         "description": "Analysis of Bodily Accidents Involving Cyclists from 2005 to 2021. To what extent do better cycling infrastructure reduce cycling accidents?",
         "tools": "Python, Streamlit, Pandas, Matplotlib",
         "width": 270, 
         "image": "https://media3.giphy.com/media/26xBNwL69IM5ng3f2/source.gif"},
    ]

    for i, project in enumerate(projects):

        if i % 2 == 0:  # display the even projects with image on the left
            col1, col2 = st.columns([2, 5])
            with col1:
                st.image(project['image'],  width=project['width'])
            with col2:
                st.header(project['title'])
                st.write(project['description'])
                st.markdown(f"*{project['tools']}*")
        else:  # display the odd projects with image on the right
            col1, col2 = st.columns([5, 2])
            with col2:
                st.image(project['image'], width=project['width'])

            with col1:
                st.header(project['title'])
                st.write(project['description'])
                st.markdown(f"*{project['tools']}*")
        st.write("")
        st.write("")

def show_experiences():
    st.write("")
    st.write("")
    st.write("")

      # --- EXPERIENCE & QUALIFICATIONS ---
    st.write("\n")
    st.subheader("Experience & Qualifications", anchor=False)
    st.write(
    """
    - 4 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """
    )
    # --- SKILLS ---
    st.write("\n")
    st.subheader("Hard Skills", anchor=False)
    st.write(
    """
    - Programming: Python (Scikit-learn, Pandas), SQL, VBA
    - Data Visualization: PowerBi, MS Excel, Plotly
    - Modeling: Logistic regression, linear regression, decision trees
    - Databases: Postgres, MongoDB, MySQL
    """
)
    st.header("My Professional background🗓️")

    timeline_data = [
        {
            "year": 2026,
            "title": "Master's degree in Big Data Engineering",
            "description": "Diplome d'ingénieur en cours d'étude",
            "width": 150,
            "image": "https://etudestech.com/wp-content/uploads/2022/01/logo_efrei_web_bleu-1024x334.png"
        },
        {
            "year": 2025,
            "title": "Second year of Engineering Program - M1",
            "description": "Efrei Paris - Data engineering courses",
            "width": 70,
            "image": "https://etudestech.com/wp-content/uploads/2022/01/logo_efrei_web_bleu-1024x334.png"
        },
        {
            "year": 2024,
            "title": "First year of Engineering Program - L3",
            "description": "learning of Apache Spark, PySpark and Power BI ",
            "width": 120,
            "image": "https://etudestech.com/wp-content/uploads/2022/01/logo_efrei_web_bleu-1024x334.png"
        },
        {
            "year": 2024,
            "title": "EXCHANGE SEMESTER",
            "description": "AGH University of Science and Technology \n Network programming, Réseaux et telecoms",
            "width": 120,
            "image": "./images/photo1.jpg"
        },
        {
            "year": 2023,
            "title": "CPGE",
            "description": "FRENCH PRE-ENGINEERING CLASSES: MPSI (MATHEMATICS, PHYSICS) \n Institut National Polytechnique Felix Houphouët Boigny \n Côte d'Ivoire",
            "width": 80,
            "image": "./images/photo1.jpg"
        },
        {
            "year": 2021,
            "title": "HIGH SCHOOL DEGREE",
            "description": "Scientific High School of Yamoussoukro \n Côte d'Ivoire",
            "width": 70,
            "image": "./images/photo1.jpg"
        },
    ]

    for milestone in timeline_data:
        with st.expander(f"**{milestone['year']} - *{milestone['title']}***"):
            st.markdown(milestone["description"])
            st.image(milestone['image'], width=milestone['width'])

