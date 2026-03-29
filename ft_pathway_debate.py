#!/usr/bin/env python3

# Absolute imports (full path)
def absolute_import():
    from alchemy.transmutation.basic import lead_to_gold, stone_to_gem
    print("\nTesting Absolute Imports (from basic.py):")
    print(f"lead_to_gold(): {lead_to_gold()}")
    print(f"stone_to_gem(): {stone_to_gem()}")


# Relative imports (dots)
def relative_import():
    from alchemy.transmutation.advanced import (
        philosophers_stone,
        elixir_of_life
    )
    print("\nTesting Relative Imports (from advanced.py):")
    print(f"philosophers_stone(): {philosophers_stone()}")
    print(f"elixir_of_life(): {elixir_of_life()}")


# Package access
def package_access():
    import alchemy.transmutation
    print("\nTesting Package Access (transmutation/__init__.py):")
    print(f"alchemy.transmutation.lead_to_gold(): "
          f"{alchemy.transmutation.lead_to_gold()}")
    print(f"alchemy.transmutation.philosophers_stone(): "
          f"{alchemy.transmutation.philosophers_stone()}")


def ft_pathway_debate():
    print("\n=== Pathway Debate Mastery ===")
    absolute_import()
    relative_import()
    package_access()
    print("\nBoth pathways work! Absolute: clear, Relative: concise")


if __name__ == "__main__":
    ft_pathway_debate()
