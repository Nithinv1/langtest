# This module is used to register the test classes in the registry
# decorator. The registry decorator is used to register the test classes

# example of a registry decorator
# @registry.test_info("domain", "category", "test_type", "description", "langtest_version")
#    "title": "Uppercase",
#    "test_type": "uppercase",
#    "category": "robustness",
#    "description": "Uppercase all characters in the input.",
#    "input": "The quick brown fox jumps over the lazy dog.",
#    "test_case": "THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.",
#    "arguments": {
#        "prob": 1.0
#    }

import functools

class Registry:
    """Registry class to store test classes."""

    registry = {}

    @classmethod
    def test_info(cls, func, domain, category, test_type, description, langtest_version):
        """Decorator to register test classes."""
        @functools.wraps(func)
        def decorator(test_cls):
            cls.registry[test_cls.__name__] = {
                "domain": domain,
                "category": category,
                "test_type": test_type,
                "description": description,
                "langtest_version": langtest_version,
            }
            return test_cls
        return decorator
