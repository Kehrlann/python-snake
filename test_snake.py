import unittest
import os
import ast
from unittest.mock import patch
from unittest.mock import ANY


class TestSnake(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(os.path.isfile("snake.py"),
                        "Un fichier snake.py doit exister...")

    def test_has_pygame(self):
        import_pygame = "import pygame"
        from_pygame = "from pygame import"
        with open("snake.py", "r") as f:
            contents = f.read()
            self.assertTrue(
                import_pygame in contents or from_pygame in contents, "Le fichier snake.py doit importer pygame")

    def test_parses(self):
        with open("snake.py", "r") as f:
            try:
                ast.parse(f.read())
            except:
                self.fail(
                    "Le fichier snake.py ne contient pas un script python valide...")

    def test_runs(self):
        with patch('pygame.init') as init, patch('pygame.display.set_mode') as display:
            try:
                import snake
            except:
                pass
            init.assert_any_call()
            display.assert_any_call(ANY)
