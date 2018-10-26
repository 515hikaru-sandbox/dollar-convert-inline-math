import unittest

import do2im

class TestCountDollar(unittest.TestCase):
    """
    Dollar の数え上げ処理テスト
    """

    def test_count_no_dollar(self):
        """
        dollar を数えるテスト

        dollar を含まない場合
        """
        s = 'foobarboo'
        result = do2im.count_dollar(s)
        expected = 0
        self.assertEqual(result, expected)

    def test_count_one_dollar(self):
        """
        dollar を数えるテスト

        dollar をひとつ含む
        """
        s = 'this is $'
        result = do2im.count_dollar(s)
        expected = 1
        self.assertEqual(result, expected)

    def test_count_four_dollar(self):
        """
        dollar を数えるテスト

        dollar を4つ含む場合
        """
        s = '$a$ is a number. $a + b$ is expression.'
        expected = 4
        result = do2im.count_dollar(s)
        self.assertEqual(result, expected)

    def test_count_linebreak_dollar(self):
        """
        dollar を数えるテスト

        dollar を改行のある文章が6つ含む場合
        """
        s = '''$a$ is a number. $a + b$ is expression.
        But I want a number $d$.
        '''
        expected = 6
        result = do2im.count_dollar(s)
        self.assertEqual(result, expected)


class TestReplaceDollar(unittest.TestCase):
    """
    $ の置換処理
    """

    def test_no_replace(self):
        """
        $ を含まない文章は置換しない
        """
        s = 'foobarboo'
        result = do2im.replace_dollar(s, even=False)
        expected = 'foobarboo'
        self.assertEqual(result, expected)

    def test_replace(self):
        """
        $...$ を \\(...\\) に置換
        """
        s = '$a$'
        result_one = do2im.replace_dollar(s, even=False)
        expected_one = '\\\\(a$'
        self.assertEqual(result_one, expected_one)
        result_two = do2im.replace_dollar(result_one, even=True)
        expected_two = '\\\\(a\\\\)'
        self.assertEqual(result_two, expected_two)

class TestProcessLine(unittest.TestCase):
    """
    process_line のテスト
    """

    def test_one_line(self):
        """
        1行の変換のテスト
        """
        line = '$a = b$, $a+b$, $\sin x + b$'
        result = do2im.process_line(line)
        expected = '\\\\(a = b\\\\), \\\\(a+b\\\\), \\\\(\sin x + b\\\\)'
        self.assertEqual(result, expected)
