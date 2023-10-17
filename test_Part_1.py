import unittest
import os
import sys
import tempfile


from Partie_1 import*

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
                    "PTS": 80, "VRP": 35, "BP": 205, "BC": 146, "DIFF": 59
                },
                "Toronto": {
                    "ABV": "TOR", "MJ": 51, "V": 31, "D": 17, "DP": 3, 
                    "PTS": 65, "VRP": 31, "BP": 179, "BC": 145, "DIFF": 34
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
                    "PTS": 80, "VRP": 35, "BP": 205, "BC": 146, "DIFF": 59
                },
                "Toronto": {
                    "ABV": "TOR", "MJ": 51, "V": 31, "D": 17, "DP": 3, 
                    "PTS": 65, "VRP": 31, "BP": 179, "BC": 145, "DIFF": 34
                }
            },
            "Metropolitan": {
                "NY_Islanders": {
                    "ABV": "NYI", "MJ": 51, "V": 30, "D": 15, "DP": 6, 
                    "PTS": 66, "VRP": 28, "BP": 151, "BC": 125, "DIFF": 26
                },
                "Pittsburgh": {
                    "ABV": "PIT", "MJ": 52, "V": 28, "D": 18, "DP": 6, 
                    "PTS": 62, "VRP": 27, "BP": 183, "BC": 160, "DIFF": 23
                }
            },
            "Central": {
                "Winnipeg": {
                    "ABV": "WIN", "MJ": 52, "V": 34, "D": 16, "DP": 2, 
                    "PTS": 70, "VRP": 32, "BP": 185, "BC": 146, "DIFF": 39
                },
                "Nashville": {
                    "ABV": "NAS", "MJ": 54, "V": 31, "D": 19, "DP": 4, 
                    "PTS": 66, "VRP": 30, "BP": 166, "BC": 139, "DIFF": 27
                },
                "Dallas": {
                    "ABV": "DAL", "MJ": 52, "V": 27, "D": 21, "DP": 4, 
                    "PTS": 58, "VRP": 27, "BP": 133, "BC": 130, "DIFF": 3
                }
            }
        }

        self.assertEqual(result, expected)

class TestLireMatch(unittest.TestCase):

    def test_fichier_vide(self):
        path = "./database/empty.txt"
        result = lire_match(path)
        self.assertEqual(result, [])

    def test_fichier_avec_rencontres(self):
        expected_output = [
            ['ANA', 'TOR'],
            ['L-A', 'NYR'],
            ['VAN', 'PHI']
        ]
        path = "./database/test_match.txt"
        result = lire_match(path)

        self.assertEqual(result, expected_output)

class TestEcrireClassement(unittest.TestCase):

    def setUp(self):
        self.classement_sample = {
            "Atlantic": {
                "Tampa_Bay": {
                    "ABV": "T-B", "MJ": 52, "V": 39, "D": 11, "DP": 2, 
                    "PTS": 80, "VRP": 35, "BP": 205, "BC": 146, "DIFF": 59
                },
                "Toronto": {
                    "ABV": "TOR", "MJ": 51, "V": 31, "D": 17, "DP": 3, 
                    "PTS": 65, "VRP": 31, "BP": 179, "BC": 145, "DIFF": 34
                }
            }
        }
        # Crée un fichier temporaire
        self.temp_file = tempfile.NamedTemporaryFile(delete=False)
        self.temp_file.close()  

    def tearDown(self):
        # Supprime le fichier temporaire après le test
        os.unlink(self.temp_file.name)

    def test_ecrire_classement(self):
        expected_content = (
                            "Atlantic     ABV MJ V  D  DP PTS VRP BP  BC  DIFF\n"
                            "Tampa_Bay    T-B 52 39 11  2  80 35  205 146 +59  \n"
                            "Toronto      TOR 51 31 17  3  65 31  179 145 +34  \n"
                            "\n"
                        )

        ecrire_classement(self.classement_sample, self.temp_file.name)

        with open(self.temp_file.name, 'r') as f:
            content = f.read()
        
        self.assertEqual(content, expected_content)

