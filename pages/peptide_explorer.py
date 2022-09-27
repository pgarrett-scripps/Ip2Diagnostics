import streamlit as st
from senpy.dtaSelectFilter.parser2 import read_file
from util import ployfit_alignment, convert_dta_filter_results_to_peptide_df, get_lines_from_uploaded_file
import plotly.express as px

import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.title('Peptide Explorer')

dta_filter_file = st.file_uploader(label="DTASelect-filter.txt",
                                   type=".txt",
                                   help='DTASelect-filter.txt file containing filtered IDs')


if st.button("Run"):
    _, dta_filter_results, _ = read_file(get_lines_from_uploaded_file(dta_filter_file))
    df = convert_dta_filter_results_to_peptide_df(dta_filter_results)

    df['AlignedPPM'] = ployfit_alignment(df['RetTime'], df['PPM'], 1)
    st.dataframe(df)

    with st.expander('Mass Drift'):
        fig = px.scatter(df,
                         x='RetTime',
                         y='PPM',
                         hover_data=['Sequence'])
        st.plotly_chart(fig)

    pr = df.profile_report()
    st_profile_report(pr)





