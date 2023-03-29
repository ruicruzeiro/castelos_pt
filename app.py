import folium as fl
import streamlit as st
from streamlit_folium import st_folium
from castelos_dict import castelos_info

st.set_page_config(
    page_title='Castelos de Portugal',
    page_icon='castelo_icon_site.png',
    layout="centered",
    initial_sidebar_state="auto",
    menu_items=None)

st.markdown("""
        ## CASTELOS PORTUGUESES
        """)

st.markdown('<p class="small-font">Informação obtida no excelente site \
    <a href="https://www.castelosdeportugal.pt/">Castelos de Portugal</a></p>',\
    unsafe_allow_html=True)


name_list = []
coord_list = []
popup_list = []

for castelo, info in castelos_info.items():
    if type(info['coordinates']) == list:
        name_list.append(castelo)
        coord_list.append(info['coordinates'])
        html = f'''
            <div style="font-family: Verdana; font-size: 14px">
            <p><u><strong>{castelo}</strong></u></p>
            <p>Concelho: {info['council']}</p>
            <p>Ano de construção: {info['century']}</p>
            <p>Reinado: {info['king']}</p>
            </div>
            '''
        iframe = fl.IFrame(html)
        popup_list.append(fl.Popup(iframe, min_width=300, max_width=300, max_height=125))


map = fl.Map(location=[39.9185272, -7.9137986], tiles='cartodbpositron', zoom_start=7)

feature_group = fl.FeatureGroup(name='Castelos')

for coord, name, popup in zip(coord_list, name_list, popup_list):
    marker = fl.Marker(location=coord, popup=popup, icon=fl.Icon(color='blue', icon='tower'))
    marker.add_to(feature_group)

feature_group.add_to(map)

st_data = st_folium(map, width=725)
