import pandas as pd

def analyze_dna_patterns(samples: pd.DataFrame) -> pd.DataFrame:
    samples['has_start'] = samples['dna_sequence'].str.startswith('ATG').astype(int)
    samples['has_stop'] = samples['dna_sequence'].str.endswith(('TAA', 'TAG', 'TGA')).astype(int)
    samples['has_atat'] = samples['dna_sequence'].str.contains('ATAT', na=False).astype(int)
    samples['has_ggg'] = samples['dna_sequence'].str.contains('G{3,}', na=False).astype(int)
    
    result = samples[['sample_id', 'dna_sequence', 'species', 'has_start', 'has_stop', 'has_atat', 'has_ggg']]
    
    return result.sort_values('sample_id')