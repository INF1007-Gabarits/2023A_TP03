import unittest
import os
import sys
import tempfile
import numpy as np
from io import StringIO



from Partie_2 import*

import unittest


class TestLireClassement(unittest.TestCase):
    def test_empty_file(self):        
        path = "./database/empty.txt"
        result = lire_classement(path)
        self.assertEqual(result, {})

    def test_single_division(self):        
        path = "./database/test_div_1.txt"
        result = lire_classement(path)
        expected = {
            "Atlantic": {
                "Tampa_Bay": {
                    "ABV": "T-B", "MJ": 52, "V": 39, "D": 11, "DP": 2, 
                    "PTS": 80, "VRP": 35, "BP": 205, "BC": 146, "DIFF": 59, "DIV": "Atlantic"
                },
                "Toronto": {
                    "ABV": "TOR", "MJ": 51, "V": 31, "D": 17, "DP": 3, 
                    "PTS": 65, "VRP": 31, "BP": 179, "BC": 145, "DIFF": 34, "DIV": "Atlantic"
                }
            }
        }
        self.assertEqual(result, expected)

    def test_multiple_divisions(self):
        path = "./database/test_div_2.txt"
        result = lire_classement(path)
        expected = {
            "Atlantic": {
                "Tampa_Bay": {
                    "ABV": "T-B", "MJ": 52, "V": 39, "D": 11, "DP": 2, 
                    "PTS": 80, "VRP": 35, "BP": 205, "BC": 146, "DIFF": 59, "DIV": "Atlantic"
                },
                "Toronto": {
                    "ABV": "TOR", "MJ": 51, "V": 31, "D": 17, "DP": 3, 
                    "PTS": 65, "VRP": 31, "BP": 179, "BC": 145, "DIFF": 34, "DIV": "Atlantic"
                }
            },
            "Metropolitan": {
                "NY_Islanders": {
                    "ABV": "NYI", "MJ": 51, "V": 30, "D": 15, "DP": 6, 
                    "PTS": 66, "VRP": 28, "BP": 151, "BC": 125, "DIFF": 26, "DIV": "Metropolitan"
                },
                "Pittsburgh": {
                    "ABV": "PIT", "MJ": 52, "V": 28, "D": 18, "DP": 6, 
                    "PTS": 62, "VRP": 27, "BP": 183, "BC": 160, "DIFF": 23, "DIV": "Metropolitan"
                }
            },
            "Central": {
                "Winnipeg": {
                    "ABV": "WIN", "MJ": 52, "V": 34, "D": 16, "DP": 2, 
                    "PTS": 70, "VRP": 32, "BP": 185, "BC": 146, "DIFF": 39, "DIV": "Central"
                },
                "Nashville": {
                    "ABV": "NAS", "MJ": 54, "V": 31, "D": 19, "DP": 4, 
                    "PTS": 66, "VRP": 30, "BP": 166, "BC": 139, "DIFF": 27, "DIV": "Central"
                },
                "Dallas": {
                    "ABV": "DAL", "MJ": 52, "V": 27, "D": 21, "DP": 4, 
                    "PTS": 58, "VRP": 27, "BP": 133, "BC": 130, "DIFF": 3, "DIV": "Central"
                }
            }
        }

        self.assertEqual(result, expected)

