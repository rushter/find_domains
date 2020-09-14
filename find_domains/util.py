import re
from tldextract import TLDExtract

extractor = TLDExtract()
CACHE = {
    'tlds': None,
}

# I use \w instead of \p{Letter} and \p{Number}
# because python rex engine does not suppoort unicode categories
# As result found domains might contain "_" character
# Additition check must be done to filter out items with "_"
RE_DOMAIN = re.compile(
    r' \b'
    r' \w \.? (?: [-\w]{1,63} \. ){0,10}'
    r' (?<=\.)( \w [-\w]{0,63} \w )'
    r' \.?'
    r' \b'
    , re.X
)


def is_tld(name):
    if not CACHE['tlds']:
        CACHE['tlds'] = extractor.tlds
    return name.lower() in CACHE['tlds']


def find_domains(data):
    ret = set()
    for match in RE_DOMAIN.finditer(data):
        dom = match.group(0).rstrip('.').lower()
        if '_' not in dom:
            tld = dom.rsplit('.', 1)[1]
            if is_tld(tld):
                ret.add(dom)
    return ret
