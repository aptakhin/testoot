Basics
===================================

Test generated files by filenames::

    from pathlib import Path

    def generate_file():
        filename = Path('test.txt')
        filename.write_test('abc')
        return filename

    def test_file(regress: RegressFixture):
        regress.test_filename(generate_file())
