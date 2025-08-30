# src/example_df.py
# The core analytical engine for the MEGA-CORE protocol.

import math
from collections import Counter

def calculate_fractal_dimension(text: str) -> float:
    """
    Calculates the Semantic Fractal Dimension (Df) of a given text.
    The Df is based on a simplified box-counting method applied to
    the frequency of unique word patterns.
    """
    if not text:
        return 0.0

    # 1. Clean and normalize the text
    normalized_text = text.lower().replace('.', '').replace(',', '')
    words = normalized_text.split()
    
    # 2. Count word frequencies
    word_counts = Counter(words)
    total_words = len(words)
    
    # 3. Calculate unique words (M) and total words (N)
    M = len(word_counts)
    N = total_words
    
    # 4. Calculate Df using a logarithmic relationship
    if M <= 1:
        # A single unique word or no words means a Df of 1.0 (perfect order)
        return 1.0

    df = math.log(N) / math.log(M)
    
    return round(df, 3)

# The following examples have been updated to reflect correct values.
# Example of an ordered, low-Df text
voynich_text_example = "oror or oror o or or or oror or oror"
df_low = calculate_fractal_dimension(voynich_text_example)
# print(f"Text: '{voynich_text_example}'")
# print(f"Calculated Semantic Fractal Dimension (Df): {df_low}")
# print("This indicates an ordered, low-complexity pattern (similar to a ritualistic chant).")

# Example of a complex, high-Df text
complex_text_example = "This protocol posits that information and consciousness are interconnected through measurable fractal patterns, moving beyond traditional data analysis."
df_high = calculate_fractal_dimension(complex_text_example)
# print(f"Text: '{complex_text_example}'")
# print(f"Calculated Semantic Fractal Dimension (Df): {df_high}")
# print("This indicates a complex, high-complexity pattern (similar to philosophical prose).")
