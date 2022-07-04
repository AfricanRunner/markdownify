import re

# To-do: Create better regex patters or use an external
# library. These regex patterns only work for simple
# urls without exotic characters.


def get_domain(url: str) -> str:
    match = re.search('([A-Za-z0-9-]+\\.)+[A-Za-z]+', url)
    return match[0] if match else ''


def get_path(url: str) -> str:
    match = re.search('(/[A-Za-z0-9-_\\.]+)+/{0,1}', url)
    return match[0] if match else '/'


def get_path_segments(url: str) -> list[str]:
    return get_path(url).split('/')


def get_anchor(url: str) -> str:
    match = re.search('(?<=#)[A-Za-z0-9-_\\.]+', url)
    return match[0] if match else ''


def build_url(domain: str, paths: list[str]) -> str:
    return f'https://{domain}/{"/".join(paths)}'


def titlize(text: str) -> str:
    text = re.sub('([a-z])([A-Z])', '\\1 \\2', text)
    text = re.sub('(\\w)[-_]+(\\w)', '\\1 \\2', text)
    return ' '.join([word.capitalize() for word in text.split(' ')])


def markup(title: str, url: str):
    return f'[{title}]({url})'


def is_markdown(url: str) -> bool:
    return re.match('^\\[[A-Za-z0-9-_\\.]+\\]\\(.+\\)$', url) is not None
