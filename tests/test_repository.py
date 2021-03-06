import os

import pytest

from . import DATA_ROOT, requirerepositoryformodule
from archeogit.models import Section
from archeogit.repository import Repository

requirerepositoryformodule('ffmpeg')
REPOSITORY_PATH = os.path.join(DATA_ROOT, 'ffmpeg')


def test_get_sections():
    repository = Repository(REPOSITORY_PATH)
    commit = repository.get('8ff432eb447ec0eca9954829aa58b611eafd835d')
    expected = {
        'tools/enum_options.c': [
            Section(
                header=[88, 89, 90],
                body={'-': [91, 92], '+': [91, 92, 93, 94]},
                footer=[93, 94, 95, 96, 97]
            ),
            Section(
                header=[93, 94, 95, 96, 97],
                body={'-': [98], '+': [100]},
                footer=[99, 100, 101, 102, 103]
            ),
            Section(
                header=[99, 100, 101, 102, 103],
                body={'-': [104], '+': [106]},
                footer=[105, 106, 107]
            )
        ]
    }
    actual = repository.get_sections(commit)
    assert actual == expected


def test_get_sections_newline_change():
    repository = Repository(REPOSITORY_PATH)
    commit = repository.get('3c7a2a0b92e670a1dc70be3198ece2646f25d495')
    expected = {
        'tests/ref/fate/vc1test_smm0005': [
            Section(
                header=[26, 27, 28], body={'-': [29], '+': [29]}, footer=[]
            )
        ]
    }
    actual = repository.get_sections(commit)
    assert actual == expected
