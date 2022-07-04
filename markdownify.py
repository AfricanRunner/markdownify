
import fileinput

import decorator
import rules
import utils


def markdownify(url: str) -> str:
    if utils.is_markdown(url):
        return url
    handler = decorator.find_handler(url)
    return handler(url) if handler is not None else url


def main():
    lines = [str(line).strip() for line in fileinput.input()]
    lines = [markdownify(line) for line in lines]
    print('\n'.join(lines), end='')


if __name__ == '__main__':
    main()
