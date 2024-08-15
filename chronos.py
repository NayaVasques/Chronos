# -*- coding: utf-8 -*-
"""chronos.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1bv0lt7lcJZItMuz0BRiZM72h-dX5pyad
"""

import streamlit as st
import pandas as pd 

# Dicionário para armazenar a disponibilidade (simulação de banco de dados)
availability_data = {'Name': [], 'Monday': [], 'Tuesday': [], 'Wednesday': [], 'Thursday': [], 'Friday': []}

# Função para trocar entre inglês e francês
def translate(language, en_text, fr_text):
    if language == 'English':
        return en_text
    else:
        return fr_text

# Título da Aplicação
st.title('CHRONOS')

# Seleção de Idioma
language = st.selectbox('Choose your language / Choisissez votre langue', ['English', 'Français'])

# Nome do Usuário
name = st.text_input(translate(language, "Your Name", "Votre Nom"))

studentNumber = st.text_input(translate(language, "Your Student Number", "Votre No étudiant"))


# Formulário de Disponibilidade
st.subheader(translate(language, "Select your Availability", "Sélectionnez votre Disponibilité"))
'''Please select all available days and times / Veuillez sélectionner tous les jours et heures disponibles'''


monday = st.multiselect(translate(language, 'Monday', 'Lundi'),
                        ['08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00'])
tuesday = st.multiselect(translate(language, 'Tuesday', 'Mardi'),
                        ['08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00'])
wednesday = st.multiselect(translate(language, 'Wednesday', 'Mercredi'),
                        ['08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00'])
thursday = st.multiselect(translate(language, 'Thursday', 'Jeudi'),
                        ['08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00'])
friday = st.multiselect(translate(language, 'Friday', 'Vendredi'),
                        ['08:00-09:00', '09:00-10:00', '10:00-11:00', '11:00-12:00', '12:00-13:00', '13:00-14:00', '14:00-15:00', '15:00-16:00', '16:00-17:00'])

if st.button(translate(language, 'Submit Availability', 'Envoyer la Disponibilité')):
    # Simula o salvamento no "banco de dados"
    availability_data['Name'].append(name)
    availability_data['Monday'].append(', '.join(monday))
    availability_data['Tuesday'].append(', '.join(tuesday))
    availability_data['Wednesday'].append(', '.join(wednesday))
    availability_data['Thursday'].append(', '.join(thursday))
    availability_data['Friday'].append(', '.join(friday))
    st.success(translate(language, 'Availability submitted!', 'Disponibilité envoyée!'))

# Exibir a disponibilidade de todos
#if st.button(translate(language, 'View Final Schedule', 'Voir le Calendrier Final')):
#   st.subheader(translate(language, 'Collective Schedule', 'Calendrier Collectif'))
#    df = pd.DataFrame(availability_data)
#    st.dataframe(df) 

