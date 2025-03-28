import pytest
from main import read_file

@pytest.fixture
def temp_input_file(tmp_path):
    file_path = tmp_path / "test_input.txt"
    content = """
    Ще не вмерла Україна, і слава, і воля,
    Ще нам, браття молодії, усміхнеться доля.
    Згинуть наші вороженьки, як роса на сонці,
    Запануєм і ми, браття, у своїй сторонці.
    """
    file_path.write_text(content, encoding='utf-8')
    return str(file_path)

def test_read_file(temp_input_file):
    content = read_file(temp_input_file)
    assert content.strip() == """
    Ще не вмерла Україна, і слава, і воля,
    Ще нам, браття молодії, усміхнеться доля.
    Згинуть наші вороженьки, як роса на сонці,
    Запануєм і ми, браття, у своїй сторонці.
    """.strip()
    assert isinstance(content, str)

def test_read_file_not_found():
    content = read_file("non_existent_file.txt")
    assert content == ""