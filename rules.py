
from decorator import markdown
import utils


@markdown('github.com')
def github(url: str) -> str:
    return utils.markup('test', url)


@markdown('developer.mozilla.org', '/.+/docs/.+')
def mozilla(url: str) -> str:
    path = utils.get_path_segments(url)
    title = utils.titlize(path[-1])
    return utils.markup(title, url)
