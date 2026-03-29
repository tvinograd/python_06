#!/usr/bin/env python3

def test_validation():
    from alchemy.grimoire.validator import validate_ingredients
    print("\nTesting ingredient validation:")
    print(f'validate_ingredients("fire air"): '
          f'{validate_ingredients("fire air")}')
    print(f'validate_ingredients("dragon scales"): '
          f'{validate_ingredients("dragon scales")}')


def test_spell_recording():
    from alchemy.grimoire.spellbook import record_spell
    print("\nTesting spell recording with validation:")
    print(f'record_spell("Fireball", "fire air"): '
          f'{record_spell("Fireball", "fire air")}')
    print(f'record_spell("Dark Magic", "shadow"): '
          f'{record_spell("Dark Magic", "shadow")}')


def test_late_import():
    from alchemy.grimoire import record_spell
    print("\nTesting late import technique:")
    print(f'record_spell("Lightning", "air"): '
          f'{record_spell("Lightning", "air")}')
    print("\nCircular dependency curse avoided using late imports!")


def ft_circular_curse():
    print("\n=== Circular Curse Breaking ===")
    test_validation()
    test_spell_recording()
    test_late_import()
    print("All spells processed safely!")


if __name__ == "__main__":
    ft_circular_curse()