class TestJouerMatch(unittest.TestCase):

    def test_basic(self):
        pts_vis, pts_dom, but_vis, but_dom, vrp = jouer_match(0, 0)
        
        # Assurez-vous que le total des points est 2 ou 3 (soit 2-1, 1-2, 2-0, 0-2).
        self.assertTrue((4 > pts_vis + pts_dom >= 2))
        
        # Assurez-vous que le score est logique.
        self.assertTrue((but_vis > but_dom and pts_vis == 2) or (but_dom > but_vis and pts_dom == 2) or (but_dom == but_vis))

    def test_extreme_diff(self):
        for _ in range(1000):  # Répétez plusieurs fois pour avoir une idée générale.
            _, _, but_vis, but_dom, _ = jouer_match(0, 1000)  # Extrêmement en faveur de l'équipe à domicile.
            self.assertTrue(but_dom >= but_vis)
            
            _, _, but_vis, but_dom, _ = jouer_match(1000, 0)  # Extrêmement en faveur de l'équipe visiteuse.
            self.assertTrue(but_vis >= but_dom)

class TestTrouverEquipeDivision(unittest.TestCase):

    def setUp(self):
        self.classement_sample = {
            "Atlantic": {
                "Tampa_Bay": {
                    "ABV": "T-B", "MJ": 52, "V": 39, "D": 11, "DP": 2, 
                    "PTS": 80, "VRP": 35, "BP": 205, "BC": 146, "DIFF": 59
                },
                "Toronto": {
                    "ABV": "TOR", "MJ": 51, "V": 31, "D": 17, "DP": 3, 
                    "PTS": 65, "VRP": 31, "BP": 179, "BC": 145, "DIFF": 34
                }
            },
            "Metropolitan": {
                "NY_Islanders": {
                    "ABV": "NYI", "MJ": 51, "V": 30, "D": 15, "DP": 6, 
                    "PTS": 66, "VRP": 28, "BP": 151, "BC": 125, "DIFF": 26
                }
            }
        }

    def test_basic(self):
        team, division = trouver_equipe_division("T-B", self.classement_sample)
        self.assertEqual(team, "Tampa_Bay")
        self.assertEqual(division, "Atlantic")
        
        team, division = trouver_equipe_division("NYI", self.classement_sample)
        self.assertEqual(team, "NY_Islanders")
        self.assertEqual(division, "Metropolitan")

    def test_team_not_exist(self):
        result = trouver_equipe_division("XYZ", self.classement_sample)
        self.assertIsNone(result)  # Assurez-vous que votre fonction renvoie None pour une équipe inexistante.


class TestTrierClassement(unittest.TestCase):

    def setUp(self):
        self.classement_sample = {
            "Atlantic": {
                "TeamA": {"PTS": 80, "VRP": 35},
                "TeamB": {"PTS": 65, "VRP": 31},
                "TeamC": {"PTS": 80, "VRP": 30}
            },
            "Metropolitan": {
                "TeamD": {"PTS": 60, "VRP": 29},
                "TeamE": {"PTS": 65, "VRP": 28}
            }
        }

    def test_trier_classement(self):
        trier_classement(self.classement_sample)
        
        # Vérifier le tri pour la division "Atlantic"
        atlantic_teams = list(self.classement_sample["Atlantic"].keys())
        self.assertEqual(atlantic_teams, ["TeamA", "TeamC", "TeamB"])
        
        # Vérifier le tri pour la division "Metropolitan"
        metro_teams = list(self.classement_sample["Metropolitan"].keys())
        self.assertEqual(metro_teams, ["TeamE", "TeamD"])

class TestMiseAJourClassement(unittest.TestCase):

    def setUp(self):
        self.classement = {
            "Atlantic": {
                "TeamA": {"MJ": 5, "PTS": 10, "BP": 10, "BC": 5, "DIFF": 5, "V": 5, "DP": 0, "D": 0}
            }
        }

    def test_victoire(self):
        stats = {"PTS": 2, "BP": 3, "BC": 1}
        mis_a_jour_classement("TeamA", stats, "Atlantic", self.classement)

        self.assertEqual(self.classement["Atlantic"]["TeamA"]["MJ"], 6)
        self.assertEqual(self.classement["Atlantic"]["TeamA"]["PTS"], 12)
        self.assertEqual(self.classement["Atlantic"]["TeamA"]["V"], 6)
        self.assertEqual(self.classement["Atlantic"]["TeamA"]["DIFF"], 7)

    def test_defaite_prolongation(self):
        stats = {"PTS": 1, "BP": 2, "BC": 3}
        mis_a_jour_classement("TeamA", stats, "Atlantic", self.classement)

        self.assertEqual(self.classement["Atlantic"]["TeamA"]["MJ"], 6)
        self.assertEqual(self.classement["Atlantic"]["TeamA"]["PTS"], 11)
        self.assertEqual(self.classement["Atlantic"]["TeamA"]["DP"], 1)
        self.assertEqual(self.classement["Atlantic"]["TeamA"]["DIFF"], 4)

    def test_defaite(self):
        stats = {"PTS": 0, "BP": 1, "BC": 4}
        mis_a_jour_classement("TeamA", stats, "Atlantic", self.classement)

        self.assertEqual(self.classement["Atlantic"]["TeamA"]["MJ"], 6)
        self.assertEqual(self.classement["Atlantic"]["TeamA"]["PTS"], 10)
        self.assertEqual(self.classement["Atlantic"]["TeamA"]["D"], 1)
        self.assertEqual(self.classement["Atlantic"]["TeamA"]["DIFF"], 2)