class TestCreerDf(unittest.TestCase):

    def test_empty_dict(self):
        classement = {}
        result = creer_df(classement)
        expected = pd.DataFrame()
        pd.testing.assert_frame_equal(result, expected)

    def test_single_team(self):
        classement = {
            "Atlantic": {
                "Tampa_Bay": {
                    "ABV": "T-B", "MJ": 52, "V": 39, "D": 11, "DP": 2, 
                    "PTS": 80, "VRP": 35, "BP": 205, "BC": 146, "DIFF": 59, "DIV": "Atlantic"
                }
            }
        }
        result = creer_df(classement)
        expected_data = {
            "ABV": ["T-B"],
            "MJ": [52],
            "V": [39],
            "D": [11],
            "DP": [2],
            "PTS": [80],
            "VRP": [35],
            "BP": [205],
            "BC": [146],
            "DIFF": [59],
            "DIV": ["Atlantic"]
        }
        expected = pd.DataFrame(expected_data, index=["Tampa_Bay"])
        pd.testing.assert_frame_equal(result, expected)

    def test_single_division(self):
        classement = {
            "Atlantic": {
                "Tampa_Bay": {
                    "ABV": "T-B", "MJ": 52, "V": 39, "D": 11, "DP": 2,
                    "PTS": 80, "VRP": 35, "BP": 205, "BC": 146, "DIFF": 59, "DIV": "Atlantic"
                },
                "Toronto": {
                    "ABV": "TOR", "MJ": 51, "V": 31, "D": 17, "DP": 3,
                    "PTS": 65, "VRP": 31, "BP": 179, "BC": 145, "DIFF": 34, "DIV": "Atlantic"
                }
            }
        }
        result = creer_df(classement)
        expected_data = {
            "ABV": ["T-B", "TOR"],
            "MJ": [52, 51],
            "V": [39, 31],
            "D": [11, 17],
            "DP": [2, 3],
            "PTS": [80, 65],
            "VRP": [35, 31],
            "BP": [205, 179],
            "BC": [146, 145],
            "DIFF": [59, 34],
            "DIV": ["Atlantic", "Atlantic"]
        }
        expected = pd.DataFrame(expected_data, index=["Tampa_Bay", "Toronto"])
        pd.testing.assert_frame_equal(result, expected)

    def test_multiple_divisions(self):
        classement = {
            "Atlantic": {
                "Tampa_Bay": {
                    "ABV": "T-B", "MJ": 52, "V": 39, "D": 11, "DP": 2,
                    "PTS": 80, "VRP": 35, "BP": 205, "BC": 146, "DIFF": 59, "DIV": "Atlantic"
                },
                "Toronto": {
                    "ABV": "TOR", "MJ": 51, "V": 31, "D": 17, "DP": 3,
                    "PTS": 65, "VRP": 31, "BP": 179, "BC": 145, "DIFF": 34, "DIV": "Atlantic"
                }
            },
            "Central": {
                "Winnipeg": {
                    "ABV": "WIN", "MJ": 52, "V": 34, "D": 16, "DP": 2,
                    "PTS": 70, "VRP": 32, "BP": 185, "BC": 146, "DIFF": 39, "DIV": "Central"
                },
                "Nashville": {
                    "ABV": "NAS", "MJ": 54, "V": 31, "D": 19, "DP": 4,
                    "PTS": 66, "VRP": 30, "BP": 166, "BC": 139, "DIFF": 27, "DIV": "Central"
                }
            }
        }
        result = creer_df(classement)
        expected_data = {
            "ABV": ["T-B", "TOR", "WIN", "NAS"],
            "MJ": [52, 51, 52, 54],
            "V": [39, 31, 34, 31],
            "D": [11, 17, 16, 19],
            "DP": [2, 3, 2, 4],
            "PTS": [80, 65, 70, 66],
            "VRP": [35, 31, 32, 30],
            "BP": [205, 179, 185, 166],
            "BC": [146, 145, 146, 139],
            "DIFF": [59, 34, 39, 27],
            "DIV": ["Atlantic", "Atlantic", "Central", "Central"]
        }
        expected = pd.DataFrame(expected_data, index=["Tampa_Bay", "Toronto", "Winnipeg", "Nashville"])
        pd.testing.assert_frame_equal(result, expected)

