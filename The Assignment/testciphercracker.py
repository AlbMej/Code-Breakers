import unittest
try:
    from ciphercracker import CipherCracker
except:
    from ciphercracker_solutions import CipherCracker

class TestCipherCracker(unittest.TestCase):
    def setUp(self):
        # Here is a text encdoded with the codeword "ZEPHYR"
        self.ciphertext = """IWYO V HYJPYOHYH RKNQ IWY JVHY NR IWY PNZPW, ZJ IWY PZSBPWY DZJ PSNJY ZSNOXJVHY, IWY HKVFYK WYSMVOX QY DVIW Z WZOH DWVPW PZGXWI QB ZKQ VO Z XKVM NR JIYYS; WVJ JIKYOXIW QGJI WZFY EYYO MKNHVXVNGJ. DVIWNGI Z DNKH WY JWNNT WVJ KYVOJ, IWY WNKJYJ IGKOYH, ZOH DY JDYMI VOIN IWY HZKTOYJJ NR IWY MZJJ. ZJ V SNNTYH EZPT V JZD IWY JIYZQ RKNQ IWY WNKJYJ NR IWY PNZPW EB IWY SVXWI NR IWY SZQMJ, ZOH MKNUYPIYH ZXZVOJI VI IWY RVXGKYJ NR QB SZIY PNQMZOVNOJ PKNJJVOX IWYQJYSFYJ. IWYO IWY HKVFYK PKZPTYH WVJ DWVM ZOH PZSSYH IN WVJ WNKJYJ, ZOH NRR IWYB JDYMI NO IWYVK DZB IN EGTNFVOZ. ZJ IWYB JZOT VOIN IWY HZKTOYJJ V RYSI Z JIKZOXY PWVSS, ZOH Z SNOYSB RYYSVOX PZQY NFYK QY; EGI Z PSNZT DZJ IWKNDO NFYK QB JWNGSHYKJ, ZOH Z KGX ZPKNJJ QB TOYYJ, ZOH IWY HKVFYK JZVH VO YCPYSSYOI XYKQZO:-- "IWY OVXWI VJ PWVSS, QYVO WYKK, ZOH QB QZJIYK IWY PNGOI EZHY QY IZTY ZSS PZKY NR BNG. IWYKY VJ Z RSZJT NR JSVFNFVIA (IWY MSGQ EKZOHB NR IWY PNGOIKB) GOHYKOYZIW IWY JYZI, VR BNG JWNGSH KYLGVKY VI." V HVH ONI IZTY ZOB, EGI VI DZJ Z PNQRNKI IN TOND VI DZJ IWYKY ZSS IWY JZQY. V RYSI Z SVIISY JIKZOXYSB, ZOH ONI Z SVIISY RKVXWIYOYH. V IWVOT WZH IWYKY EYYO ZOB ZSIYKOZIVFY V JWNGSH WZFY IZTYO VI, VOJIYZH NR MKNJYPGIVOX IWZI GOTONDO OVXWI UNGKOYB. IWY PZKKVZXY DYOI ZI Z WZKH MZPY JIKZVXWI ZSNOX, IWYO DY QZHY Z PNQMSYIY IGKO ZOH DYOI ZSNOX ZONIWYK JIKZVXWI KNZH. VI JYYQYH IN QY IWZI DY DYKY JVQMSB XNVOX NFYK ZOH NFYK IWY JZQY XKNGOH ZXZVO; ZOH JN V INNT ONIY NR JNQY JZSVYOI MNVOI, ZOH RNGOH IWZI IWVJ DZJ JN. V DNGSH WZFY SVTYH IN WZFY ZJTYH IWY HKVFYK DWZI IWVJ ZSS QYZOI, EGI V KYZSSB RYZKYH IN HN JN, RNK V IWNGXWI IWZI, MSZPYH ZJ V DZJ, ZOB MKNIYJI DNGSH WZFY WZH ON YRRYPI VO PZJY IWYKY WZH EYYO ZO VOIYOIVNO IN HYSZB. EB-ZOH-EB, WNDYFYK, ZJ V DZJ PGKVNGJ IN TOND WND IVQY DZJ MZJJVOX, V JIKGPT Z QZIPW, ZOH EB VIJ RSZQY SNNTYH ZI QB DZIPW; VI DZJ DVIWVO Z RYD QVOGIYJ NR QVHOVXWI. IWVJ XZFY QY Z JNKI NR JWNPT, RNK V JGMMNJY IWY XYOYKZS JGMYKJIVIVNO ZENGI QVHOVXWI DZJ VOPKYZJYH EB QB KYPYOI YCMYKVYOPYJ. V DZVIYH DVIW Z JVPT RYYSVOX NR JGJMYOJY."""

    def testconstructor(self):
        c = CipherCracker("X")

    def testdecode(self):
        preamble = "ABA" + "X" * 27
        message = "ABCDF"
        c = CipherCracker(preamble + message)
        self.assertEqual(c.decode(0,1), "AZYXV")
        self.assertEqual(c.decode(1,3), "BAZYW")

    def testdecodewithcodewordatend(self):
        preamble = "X" * 27 + "ZYZ"
        message = "ABZCD"
        c = CipherCracker(preamble + message)
        self.assertEqual(c.decode(0,1), "ZYBXW")
        self.assertEqual(c.decode(27,28), "ZYAXW")
        self.assertEqual(c.decode(28,30), "ZYBXW")

    def testquality(self):
        preamble = "DZEPHYRKLMNEDABCEFGHIJKLMNEFGH"
        c = CipherCracker(preamble + self.ciphertext)
        for i in range(2,20):
            self.assertTrue(c.quality(1,7) > c.quality(i, i+6))

    def testquality2(self):
        preamble = "EFGHKLMNEDABCDEFGHIJKLMNZEPHYR"
        c = CipherCracker(preamble + self.ciphertext)
        for i in range(1,20):
            self.assertTrue(c.quality(24,30) > c.quality(i, i+6))

    def testmostlikelycodeword(self):
        preamble = "EFGHKLMNEDABCDEFGHIJKLMNZEPHYR"
        c = CipherCracker(preamble + self.ciphertext)
        self.assertEqual(c.mostlikelycodeword(), "ZEPHYR")
        preamble = "KLMNEFGHIJKLMNZEPHYREDABCDEFGH"
        c = CipherCracker(preamble + self.ciphertext)
        self.assertEqual(c.mostlikelycodeword(), "ZEPHYR")

    def testmostlikelydecode(self):
        plaintext = """IN A LITTLE WHILE THE PROFESSOR SIGNALLED TO ME, SO I GOT UP AND JOINED HIM. HE HAD FOUND A WONDERFUL SPOT, A SORT OF NATURAL HOLLOW IN A ROCK, WITH AN ENTRANCE LIKE A DOORWAY BETWEEN TWO BOULDERS. HE TOOK ME BY THE HAND AND DREW ME IN: "SEE!" HE SAID, "HERE YOU WILL BE IN SHELTER; AND IF THE WOLVES DO COME I CAN MEET THEM ONE BY ONE."""
        ciphertext = """VO Z SVIISY DWVSY IWY MKNRYJJNK JVXOZSSYH IN QY, JN V XNI GM ZOH UNVOYH WVQ. WY WZH RNGOH Z DNOHYKRGS JMNI, Z JNKI NR OZIGKZS WNSSND VO Z KNPT, DVIW ZO YOIKZOPY SVTY Z HNNKDZB EYIDYYO IDN ENGSHYKJ. WY INNT QY EB IWY WZOH ZOH HKYD QY VO: "JYY!" WY JZVH, "WYKY BNG DVSS EY VO JWYSIYK; ZOH VR IWY DNSFYJ HN PNQY V PZO QYYI IWYQ NOY EB NOY."""
        preamble = "KLMNEFGHIJKZEPHYRLMNEDABCDEFGH"
        c = CipherCracker(preamble + ciphertext)
        decoded = c.mostlikelydecode()
        self.assertEqual(decoded[:25], plaintext[:25])


if __name__ == '__main__':
    unittest.main()
