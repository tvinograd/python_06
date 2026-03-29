#!/usr/bin/env python3

# Method 1 - Full module import
def module_import():
    import alchemy.elements
    print("\nMethod 1 - Full module import:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")


# Method 2 - Specific function import
def function_import():
    from alchemy.elements import create_water
    print("\nMethod 2 - Specific function import:")
    print(f"create_water(): {create_water()}")


# Method 3 - Aliased import
def alias_import():
    from alchemy.potions import healing_potion as heal
    print("\nMethod 3 - Aliased import:")
    print(f"heal(): {heal()}")


# Method 4 - Multiple imports
def multiple_import():
    from alchemy.elements import create_earth, create_fire
    from alchemy.potions import strength_potion
    print("\nMethod 4 - Multiple imports:")
    print(f"create_earth(): {create_earth()}")
    print(f"create_fire(): {create_fire()}")
    print(f"strength_potion(): {strength_potion()}")


def ft_import_transmutations():
    print("\n=== Import Transmutation Mastery ===")
    module_import()
    function_import()
    alias_import()
    multiple_import()
    print("\nAll import transmutation methods mastered!")


if __name__ == "__main__":
    ft_import_transmutations()
