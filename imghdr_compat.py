import sys
import filetype

def what(filepath):
    """Replace imghdr.what() using filetype"""
    kind = filetype.guess(filepath)
    return kind.extension if kind else None

def test(filepath, test_fn=None):
    """Replace imghdr.test()"""
    extension = what(filepath)
    if not test_fn:
        return extension
    return test_fn.lower() == extension if extension else False

# Override the imghdr module in sys.modules
sys.modules['imghdr'] = sys.modules[__name__]
