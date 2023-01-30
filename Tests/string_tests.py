from unittest import TestCase, main
from work_string import parse_string


class Tests_string(TestCase):

    def test_01(self):
        self.assertEqual(parse_string('1k'), '1000')

    def test_02(self):
        self.assertEqual(parse_string('5.6k'), '5600')

    def test_03(self):
        self.assertEqual(parse_string('17.5k'), '17500')

    def test_04(self):
        self.assertEqual(parse_string('121k'), '121000')

    def test_05(self):
        self.assertEqual(parse_string('1.33m'), '1330000')

    def test_06(self):
        self.assertEqual(parse_string('22.8m'), '22800000')

    def test_07(self):
        self.assertEqual(parse_string('666.666666m'), '666666666')

    def test_08(self):
        self.assertEqual(parse_string('0.5g'), '500000000')

    def test_09(self):
        self.assertEqual(parse_string('25.4g'), '25400000000')

    def test_10(self):
        self.assertEqual(parse_string('233.555g'), '233555000000')

    def test_11(self):
        self.assertEqual(parse_string('10k+10k'), '20000')

    def test_12(self):
        self.assertEqual(parse_string('175k+0.5m'), '675000')

    def test_13(self):
        self.assertEqual(parse_string('55.7k+53.68435m+7568.656g'), '7568709740050')

    def test_14(self):
        self.assertAlmostEqual(float(parse_string('12.5+81.6548945k+654.31864381m+687.648315681g')), 688302715992.2045)

    def test_15(self):
        self.assertEqual(parse_string('5k+7k'), '12000')

    def test_16(self):
        self.assertEqual(parse_string('2k+3m+4g'), '4003002000')

    def test_17(self):
        self.assertEqual(parse_string('(3k+5m)'), '5003000')

    def test_18(self):
        self.assertEqual(parse_string('(3k+5m)|(3k+5m)'), '2501500')

    def test_19(self):
        self.assertEqual(parse_string('(3k+5m)|5.003m'), '2501500')

    def test_20(self):
        self.assertEqual(parse_string('5M + (20K + 5M | 5M + 20K) + 5M'), '12540000')

    def test_21(self):
        self.assertEqual(parse_string('1000 + (20K + 20K)|0.04M + 1000'), '22000')

    def test_22(self):
        self.assertEqual(parse_string('((20K + 20K)|0.04M + (50K + 50K)|0.0001G)|70000'), '35000')

    def test_23(self):
        self.assertEqual(parse_string('1.2k+(191k*2+2.4k)|33k|5.1k'), '5567.137979498')

    def test_24(self):
        self.assertEqual(parse_string('1.2k|1.2k+(191k*2+2.4k)|68k|(27k|27k+191k*2)'), '51013.938323465')

    def test_25(self):
        self.assertEqual(parse_string('1.2k|1.2k+(191*k*2+2.4k)|33k|(10k|10k+191k*2)'), '28778.168856439')

    def test_26(self):
        self.assertEqual(parse_string('(1*k+k)'), '2000')

    def test_27(self):
        self.assertEqual(parse_string('(1*k+1*k)|(1*k+1*k)'), '1000')

    def test_28(self):
        self.assertEqual(parse_string('1*k*1*k'), '1000000')

    def test_29(self):
        self.assertEqual(parse_string('((1k+1k)|(1k+1k))|((1k+1k)|(1k+1k))'), '500')

    """
    def test_error(self):
        with self.assertRaises(ValueError) as e:
            calculator('t+k-l')
        self.assertEqual('text', e.exception.args[0])
"""


if __name__ == 'main':  # if ide not pycharm
    main()
