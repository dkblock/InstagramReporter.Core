import unittest
from unittest.mock import patch

from helper_methods import patch_handler
from tasks.task_1 import main
from tests.mock_data import api, mock_users


class TestFirstTask(unittest.TestCase):

    @patch_handler
    def test_empty_celebrities(
        self,
        get_followings,
        get_profile_info,
        get_last_feed,
        input,
    ):
        get_followings.return_value = [{'pk': 1}]
        get_profile_info.return_value = mock_users[0]
        self.assertEqual(main(api), {'42415631327': []})

    @patch_handler
    def test_is_celebrity(
        self,
        get_followings,
        get_profile_info,
        get_last_feed,
        input,
    ):
        get_followings.return_value = [{'pk': 1}]
        get_profile_info.return_value = mock_users[1]
        expected_value = {
            '42415631327': [{
                2: {
                    'name': 'AAA',
                    'followers': 100001,
                    'description': 'BBB',
                },
            }],
        }
        self.assertEqual(main(api), expected_value)

    @patch_handler
    def test_two_persons(
        self,
        get_followings,
        get_profile_info,
        get_last_feed,
        input,
    ):
        get_followings.return_value = [{'pk': 1}, {'pk': 1}]
        get_profile_info.return_value = mock_users[1]
        expected_value = {
            '42415631327': [
                {
                    2: {
                        'name': 'AAA',
                        'followers': 100001,
                        'description': 'BBB',
                    },
                },
                {
                    2: {
                        'name': 'AAA',
                        'followers': 100001,
                        'description': 'BBB',
                    },
                },
            ],
        }
        self.assertEqual(main(api), expected_value)

    @patch_handler
    def test_patch_get_celebrities(
        self,
        get_followings,
        get_profile_info,
        get_last_feed,
        input,
    ):
        with patch('tasks.task_1.get_celebrities', return_value='something'):
            self.assertEqual(main(api), {'42415631327': 'something'})

    @patch_handler
    def test_profile_info_without_user(
        self,
        get_followings,
        get_profile_info,
        get_last_feed,
        input,
    ):
        get_profile_info.return_value = 'something'
        self.assertEqual(main(api), {'42415631327': []})
