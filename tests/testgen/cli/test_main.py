class TestInvalidModuleName:
    @classmethod
    def setup_class(cls):
        from testgen.cli.main import InvalidModuleName

        assert InvalidModuleName

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass


def test_print_version():
    from testgen.cli.main import print_version

    assert print_version
