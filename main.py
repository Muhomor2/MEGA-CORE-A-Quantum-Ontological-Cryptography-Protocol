# main.py
# The main execution file for the MEGA-CORE protocol.

import os
from src.core import (
    load_texts_from_files, OntologicalField, 
    find_most_resonant_documents, 
    find_next_solar_eclipse, find_next_lunar_eclipse, 
    find_nearest_solstice_after, calculate_time_difference,
    ts
)
from datetime import datetime

def create_sample_data():
    """
    This function ensures the 'data' directory and sample text files exist.
    """
    if not os.path.exists('data'):
        print("Creating 'data/' directory...")
        os.makedirs('data')
    
    sample_texts = {
        "text1.txt": "The universe is a conscious fractal. The conscious mind is a fractal of the universe.",
        "text2.txt": "The future is in the past. The past is in the future. The now is eternal."
    }
    
    for filename, content in sample_texts.items():
        file_path = f"data/{filename}"
        if not os.path.exists(file_path):
            print(f"Creating sample file: {file_path}")
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(content)

if __name__ == "__main__":
    # Ensure sample data is available
    create_sample_data()

    # Define the file paths for your data
    file_paths = [
        "data/text1.txt",
        "data/text2.txt"
    ]

    # --- Text Analysis ---
    print("--- Text Analysis ---")
    documents = load_texts_from_files(file_paths)
    if documents:
        field = OntologicalField(documents=documents)
        corpus_df = field.get_corpus_df()
        print(f"Semantic Fractal Dimension (Df) of the corpus: {corpus_df}")
        
        most_resonant_pair = find_most_resonant_documents(field)
        if most_resonant_pair:
            doc1_index = most_resonant_pair["documents"][0]
            doc2_index = most_resonant_pair["documents"][1]
            resonance_value = most_resonant_pair["resonance"]
            print(f"Most resonant documents are {doc1_index} and {doc2_index} with a resonance of {resonance_value}")
    else:
        print("Error: No documents were loaded. Please check your file paths.")

    # --- Chronos Analysis ---
    print("\n--- Chronos Analysis ---")
    now = datetime.now()
    
    # 1. Calculate time to the next solar eclipse
    next_solar = find_next_solar_eclipse()
    time_to_solar = calculate_time_difference(ts.from_datetime(now), next_solar)
    print(f"Time to next Solar Eclipse: {time_to_solar[0]} days, {time_to_solar[1]} hours, {time_to_solar[2]} minutes.")

    # 2. Calculate time from next lunar eclipse to nearest solstice
    next_lunar = find_next_lunar_eclipse()
    next_solstice = find_nearest_solstice_after(next_lunar.utc_datetime())
    time_lunar_to_solstice = calculate_time_difference(next_lunar, next_solstice)
    print(f"Time from next Lunar Eclipse to nearest Solstice: {time_lunar_to_solstice[0]} days, {time_lunar_to_solstice[1]} hours, {time_lunar_to_solstice[2]} minutes.")

    print("--- Analysis Complete ---")
