import pytest

from src.node import Node
from src.mapGenerator import MapGenerator
from src.consoleMapLogger import ConsoleMapLogger
from src.htmlMapLogger import HtmlMapLogger

@pytest.fixture
def create_simple_map():
    map_gen = MapGenerator(width=2, height=2, percentage_of_trees=0)
    map_gen.generate()
    map_gen.grid[0][0].state = Node.EMPTY
    map_gen.grid[0][1].state = Node.TREE
    map_gen.grid[1][0].state = Node.FIRE
    map_gen.grid[1][1].state = Node.BURNED
    return map_gen


def test_console_logger_output(capsys, create_simple_map):
    map_gen = create_simple_map
    logger = ConsoleMapLogger()
    logger.log(map_gen)

    captured = capsys.readouterr()
    output = captured.out.strip()

    assert "🟫" in output
    assert "🌳" in output
    assert "🔥" in output
    assert "⬛" in output


def test_html_logger_creates_file(tmp_path, create_simple_map):
    output_file = tmp_path / "test_map.html"
    map_gen = create_simple_map
    logger = HtmlMapLogger(output_file=str(output_file))
    logger.log(map_gen)

    assert output_file.exists()

    content = output_file.read_text(encoding="utf-8")
    assert "<html>" in content
    assert "Carte de la Forêt" in content
    assert "🟫" in content
    assert "🌳" in content
    assert "🔥" in content
    assert "⬛" in content
