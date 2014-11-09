from . import RuleTest, get_rules


@get_rules
class Exp(RuleTest):

    #def test_padding(self):
    #    test_rule = self.get_test_rule('padding')

    #    self.assertFalse(test_rule('x += 10 / ++x & x--;\n'))
    #    self.assertFalse(test_rule('y = a ? b : c;\n'))
    #    self.assertFalse(test_rule('int *x;\n'))
    #    self.assertFalse(test_rule('&foo;\n'))
    #    self.assertFalse(test_rule('10*x;\n'))
    #    self.assertFalse(test_rule('10&x;\n'))
    #    self.assertFalse(test_rule('++y + --x;\n'))
    #    self.assertFalse(test_rule('y++ + x--;\n'))

    #    #self.assertTrue(test_rule('x+=10;\n'))
    #    self.assertTrue(test_rule('x +=10;\n'))
    #    self.assertTrue(test_rule('x+= 10;\n'))
    #    self.assertTrue(test_rule('y?w\n'))
    #    #self.assertTrue(test_rule('x += y+10;\n'))
    #    self.assertTrue(test_rule('++y+--x;\n'))
    #    self.assertTrue(test_rule('y+++ x--;\n'))
    #    self.assertTrue(test_rule('y+++--x;\n'))
    #    self.assertTrue(test_rule('y++ +--x;\n'))

    def test_nopadding(self):
        test_rule = self.get_test_rule('nopadding')

        self.assertFalse(test_rule('x.y\n'))
        self.assertFalse(test_rule('x->y\n'))
        self.assertFalse(test_rule('blah = x.y;\n'))
        self.assertFalse(test_rule('blah = x->y;\n'))

        self.assertTrue(test_rule('x .y\n'))
        self.assertTrue(test_rule('x. y\n'))
        self.assertTrue(test_rule('x . y\n'))
        self.assertTrue(test_rule('blah = x ->y;\n'))
        self.assertTrue(test_rule('blah = x-> y;\n'))
        self.assertTrue(test_rule('blah = x -> y;\n'))
