import unittest
from unittest.mock import patch

from helper_methods import patch_handler
from tasks.task_3 import main, get_hashtags
from tests.mock_data import (
    api, mock_record,
    mock_record_with_tags,
    mock_record_with_text,
    mock_two_records,
    mock_users,
    users_ids,
)


class TestThirdTask(unittest.TestCase):

    @patch_handler
    def test_empty_records(
        self,
        get_followings,
        get_profile_info,
        get_last_feed,
        input,
    ):
        get_followings.return_value = [{'pk': 1}]
        get_profile_info.return_value = mock_users[0]
        expected_value = [
            {
                42415631327: {
                    'last_activity': 'does not exist',
                    'frequency': 0,
                    'records': [],
                },
            },
        ]
        with patch('tasks.task_3.input', return_value=0):
            self.assertEqual(main(api, users_ids), expected_value)

    @patch_handler
    def test_one_record(
        self,
        get_followings,
        get_profile_info,
        get_last_feed,
        input,
    ):
        get_followings.return_value = [{'pk': 1}]
        get_profile_info.return_value = mock_users[0]
        get_last_feed.return_value = mock_record
        expected_value = [
            {
                42415631327: {
                    'last_activity': '12-06-2018, 12:55',
                    'frequency': 1,
                    'records': [
                        {
                            'id': 1,
                            'date': '12-06-2018, 12:55',
                            'description': '',
                            'tags': [],
                        },
                    ],
                },
            },
        ]
        with patch('tasks.task_3.input', return_value=1):
            self.assertEqual(main(api, users_ids), expected_value)

    @patch_handler
    def test_two_records(
        self,
        get_followings,
        get_profile_info,
        get_last_feed,
        input,
    ):
        get_followings.return_value = [{'pk': 1}]
        get_profile_info.return_value = mock_users[0]
        get_last_feed.return_value = mock_two_records
        expected_value = [
            {
                42415631327: {
                    'last_activity': '12-06-2018, 12:55',
                    'frequency': 2,
                    'records': [
                        {
                            'id': 1,
                            'date': '12-06-2018, 12:55',
                            'description': '',
                            'tags': [],
                        },
                        {
                            'id': 2,
                            'date': '12-06-2018, 12:55',
                            'description': '',
                            'tags': [],
                        },
                    ],
                },
            },
        ]
        with patch('tasks.task_3.input', return_value=2):
            self.assertEqual(main(api, users_ids), expected_value)

    @patch_handler
    def test_record_description(
        self,
        get_followings,
        get_profile_info,
        get_last_feed,
        input,
    ):
        get_followings.return_value = [{'pk': 1}]
        get_profile_info.return_value = mock_users[0]
        get_last_feed.return_value = mock_record_with_text
        expected_value = [
            {
                42415631327: {
                    'last_activity': '12-06-2018, 12:55',
                    'frequency': 1,
                    'records': [
                        {
                            'id': 1,
                            'date': '12-06-2018, 12:55',
                            'description': '123',
                            'tags': [],
                        },
                    ],
                },
            },
        ]
        with patch('tasks.task_3.input', return_value=1):
            self.assertEqual(main(api, users_ids), expected_value)

    @patch_handler
    def test_record_tags(
        self,
        get_followings,
        get_profile_info,
        get_last_feed,
        input,
    ):
        get_followings.return_value = [{'pk': 1}]
        get_profile_info.return_value = mock_users[0]
        get_last_feed.return_value = mock_record_with_tags
        expected_value = [
            {
                42415631327: {
                    'last_activity': '12-06-2018, 12:55',
                    'frequency': 1,
                    'records': [
                        {
                            'id': 1,
                            'date': '12-06-2018, 12:55',
                            'description': 'I like #sport and #travel',
                            'tags': ['sport', 'travel'],
                        },
                    ],
                },
            },
        ]
        with patch('tasks.task_3.input', return_value=1):
            self.assertEqual(main(api, users_ids), expected_value)

    def test_get_hashtags(self):
        test_description = '#tag1#tag2'
        returned_value = get_hashtags(test_description)
        excepted_value = ['tag1', 'tag2']
        self.assertEqual(returned_value, excepted_value)
