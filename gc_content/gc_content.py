from io import TextIOWrapper
from .exceptions import BadFastaFile


def gc_content(file: TextIOWrapper) -> float:
    """
    Calculate the GC content from a FASTA file containing DNA sequences.
    
    Args:
        file: A FASTA format file containing DNA sequences. Each sequence should have
             a header line starting with '>' followed by one or more lines of sequence.
        
    Returns:
        float: The GC content as a fraction (0.0 to 1.0)
    """
    total_bases = 0
    gc_count = 0
    
    for line in file:
        # Skip header lines and empty lines
        if line.startswith('>') or not line.strip():
            continue
            
        sequence = line.strip().upper()
        total_bases += len(sequence)
        gc_count += sequence.count('G') + sequence.count('C')
    
    if total_bases == 0:
        raise BadFastaFile("No sequences found in the file")
        
    print(f"GC count: {gc_count}, Total bases: {total_bases}")
    return gc_count / total_bases
