import functools
from collections import defaultdict


class Registry:
    """Registry class to store test classes."""

    registry = defaultdict(list)

    def __new__(cls):
        """Singleton instance of the Registry class."""
        if not hasattr(cls, "instance"):
            cls.instance = super(Registry, cls).__new__(cls)
        return cls.instance

    @classmethod
    def test_info(cls, domain, category, test_type, description, langtest_version):
        """Decorator to register test classes."""

        def decorator(test_cls):
            Registry.registry["test_types"].append(
                {
                    "domain": domain,
                    "category": category,
                    "test_type": test_type,
                    "description": description,
                    "langtest_version": langtest_version,
                }
            )

            return test_cls

        return decorator

    @classmethod
    def category_info(cls, title, name, description):
        """Decorator to register category info."""

        def decorator(test_class):
            Registry.registry["categories"].append(
                {
                    "title": title,
                    "name": name,
                    "description": description,
                    "class": f"{test_class.__module__}.{test_class.__qualname__}",
                }
            )

            return test_class

        return decorator
