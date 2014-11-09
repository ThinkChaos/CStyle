from . import RuleTest, get_rules


@get_rules
class Name(RuleTest):

    def test_reserved(self):
        test_rule = self.get_test_rule('reserved')

        self.assertFalse(test_rule('#define FOO 0xF00\n'))
        self.assertFalse(test_rule('int foo = 0xF00;\n'))

        self.assertTrue(test_rule('#define _FOO 0xF00\n'))
        self.assertTrue(test_rule('int _foo = 0xF00;\n'))
