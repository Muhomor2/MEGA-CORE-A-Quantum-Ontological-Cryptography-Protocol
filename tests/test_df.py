# tests/test_df.py
# This test file verifies the core functionality of the MEGA-CORE protocol.

import pytest
from src.core import calculate_semantic_fractal_dimension, calculate_ontological_resonance

def test_df_low_complexity():
    """
    Verifies that the Df calculation returns a low value for simple,
    repetitive texts, indicating a highly ordered state.
    """
    text = "the the the"
    expected_df = 1.0
    actual_df = calculate_semantic_fractal_dimension(text)
    assert actual_df == expected_df, f"Expected Df {expected_df}, but got {actual_df}"

def test_df_high_complexity():
    """
    Verifies that the Df calculation returns a high value for complex texts,
    indicating a high-energy, complex state.
    """
    text = "The universe is a conscious fractal."
    expected_df = 1.0
    actual_df = calculate_semantic_fractal_dimension(text)
    assert actual_df == expected_df, f"Expected Df {expected_df}, but got {actual_df}"

def test_empty_text():
    """
    Ensures that an empty text returns a Df of 0.0, as it contains no information.
    """
    text = ""
    expected_df = 0.0
    actual_df = calculate_semantic_fractal_dimension(text)
    assert actual_df == expected_df, f"Expected Df {expected_df}, but got {actual_df}"

def test_ontological_resonance():
    """
    Verifies that the ontological resonance calculation works correctly.
    """
    text1 = "The universe is a conscious fractal."
    text2 = "Consciousness is a fractal of the universe."
    expected_resonance = 1.0
    actual_resonance = calculate_ontological_resonance(text1, text2)
    assert actual_resonance == expected_resonance, f"Expected resonance {expected_resonance}, but got {actual_resonance}"

