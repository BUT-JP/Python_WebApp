import requests
import streamlit as st
from streamlit_lottie import st_lottie
from PIL import Image


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

# '''
# def load_lottieurl(url):
#     r = requests.get(url)
#     if r.status_code != 200:
#         return None
#     return r.json()
# '''
# Use local CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

#git add --all && git commit -m "v0.0.1" && git push
# ---- HEADER SECTION ----
with st.container():
    st.title(" WebApp powered by Streamlit")
    st.subheader("Pokorný Jan, 2024")
    st.write(
       """
        - lze embedovat kamkoliv a pokud použiji GIT tak se to projeví všude na všech webech, kde jsem to embedoval např. https://sites.google.com/vutbr.cz/vutlca/api
        - https://github.com/BUT-JP/Python_WebApp (Python_WebApp  je private repository)
        - git add --all && git commit -m "v0.0.1" && git push
        - lokální test cmdWIN: d: && cd  d:\00_coding\00_python\07_streamlit\webpage 
        - streamlit run d:\00_coding\00_python\07_streamlit\webpage\app.py
          
       """
    )
    st.write("[Learn More >](https://pythonandvba.com)")



local_css("style/style.css")


# ---- LOAD ASSETS ----
# lottie_coding = load_lottieurl(r"https://assets5.lottiefiles.com/packages/lf20_fcfjwiyb.json")


img_contact_form = Image.open('images/yt_contact_form.png') 
img_lottie_animation =Image.open('images/yt_lottie_animation.png') #Image.open(r"Images/yt_lottie_animation.png")


# ---- HEADER SECTION ----
with st.container():
    st.subheader("Hi, I am Sven :wave:")
    st.title("A Data Analyst From Germany")
    st.write(
        "I am passionate about finding ways to use Python and VBA to be more efficient and effective in business settings."
    )
    st.write("[Learn More >](https://pythonandvba.com)")

# ---- WHAT I DO ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            On my YouTube channel I am creating tutorials for people who:
            - are looking for a way to leverage the power of Python in their day-to-day work.
            - are struggling with repetitive tasks in Excel and are looking for a way to use Python and VBA.
            - want to learn Data Analysis & Data Science to perform meaningful and impactful analyses.
            - are working with Excel and found themselves thinking - "there has to be a better way."

            If this sounds interesting to you, consider subscribing and turning on the notifications, so you don’t miss any content.
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    '''
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
    '''
    
    # ---- PROJECTS ----
