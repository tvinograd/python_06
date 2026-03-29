#!/usr/bin/env python3

# Direct module access
def direct_access():
    import alchemy.elements
    print("\nTesting direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water(): "
          f"{alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_earth(): "
          f"{alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")


# Package-level access
def package_access():
    import alchemy
    print("\nTesting package-level access (controlled by __init__.py):")
    print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    print(f"alchemy.create_water(): {alchemy.create_water()}")

    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except AttributeError:
        print("alchemy.create_earth(): AttributeError - not exposed")

    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError:
        print("alchemy.create_air(): AttributeError - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


def ft_sacred_scroll():
    print("\n=== Sacred Scroll Mastery ===")
    direct_access()
    package_access()


if __name__ == "__main__":
    ft_sacred_scroll()
