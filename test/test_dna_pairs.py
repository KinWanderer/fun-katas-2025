from src.dna_pairs import dna_pairs

def test_to_return_dna_pairs_G_and_C_():
    # Arrange
    dna_string = ("G")

    # Act
    input = dna_string
    output = dna_pairs(input) # dna_pairs(["G"])

    # Assert
    expected_output = [["G", "C"]]
    assert output == expected_output
    
# Assemble