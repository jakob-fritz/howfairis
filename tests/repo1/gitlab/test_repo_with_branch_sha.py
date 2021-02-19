from howfairis import Platform
from howfairis import Repo
from tests.contracts.repo import Contract


def get_repo():
    return Repo("https://gitlab.com/owner1/repo1", branch="b3f90ec9c2b1be604f482c2d9e46a9aeca3ee45a")


class TestRepoWithBranchSHA(Contract):

    def test_api(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.api == "https://gitlab.com/api/v4/projects/owner1%2Frepo1"

    def test_branch(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.branch == "b3f90ec9c2b1be604f482c2d9e46a9aeca3ee45a"

    def test_default_branch(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.default_branch is None

    def test_owner(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.owner == "owner1"

    def test_path(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.path == ""

    def test_platform(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.platform == Platform.GITLAB

    def test_raw_url_format_string(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.raw_url_format_string == "https://gitlab.com/owner1/repo1/-/raw/" \
                                                 "b3f90ec9c2b1be604f482c2d9e46a9aeca3ee45a/{0}"

    def test_repo(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.repo == "repo1"

    def test_url(self, mocker):
        with mocker:
            repo = get_repo()
            assert repo.url == "https://gitlab.com/owner1/repo1"
