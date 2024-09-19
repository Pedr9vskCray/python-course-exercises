import pytest
from names import strip_names

# atividade 1

nomes = [
    ('pedro josé dos prazeres lobão', ('pedro', 'lobão')),
    ('maria joaquina silveira santos', ('maria', 'santos')),
    ('ronaldo pedro do alecrim', ('ronaldo', 'alecrim')),
    ('joão felipe nogueira machado', ('joão', 'machado')),
    ('ademar ferreira dos anjos', ('ademar', 'anjos'))
]

@pytest.mark.parametrize('name,name_tuple', nomes)
def test_strip_nomes(name: str, name_tuple: tuple):
    assert strip_names(name) == name_tuple