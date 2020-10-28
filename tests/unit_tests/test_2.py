# import unittest
# from unittest.mock import patch

# from instapi.instapi import InstAPI
# from tasks.task_2 import find_tags, main


# class TestSecondTask(unittest.TestCase):

#     @patch('tasks.task_2.get_blogs', return_value=[])
#     def test_empty_blogs(self, get_blogs):
#         self.assertEqual(main(), {42415631327: []})

#     @patch.object(InstAPI, "get_followings")
#     @patch.object(InstAPI, "get_profile_info")
#     def test_is_blog(self, get_profile, get_followings):
#         get_followings.return_value = [{'pk': 1}]
#         mock_user = {
#             'user': {
#                 'pk': 1,
#                 'follower_count': 100001,
#                 'full_name': 'AAA',
#                 'biography': 'Sport blogger',
#             },
#         }
#         get_profile.return_value = mock_user
#         expected_value = {
#             42415631327: [{
#                 1: {
#                     'name': 'AAA',
#                     'followers': 100001,
#                     'description': 'Sport blogger',
#                     'tags': ['sport'],
#                 },
#             }],
#         }
#         self.assertEqual(main(), expected_value)

#     @patch.object(InstAPI, "get_followings")
#     @patch.object(InstAPI, "get_profile_info")
#     def test_not_is_blog(self, get_profile, get_followings):
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

#     def test_find_tags(self):
#         blogger = 'It is my personal blog about sport and travel.'
#         tags = ['travel', 'sport', 'cooking', 'кухня', 'спорт', 'фитнес']
#         not_blogger = 'something'
#         expected_tags = ['travel', 'sport']
#         self.assertEqual(find_tags(blogger, tags), expected_tags)
#         self.assertEqual(find_tags(not_blogger, tags), [])
