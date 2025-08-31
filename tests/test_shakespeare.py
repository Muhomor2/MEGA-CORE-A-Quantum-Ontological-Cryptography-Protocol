# tests/test_shakespeare.py
# This test file performs an ontological analysis of Shakespeare's Sonnet 18.

import pytest
from src.core import calculate_semantic_fractal_dimension, OntologicalField

def test_shakespeare_df():
    """
    Verifies the semantic fractal dimension of Shakespeare's Sonnet 18.
    """
    sonnet_text = """Shall I compare thee to a summer’s day?
    Thou art more lovely and more temperate:
    Rough winds do shake the darling buds of May,
    And summer’s lease hath all too short a date:
    Sometime too hot the eye of heaven shines,
    And often is his gold complexion dimm'd;
    And every fair from fair sometime declines,
    By chance or nature’s changing course untrimm'd;
    But thy eternal summer shall not fade,
    Nor lose possession of that fair thou owest;
    Nor shall Death brag thou wander’st in his shade,
    When in eternal lines to time thou growest:
    So long as men can breathe or eyes can see,
    So long lives this, and this gives life to thee."""

    # The correct value based on our current algorithm.
    expected_df = 0.942
    
    actual_df = calculate_semantic_fractal_dimension(sonnet_text)
    assert actual_df == expected_df, f"Expected Df {expected_df}, but got {actual_df}"

def test_ontological_field_df():
    """
    Verifies the Df calculation for an entire ontological field (corpus).
    """
    text1 = "To be, or not to be, that is the question."
    text2 = "Romeo, Romeo! wherefore art thou Romeo?"
    text3 = "All the world's a stage, and all the men and women merely players."
    
    field = OntologicalField(documents=[text1, text2, text3])
    
    # The correct Df for the combined corpus.
    expected_df = 0.962
    
    actual_df = field.get_corpus_df()
    assert actual_df == expected_df, f"Expected corpus Df {expected_df}, but got {actual_df}"

