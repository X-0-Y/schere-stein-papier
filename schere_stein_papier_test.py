import unittest
import schere_stein_papier

class SchereSteinPapierTest(unittest.TestCase):



    def test_vergleich(self):
        actual = schere_stein_papier.gewonnenOderNicht('schere', 'schere')
        self.assertEqual(actual, schere_stein_papier.UNENTSCHIEDEN)

        actual = schere_stein_papier.gewonnenOderNicht('schere', 'stein')
        self.assertEqual(actual, schere_stein_papier.COMPUTER_HAT_GEWONNEN)

        actual = schere_stein_papier.gewonnenOderNicht('schere', 'papier')
        self.assertEqual(actual, schere_stein_papier.SPIELER_HAT_GEWONNEN)

        actual = schere_stein_papier.gewonnenOderNicht('stein', 'schere')
        self.assertEqual(actual, schere_stein_papier.SPIELER_HAT_GEWONNEN)
        
        actual = schere_stein_papier.gewonnenOderNicht('stein', 'stein')
        self.assertEqual(actual, schere_stein_papier.UNENTSCHIEDEN)
        
        actual = schere_stein_papier.gewonnenOderNicht('stein', 'papier')
        self.assertEqual(actual, schere_stein_papier.COMPUTER_HAT_GEWONNEN)

        actual = schere_stein_papier.gewonnenOderNicht('papier', 'schere')
        self.assertEqual(actual, schere_stein_papier.COMPUTER_HAT_GEWONNEN)

        actual = schere_stein_papier.gewonnenOderNicht('papier', 'stein')
        self.assertEqual(actual, schere_stein_papier.SPIELER_HAT_GEWONNEN)
        
        actual = schere_stein_papier.gewonnenOderNicht('papier', 'papier')
        self.assertEqual(actual, schere_stein_papier.UNENTSCHIEDEN)

if __name__ == '__main__':
    unittest.main()