class TestSimulerRencontres(unittest.TestCase):

    def setUp(self):
        self.classement = {
            "Atlantic": {
                "TeamA": {"ABV": "T-A", "MJ": 5, "PTS": 2, "BP": 10, "BC": 5, "DIFF": 5, "V": 0, "DP": 1, "D": 4, "VRP": 1},
                "TeamB": {"ABV": "T-B", "MJ": 5, "PTS": 5, "BP": 5, "BC": 10, "DIFF": -5, "V": 2, "DP": 1, "D": 2, "VRP": 2}
            }
        }
        self.matchs = [("T-A", "T-B")]

    def test_simulation(self):
        simuler_rencontres(self.matchs, self.classement)
        
        # Vérification des matchs joués
        self.assertEqual(self.classement["Atlantic"]["TeamA"]["MJ"], 6)
        self.assertEqual(self.classement["Atlantic"]["TeamB"]["MJ"], 6)

        # Vérification de la différence de buts
        bp_a = self.classement["Atlantic"]["TeamA"]["BP"]
        bc_a = self.classement["Atlantic"]["TeamA"]["BC"]
        self.assertEqual(bp_a - bc_a, self.classement["Atlantic"]["TeamA"]["DIFF"])

        bp_b = self.classement["Atlantic"]["TeamB"]["BP"]
        bc_b = self.classement["Atlantic"]["TeamB"]["BC"]
        self.assertEqual(bp_b - bc_b, self.classement["Atlantic"]["TeamB"]["DIFF"])

        # Vérification des points
        if self.classement["Atlantic"]["TeamA"]["PTS"] == 4:
            self.assertEqual(self.classement["Atlantic"]["TeamA"]["V"], 1)
        elif self.classement["Atlantic"]["TeamA"]["PTS"] == 3:
            self.assertEqual(self.classement["Atlantic"]["TeamA"]["DP"], 2)
        else:
            self.assertEqual(self.classement["Atlantic"]["TeamA"]["D"], 5)

        if self.classement["Atlantic"]["TeamB"]["PTS"] == 7:
            self.assertEqual(self.classement["Atlantic"]["TeamB"]["V"], 3)
        elif self.classement["Atlantic"]["TeamB"]["PTS"] == 6:
            self.assertEqual(self.classement["Atlantic"]["TeamB"]["DP"], 2)
        else:
            self.assertEqual(self.classement["Atlantic"]["TeamB"]["D"], 3)

        # Vérification du classement
        sorted_teams = list(self.classement["Atlantic"].keys())
        self.assertTrue(self.classement["Atlantic"][sorted_teams[0]]["PTS"] >= self.classement["Atlantic"][sorted_teams[1]]["PTS"])

