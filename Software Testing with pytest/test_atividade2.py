import pytest
from abbreviation import abbreviate_name

# atividade 2

nomes = [
    ('pedro josé dos prazeres lobão', ('P', 'J', 'D', 'P', 'L')),
    ('maria joaquina silveira santos', ('M', 'J', 'S', 'S')),
    ('ronaldo pedro do alecrim', ('R', 'P', 'D', 'A')),
    ('joão felipe nogueira machado', ('J', 'F', 'N', 'M')),
    ('ademar ferreira dos anjos', ('A', 'F', 'D', 'A'))
]

@pytest.mark.parametrize('name,abbreviated_name', nomes)
def test_abbreviate_name(name: str, abbreviated_name: tuple):
    assert abbreviate_name(name) == abbreviated_name