import streamlit as st
from helper.helper import Helper
import pandas as pd

if 'herlper' not in st.session_state:
    st.session_state.helper = Helper(dsn='impala-prod-cdppc')

if 'df' not in st.session_state:
    st.session_state.df = pd.DataFrame()

if 'check_set' not in st.session_state:
    st.session_state.check_set = dict()

if 'type_flag' not in st.session_state:
    st.session_state.type_flag = True

def back():
    st.session_state.type_flag = True

def load_table():
    try:
        st.session_state.df = st.session_state.helper.obtener_dataframe(f'SELECT * FROM {st.session_state.table_name} LIMIT 5;')
    except:
        st.warning('No se pudo cargar la tabla')

def select():
    st.session_state.type_flag = False
    st.session_state.type = st.session_state.type_selected

    

st.title("🧪 PyDQ Studio – Data Quality Monitor")

st.write("Configura el monitoreo de calidad de datos para tablas de la LZ.")

with st.form('load_table_form'):
    st.text_input(
        "Nombre completo de la tabla en la LZ",
        placeholder="ej: resultados.cartera_detallada",
        key='table_name'
    )
    st.form_submit_button('Monitorear tabla', type='primary', width='stretch', on_click=load_table)

st.divider()
with st.expander(':material/flyover: Vista de la tabla'):
    st.dataframe(st.session_state.df)
st.divider()

if not st.session_state.df.empty:

    st.title("Gestor de Conjuntos de Checks")
    

    rowcheck_available = ['ColumnLessThanCheck', 'ColumnGreaterThanCheck', 'DateBetweenCheck', 'DateMaxCheck', 'IsContainedInCheck']
    aggrecheck_available = ['ColumnsAreCompleteCheck', 'IsNotContainedInCheck', 'CompletenessRatioCheckConfig']

    
    if st.session_state.type_flag:
        with st.form('select_type'):
            st.selectbox('Tipo de check', options=['Row-level check', 'Aggregate check', 'Custom check'], key='type_selected')
            st.form_submit_button('Continuar', type='primary', width='stretch', on_click=select)

    else:
        izq,_,_,_ = st.columns(4)
        with izq:
            st.button(':material/arrow_back:', on_click=back)
        
        if st.session_state.type == 'Row-level check':
            st.subheader('Check por registro')
        elif st.session_state.type == 'Aggregate check':
            st.subheader('Check por df')
        else:
            st.subheader('Check personalizado')

    
    









