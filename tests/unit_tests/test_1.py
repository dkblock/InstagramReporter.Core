# import unittest
# from unittest.mock import patch

# from instapi.instapi import InstAPI
# from tasks.task_1 import main


# class TestFirstTask(unittest.TestCase):

#     @patch('tasks.task_1.get_celebrities', return_value=[])
#     def test_empty_celebrities(self, get_celebrities):
#         self.assertEqual(main(), {42415631327: []})

#     @patch.object(InstAPI, "get_followings")
#     @patch.object(InstAPI, "get_profile_info")
#     def test_is_celebrity(self, get_profile, get_followings):
#         get_followings.return_value = [{'pk': 1}]
#         mock_user = {
#             'user': {
#                 'pk': 1,
#                 'follower_count': 100001,
#                 'full_name': 'AAA',
#                 'biography': 'BBB',
#             },
#         }
#         get_profile.return_value = mock_user
#         expected_value = {
#             42415631327: [{
#                 1: {
#                     'name': 'AAA',
#                     'followers': 100001,
#                     'description': 'BBB',
#                 },
#             }],
#         }
#         self.assertEqual(main(), expected_value)

#     @patch.object(InstAPI, "get_followings")
#     @patch.object(InstAPI, "get_profile_info")
#     def test_not_is_celebrity(self, get_profile, get_followings):
#         get_followings.return_value = [{'pk': 1}]
#         mock_user = {
#             'user': {
#                 'pk': 1,
#                 'follower_count': 99999,
#                 'full_name': 'AAA',
#                 'biography': 'BBB',
#             },
#         }
#         get_profile.return_value = mock_user
#         expected_value = {42415631327: []}
#         self.assertEqual(main(), expected_value)

#     @patch.object(InstAPI, "get_followings")
#     def test_real_not_celebrities(self, get_followings):
#         get_followings.return_value = [{'pk': 1396398358}, {'pk': 42415631327}]
#         expected_value = {
#             42415631327: []
#         }
#         self.assertEqual(main(), expected_value)

#     @patch('tasks.task_1.get_celebrities', return_value='mock')
#     @patch.object(InstAPI, "get_followings")
#     @patch.object(InstAPI, "get_profile_info")
#     def test_all_patch(self, get_profile, get_followings, get_celebrities):
#         get_followings.return_value = [{'pk': 1}]
#         get_profile.return_value = 'something'
#         expected_value = {42415631327: 'mock'}
#         self.assertEqual(main(), expected_value)
