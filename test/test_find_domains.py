from find_domains import (
    find_domains, RE_DOMAIN, is_tld, iter_domains
)


def test_re_domain():
    test_domains = [
        'Www.weloVeAlLanimals.cOM.',
        'example.com',
        'foo-bar.com',
        'foo.рф',
        'привет.рф',
        'foo#bar.рф', # invalid
        'foo.*.bar.рф', # invalid
        '*.foo.com', # invalid
    ]
    valid_domains = [
        'Www.weloVeAlLanimals.cOM.',
        'example.com',
        'foo-bar.com',
        'foo.рф',
        'привет.рф',
    ]

    res = set()
    for domain in test_domains:
        match = RE_DOMAIN.match(domain)
        if match:
            print(domain, '-->', match)
            res.add(domain)
    assert res == set(valid_domains)


def test_find_domains1():
    doms = find_domains(
        'LINE: 1597269193||foo||101.102.103.104||101.102.103.104||IN||'
        'Foo16-B0Ro-D-BAZ.DoMaIN.CoM.pArT.Net.'
        '||CNAME||e73737.foo9.someserver.Net.||9999||2'
    )
    assert doms == set([
        'foo16-b0ro-d-baz.domain.com.part.net',
        'e73737.foo9.someserver.net',
    ])


def test_find_domains2():
    doms = find_domains('''
        Www.weloVeAlLanimals.cOM.
        example.com
        foo-bar.com
        foo.рф
        привет.рф
        foo#bar.рф
        foo.*.bar.рф
        *.foo.com
    ]
    ''')
    assert doms == set([
        'www.weloveallanimals.com',
        'example.com',
        'foo-bar.com',
        'foo.рф',
        'привет.рф',
        'bar.рф',
        'foo.com',
    ])


def test_is_tld():
    assert is_tld('ru') is True
    assert is_tld('zzzzzz') is False
    assert is_tld('рф') is True
    assert is_tld('info') is True
    assert is_tld('impossibleshit') is False

#foo bar google.com. zzzzz ya.ru

def test_iter_domains():
    data = 'foo bar google.com. zzzzz ya.ru'
    items = list(iter_domains(data))
    assert items == [
        ('google.com', 8, 10),
        ('ya.ru', 26, 5),
    ]
