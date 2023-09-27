def is_aa(seq: str) -> bool:
    """
    Check if a sequence contains only amino acids.

    Args:
        seq (str): The input sequфence to be checked.

    Returns:
        bool: True if the sequence contains only amino acids, False otherwise.
    """
    aa_list = ['V', 'I', 'L', 'E', 'Q', 'D', 'N', 'H', 'W', 'F', 'Y', 'R', 'K', 'S', 'T', 'M', 'A', 'G', 'P', 'C',
               'v', 'i', 'l', 'e', 'q', 'd', 'n', 'h', 'w', 'f', 'y', 'r', 'k', 's', 't', 'm', 'a', 'g', 'p', 'c']
    unique_chars = set(seq)
    amino_acids = set(aa_list)
    return unique_chars <= amino_acids
