import pandas as pd

dic_abv = {
            'V': "victoire",
            'D': "défaite",
            'DP': "défaite par prolongation",
            'PTS': "points",
            'BP': "buts marqués",
            'BC': "buts encaissés",
            'DIFF': "différence de buts"
        }

division = ["Atlantic","Metropolitan","Central","Pacific"]

def lire_classement(path):
    pass


def creer_df(classement):
    pass

def df_extraite_divison(df, divison):
    pass

def df_sort_type(df, type_sort, ascendant):
    pass

def df_summary_inf(df):
    pass

if __name__ == '__main__':
    path = './database/classement2019.txt'
    ligue_classement = lire_classement(path)

    nhl_df = creer_df(ligue_classement)

    print(nhl_df)
    print("\n")

    for div in division:
        print(df_extraite_divison(nhl_df, div))
        print("\n")


    nhl_df_sort_by_pts = df_sort_type(nhl_df, "PTS", False)
    print(nhl_df_sort_by_pts)
    print("\n")

    nhl_div_df = df_extraite_divison(nhl_df, "Atlantic")
    nhl_div_df_sort_by_v = df_sort_type(nhl_div_df, "V", True)
    print(nhl_div_df_sort_by_v)

    print("\n")
    df_summary_inf(nhl_df)