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
    for domain, _, _ in iterate_domains(data):
        ret.add(domain)
    return ret


def iterate_domains(data):
    for match in RE_DOMAIN.finditer(data):
        # Here:
        # match.group(0) - matched domain name
        # match.group(1) - top level domain name segment
        if '_' not in match.group(0):
            if is_tld(match.group(1)):
                dom = match.group(0).rstrip('.').lower()
                yield (dom, match.start(0), len(dom))
