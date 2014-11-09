from . import RuleTest, get_rules


@get_rules
class Braces(RuleTest):

    def test(self):
        test_rule = self.get_test_rule(None)

        self.assertFalse(test_rule(
            'else',
            '{',
            lineno=1
        ))
        self.assertFalse(test_rule(
            'else',
            '  {',
            lineno=1
        ))

        self.assertTrue(test_rule('else{'))
        self.assertTrue(test_rule('else {'))

    def test_open(self):
        test_rule = self.get_test_rule('open')

        self.assertFalse(test_rule(
            'else',
            '{',
            lineno=1
        ))
        self.assertFalse(test_rule(
            'else',
            '  {',
            lineno=1
        ))

        self.assertTrue(test_rule(
            'else',
            '    {',
            lineno=1
        ))

    def test_indent(self):
        test_rule = self.get_test_rule('indent')

        self.assertFalse(test_rule(
            '{\n',
            '    foo();\n',
            '}\n',
            lineno=1
        ))
        self.assertFalse(test_rule(
            '{\n',
            '    foo();\n',
            '}\n',
            lineno=-1
        ))
        self.assertFalse(test_rule(
            '{\n',
            '    foo();\n',
            '\n',
            '}\n',
            lineno=-1
        ))

        self.assertTrue(test_rule(
            '{\n',
            'foo();\n',
            '}\n',
            lineno=1
        ))
        self.assertTrue(test_rule(
            '{\n',
            'foo();\n',
            '}\n',
            lineno=-1
        ))
        self.assertTrue(test_rule(
            '{\n',
            '        foo();\n',
            '}\n',
            lineno=1
        ))
        self.assertTrue(test_rule(
            'foo\n',
            '}\n',
            '{\n',
            lineno=1
        ))
        self.assertTrue(test_rule(
            '}\n',
            '{\n',
            'foo\n',
            lineno=-1
        ))

    def test_dowhile(self):
        test_rule = self.get_test_rule('dowhile')

        self.assertFalse(test_rule('do {\n'))

        self.assertTrue(test_rule(
            'do\n',
            '{\n'
        ))

    def test_useless(self):
        test_rule = self.get_test_rule('useless')

        self.assertFalse(test_rule(
            '{\n',
            '  foo();\n',
            '  bar()\n;',
            '}\n'
        ))

        self.assertTrue(test_rule(
            'if (foo)\n',
            '{\n',
            '  foo();\n',
            '}\n',
            lineno=2
        ))
