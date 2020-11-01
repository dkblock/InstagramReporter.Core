import unittest
from unittest.mock import patch

from helper_methods import patch_handler
from tasks.task_2 import find_tags, get_blogs
from tests.mock_data import mock_users_test_1


class TestFirstTask(unittest.TestCase):

    @patch_handler
    def test_find_tags(
        self,
        login,
        get_followings,
        get_profile_info,
        get_last_feed,
        input,
        getpass
    ):
        login.return_value = True
        getpass.return_value = ''
        returned_value = find_tags(
            'This is my blog about sport and travel',
            ['travel', 'sport', 'cooking', 'кухня', 'спорт', 'фитнес']
        )
        expected_value = ['travel', 'sport']
        self.assertEqual(returned_value, expected_value)

    @patch_handler
    def test_get_blogs(
        self,
        login,
        get_followings,
        get_profile_info,
        get_last_feed,
        input,
        getpass
    ):
        login.return_value = True
        getpass.return_value = ''
        get_profile_info.return_value = mock_users_test_1[1]
        with patch('tasks.task_2.find_tags', return_value=[]):
            returned_value = get_blogs(login, [{'pk': 1}], ['travel', 'sport'])
            expected_value = []
            self.assertEqual(returned_value, expected_value)

    # @patch_handler
    # def test_two_persons(
    #     self,
    #     login,
    #     get_followings,
    #     get_profile_info,
    #     get_last_feed,
    #     input,
    #     getpass
    # ):
    #     login.return_value = True
    #     getpass.return_value = ''
    #     get_followings.return_value = [{'pk': 1}, {'pk': 1}]
    #     get_profile_info.return_value = mock_users_test_1[1]
    #     expected_value = {
    #             42415631327: [
    #                 {
    #                     2: {
    #                         'name': 'AAA',
    #                         'followers': 100001,
    #                         'description': 'BBB',
    #                     }
    #                 },
    #                 {
    #                     2: {
    #                         'name': 'AAA',
    #                         'followers': 100001,
    #                         'description': 'BBB',
    #                     },
    #                 },
    #             ],
    #         }
    #     self.assertEqual(main(), expected_value)

    # @patch_handler
    # def test_patch_get_celebrities(
    #     self,
    #     login,
    #     get_followings,
    #     get_profile_info,
    #     get_last_feed,
    #     input,
    #     getpass
    # ):
    #     login.return_value = True
    #     getpass.return_value = ''
    #     with patch('tasks.task_1.get_celebrities', return_value='something'):
    #         self.assertEqual(main(), {42415631327: 'something'})

    # @patch_handler
    # def test_profile_info_without_user(
    #     self,
    #     login,
    #     get_followings,
    #     get_profile_info,
    #     get_last_feed,
    #     input,
    #     getpass
    # ):
    #     login.return_value = True
    #     getpass.return_value = ''
    #     get_profile_info.return_value = 'something'
    #     self.assertEqual(main(), {42415631327: []})