class TestDfExtraiteDivison(unittest.TestCase):

    def setUp(self):
        self.data = {
            "ABV": ["T-B", "TOR", "WIN", "NAS"],
            "MJ": [52, 51, 52, 54],
            "V": [39, 31, 34, 31],
            "D": [11, 17, 16, 19],
            "DP": [2, 3, 2, 4],
            "PTS": [80, 65, 70, 66],
            "VRP": [35, 31, 32, 30],
            "BP": [205, 179, 185, 166],
            "BC": [146, 145, 146, 139],
            "DIFF": [59, 34, 39, 27],
            "DIV": ["Atlantic", "Atlantic", "Central", "Central"]
        }
        self.df = pd.DataFrame(self.data, index=["Tampa_Bay", "Toronto", "Winnipeg", "Nashville"])
        

    def test_extract_atlantic_division(self):
        result = df_extraite_divison(self.df, "Atlantic")
        expected_data = {
            "ABV": ["T-B", "TOR"],
            "MJ": [52, 51],
            "V": [39, 31],
            "D": [11, 17],
            "DP": [2, 3],
            "PTS": [80, 65],
            "VRP": [35, 31],
            "BP": [205, 179],
            "BC": [146, 145],
            "DIFF": [59, 34]
        }
        expected = pd.DataFrame(expected_data, index=["Tampa_Bay", "Toronto"])
        pd.testing.assert_frame_equal(result, expected)

    def test_extract_central_division(self):
        result = df_extraite_divison(self.df, "Central")
        expected_data = {
            "ABV": ["WIN", "NAS"],
            "MJ": [52, 54],
            "V": [34, 31],
            "D": [16, 19],
            "DP": [2, 4],
            "PTS": [70, 66],
            "VRP": [32, 30],
            "BP": [185, 166],
            "BC": [146, 139],
            "DIFF": [39, 27]
        }
        expected = pd.DataFrame(expected_data, index=["Winnipeg", "Nashville"])
        pd.testing.assert_frame_equal(result, expected)

class TestDfSortType(unittest.TestCase):

    def test_numeric_ascending(self):
        df = pd.DataFrame({'A': [3, 1, 2], 'B': ['c', 'a', 'b']})
        sorted_df = df_sort_type(df, 'A', True)
        self.assertTrue((sorted_df['A'].values == [1, 2, 3]).all())

    def test_numeric_descending(self):
        df = pd.DataFrame({'A': [3, 1, 2], 'B': ['c', 'a', 'b']})
        sorted_df = df_sort_type(df, 'A', False)
        self.assertTrue((sorted_df['A'].values == [3, 2, 1]).all())

    def test_string_ascending(self):
        df = pd.DataFrame({'A': [3, 1, 2], 'B': ['c', 'a', 'b']})
        sorted_df = df_sort_type(df, 'B', True)
        self.assertTrue((sorted_df['B'].values == ['a', 'b', 'c']).all())

    def test_string_descending(self):
        df = pd.DataFrame({'A': [3, 1, 2], 'B': ['c', 'a', 'b']})
        sorted_df = df_sort_type(df, 'B', False)
        self.assertTrue((sorted_df['B'].values == ['c', 'b', 'a']).all())


