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
    st.title("Welcome to My Portfolio 🌝🌝🌝! ", anchor=False)
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
    "GitHub": "https://github.com/sarafa19",
    "YouTube": "https://www.youtube.com/",
    "LinkedIn": "https://www.linkedin.com/in/aminata-sarah-fatim-diomande/",
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
        {"title": "Diabetes prediction - October 2024",
         "description": "Analyzed the Pima Indian Diabetes dataset to develop a predictive AI model assessing the likelihood of diabetes onset among Pima Indian patients based on historical medical records. The project focused on identifying significant health factors linked to diabetes risk, with model training and testing to maximize prediction accuracy",
         "tools": "Python, Jupyter Notebook, Pandas, Sklearn, Matplotlib",
         "width": 270, 
         "image": "https://c.tenor.com/-ByTb1L5m2EAAAAj/virus.gif"},
        {"title": "Cloud Computing Project: Virtual Machine Network with Linux - October 2024",
         "description": "Executed a cloud computing project involving the creation and configuration of virtual machines (VMs) running Linux, specifically using Ubuntu and Debian distributions. The project focused on establishing a network between the VMs, enabling them to connect, communicate, and exchange messages. This setup provided a practical understanding of cloud networking, inter-VM communication, and system configuration, essential for scalable cloud infrastructure",
         "tools": " Linux (Ubuntu, Debian), VMWare, used for operating system deployment and network configuration across virtual machines to simulate cloud environments and support message exchange",
         "width": 270, 
         "image": "https://media1.giphy.com/media/f9k1tV7HyORcngKF8v/source.gif"},
        {"title": "EfreiCar Datacamp - October 2024",
         "description": "Created EfreiCar, a low-code web application that helps users find cars based on specified locations using the Google Places API. The project aimed to design an intuitive, location-based car search feature, utilizing a low-code approach to streamline development and facilitate a user-friendly experience",
         "tools": "Bubble, Google Cloud Platform - employed for low-code development and API integration to deliver a responsive and efficient search interface",
         "width": 270, 
         "image": "https://th.bing.com/th/id/R.9ec47ab984e936ac2fc55dec45c51d22?rik=ccDh76ujX8Da6w&pid=ImgRaw&r=0"},
        {"title": "Amazon BeReal - October 2024",
         "description": "Advanced Analysis of Real-Time Web-Scraped Data from Amazon. In today's data-driven environment, vast amounts of information are available on the internet across various domains such as news outlets, blogs, forums, and public datasets. Analyzing this data in real-time can uncover valuable insights, trends, and patterns beneficial to businesses, researchers, and policymakers.",
         "tools": "WebScraping, Apache Kafka, Spark Streaming, Hadoop HDFS, Docker",
         "width": 270, 
         "image": "https://i.pinimg.com/originals/71/3a/45/713a458f915977f6599326cf699cd37f.gif"},
        {"title": "Cyclo Paris - October 2024",
         "description": "Conducted an in-depth analysis of bodily accidents involving cyclists in Paris from 2005 to 2021 to explore the impact of improved cycling infrastructure on accident rates. This project aimed to identify trends in cyclist safety, assess factors associated with accident severity, and evaluate the role of urban planning in enhancing cycling safety. Key research questions included: What types of infrastructure are most effective in reducing accident rates? How do accident patterns vary by location, time, and cyclist demographics?",
         "tools": "Python, Streamlit, Pandas, Matplotlib - leveraged for data processing, interactive visualizations, and statistical analyses",
         "width": 270, 
         "image": "https://media3.giphy.com/media/26xBNwL69IM5ng3f2/source.gif"},
        {"title": "Social Network Database management - October 2024",
         "description": "Developed a social network platform enabling users to connect and interact through relationships (friends, romantic connections) and groups. Each user has a personal profile containing basic information (name, email, birthdate, gender, etc.) as well as options to post updates, create pages, and join groups. Users can like pages, comment on friends' posts, and engage in private conversations within their contact circles",
         "tools": "used Oracle SQL for managing user profiles, relationships, and permissions; designed triggers to ensure interaction consistency; and integrated cursors to optimize queries on user interactions (likes, private messages, posts)",
         "width": 270, 
         "image": "https://cdn.dribbble.com/users/473297/screenshots/1533865/socialmedia.gif"},
        {"title": "Multi-label patent classification - September 2024",
         "description": "Developed a Natural Language Processing (NLP) prediction model in response to a request for proposals from LIPSTIP company, aimed at classifying patents by multiple Cooperative Patent Classification (CPC) labels. This project involved building a robust multi-label classification system to accurately categorize patent texts into relevant CPC labels, optimizing model accuracy for diverse and complex classifications in intellectual property",
         "tools": "Python, TensorFlow, Scikit-learn, Multi-Layer Perceptron (MLP) - utilized for model development, training, and evaluation to ensure high precision in multi-label classification tasks.",
         "width": 270, 
         "image": "https://cdn.dribbble.com/users/2851002/screenshots/7151143/media/ceb737f35e10415cd3ce2379040be8a4.gif"},
        {"title": " Scheduling and Shortest Path Optimization Algorithm - September 2024",
         "description": "Developed an applied mathematics algorithm focused on scheduling and path optimization to solve complex routing problems, such as finding the shortest path and determining the critical path. The project utilized algorithms like Bellman-Ford and Dijkstra to efficiently calculate optimal routes and manage task scheduling. This approach enabled precise identification of the most time-efficient paths and key dependencies in project networks, supporting effective resource allocation and minimizing delays.",
         "tools": "Objected Oriented Programming in Java, Bellman-Ford, Dijkstra - applied for shortest path and critical path calculations, enhancing scheduling accuracy and route optimization.",
         "width": 270, 
         "image": "https://media1.tenor.com/images/a1116874768fa37cf0a2ad5147aab585/tenor.gif?itemid=7202023f"},
        {"title": "Sarah Shop architecture based on restful APIs - July 2024",
         "description": " Designed and implemented a comprehensive e-commerce platform, Sarah Shop, with full CRUD (Create, Read, Update, Delete) functionality and integrated state and transaction management. The platform architecture was built on RESTful APIs to enable seamless and efficient handling of e-commerce operations, providing a dynamic and responsive user experience",
         "tools": "MySQL, PHPMyAdmin, JavaScript, vue.js, react.js, Node.js ",
         "width": 270, 
         "image": "https://img.pikbest.com/png-images/20191028/push-shopping-cart-to-woman-gif_2515298.png!bw700"},
        {"title": "E-Library: Library of E-books and Paper Books - July 2024",
         "description": " Developed a modern library management system that accommodates both e-books and paper book resources, offering clients a seamless experience to register online, search the library catalog, reserve books, and manage their borrowings. The project focuses on delivering an efficient user interface for a hybrid library model and relies on a detailed system architecture to support user interactions. Unified Modeling Language (UML) was employed to map out the system's requirements, functionalities, and interactions, covering key areas such as user registration, catalog search, reservations, and borrowing management.",
         "tools": "UML - used extensively for system modeling and defining interactions across core library management functions.",
         "width": 270, 
         "image": "https://media0.giphy.com/media/W4uQ2KZt14br2hJ3sM/giphy.gif"},
        {"title": "Operational Research Algorithm for Transport Optimization - July 2024",
         "description": "Implemented an applied mathematics algorithm in Java to solve transportation problems and optimize costs. The project incorporated the Balas-Hammer and Northwest Corner methods, focusing on minimizing transportation expenses across various shipping routes. The Balas-Hammer algorithm enabled efficient solutions to integer programming problems, while the Northwest Corner method provided an initial feasible solution for optimizing distribution paths, laying the foundation for cost minimization in logistics",
         "tools": " Java - utilized to develop and execute the algorithm, with a focus on transportation optimization and cost efficiency",
         "width": 270, 
         "image": "https://th.bing.com/th/id/R.e62d9afe38bf6bbc8cb336943a7672e6?rik=7%2fjLk7k%2bmfLkUA&riu=http%3a%2f%2fwww.cybervulcans.net%2fsite%2fwp-content%2fuploads%2f2016%2f06%2ftumblr_nihgbrO8La1qa763mo1_500.gif-Image-GIF-500-%c3%97-281-pix.gif&ehk=1dUltbmjVjWcnwr%2b7XMe5b6cOhLM8ygu6KmDX3SwaJs%3d&risl=&pid=ImgRaw&r=0"},
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
    st.subheader("Welcome to My Passionate Journey in Big Data Engineering !", anchor=False)
    st.write(
    """
    I am excited to welcome you to this space that reflects my passion for Data Engineering and the development of innovative solutions😄. As a person full of energy, I firmly believe that curiosity and determination are key to transforming ideas into tangible accomplishments.
    Through my projects, I aim to tackle complex problems 👾 by leveraging my skills in data analysis, machine learning, and web development. Each project you will discover here showcases my commitment to excellence and my ability to face technical challenges.
    """
    )
    # --- SKILLS ---
    st.write("\n")
    st.subheader("Exploring Creativity Through Travel and Collaboration !", anchor=False)
    st.write(
    """
    But beyond my technical skills, I am also a fun and dynamic individual, always ready to take on new challenges. I love to travel and explore unusual places 🌍️, which fuels my creativity and inspires my work. These enriching experiences broaden my horizons and motivate me to incorporate new perspectives 🌷 into my projects.
    I invite you to explore my achievements and see how I combine my technical skills with my passion for innovation. Please feel free to reach out if you'd like to exchange ideas, collaborate, or simply discuss exciting projects🤗. Together, let's push the boundaries of technology and explore new frontiers 🪐!
    """
)
    st.header("My Academic background🗓️")

    timeline_data = [
        {
            "year": 2026,
            "title": "Engineering degree in Big Data Engineering",
            "description": "I will obtain my engineering degree in Big Data Engineering from Efrei Paris. This program is designed to equip me with advanced skills in data processing, analytics, and machine learning, positioning me for success in the ever-evolving landscape of data science.",
            "width": 150,
            "image": "https://etudestech.com/wp-content/uploads/2022/01/logo_efrei_web_bleu-1024x334.png"
        },
        {
            "year": 2025,
            "title": "Second year of Engineering Program - M1",
            "description": "Currently, I am in the second year of the engineering program (M1), focusing on data engineering courses that strengthen my understanding of key concepts and technologies in the field. This year has been pivotal in solidifying my foundation for future studies and professional endeavors.",
            "width": 150,
            "image": "https://etudestech.com/wp-content/uploads/2022/01/logo_efrei_web_bleu-1024x334.png"
        },
        {
            "year": 2024,
            "title": "First year of Engineering Program - L3",
            "description": "In my first year of the engineering program at EFREI, I learned essential tools such as Apache Spark, PySpark, and Power BI. This knowledge has been crucial in enhancing my ability to analyze and visualize data effectively",
            "width": 150,
            "image": "https://www.mondedesgrandesecoles.fr/wp-content/uploads/Efrei-Paris-Campus-Villejuif-ILab-Campus-05000-scaled.jpg"
        },
        {
            "year": 2024,
            "title": "EXCHANGE SEMESTER",
            "description": "I had the opportunity to participate in an exchange semester at AGH University of Science and Technology in Poland, where I studied network programming, networks, and telecommunications. This experience broadened my perspective on the intersection of data engineering and networking.",
            "width": 150,
            "image": "https://www.eduopinions.com/wp-content/uploads/2017/09/University-of-Science-and-Technology-AGH-campus.jpg"
        },
        {
            "year": 2023,
            "title": "CPGE",
            "description": "I attended the French Pre-Engineering Classes (CPGE) in Mathematics and Physics (MPSI) at the Institut National Polytechnique Felix Houphouët Boigny in Côte d'Ivoire. This rigorous program prepared me for the challenges of engineering studies and laid the groundwork for my future academic pursuits",
            "width": 150,
            "image": "https://afriqueitnews.com/wp-content/uploads/inphb.jpeg"
        },
        {
            "year": 2021,
            "title": "HIGH SCHOOL DEGREE",
            "description": "I graduated with hight honors from the Scientific High School of Yamoussoukro in Côte d'Ivoire, where I developed a strong foundation in the sciences. This achievement marked the beginning of my journey into the world of engineering and technology",
            "width": 150,
            "image": "https://bunny-wp-pullzone-vil2btjhll.b-cdn.net/wp-content/uploads/2023/10/Le_Lycee_scientifique_de_Yamoussoukro_03.jpg"
        },
    ]

    for milestone in timeline_data:
        with st.expander(f"**{milestone['year']} - *{milestone['title']}***"):
            st.markdown(milestone["description"])
            st.image(milestone['image'], width=milestone['width'])

