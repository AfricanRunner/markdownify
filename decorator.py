
from typing import Callable, Pattern, TypeVar
import re
import utils

markdown_handlers: dict[str, list[tuple[Pattern, Callable[[str], str]]]] = {}


def find_handler(url: str) -> Callable[[str], str] | None:
    domain = utils.get_domain(url)
    if handlers := markdown_handlers[domain]:
        path = utils.get_path(url)
        for pattern, handler in handlers:
            if pattern.search(path) is not None:
                return handler
    return None


K = TypeVar('K')
V = TypeVar('V')


def dict_append(dictionary: dict[K, list[V]], key: K, value: V):
    if key in dictionary:
        dictionary[key].append(value)
    else:
        dictionary[key] = [value]


def markdown(domain: str, path: str = '.*'):
    def decorator_markdown(func: Callable[[str], str]):
        dict_append(markdown_handlers, domain, (re.compile(path), func))
        return func
    return decorator_markdown
