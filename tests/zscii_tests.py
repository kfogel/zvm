#
# Unit tests for the zscii class.
#
# For the license of this file, please consult the LICENSE file in the
# root directory of this distribution.
#
from unittest import TestCase
from zvm import zstring
from zvm import zmemory

def make_zmemory():
    # We use Graham Nelson's 'curses' game for our unittests.
    storydata = open("stories/curses.z5", "rb").read()
    return zmemory.ZMemory(storydata)

class ZsciiTranslatorTests(TestCase):
    def testCreateTranslator(self):
        """Test that the ZSCII translator can be instanciated
        correctly."""
        z = zstring.ZsciiTranslator(make_zmemory())

    def testGetUnicode(self):
        """Try a couple of zscii-to-unicode conversions, involving
        various ranges of the output spectrum."""
        z = zstring.ZsciiTranslator(make_zmemory())
        self.assertEqual(z.ztou(97), "a")
        self.assertEqual(z.ztou(10), "\n")
        self.assertEqual(z.ztou(168), "\xcf")
        self.assertRaises(IndexError, z.ztou, z.CUR_UP)

    def testGetZscii(self):
        """Try a couple of unicode-to-zscii conversions, involving
        various ranges of the input spectrum."""
        z = zstring.ZsciiTranslator(make_zmemory())
        self.assertEqual(z.utoz("a"), 97)
        self.assertEqual(z.utoz("\n"), 10)
        self.assertEqual(z.utoz("\xcf"), 168)
        self.assertEqual(z.utoz(z.CUR_UP), 129)
        self.assertEqual(z.utoz(z.MOUSE_CLICK), 254)


class ZCharTranslatorTest(TestCase):
    def testZCharTranslation(self):
        z = zstring.ZCharTranslator(make_zmemory())
        # This should spell 'Test!'.
        test_zstr = [4, 25, 10, 24, 25, 5, 20]
        expected_zscii = [c for c in 'Test!']
        result_zscii = z.get(test_zstr)


class ZStringTranslatorTest(TestCase):
    def testZStringTranslator(self):
        mem = make_zmemory()
        z = zstring.ZStringTranslator(mem)
        # Read the word 'adamantin' from the curses dictionary. It is
        # located at address 29667 in the curses memory.
        expected_zstr = [6, 9, 6, 18, 6, 19, 25, 14, 19]
        output_zstr = z.get(29667)
        self.assertEqual(output_zstr, expected_zstr)
