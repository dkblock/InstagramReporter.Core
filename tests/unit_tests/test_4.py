import unittest
from unittest.mock import patch

from helper_methods import patch_handler
from tasks.task_4 import main
from tests.mock_data import (
    mock_record,
    mock_record_with_tags,
    mock_records_with_same_geotags,
    mock_records_with_different_geotags,
    mock_users,
)


class TestFourthTask(unittest.TestCase):

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
        expected_value = [
            {
                '42415631327': {
                    'geotags': [],
                    'records': [],
                },
            },
        ]
        with patch('tasks.task_4.input', return_value=0):
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
        expected_value = [
            {
                '42415631327': {
                    'geotags': [],
                    'records': [
                        {
                            'date': '12-06-2018, 12:55',
                            'description': '',
                            'geotag': None,
                            'id': 1,
                        },
                    ],
                },
            },
        ]
        with patch('tasks.task_4.input', return_value=0):
            self.assertEqual(main(), expected_value)

    @patch_handler
    def test_record_with_geotag(
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
        get_last_feed.return_value = mock_record_with_tags
        expected_value = [
            {
                '42415631327': {
                    'geotags': ['Yaroslavl'],
                    'records': [
                        {
                            'date': '12-06-2018, 12:55',
                            'description': 'I like #sport and #travel',
                            'geotag': 'Yaroslavl',
                            'id': 1,
                        },
                    ],
                },
            },
        ]
        with patch('tasks.task_4.input', return_value=0):
            self.assertEqual(main(), expected_value)

    @patch_handler
    def test_two_same_geotags(
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
        get_last_feed.return_value = mock_records_with_same_geotags
        expected_value = [
            {
                '42415631327': {
                    'geotags': ['Yaroslavl'],
                    'records': [
                        {
                            'date': '12-06-2018, 12:55',
                            'description': '1',
                            'geotag': 'Yaroslavl',
                            'id': 1,
                        },
                        {
                            'date': '12-06-2018, 12:55',
                            'description': '2',
                            'geotag': 'Yaroslavl',
                            'id': 2,
                        },
                    ],
                },
            },
        ]
        with patch('tasks.task_4.input', return_value=2):
            self.assertEqual(main(), expected_value)

    @patch_handler
    def test_two_different_geotags(
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
        get_last_feed.return_value = mock_records_with_different_geotags
        with patch('tasks.task_4.input', return_value=0):
            geotags = ['Moscow', 'Yaroslavl']
            returned_value = main()
            if returned_value[0]['42415631327']['geotags'] != geotags:
                geotags = ['Yaroslavl', 'Moscow']
            expected_value = [
                {
                    '42415631327': {
                        'geotags': geotags,
                        'records': [
                            {
                                'date': '12-06-2018, 12:55',
                                'description': '1',
                                'geotag': 'Yaroslavl',
                                'id': 1,
                            },
                            {
                                'date': '12-06-2018, 12:55',
                                'description': '2',
                                'geotag': 'Moscow',
                                'id': 2,
                            },
                        ],
                    },
                },
            ]
            self.assertEqual(returned_value, expected_value)
