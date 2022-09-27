import numpy as np
import pandas as pd


def ployfit_alignment(x, y, deg):
    alignment_func = np.poly1d(np.polyfit(x, y, deg))
    shifts = alignment_func(x)
    return y - shifts


def get_lines_from_uploaded_file(file) -> list[str]:
    return file.getvalue().decode("utf-8").split("\n")


def convert_dta_filter_results_to_protein_df(dta_filter_results):
    lines = [line.data for result in dta_filter_results for line in result.proteins]
    df = convert_lines_to_df(lines)
    df['Sequence Coverage'] = list(map(lambda x: float(x.replace("%", "")), df['Sequence Coverage']))
    return df


def convert_dta_filter_results_to_peptide_df(dta_filter_results):
    lines = [line.data for result in dta_filter_results for line in result.peptides]
    df = convert_lines_to_df(lines)
    df['Charge'] = list(map(lambda x: int(x.split(".")[3]), df['FileName']))
    df['ScanNumber'] = list(map(lambda x: int(x.split(".")[1]), df['FileName']))
    df['FileName'] = list(map(lambda x: x.split(".")[0], df['FileName']))
    return df


def convert_lines_to_df(lines):

    df = pd.DataFrame(lines)
    for column in df.columns:
        try:
            df[column] = list(map(int, df[column]))
        except ValueError:
            pass

        try:
            df[column] = list(map(float, df[column]))
        except ValueError:
            pass

    return df