with st.container():
    st.write("---")
    st.header("My Projects")
    st.write("##")
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_lottie_animation)
    with text_column:
        st.subheader("Integrate Lottie Animations Inside Your Streamlit App")
        st.write(
            """
            Learn how to use Lottie Files in Streamlit!
            Animations make our web app more engaging and fun, and Lottie Files are the easiest way to do it!
            In this tutorial, I'll show you exactly how to do it
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/TXSOitGoINE)")
with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
         st.image(img_contact_form)
    with text_column:
        st.subheader("How To Add A Contact Form To Your Streamlit App")
        st.write(
            """
            Want to add a contact form to your Streamlit website?
            In this video, I'm going to show you how to implement a contact form in your Streamlit app using the free service ‘Form Submit’.
            """
        )
        st.markdown("[Watch Video...](https://youtu.be/FOULV9Xij_8)")

# ---- CONTACT ----
with st.container():
    st.write("---")
    st.header("Get In Touch With Me!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/YOUR@MAIL.COM" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Your message here" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
   
# ---- VUT ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Odkazy Streamlit, Github, apod.")
        st.write("##")
        st.write(
            """
            Zajímavé odkazy:
            - https://share.streamlit.io/sven-bo/personal-website-streamlit/app.py
            - https://www.youtube.com/watch?v=VqgUkExPvLY
            - https://blog.streamlit.io/introducing-theming/
            - https://github.com/Sven-Bo/personal-website-streamlit
            - https://medium.com/mlearning-ai/pros-and-cons-of-streamlit-8715ca17cc84
            - https://blog.streamlit.io/host-your-streamlit-app-for-free/
            - https://docs.streamlit.io/knowledge-base/tutorials/deploy?ref=blog.streamlit.io
            - https://discuss.streamlit.io/t/is-it-possible-to-display-an-html-file-in-streamlit/23594/6
            - https://morioh.com/a/4d372cfa1d18/how-to-build-a-basic-dashboard-app-with-python-and-streamlit
            - https://python.plainenglish.io/5-creative-python-projects-to-automate-your-life-b3794518d2fc
            - -----------------------------------------------------------------------------
            - https://www.ditoweb.com/2011/08/how-to-copy-google-site-from-one-domain/
            - https://support.google.com/sites/thread/221205420/can-i-transfer-my-google-site-to-a-website-hosting-company?hl=en
            - -----------------------------------------------------------------------------
            - https://stackoverflow.com/questions/37643506/what-is-the-difference-between-a-web-application-and-web-api
            - -----------------------------------------------------------------------------
            - https://www.youtube.com/watch?v=nJHrSvYxzjE
            - -----------------------------------------------------------------------------    
            - https://discuss.streamlit.io/t/two-problems-when-deploying-from-a-folder-in-windows/56169/2
            - always use posix file paths with /, even on windows
            - always use relative paths
            - paths must be relative to the root folder of the github repo to work on streamlit cloud
              
            Python na vše??? Python na matematické výpočty, na Webapp pomocí streamlit, WebAPI pomocí waitress, podopora PowerBI, a další...
            - -----------------------------------------------------------------------------               
            - https://discuss.streamlit.io/t/streamlit-as-a-web-page/39112
            - https://discuss.streamlit.io/t/using-streamlit-to-showcase-my-excel-or-google-sheets-on-a-webpage/51686
            - read://https_discuss.streamlit.io/?url=https%3A%2F%2Fdiscuss.streamlit.io%2Ft%2Fnew-library-streamlit-jupyter-a-new-way-to-develop-streamlit-apps-in-jupyter-notebooks%2F35679
            - https://www.root.cz/clanky/jupyter-notebook-nastroj-pro-programatory-vyzkumniky-i-lektory/     
            -  https://www.dataquest.io/blog/jupyter-notebook-tutorial/      
            - https://github.com/pyvec/naucse-python/blob/main/lessons/intro/notebook/index.ipynb
            - -----------------------------------------------------------------------------    
            - Streamlit code to html to be possible used as applet on sites,google
            - https://discuss.streamlit.io/t/saving-streamlit-application-to-a-webpage/2991
            - IMPORTANT: https://github.com/streamlit/streamlit/issues/611
            It would made streamlit extremely popular if the HTML export existed It is incredible usefull for Data Scientists and the stakeholders would love it
            I hope it gets implemented one day
            - -----------------------------------------------------------------------------   
            - https://stackoverflow.com/questions/74851816/how-to-download-streamlit-output-as-html-file    
            - https://streamlit-release-demos-0-88streamlit-app-0-88-v8ram3.streamlit.app/#download-a-dataframe-converted-to-a-csv
            - -----------------------------------------------------------------------------   
            - https://towardsdatascience.com/3-easy-ways-to-deploy-your-streamlit-web-app-online-7c88bb1024b1
            - https://docs.streamlit.io/streamlit-community-cloud/share-your-app/embed-your-app
              https://pythonwebapp-m7chhvdpacwkmeqpvsed8b.streamlit.app//?embed=true   
            - -----------------------------------------------------------------------------     
            - https://discuss.streamlit.io/t/powerbi-dashboards-and-streamlit/15323
            - https://www.youtube.com/c/MSPowerBI/search
            - https://www.youtube.com/watch?v=Ynt7Etci1KU
            - -----------------------------------------------------------------------------   
            - https://www.youtube.com/watch?v=0T16w4Ubmqk
            - https://www.nobleprog.cz/cc/spacy
            - https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging
            - https://www.freecodecamp.org/news/git-switch-branch/
            - https://www.git-tower.com/learn/git/commands/git-checkout
            - ----------------------------------------------------------------------------- 
            - https://www.mathworks.com/matlabcentral/answers/426258-how-to-convert-the-matlab-code-into-the-python#:~:text=To%20convert%20Matlab%20to%20python,best%20for%20small%2Dlevel%20codes.https://www.mathworks.com/matlabcentral/answers/426258-how-to-convert-the-matlab-code-into-the-python#:~:text=To%20convert%20Matlab%20to%20python,best%20for%20small%2Dlevel%20codes.
            - ----------------------------------------------------------------------------- 
            
            - GIT--------------------------------------------------------- 
            git add --all && git commit -m "v0.0.2" && git push
            git ls-files
            git status
            git ls-tree -r master --name-only
            git checkout master
            git checkout -
            git branch -d repo-01
            
            - GLOBALNE--------------------------------------------------------- 
            git add --all && git commit -m "v0.0.1" && git push
            - LOKALNE---------------------------------------------------------- 
            d:
            cd d:\00_coding\00_python\07_streamlit\webpage 
            streamlit run d:\00_coding\00_python\07_streamlit\webpage\app.py
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    '''
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")
    '''        


# import pandas as pd
# # import streamlit as st


# df=pd.read_csv("test.csv")

# @st.cache
# def convert_df(df):
#     return df.to_html().encode('utf-8')

# html = convert_df(df)

# st.download_button(
#     "Press to Download",
#     html,
#     "test.html"
# )