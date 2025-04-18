from io import StringIO
from gc_content.gc_content import gc_content
from gc_content.exceptions import BadFastaInput
from pytest import raises

def test_gc_content_correct_ratio():
    # Create a FASTA file with exactly:
    # 1 G, 2 C's, 3 A's, and 4 T's (10 bases total)
    # GC content should be (1 + 2)/(1 + 2 + 3 + 4) = 3/10 = 0.3
    fasta_content = ">test_sequence\nGCCAAAT\nTTT\n"
    fake_file = StringIO(fasta_content)
    
    result = gc_content(fake_file)
    expected = 0.3  # 3 GC bases out of 10 total bases
    assert abs(result - expected) < 1e-10  # pytest's way of comparing floats

def test_gc_content_no_sequences():
    fasta_content = ""
    fake_file = StringIO(fasta_content)

    with raises(BadFastaInput):
        gc_content(fake_file)

def test_gc_content_of_file():
    """Vary the test by starting with a file to open"""
    with open("tests/data/test.fasta", "r") as fasta_file:
        result = gc_content(fasta_file)
        expected = 0.3  # 3 GC bases out of 10 total bases
        assert abs(result - expected) < 1e-10

def test_gc_content_of_string():
    """Vary the test by starting with a string"""
    fasta_str = ">test_sequence\nGCCAAAT\nTTT\n"
    result = gc_content(fasta_str)
    expected = 0.3  # 3 GC bases out of 10 total bases
    assert abs(result - expected) < 1e-10

def test_gc_content_of_int_fails():
    with raises(BadFastaInput) as exc_info:
        gc_content(17)
    assert str(exc_info.value) == "Unsupported FASTA input type: <class 'int'>"
