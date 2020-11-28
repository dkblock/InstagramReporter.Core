import unittest
from unittest.mock import patch

from helper_methods import patch_handler
from tasks.task_5 import main
from tests.mock_data import (
    mock_record,
    mock_record_without_likes,
    mock_three_records,
    mock_two_records,
    mock_users,
)


class TestFifth(unittest.TestCase):

    @patch_handler
    def test_empty_records(
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
        get_profile_info.return_value = mock_users[0]
        with patch('tasks.task_5.input', return_value=0):
            expected_value = [
                {
                    42415631327: {
                        'max': 'does not exist',
                        'middle': 'does not exist',
                        'min': 'does not exist',
                        'records': [],
                    },
                },
            ]
            self.assertEqual(main(), expected_value)

    @patch_handler
    def test_one_record(
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
        get_profile_info.return_value = mock_users[0]
        get_last_feed.return_value = mock_record
        with patch('tasks.task_5.input', return_value=0):
            expected_value = [
                {
                    42415631327: {
                        'max': 99,
                        'min': 99,
                        'middle': 99.0,
                        'records': [
                            {
                                'id': 1,
                                'date': '12-06-2018, 12:55',
                                'description': '',
                                'count': 99,
                            },
                        ],
                    },
                },
            ]
            self.assertEqual(main(), expected_value)

    @patch_handler
    def test_two_records(
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
        get_profile_info.return_value = mock_users[0]
        get_last_feed.return_value = mock_two_records
        with patch('tasks.task_5.input', return_value=0):
            expected_value = [
                {
                    42415631327: {
                        'max': 101,
                        'min': 99,
                        'middle': 100.0,
                        'records': [
                            {
                                'id': 1,
                                'date': '12-06-2018, 12:55',
                                'description': '',
                                'count': 99,
                            },
                            {
                                'id': 2,
                                'date': '12-06-2018, 12:55',
                                'description': '',
                                'count': 101,
                            },
                        ],
                    },
                },
            ]
            self.assertEqual(main(), expected_value)

    @patch_handler
    def test_bad_middle(
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
        get_profile_info.return_value = mock_users[0]
        get_last_feed.return_value = mock_three_records
        with patch('tasks.task_5.input', return_value=0):
            expected_value = [
                {
                    42415631327: {
                        'max': 4,
                        'min': 2,
                        'middle': 3.33,
                        'records': [
                            {
                                'id': 1,
                                'date': '12-06-2018, 12:55',
                                'description': '',
                                'count': 2,
                            },
                            {
                                'id': 2,
                                'date': '12-06-2018, 12:55',
                                'description': '',
                                'count': 4,
                            },
                            {
                                'id': 3,
                                'date': '12-06-2018, 12:55',
                                'description': '',
                                'count': 4,
                            },
                        ],
                    },
                },
            ]
            self.assertEqual(main(), expected_value)

    @patch_handler
    def test_record_without_likes(
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
        get_profile_info.return_value = mock_users[0]
        get_last_feed.return_value = mock_record_without_likes
        with patch('tasks.task_5.input', return_value=0):
            expected_value = [
                {
                    42415631327: {
                        'max': 0,
                        'min': 0,
                        'middle': 0.0,
                        'records': [
                            {
                                'id': 1,
                                'date': '12-06-2018, 12:55',
                                'description': '',
                                'count': 0,
                            },
                        ],
                    },
                },
            ]
            self.assertEqual(main(), expected_value)
