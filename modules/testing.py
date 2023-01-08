def test(element: str) -> int:
    if element not in ['enc', 'dec', 'com', 'decom']:
        raise ValueError

    return 0
