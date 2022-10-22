import ast
import os
import sys
import unittest
from unittest.mock import ANY, MagicMock, Mock, patch


class TestSnake(unittest.TestCase):
    def test_file_exists(self):
        self.assertTrue(os.path.isfile("snake.py"),
                        "Un fichier snake.py doit exister...")

    def test_does_not_have_numpy(self):
        import_numpy = "import numpy"
        from_numpy = "from numpy"
        with open("snake.py", "r") as f:
            contents = f.read()
            self.assertTrue(
                import_numpy not in contents and from_numpy not in contents, "Le fichier snake.py ne doit pas importer numpy")

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
        pygame = MagicMock()
        pygame.init = Mock()
        pygame.display = Mock()
        pygame.display.set_mode = Mock()
        # Make sure that the "while" loop is not executed
        pygame.display.set_mode.side_effect = Exception("stop run")
        sys.modules['pygame'] = pygame
        # Stuff that could be imported and would make the test fail
        sys.modules['pygame.constants'] = Mock()
        sys.modules['pygame.time'] = Mock()
        sys.modules['pygame.event'] = Mock()
        sys.modules['pygame.draw'] = Mock()
        try:
            import snake
        except:
            pass
        pygame.init.assert_any_call()
        pygame.display.set_mode.assert_any_call(ANY)
