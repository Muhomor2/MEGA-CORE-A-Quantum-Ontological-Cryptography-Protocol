# tests/test_df.py
# This test file verifies the core functionality of the MEGA-CORE protocol.

import pytest
from src.example_df import calculate_fractal_dimension

def test_df_low_complexity():
    """
    Verifies that the Df calculation returns a low value for simple,
    repetitive texts, indicating a highly ordered state.
    """
    text = "oror or oror o or or or oror or oror"
    expected_df = 1.226
    actual_df = calculate_fractal_dimension(text)
    assert actual_df == expected_df, f"Expected Df {expected_df}, but got {actual_df}"

def test_df_high_complexity():
    """
    Verifies that the Df calculation returns a high value for complex texts,
    indicating a high-energy, complex state.
    """
    text = "This protocol posits that information and consciousness are interconnected through measurable fractal patterns, moving beyond traditional data analysis."
    expected_df = 1.631
    actual_df = calculate_fractal_dimension(text)
    assert actual_df == expected_df, f"Expected Df {expected_df}, but got {actual_df}"

def test_empty_text():
    """
    Ensures that an empty text returns a Df of 0.0, as it contains no information.
    """
    text = ""
    expected_df = 0.0
    actual_df = calculate_fractal_dimension(text)
    assert actual_df == expected_df, f"Expected Df {expected_df}, but got {actual_df}"
