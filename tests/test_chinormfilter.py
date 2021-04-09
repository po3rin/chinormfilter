from chinormfilter import __version__
from chinormfilter.cli import Filter


def test_version():
    assert __version__ == '0.1.0'


def test_kuro2sudachi_cli(capsys):
    f = Filter(dict_type="full")
    assert f.duplicated("林檎,りんご") is True
    assert f.duplicated("レナリドミド, レナリドマイド") is False
    assert f.duplicated("エダマメ,枝豆") is True
    assert f.duplicated("えだまめ,枝豆") is True
    assert f.duplicated("飲む,呑む") is True
    assert f.duplicated("エダマメ,枝豆") is True
    assert f.duplicated("tlc => tlc,全肺気量") is False
    assert f.duplicated("リンたんぱく質,リン蛋白質,リンタンパク質") is True
    assert f.duplicated("グルタチオン => グルタチオン,タチオン,ランデールチオン") is False
