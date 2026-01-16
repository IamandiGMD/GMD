"""
Motor de distribuție liniară
Calculează poziții egale pentru bare verticale / orizontale
"""

def distribute_linear(
    total_length: float,
    count: int,
    element_size: float
) -> list[float]:
    """
    Returnează poziții relative (offset) pentru elemente,
    distribuite egal pe o lungime dată.

    total_length  = spațiul disponibil
    count         = număr de elemente
    element_size  = lățimea / înălțimea elementului

    Return:
        listă de offset-uri (float)
    """

    if count <= 0:
        return []

    if count == 1:
        return [(total_length - element_size) / 2.0]

    free_space = total_length - count * element_size
    if free_space < 0:
        raise ValueError(
            f"Nu există spațiu suficient: "
            f"length={total_length}, "
            f"count={count}, "
            f"element={element_size}"
        )

    gap = free_space / (count - 1)

    positions = []
    pos = 0.0
    for _ in range(count):
        positions.append(pos)
        pos += element_size + gap

    return positions
