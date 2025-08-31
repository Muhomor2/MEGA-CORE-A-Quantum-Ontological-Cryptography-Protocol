# src/core.py
# The core analytical engine for the MEGA-CORE protocol.

import math
from collections import Counter
import networkx as nx
from skyfield.api import load, T
from skyfield.almanac import find_solar_eclipses, find_lunar_eclipses, find_solstices
from datetime import datetime

def calculate_semantic_fractal_dimension(text: str) -> float:
    """
    Calculates the Semantic Fractal Dimension (Df) of a given text,
    based on word frequency and network analysis.
    """
    if not text:
        return 0.0

    normalized_text = text.lower().replace('.', '').replace(',', '')
    words = normalized_text.split()
    
    G = nx.Graph()
    for i in range(len(words) - 1):
        G.add_edge(words[i], words[i+1])

    num_nodes = G.number_of_nodes()
    num_edges = G.number_of_edges()

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
    
    return round(jaccard_index, 3)

class OntologicalField:
    """
    Represents a collection of texts as a single, coherent ontological field.
    """
    def __init__(self, documents: list[str]):
        self.documents = documents
        self.corpus = " ".join(documents)

    def get_corpus_df(self) -> float:
        """
        Returns the Df of the entire corpus.
        """
        return calculate_semantic_fractal_dimension(self.corpus)

    def get_document_resonance(self, doc_index1: int, doc_index2: int) -> float:
        """
        Returns the ontological resonance between two documents in the field.
        """
        text1 = self.documents[doc_index1]
        text2 = self.documents[doc_index2]
        return calculate_ontological_resonance(text1, text2)

def find_most_resonant_documents(field: OntologicalField) -> dict:
    """
    Finds the two most ontologically resonant documents in the field.
    """
    if len(field.documents) < 2:
        return {}

    max_resonance = -1
    resonant_pair = None

    for i in range(len(field.documents)):
        for j in range(i + 1, len(field.documents)):
            resonance = field.get_document_resonance(i, j)
            if resonance > max_resonance:
                max_resonance = resonance
                resonant_pair = (i, j)

    if resonant_pair:
        return {
            "documents": [resonant_pair[0], resonant_pair[1]],
            "resonance": max_resonance
        }
    return {}

def load_texts_from_files(file_paths: list[str]) -> list[str]:
    """
    Loads text content from a list of files.
    """
    texts = []
    for path in file_paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                texts.append(f.read())
        except FileNotFoundError:
            print(f"Error: File not found at {path}")
    return texts

# --- New Chronos Functions ---
ts = load.timescale()
eph = load('de421.bsp')

def find_next_solar_eclipse() -> T:
    """
    Finds the next solar eclipse from the current date.
    """
    t0 = ts.now()
    t1 = ts.utc(t0.utc.year + 2, 1, 1)
    t, y, x = find_solar_eclipses(eph, t0, t1)
    return t[0]

def find_next_lunar_eclipse() -> T:
    """
    Finds the next lunar eclipse from the current date.
    """
    t0 = ts.now()
    t1 = ts.utc(t0.utc.year + 2, 1, 1)
    t, y, x = find_lunar_eclipses(eph, t0, t1)
    return t[0]

def find_nearest_solstice_after(date: datetime) -> T:
    """
    Finds the nearest solstice after a given date.
    """
    t0 = ts.from_datetime(date)
    t1 = ts.utc(t0.utc.year + 2, 1, 1)
    t, y, x = find_solstices(eph, t0, t1)
    return t[0]

def calculate_time_difference(t1: T, t2: T) -> tuple:
    """
    Calculates the time difference between two Skyfield Time objects.
    Returns a tuple of (days, hours, minutes).
    """
    delta = t2 - t1
    days = delta.days
    hours = delta.hours - (days * 24)
    minutes = delta.minutes - (days * 1440) - ((hours) * 60)
    
    return (int(days), int(hours), int(minutes))

if __name__ == '__main__':
    print("This is the core library, run main.py to see an example.")

    jaccard_index = intersection_size / union_size
    
    # Resonance is amplified by the presence of a connection
    return round(jaccard_index, 3)

# New functionality for handling multiple documents
class OntologicalField:
    """
    Represents a collection of texts as a single, coherent ontological field.
    """
    def __init__(self, documents: list[str]):
        self.documents = documents
        self.corpus = " ".join(documents)

    def get_corpus_df(self) -> float:
        """
        Returns the Df of the entire corpus.
        """
        return calculate_semantic_fractal_dimension(self.corpus)

    def get_document_resonance(self, doc_index1: int, doc_index2: int) -> float:
        """
        Returns the ontological resonance between two documents in the field.
        """
        text1 = self.documents[doc_index1]
        text2 = self.documents[doc_index2]
        return calculate_ontological_resonance(text1, text2)

# New function to read texts from files
def load_texts_from_files(file_paths: list[str]) -> list[str]:
    """
    Loads text content from a list of files.
    """
    texts = []
    for path in file_paths:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                texts.append(f.read())
        except FileNotFoundError:
            print(f"Error: File not found at {path}")
    return texts

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
