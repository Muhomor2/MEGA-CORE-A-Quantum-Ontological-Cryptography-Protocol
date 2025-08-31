# src/core.py
# The core analytical engine for the MEGA-CORE protocol.

import math
from collections import Counter
import networkx as nx

def calculate_semantic_fractal_dimension(text: str) -> float:
    """
    Calculates the Semantic Fractal Dimension (Df) of a given text,
    based on word frequency and network analysis.
    """
    if not text:
        return 0.0

    # 1. Normalize and tokenize the text
    normalized_text = text.lower().replace('.', '').replace(',', '')
    words = normalized_text.split()
    
    # 2. Build a simple word network (graph)
    G = nx.Graph()
    for i in range(len(words) - 1):
        G.add_edge(words[i], words[i+1])

    # 3. Calculate network metrics
    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()

    # 4. Calculate Df based on network properties
    # Df = log(number of nodes) / log(number of edges) - a simplified box-counting variant
    if num_edges <= 1:
        return 1.0

    df = math.log(num_nodes) / math.log(num_edges)
    
    return round(df, 3)

def calculate_ontological_resonance(text1: str, text2: str) -> float:
    """
    Calculates the ontological resonance between two texts.
    This is a simplified metric based on the Jaccard index of their words.
    """
    words1 = set(text1.lower().split())
    words2 = set(text2.lower().split())

    intersection_size = len(words1.intersection(words2))
    union_size = len(words1.union(words2))

    if union_size == 0:
        return 0.0

    jaccard_index = intersection_size / union_size
    
    # Resonance is amplified by the presence of a connection
    return round(jaccard_index, 3)

if __name__ == '__main__':
    # Examples of usage
    text1 = "The universe is a conscious fractal."
    text2 = "Consciousness is a fractal of the universe."
    
    # Calculate Df for each text
    df1 = calculate_semantic_fractal_dimension(text1)
    df2 = calculate_semantic_fractal_dimension(text2)
    print(f"Df for Text 1: {df1}")
    print(f"Df for Text 2: {df2}")
    
    # Calculate resonance between texts
    resonance = calculate_ontological_resonance(text1, text2)
    print(f"Ontological Resonance: {resonance}")
