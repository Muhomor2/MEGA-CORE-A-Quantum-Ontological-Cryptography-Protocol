<?php
// calculate_df.php

header('Content-Type: application/json');

function calculateFractalDimension(string $text): float {
    if (empty($text)) {
        return 0.0;
    }

    // 1. Clean and normalize the text
    $normalized_text = strtolower(str_replace(['.', ','], '', $text));
    $words = explode(' ', $normalized_text);
    
    // 2. Count word frequencies
    $word_counts = array_count_values($words);
    $total_words = count($words);
    
    // 3. Calculate unique words (M) and total words (N)
    $M = count($word_counts);
    $N = $total_words;
    
    // 4. Calculate Df using a logarithmic relationship
    if ($M <= 1) {
        return 1.0;
    }

    $df = log($N) / log($M);
    
    return round($df, 3);
}

// Example of a complex, high-Df text (for demonstration)
$text_to_analyze = "This protocol posits that information and consciousness are interconnected through measurable fractal patterns, moving beyond traditional data analysis.";

$df_value = calculateFractalDimension($text_to_analyze);

// Prepare the output as JSON for client-side usage
$response = [
    'status' => 'success',
    'input_text' => $text_to_analyze,
    'semantic_fractal_dimension' => $df_value,
    'description' => 'Calculated Df for the provided text. This value can be used for client-side visualization.'
];

echo json_encode($response, JSON_PRETTY_PRINT);

?>
