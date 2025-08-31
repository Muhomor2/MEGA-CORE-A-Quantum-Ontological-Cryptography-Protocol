# main.py
# The main execution file for the MEGA-CORE protocol.

from src.core import load_texts_from_files, OntologicalField

if __name__ == "__main__":
    # Define the file paths for your data
    # Be sure to create a 'data/' folder and add your text files there.
    file_paths = [
        "data/sonnet18.txt", 
        "data/frankenstein.txt" 
    ]

    # Load the texts from the specified files
    documents = load_texts_from_files(file_paths)

    if not documents:
        print("Error: No documents were loaded. Please check your file paths.")
    else:
        # Create an ontological field from the documents
        field = OntologicalField(documents=documents)

        # Print a summary of the analysis
        print("--- Ontological Field Analysis ---")
        print(f"Total documents loaded: {len(field.documents)}")
        
        # Calculate and print the Df for the entire corpus
        corpus_df = field.get_corpus_df()
        print(f"Semantic Fractal Dimension (Df) of the corpus: {corpus_df}")

        # You can add more analysis here, for example, comparing individual documents
        if len(field.documents) >= 2:
            resonance = field.get_document_resonance(0, 1)
            print(f"Ontological Resonance between document 1 and 2: {resonance}")

    print("--- Analysis Complete ---")
