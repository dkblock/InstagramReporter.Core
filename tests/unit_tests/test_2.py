import unittest
from unittest.mock import patch

from helper_methods import patch_handler
from tasks.task_2 import find_tags, get_blogs, main
from tests.mock_data import mock_users


class TestFirstTask(unittest.TestCase):

    def test_find_tags(self):
        returned_value = find_tags(
            'This is my blog about sport and traveling',
            ['travel', 'sport', 'cooking', 'кухня', 'спорт', 'фитнес'],
        )
        expected_value = ['travel', 'sport']
        self.assertEqual(returned_value, expected_value)

    def test_find_empty_tags(self):
        returned_value = find_tags(
            'This is my blog about sport and traveling',
            [],
        )
        self.assertEqual(returned_value, [])

    def test_find_wrong_tags(self):
        returned_value = find_tags(
            'This is my blog about sport and traveling',
            ['programming', 'science', 'cooking'],
        )
        self.assertEqual(returned_value, [])

    @patch_handler
    def test_get_empty_blogs(
        self,
        login,
        get_followings,
        get_profile_info,
        get_last_feed,
        input,
        getpass,
    ):
        login.return_value = True
        getpass.return_value = ''
        get_profile_info.return_value = mock_users[1]
        with patch('tasks.task_2.find_tags', return_value=[]):
            returned_value = get_blogs(login, [{'pk': 1}], ['travel', 'sport'])
            self.assertEqual(returned_value, [])

    @patch_handler
    def test_get_blogs(
        self,
        login,
        get_followings,
        get_profile_info,
        get_last_feed,
        input,
        getpass,
    ):
        login.return_value = True
        getpass.return_value = ''
        get_followings.return_value = [{'pk': 1}]
        get_profile_info.return_value = mock_users[2]

        expected_value = {
            42415631327: [
                {
                    1: {
                        'name': 'AAA',
                        'followers': 100000,
                        'description': 'only sport',
                        'tags': ['sport'],
                    },
                },
            ],
        }
        self.assertEqual(main(), expected_value)
