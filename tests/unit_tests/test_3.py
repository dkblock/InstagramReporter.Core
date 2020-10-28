# import unittest
# from unittest.mock import patch

# from instapi.instapi import InstAPI
# from tasks.task_3 import main


# class TestThirdTask(unittest.TestCase):

#     @patch('builtins.input', return_value='0')
#     def test_count_is_zero(self, mock_count):
#         expected_value = [
#             {
#                 42415631327: {
#                     'last_activity': 'does not exist',
#                     'frequency': 0,
#                     'records': [],
#                 },
#             },
#         ]
#         self.assertEqual(main(), expected_value)

#     @patch('builtins.input', return_value='1')
#     def test_count_is_one(self, mock_count):
#         expected_value = [
#             {
#                 42415631327: {
#                     'last_activity': 'does not exist',
#                     'frequency': 0,
#                     'records': [],
#                 },
#             },
#         ]
#         self.assertEqual(main(), expected_value)

#     @patch('builtins.input', return_value='1')
#     @patch('tasks.task_3.get_records', return_value=[])
#     def test_empty_records(self, get_records, mock_count):
#         expected_value = [
#             {
#                 42415631327: {
#                     'last_activity': 'does not exist',
#                     'frequency': 0,
#                     'records': [],
#                 },
#             },
#         ]
#         self.assertEqual(main(), expected_value)

#     @patch('builtins.input', return_value='1')
#     @patch.object(InstAPI, "get_followings")
#     @patch.object(InstAPI, "get_last_feed")
#     def test_one_record(self, get_last_feed, get_followings, mock_count):
#         get_followings.return_value = [{'pk': 1}]
#         mock_posts = [{
#             'pk': 1,
#             'taken_at': 1528797322,
#             'text': '',
#         }]
#         get_last_feed.return_value = mock_posts
#         expected_value = [
#             {
#                 42415631327: {
#                     'last_activity': '12-06-2018, 12:55',
#                     'frequency': 1,
#                     'records': [
#                         {
#                             'id': 1,
#                             'date': '12-06-2018, 12:55',
#                             'description': '',
#                             'tags': [],
#                         },
#                     ],
#                 },
#             },
#         ]
#         self.assertEqual(main(), expected_value)

#     @patch('builtins.input', return_value='1')
#     @patch.object(InstAPI, "get_followings")
#     @patch.object(InstAPI, "get_last_feed")
#     def test_two_records(self, get_last_feed, get_followings, mock_count):
#         get_followings.return_value = [{'pk': 1}]
#         mock_posts = [
#             {
#                 'pk': 1,
#                 'taken_at': 1528797322,
#                 'text': '',
#             },
#             {
#                 'pk': 2,
#                 'taken_at': 1528797322,
#                 'text': 'I like #sport and #travel',
#             }
#         ]
#         get_last_feed.return_value = mock_posts
#         expected_value = [
#             {
#                 42415631327: {
#                     'last_activity': '12-06-2018, 12:55',
#                     'frequency': 1,
#                     'records': [
#                         {
#                             'id': 1,
#                             'date': '12-06-2018, 12:55',
#                             'description': '',
#                             'tags': [],
#                         },
#                         {
#                             'id': 2,
#                             'date': '12-06-2018, 12:55',
#                             'description': 'I like #sport and #travel',
#                             'tags': ['#sport', '#travel'],
#                         },
#                     ],
#                 },
#             },
#         ]
#         print(main())
#         self.assertEqual(main(), expected_value)
