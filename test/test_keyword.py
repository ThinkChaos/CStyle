from . import RuleTest, get_rules


@get_rules
class Keyword(RuleTest):

    def test(self):
        test_rule = self.get_test_rule(None)

        self.assertFalse(test_rule('for (;;)\n'))
        self.assertFalse(test_rule('if (foo)\n'))
        self.assertFalse(test_rule('switch (foo)\n'))
        self.assertFalse(test_rule('while (foo)\n'))
        self.assertFalse(test_rule('break;\n'))
        self.assertFalse(test_rule('  continue;\n'))

        self.assertTrue(test_rule('for(;;)\n'))
        self.assertTrue(test_rule('if  (foo)\n'))
        self.assertTrue(test_rule('switch(foo)\n'))
        self.assertTrue(test_rule('while(foo)\n'))
        self.assertTrue(test_rule('break ;\n'))
        self.assertTrue(test_rule('  continue\t;\n'))

    def test_return(self):
        test_rule = self.get_test_rule('return')

        self.assertFalse(test_rule('return 0;\n'))
        self.assertFalse(test_rule('return a + b;\n'))
        self.assertFalse(test_rule('return;\n'))
        self.assertFalse(test_rule(
            'return (a && b\n',
            '  || c && d);\n'
        ))

        self.assertTrue(test_rule('return (0);\n'))
        self.assertTrue(test_rule('return (a + b);\n'))
        self.assertTrue(test_rule('return ();\n'))
        self.assertTrue(test_rule(
            'return a && b ||\n',
            '  c && d;\n'
        ))

    def test_goto(self):
        test_rule = self.get_test_rule('goto')

        self.assertTrue(test_rule('goto foo;\n'))