class TestDfSummaryInf(unittest.TestCase):
    def test_summary_output(self):

        data = {
            'MJ': [10, 8, 9, 10, 8, 9, 10, 8, 9, 10, 8, 9, 10, 8, 9],
            'V': [8, 5, 7, 7, 6, 5, 6, 7, 6, 5, 6, 7, 7, 6, 5],
            'D': [1, 2, 1, 1, 2, 2, 2, 1, 2, 2, 1, 1, 1, 2, 3],
            'DP': [1, 1, 1, 2, 0, 2, 2, 0, 1, 3, 1, 1, 2, 0, 1],
            'PTS': [17, 11, 15, 16, 12, 12, 14, 14, 13, 13, 13, 15, 16, 12, 11],
            'BP': [25, 20, 23, 24, 22, 21, 22, 23, 21, 20, 21, 24, 25, 22, 19],
            'BC': [12, 15, 13, 14, 13, 14, 15, 14, 15, 17, 14, 13, 12, 13, 16],
            'DIFF': [13, 5, 10, 10, 9, 7, 7, 9, 6, 3, 7, 11, 13, 9, 3],
            'DIV': ['Atlantic', 'Atlantic', 'Atlantic', 
                    'Metropolitan', 'Metropolitan', 'Metropolitan', 
                    'Central', 'Central', 'Central', 
                    'Pacific', 'Pacific', 'Pacific', 
                    'Pacific', 'Pacific', 'Pacific']
        }

        teams = ['Tampa_Bay', 'Toronto', 'Montreal', 
                 'NY_Islanders', 'Pittsburgh', 'Washington', 
                 'Winnipeg', 'Nashville', 'Dallas', 
                 'San_Jose', 'LA_Kings', 'Anaheim_Ducks', 
                 'Vegas_Golden_Knights', 'Calgary', 'Edmonton']

        df_test = pd.DataFrame(data, index=teams)

        # Rediriger la sortie standard vers un tampon pour capturer l'affichage.
        captured_output = StringIO()
        sys.stdout = captured_output
        df_summary_inf(df_test)
        sys.stdout = sys.__stdout__

        # Chaîne de caractère attendue
        expected_output = """Stats division Atlantic:
\t l'équipe qui a le plus de victoire est Tampa_Bay avec 8 victoire
\t l'équipe qui a le plus de défaite est Toronto avec 2 défaite
\t l'équipe qui a le plus de défaite par prolongation est Tampa_Bay avec 1 défaite par prolongation
\t l'équipe qui a le plus de points est Tampa_Bay avec 17 points
\t l'équipe qui a le plus de buts marqués est Tampa_Bay avec 25 buts marqués
\t l'équipe qui a le plus de buts encaissés est Toronto avec 15 buts encaissés
\t l'équipe qui a le plus de différence de buts est Tampa_Bay avec 13 différence de buts

Stats division Metropolitan:
\t l'équipe qui a le plus de victoire est NY_Islanders avec 7 victoire
\t l'équipe qui a le plus de défaite est Pittsburgh avec 2 défaite
\t l'équipe qui a le plus de défaite par prolongation est NY_Islanders avec 2 défaite par prolongation
\t l'équipe qui a le plus de points est NY_Islanders avec 16 points
\t l'équipe qui a le plus de buts marqués est NY_Islanders avec 24 buts marqués
\t l'équipe qui a le plus de buts encaissés est NY_Islanders avec 14 buts encaissés
\t l'équipe qui a le plus de différence de buts est NY_Islanders avec 10 différence de buts

Stats division Central:
\t l'équipe qui a le plus de victoire est Nashville avec 7 victoire
\t l'équipe qui a le plus de défaite est Winnipeg avec 2 défaite
\t l'équipe qui a le plus de défaite par prolongation est Winnipeg avec 2 défaite par prolongation
\t l'équipe qui a le plus de points est Winnipeg avec 14 points
\t l'équipe qui a le plus de buts marqués est Nashville avec 23 buts marqués
\t l'équipe qui a le plus de buts encaissés est Winnipeg avec 15 buts encaissés
\t l'équipe qui a le plus de différence de buts est Nashville avec 9 différence de buts

Stats division Pacific:
\t l'équipe qui a le plus de victoire est Anaheim_Ducks avec 7 victoire
\t l'équipe qui a le plus de défaite est Edmonton avec 3 défaite
\t l'équipe qui a le plus de défaite par prolongation est San_Jose avec 3 défaite par prolongation
\t l'équipe qui a le plus de points est Vegas_Golden_Knights avec 16 points
\t l'équipe qui a le plus de buts marqués est Vegas_Golden_Knights avec 25 buts marqués
\t l'équipe qui a le plus de buts encaissés est San_Jose avec 17 buts encaissés
\t l'équipe qui a le plus de différence de buts est Vegas_Golden_Knights avec 13 différence de buts

Stats ligue:
\t l'équipe qui a le plus de victoire est Tampa_Bay avec 8 victoire
\t l'équipe qui a le plus de défaite est Edmonton avec 3 défaite
\t l'équipe qui a le plus de défaite par prolongation est San_Jose avec 3 défaite par prolongation
\t l'équipe qui a le plus de points est Tampa_Bay avec 17 points
\t l'équipe qui a le plus de buts marqués est Tampa_Bay avec 25 buts marqués
\t l'équipe qui a le plus de buts encaissés est San_Jose avec 17 buts encaissés
\t l'équipe qui a le plus de différence de buts est Tampa_Bay avec 13 différence de buts
"""
        self.assertIn(expected_output, captured_output.getvalue())


if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results_Part_2.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)