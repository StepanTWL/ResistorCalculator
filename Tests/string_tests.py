from unittest import TestCase, main
from work_string import parse_string


class Tests_string(TestCase):

    def test_01(self):
        self.assertEqual(parse_string('1k', 'resistor'), '1000.0000000000000')

    def test_02(self):
        self.assertEqual(parse_string('5.6k', 'resistor'), '5600.0000000000000')

    def test_03(self):
        self.assertEqual(parse_string('17.5k', 'resistor'), '17500.0000000000000')

    def test_04(self):
        self.assertEqual(parse_string('121k', 'resistor'), '121000.0000000000000')

    def test_05(self):
        self.assertEqual(parse_string('1.33m', 'resistor'), '1330000.0000000000000')

    def test_06(self):
        self.assertEqual(parse_string('22.8m', 'resistor'), '22800000.0000000000000')

    def test_07(self):
        self.assertEqual(parse_string('666.666666m', 'resistor'), '666666666.0000000000000')

    def test_08(self):
        self.assertEqual(parse_string('0.5g', 'resistor'), '500000000.0000000000000')

    def test_09(self):
        self.assertEqual(parse_string('25.4g', 'resistor'), '25400000000.0000000000000')

    def test_10(self):
        self.assertEqual(parse_string('233.555g', 'resistor'), '233555000000.0000000000000')

    def test_11(self):
        self.assertEqual(parse_string('10k+10k', 'resistor'), '20000.0000000000000')

    def test_12(self):
        self.assertEqual(parse_string('175k+0.5m', 'resistor'), '675000.0000000000000')

    def test_13(self):
        self.assertEqual(parse_string('55.7k+53.68435m+7568.656g', 'resistor'), '7568709740050.0000000000000')

    def test_14(self):
        self.assertAlmostEqual(float(parse_string('12.5+81.6548945k+654.31864381m+687.648315681g', 'resistor')), 688302715992.2045)

    def test_15(self):
        self.assertEqual(parse_string('5k+7k', 'resistor'), '12000.0000000000000')

    def test_16(self):
        self.assertEqual(parse_string('2k+3m+4g', 'resistor'), '4003002000.0000000000000')

    def test_17(self):
        self.assertEqual(parse_string('(3k+5m)', 'resistor'), '5003000.0000000000000')

    def test_18(self):
        self.assertEqual(parse_string('(3k+5m)|(3k+5m)', 'resistor'), '2501500.0000000000000')

    def test_19(self):
        self.assertEqual(parse_string('(3k+5m)|5.003m', 'resistor'), '2501500.0000000000000')

    def test_20(self):
        self.assertEqual(parse_string('5M + (20K + 5M | 5M + 20K) + 5M', 'resistor'), '12540000.0000000000000')

    def test_21(self):
        self.assertEqual(parse_string('1000 + (20K + 20K)|0.04M + 1000', 'resistor'), '22000.0000000000000')

    def test_22(self):
        self.assertEqual(parse_string('((20K + 20K)|0.04M + (50K + 50K)|0.0001G)|70000', 'resistor'), '35000.0000000000000')

    def test_23(self):
        self.assertEqual(parse_string('1.2k+(191k*2+2.4k)|33k|5.1k', 'resistor'), '5567.1379794976893')

    def test_24(self):
        self.assertEqual(parse_string('1.2k|1.2k+(191k*2+2.4k)|68k|(27k|27k+191k*2)', 'resistor'), '51013.9383234648406')

    def test_25(self):
        self.assertEqual(parse_string('1.2k|1.2k+(191*k*2+2.4k)|33k|(10k|10k+191k*2)', 'resistor'), '28778.1688564393092')

    def test_26(self):
        self.assertEqual(parse_string('(1*k+k)', 'resistor'), '2000.0000000000000')

    def test_27(self):
        self.assertEqual(parse_string('(1*k+1*k)|(1*k+1*k)', 'resistor'), '1000.0000000000000')

    def test_28(self):
        self.assertEqual(parse_string('1*k*1*k', 'resistor'), '1000000.0000000000000')

    def test_29(self):
        self.assertEqual(parse_string('((1k+1k)|(1k+1k))|((1k+1k)|(1k+1k))', 'resistor'), '500.0000000000000')

    """
    def test_error(self):
        with self.assertRaises(ValueError) as e:
            calculator('t+k-l')
        self.assertEqual('text', e.exception.args[0])
"""


if __name__ == 'main':  # if ide not pycharm
    main()
