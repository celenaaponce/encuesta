import streamlit_survey as ss
import streamlit as st
import smtplib
import json
from streamlit.components.v1 import html
st.markdown("""
            <style>
            .big-font {
                font-size:20px !important;
            }
            </style>
            """, unsafe_allow_html=True)
def send_email(sender, password, receiver, smtp_server, smtp_port, email_message, subject, attachments=None):
    server = smtplib.SMTP(smtp_server, smtp_port)
    server.starttls()
    server.login(sender, password)
    server.sendmail(sender, receiver, email_message)
    server.quit()

placeholder = st.empty()
survey = ss.StreamlitSurvey()

with placeholder.container():

    with st.form("Clases de ASL"):
        st.audio('https://raw.githubusercontent.com/celenaaponce/sandbox/main/additional.mp3')
        st.subheader("¡Hola!  Le he enviado esta encuesta a usted porque usted le ha registrado para las clases de Lengua de Señas en Español y no ha asistido a las clases." 
              + "Para mejorar mis clases, quiero saber más sobre la razon por la que no ha asistido.  Gracias por su tiempo e información.")

        st.markdown('<p class="big-font">Tengo que trabajar durante la clase.</p>', unsafe_allow_html=True)

        survey.select_slider(
            "", options=["Muy de Acuerdo 👍🏽👍🏽", "Algo de Acuerdo 👍🏽", "Ni de Acuerdo Ni en Desacuerdo", "Algo en Desacuerdo 👎🏽", "Muy en Desacuerdo 👎🏽👎🏽"], id="Q1"
        )
        st.header('')
        st.markdown('<p class="big-font">No tengo interés en la clase.</p>', unsafe_allow_html=True)
        survey.select_slider(
            "", options=["Muy de Acuerdo", "Algo de Acuerdo", "Ni de Acuerdo Ni en Desacuerdo", "Algo en Desacuerdo", "Muy en Desacuerdo"], id="Q2"
        )
        st.header('')
        st.markdown('<p class="big-font">No recibí información del horario.</p>', unsafe_allow_html=True)
        survey.select_slider(
            "No recibí información del horario.", options=["Muy de Acuerdo", "Algo de Acuerdo", "Ni de Acuerdo Ni en Desacuerdo", "Algo en Desacuerdo", "Muy en Desacuerdo"], id="Q3"
        )
        st.header('')
        st.markdown('<p class="big-font">No me gusta como enseñan la clase.</p>', unsafe_allow_html=True)

        survey.select_slider(
            "No me gusta como enseñan la clase.", options=["Muy de Acuerdo", "Algo de Acuerdo", "Ni de Acuerdo Ni en Desacuerdo", "Algo en Desacuerdo", "Muy en Desacuerdo"], id="Q4"
        )
        survey.text_input('Información Addiccional:', id='Q5')
        survey.text_input("Nombre y correo electronico (opcional):", id='Q6')
        submitted = st.form_submit_button("Entregar")
        if submitted:


            answers = survey.to_json()
            text = []
            dict_obj = json.loads(answers)
            text.append("I have to work " + dict_obj['Q1']['value'] + "\nNot interested " +dict_obj['Q2']['value'] 
                        + "\nNo schedule " +dict_obj['Q3']['value']+ "\nNot lke " + dict_obj['Q4']['value']
                        + "More info " + dict_obj['Q5']['value'] + "Name " + dict_obj['Q6']['value'])
            variable = "\n".join(text)

            st.write(answers)
            text = send_email(sender = "celena.a.ponce@gmail.com", password = "itsn tbct owcx rbnh", receiver = "celena.a.ponce@gmail.com", smtp_server = "smtp.gmail.com", smtp_port = 587, email_message = variable, subject = "")

            placeholder.empty()

if submitted:
    with placeholder.container():
        st.write(text)
        st.balloons()
        st.header("¡Gracias por su respuesta!")
