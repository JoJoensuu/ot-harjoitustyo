import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()

    def test_kassan_rahamaara_oikein(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_kassan_myydyt_lounaat_oikein(self):
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kaitesella_maksu_riittava_kassan_rahamaara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100240)

    def test_syo_edullisesti_kaitesella_maksu_riittava_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(400), 160)

    def test_syo_edullisesti_kateisella_maksu_riittava_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_edullisesti_kateisella(240)
        self.assertEqual(self.kassapaate.edulliset, 1)

    def test_syo_edullisesti_kateisella_maksu_ei_riittava_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_edullisesti_kateisella_maksu_ei_riittava_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_edullisesti_kateisella(200), 200)

    def test_syo_edullisesti_kateisella_maksu_ei_riittava_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_edullisesti_kateisella(200)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kaitesella_maksu_riittava_kassan_rahamaara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100400)

    def test_syo_maukkaasti_kaitesella_maksu_riittava_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(500), 100)

    def test_syo_maukkaasti_kateisella_maksu_riittava_lounaiden_maara_kasvaa(self):
        self.kassapaate.syo_maukkaasti_kateisella(400)
        self.assertEqual(self.kassapaate.maukkaat, 1)

    def test_syo_maukkaasti_kateisella_maksu_ei_riittava_kassan_rahamaara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kateisella_maksu_ei_riittava_vaihtoraha_oikea(self):
        self.assertEqual(self.kassapaate.syo_maukkaasti_kateisella(200), 200)

    def test_syo_maukkaasti_kateisella_maksu_ei_riittava_lounaiden_maara_ei_muutu(self):
        self.kassapaate.syo_maukkaasti_kateisella(200)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_kortilla_tarpeeksi_rahaa_kortin_saldo_muuttuu_oikein(self):
        self.maksukortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_syo_edullisesti_kortilla_kortilla_tarpeeksi_rahaa_kortti_palauttaa_true(self):
        self.maksukortti = Maksukortti(240)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), True)

    def test_syo_edullisesti_kortilla_tarpeeksi_rahaa_lounaiden_maara_kasvaa(self):
        self.maksukortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 1)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_ei_tarpeeksi_rahaa_kortin_saldo_ei_muutu(self):
        self.maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")

    def test_syo_edullisesti_kortilla_ei_tarpeeksi_rahaa_lounaiden_maara_ei_muutu(self):
        self.maksukortti = Maksukortti(200)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.edulliset, 0)
        self.assertEqual(self.kassapaate.maukkaat, 0)

    def test_syo_edullisesti_kortilla_ei_tarpeeksi_rahaa_kortti_palauttaa_false(self):
        self.maksukortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_edullisesti_kortilla(self.maksukortti), False)

    def test_syo_edullisesti_kassan_rahamaara_ei_muutu(self):
        self.maksukortti = Maksukortti(240)
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_syo_maukkaasti_kortilla_kortilla_tarpeeksi_rahaa_kortin_saldo_muuttuu_oikein(self):
        self.maksukortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 0.0")

    def test_syo_maukkaasti_kortilla_kortilla_tarpeeksi_rahaa_kortti_palauttaa_true(self):
        self.maksukortti = Maksukortti(400)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), True)

    def test_syo_maukkaasti_kortilla_tarpeeksi_rahaa_lounaiden_maara_kasvaa(self):
        self.maksukortti = Maksukortti(400)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 1)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kortilla_ei_tarpeeksi_rahaa_kortin_saldo_ei_muutu(self):
        self.maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")

    def test_syo_maukkaasti_kortilla_ei_tarpeeksi_rahaa_lounaiden_maara_ei_muutu(self):
        self.maksukortti = Maksukortti(200)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.maukkaat, 0)
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_syo_maukkaasti_kortilla_ei_tarpeeksi_rahaa_kortti_palauttaa_false(self):
        self.maksukortti = Maksukortti(200)
        self.assertEqual(self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti), False)

    def test_syo_maukkaasti_kassan_rahamaara_ei_muutu(self):
        self.maksukortti = Maksukortti(240)
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_lataa_rahaa_kortille_kortin_saldo_muuttuu(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(str(self.maksukortti), "saldo: 2.0")

    def test_lataa_rahaa_kortille_kassan_rahamaara_kasvaa(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, 100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100100)

    def test_lataa_rahaa_kortille_negatiivinen_summa_ei_muuta_kortin_saldoa(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(str(self.maksukortti), "saldo: 1.0")

    def test_lataa_rahaa_kortille_negatiivinen_summa_ei_muuta_kassan_saldoa(self):
        self.maksukortti = Maksukortti(100)
        self.kassapaate.lataa_rahaa_kortille(self.maksukortti, -100)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)