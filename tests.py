import pytest
from main import read_file, count_words, get_top_words, write_results

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

@pytest.fixture
def temp_output_file(tmp_path):
    return str(tmp_path / "test_output.txt")

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

@pytest.mark.parametrize("text, expected", [
    ("ще ще україна", {"ще": 2, "україна": 1}),
    ("браття, браття. браття!", {"браття": 3}),
    ("", {}),
    ("воля воля ВОЛЯ", {"воля": 3}),
])
def test_count_words(text, expected):
    result = count_words(text)
    assert result == expected

@pytest.mark.parametrize("word_freq, top_n, expected", [
    ({"ще": 2, "україна": 3, "доля": 1}, 2, [("україна", 3), ("ще", 2)]),
    ({"a": 1, "b": 2, "c": 3}, 1, [("c", 3)]),
    ({}, 5, []),
    ({"свобода": 5}, 10, [("свобода", 5)]),
])
def test_get_top_words(word_freq, top_n, expected):
    result = get_top_words(word_freq, top_n)
    assert result == expected

def test_write_results(temp_output_file):
    top_words = [("україна", 3), ("ще", 2)]
    write_results(top_words, temp_output_file)
    
    with open(temp_output_file, 'r', encoding='utf-8') as f:
        content = f.read().strip()
    assert content == "україна-3\nще-2"