from docdict.DocString2Json import DocString2Json


generated = dict(DocString2Json("""@json
    @name Slavik
    @second_name Nychkalo
    @tags slavik
    @tags nychkalo
"""))


def test_name():
    assert generated['name'] == 'Slavik'


def test_second_name():
    assert generated['second_name'] == 'Nychkalo'


def test_tags():
    assert generated['tags'] == ["slavik", "nychkalo"]
