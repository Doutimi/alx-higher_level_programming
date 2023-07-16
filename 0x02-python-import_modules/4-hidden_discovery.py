if __name__ == "__main__":
    """Print all names defined by hidden_4 module."""
    import hidden_4

    dnames = dir(hidden_4)
    for name in dnames:
        if name[:2] != "__":
            print(name)
