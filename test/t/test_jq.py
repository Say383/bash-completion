import pytest


class TestJq(object):

    @pytest.mark.complete("jq ")
    def test_1(self, completion):
        assert not completion.list

    @pytest.mark.complete("jq . ")
    def test_2(self, completion):
        assert completion.list

    @pytest.mark.complete("jq -",
                          skipif="! (jq --help 2>&1 || :) | "
                          "command grep -qF 'options include'")
    def test_3(self, completion):
        assert completion.list

    @pytest.mark.complete("jq --arg ")
    def test_4(self, completion):
        assert not completion.list

    @pytest.mark.complete("jq --slurpfile ")
    def test_5(self, completion):
        assert not completion.list

    @pytest.mark.complete("jq --slurpfile foo ")
    def test_6(self, completion):
        assert completion.list
