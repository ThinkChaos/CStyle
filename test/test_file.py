from . import RuleTest, get_rules


@get_rules
class File(RuleTest):

    def test_80cols(self):
        test_rule = self.get_test_rule('80cols')
        self.assertFalse(test_rule('a' * 80 + '\n'))

        self.assertTrue(test_rule('a' * 81 + '\n'))

    def test_indentation(self):
        test_rule = self.get_test_rule('indentation')

        self.assertFalse(test_rule('    foo\n'))

        self.assertTrue(test_rule('\tfoo\n'))
        self.assertTrue(test_rule('    \t foo\n'))

    def test_terminate(self):
        test_rule = self.get_test_rule('terminate')

        self.assertFalse(test_rule('foo\n'))

        self.assertTrue(test_rule('foo'))

    def test_dos(self):
        test_rule = self.get_test_rule('dos')

        self.assertFalse(test_rule('foo\n'))

        self.assertTrue(test_rule('foo\r\n'))

    def test_trailing(self):
        test_rule = self.get_test_rule('trailing')

        self.assertFalse(test_rule('foo\n'))

        self.assertTrue(test_rule('foo  \n'))
        self.assertTrue(test_rule('foo\t\n'))
        self.assertTrue(test_rule('foo \t  \n'))

    def test_spurious(self):
        test_rule = self.get_test_rule('spurious')

        self.assertFalse(test_rule('foo\n'))

        self.assertTrue(test_rule(
            '\n',
            'foo\n'
        ))
        self.assertTrue(test_rule(
            '\n',
            '\n',
            'foo\n'
        ))
        self.assertTrue(test_rule(
            'foo\n',
            '\n',
            lineno=-1
        ))
        self.assertTrue(test_rule(
            'foo\n',
            '\n',
            '\n',
            lineno=-1
        ))
