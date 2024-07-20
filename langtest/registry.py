import functools
from collections import defaultdict


class Registry:
    """Registry class to store test classes."""

    registry = defaultdict(lambda: list)

    @classmethod
    def test_info(cls, domain, category, test_type, description, langtest_version):
        """Decorator to register test classes."""

        def decorator(test_cls):
            @functools.wraps(test_cls)
            def wrapper(*args, **kwargs):
                cls.registry["test_types"] = {
                    "domain": domain,
                    "category": category,
                    "test_type": test_type,
                    "description": description,
                    "langtest_version": langtest_version,
                }
                return test_cls(*args, **kwargs)

            return wrapper

        return decorator

    @classmethod
    def category_info(cls, title, name, description):
        """Decorator to register category info."""

        def decorator(test_class):
            @functools.wraps(test_class)
            def wrapper(*args, **kwargs):
                cls.registry["test_categories"] = {
                    "title": title,
                    "name": name,
                    "description": description,
                    "class": test_class.__qualname__,
                }
                return test_class(*args, **kwargs)

            return wrapper

        return decorator
