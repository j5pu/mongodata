import unittest

from .. import utils


class TestFind(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        utils.drop_database()

    @classmethod
    def tearDownClass(cls) -> None:
        utils.drop_database()

    # noinspection PyPep8Naming
    def test_one(self) -> None:
        client = utils.create_client()
        User = utils.create_class("user", client)

        user = User("John Howard", "john@gmail.com", 8771, "PH")
        inserted = user.insert()
        self.assertEqual(inserted, user.one())


if __name__ == "__main__":
    unittest.main()
