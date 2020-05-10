from testoot.base import FileType


def test_file_type():
    assert FileType(mime='application/json').get_file_extension() == '.json'
    assert (FileType(mime='application/json', override_file_ext='.txt')
            .get_file_extension() == '.txt')
