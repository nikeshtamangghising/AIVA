import filetype

def what(filepath):
    """Compatibility shim for imghdr.what() using filetype"""
    kind = filetype.guess(filepath)
    return kind.extension if kind else None

def test(filepath, test_fn=None):
    """Compatibility shim for imghdr.test()"""
    extension = what(filepath)
    if not test_fn:
        return extension
    return test_fn.lower() == extension if extension else False
