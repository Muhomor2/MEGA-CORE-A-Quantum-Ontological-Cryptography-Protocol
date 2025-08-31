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
    This function ensures the 'data' directory and a sample text file exist.
    """
    if not os.path.exists('data'):
        print("Creating 'data/' directory...")
        os.makedirs('data')
        
    sample_text = """To be, or not to be, that is the question:
    Whether 'tis nobler in the mind to suffer
    The slings and arrows of outrageous fortune,
    Or to take Arms against a Sea of troubles,
    And by opposing end them: to die, to sleep
    No more; and by a sleep, to say we end
    The heart-ache, and the thousand natural shocks
    That Flesh is heir to? 'Tis a consummation
    Devoutly to be wished. To die, to sleep,
    To sleep, perchance to Dream; aye, there's the rub,
    For in that sleep of death, what dreams may come,
    When we have shuffled off this mortal coil,
    Must give us pause: there's the respect
    That makes Calamity of so long life:
    For who would bear the Whips and Scorns of time,
    The Oppressor's wrong, the proud man's contumely,
    The pangs of despised love, the law’s delay,
    The insolence of office, and the spurns
    That patient merit of the unworthy takes,
    When he himself might his quietus make
    With a bare Bodkin? Who would Fardels bear,
    To grunt and sweat under a weary life,
    But that the dread of something after death,
    The undiscovered country, from whose bourn
    No traveller returns, puzzles the will,
    And makes us rather bear those ills we have,
    Than fly to others that we know not of?
    Thus conscience does make Cowards of us all,
    And thus the native hue of Resolution
    Is sicklied o'er, with the pale cast of Thought,
    And enterprises of great pith and moment,
    With this regard their Currents turn awry,
    And lose the name of Action. Soft you now,
    The fair Ophelia? Nymph, in thy Orisons
    Be all my sins remember'd."""
    
    file_path = "data/hamlet.txt"
    if not os.path.exists(file_path):
        print(f"Creating sample file: {file_path}")
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(sample_text)
            

if __name__ == "__main__":
    # Ensure sample data is available
    create_sample_data()

    # Define the file paths for your data
    file_paths = [
        "data/hamlet.txt"
    ]

    # --- Text Analysis ---
    print("--- Text Analysis ---")
    documents = load_texts_from_files(file_paths)
    if documents:
        field = OntologicalField(documents=documents)
        corpus_df = field.get_corpus_df()
        print(f"Semantic Fractal Dimension (Df) of the corpus: {corpus_df}")

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
