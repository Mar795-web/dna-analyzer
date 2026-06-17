import pytest
from src.core.dna import *

def test_gc():
    assert calculate_gc("GGCC")==100.0

def test_complement():
    assert reverse_complement("ATGC")=="GCAT"

def test_rna():
    assert transcribe_rna("ATGC")=="AUGC"

def test_invalid():
    with pytest.raises(ValueError):
        validate_sequence("ATXB")

def test_empty():
    with pytest.raises(ValueError):
        validate_sequence("")