class TestQualification(unittest.TestCase):
    def test_scenario1(self):
        classement = {
            "Atlantic": {
                "ATeam1": {"PTS": 100, "VRP": 5},
                "ATeam2": {"PTS": 99, "VRP": 4},
                "ATeam3": {"PTS": 98, "VRP": 3},
                "ATeam4": {"PTS": 97, "VRP": 2},
                "ATeam5": {"PTS": 96, "VRP": 1},
            },
            "Metropolitan": {
                "MTeam1": {"PTS": 100, "VRP": 5},
                "MTeam2": {"PTS": 99, "VRP": 4},
                "MTeam3": {"PTS": 98, "VRP": 3},
                "MTeam4": {"PTS": 97, "VRP": 2},
                "MTeam5": {"PTS": 91, "VRP": 1},
            },
            "Central": {
                "CTeam1": {"PTS": 100, "VRP": 5},
                "CTeam2": {"PTS": 99, "VRP": 4},
                "CTeam3": {"PTS": 98, "VRP": 3},
                "CTeam4": {"PTS": 87, "VRP": 2},
                "CTeam5": {"PTS": 86, "VRP": 1},
            },
            "Pacific": {
                "PTeam1": {"PTS": 100, "VRP": 5},
                "PTeam2": {"PTS": 99, "VRP": 4},
                "PTeam3": {"PTS": 98, "VRP": 3},
                "PTeam4": {"PTS": 89, "VRP": 2},
                "PTeam5": {"PTS": 81, "VRP": 1},
            }
        }
        output = equipes_qualifiees(classement)
        expected_output = {
            'Est': ["ATeam1", "ATeam2", "ATeam3", "ATeam4", "MTeam1", "MTeam2", "MTeam3", "MTeam4"],
            'Ouest': ["CTeam1", "CTeam2", "CTeam3", "CTeam4", "PTeam1", "PTeam2", "PTeam3", "PTeam4"]
        }
        self.assertEqual(output, expected_output)

    def test_scenario2(self):
        classement = {
            "Atlantic": {
                "ATeam1": {"PTS": 100, "VRP": 5},
                "ATeam2": {"PTS": 99, "VRP": 4},
                "ATeam3": {"PTS": 98, "VRP": 3},
                "ATeam4": {"PTS": 90, "VRP": 2},
                "ATeam5": {"PTS": 89, "VRP": 1},
            },
            "Metropolitan": {
                "MTeam1": {"PTS": 100, "VRP": 5},
                "MTeam2": {"PTS": 99, "VRP": 4},
                "MTeam3": {"PTS": 98, "VRP": 3},
                "MTeam4": {"PTS": 92, "VRP": 2},
                "MTeam5": {"PTS": 91, "VRP": 1},
            },
            "Central": {
                "CTeam1": {"PTS": 100, "VRP": 5},
                "CTeam2": {"PTS": 99, "VRP": 4},
                "CTeam3": {"PTS": 98, "VRP": 3},
                "CTeam4": {"PTS": 87, "VRP": 2},
                "CTeam5": {"PTS": 86, "VRP": 1},
            },
            "Pacific": {
                "PTeam1": {"PTS": 100, "VRP": 5},
                "PTeam2": {"PTS": 99, "VRP": 4},
                "PTeam3": {"PTS": 98, "VRP": 3},
                "PTeam4": {"PTS": 82, "VRP": 2},
                "PTeam5": {"PTS": 81, "VRP": 1},
            }
        }

        output = equipes_qualifiees(classement)
        expected_output = {
            'Est': ["ATeam1", "ATeam2", "ATeam3", "MTeam5", "MTeam1", "MTeam2", "MTeam3", "MTeam4"],
            'Ouest': ["CTeam1", "CTeam2", "CTeam3", "CTeam4", "PTeam1", "PTeam2", "PTeam3", "CTeam5"]
        }
        self.assertEqual(output, expected_output)

    def test_scenario3(self):
        classement = {
            "Atlantic": {
                "ATeam1": {"PTS": 100, "VRP": 5},
                "ATeam2": {"PTS": 99, "VRP": 4},
                "ATeam3": {"PTS": 98, "VRP": 3},
                "ATeam4": {"PTS": 92, "VRP": 2},
                "ATeam5": {"PTS": 91, "VRP": 1},
            },
            "Metropolitan": {
                "MTeam1": {"PTS": 100, "VRP": 5},
                "MTeam2": {"PTS": 99, "VRP": 4},
                "MTeam3": {"PTS": 98, "VRP": 3},
                "MTeam4": {"PTS": 90, "VRP": 2},
                "MTeam5": {"PTS": 89, "VRP": 1},
            },
            "Central": {
                "CTeam1": {"PTS": 100, "VRP": 5},
                "CTeam2": {"PTS": 99, "VRP": 4},
                "CTeam3": {"PTS": 98, "VRP": 3},
                "CTeam4": {"PTS": 87, "VRP": 2},
                "CTeam5": {"PTS": 86, "VRP": 1},
            },
            "Pacific": {
                "PTeam1": {"PTS": 100, "VRP": 5},
                "PTeam2": {"PTS": 99, "VRP": 4},
                "PTeam3": {"PTS": 98, "VRP": 3},
                "PTeam4": {"PTS": 88, "VRP": 3},
                "PTeam5": {"PTS": 87, "VRP": 3},
            }
        }

        output = equipes_qualifiees(classement)
        expected_output = {
            'Est': ["ATeam1", "ATeam2", "ATeam3", "ATeam4", "MTeam1", "MTeam2", "MTeam3", "ATeam5"],
            'Ouest': ["CTeam1", "CTeam2", "CTeam3", "PTeam5", "PTeam1", "PTeam2", "PTeam3", "PTeam4"]
        }
        self.assertEqual(output, expected_output)

    def test_scenario4(self):
        classement = {
            "Atlantic": {
                "ATeam1": {"PTS": 100, "VRP": 5},
                "ATeam2": {"PTS": 99, "VRP": 4},
                "ATeam3": {"PTS": 98, "VRP": 3},
                "ATeam4": {"PTS": 92, "VRP": 2},
                "ATeam5": {"PTS": 91, "VRP": 1},
            },
            "Metropolitan": {
                "MTeam1": {"PTS": 100, "VRP": 5},
                "MTeam2": {"PTS": 99, "VRP": 4},
                "MTeam3": {"PTS": 98, "VRP": 3},
                "MTeam4": {"PTS": 90, "VRP": 2},
                "MTeam5": {"PTS": 89, "VRP": 1},
            },
            "Central": {
                "CTeam1": {"PTS": 100, "VRP": 5},
                "CTeam2": {"PTS": 99, "VRP": 4},
                "CTeam3": {"PTS": 98, "VRP": 3},
                "CTeam4": {"PTS": 87, "VRP": 2},
                "CTeam5": {"PTS": 86, "VRP": 1},
            },
            "Pacific": {
                "PTeam1": {"PTS": 100, "VRP": 5},
                "PTeam2": {"PTS": 99, "VRP": 4},
                "PTeam3": {"PTS": 98, "VRP": 3},
                "PTeam4": {"PTS": 88, "VRP": 2},
                "PTeam5": {"PTS": 81, "VRP": 1},
            }
        }

        output = equipes_qualifiees(classement)
        expected_output = {
            'Est': ["ATeam1", "ATeam2", "ATeam3", "ATeam4", "MTeam1", "MTeam2", "MTeam3", "ATeam5"],
            'Ouest': ["CTeam1", "CTeam2", "CTeam3", "CTeam4", "PTeam1", "PTeam2", "PTeam3", "PTeam4"]
        }
        self.assertEqual(output, expected_output)

    def test_scenario5(self):
        classement = {
            "Atlantic": {
                "ATeam1": {"PTS": 100, "VRP": 5},
                "ATeam2": {"PTS": 99, "VRP": 4},
                "ATeam3": {"PTS": 98, "VRP": 3},
                "ATeam4": {"PTS": 97, "VRP": 2},
                "ATeam5": {"PTS": 96, "VRP": 1},
            },
            "Metropolitan": {
                "MTeam1": {"PTS": 100, "VRP": 5},
                "MTeam2": {"PTS": 99, "VRP": 4},
                "MTeam3": {"PTS": 98, "VRP": 3},
                "MTeam4": {"PTS": 97, "VRP": 2},
                "MTeam5": {"PTS": 91, "VRP": 1},
            },
            "Central": {
                "CTeam1": {"PTS": 100, "VRP": 5},
                "CTeam2": {"PTS": 99, "VRP": 4},
                "CTeam3": {"PTS": 98, "VRP": 3},
                "CTeam4": {"PTS": 87, "VRP": 0},
                "CTeam5": {"PTS": 86, "VRP": 0},
            },
            "Pacific": {
                "PTeam1": {"PTS": 100, "VRP": 5},
                "PTeam2": {"PTS": 99, "VRP": 4},
                "PTeam3": {"PTS": 98, "VRP": 3},
                "PTeam4": {"PTS": 98, "VRP": 2},
                "PTeam5": {"PTS": 87, "VRP": 1},
            }
        }

        output = equipes_qualifiees(classement)
        expected_output = {
            'Est': ["ATeam1", "ATeam2", "ATeam3", "ATeam4", "MTeam1", "MTeam2", "MTeam3", "MTeam4"],
            'Ouest': ["CTeam1", "CTeam2", "CTeam3", "PTeam5", "PTeam1", "PTeam2", "PTeam3", "PTeam4"]
        }
        self.assertEqual(output, expected_output)

if __name__ == '__main__':
    if not os.path.exists('logs'):
        os.mkdir('logs')
    with open('logs/tests_results_Part_1.txt', 'w') as f:
        loader = unittest.TestLoader()
        suite = loader.loadTestsFromModule(sys.modules[__name__])
        unittest.TextTestRunner(f, verbosity=2).run(suite)
