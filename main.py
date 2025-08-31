# main.py
# The main script to run the MEGA-CORE-A-Quantum-Ontological-Cryptography-Protocol.

import os
from src.core import (
    calculate_semantic_fractal_dimension,
    calculate_ontological_resonance,
    OntologicalField,
    find_most_resonant_documents,
    load_texts_from_files
)

def create_sample_files():
    """Create sample text files for demonstration."""
    if not os.path.exists('data'):
        os.makedirs('data')
        print("Creating 'data/' directory...")

    # Sample texts for demonstration
    text1 = "The quick brown fox jumps over the lazy dog."
    text2 = "A lazy dog is sleeping under a large oak tree."
    
    with open('data/text1.txt', 'w') as f:
        f.write(text1)
        print("Creating sample file: data/text1.txt")
    
    with open('data/text2.txt', 'w') as f:
        f.write(text2)
        print("Creating sample file: data/text2.txt")

def main():
    """
    Main function to run the protocol.
    """
    create_sample_files()
    
    print("\n--- Text Analysis ---")
    
    # Load documents from the sample files
    documents = load_texts_from_files(['data/text1.txt', 'data/text2.txt'])
    
    if not documents:
        print("No documents found. Exiting.")
        return

    # Create an Ontological Field
    field = OntologicalField(documents)

    # Calculate and print the Semantic Fractal Dimension of the entire corpus
    corpus_df = field.get_corpus_df()
    print(f"Semantic Fractal Dimension (Df) of the corpus: {corpus_df}")

    # Find the most resonant documents
    resonant_pair = find_most_resonant_documents(field)
    if resonant_pair:
        doc1_index = resonant_pair['documents'][0]
        doc2_index = resonant_pair['documents'][1]
        resonance_value = resonant_pair['resonance']
        print(f"Most resonant documents are {doc1_index} and {doc2_index} with a resonance of {resonance_value}")
    else:
        print("Could not find a resonant pair.")

if __name__ == '__main__':
    main()
