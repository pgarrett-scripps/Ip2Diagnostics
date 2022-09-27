import streamlit as st
from senpy.dtaSelectFilter.parser2 import read_file
from util import get_lines_from_uploaded_file, convert_dta_filter_results_to_protein_df

import pandas_profiling
from streamlit_pandas_profiling import st_profile_report

st.title('Protein Explorer')

dta_filter_file = st.file_uploader(label="DTASelect-filter.txt",
                                   type=".txt",
                                   help='DTASelect-filter.txt file containing filtered IDs')

if st.button("Run"):
    _, dta_filter_results, _ = read_file(get_lines_from_uploaded_file(dta_filter_file))

    df = convert_dta_filter_results_to_protein_df(dta_filter_results)
    st.dataframe(df)

    pr = df.profile_report()
    st_profile_report(pr)





