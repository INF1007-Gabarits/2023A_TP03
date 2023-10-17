import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from Partie_2 import *

def df_summary_divison(df,type_sort, ascendant):
    pass

def df_summary_league(df,type_sort, ascendant):    
    pass
    

def df_groupby_div(df):
    pass

def df_secteur_div(df, type_data, ascendant):
    pass


if __name__ == '__main__':
    ligue_classement = lire_classement()
    nhl_df = creer_df(ligue_classement)

    df_summary_divison(nhl_df,"PTS", False)
    df_summary_divison(nhl_df,"V", False)
    df_summary_divison(nhl_df,"BP", False)

    df_summary_league(nhl_df,"PTS", False)
    df_summary_league(nhl_df,"V", False)
    df_summary_league(nhl_df,"DIFF", False)
    df_summary_league(nhl_df,"DIFF", True)

    df_secteur_div(nhl_df, "PTS", False)
    df_secteur_div(nhl_df, "PTS", True)

    df_secteur_div(nhl_df, "V", False)
    df_secteur_div(nhl_df, "V", True)
