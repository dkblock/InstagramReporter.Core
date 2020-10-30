# import unittest
# from unittest.mock import patch

# from instapi.instapi import InstAPI
# from tasks.task_5 import main


# class TestFifth(unittest.TestCase):

#     @patch('builtins.input', return_value='0')
#     def test_count_is_zero(self, mock_count):
#         expected_value = [
#             {
#                 42415631327: {
#                     'max': 'does not exist',
#                     'min': 'does not exist',
#                     'middle': 'does not exist',
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
#                     'max': 'does not exist',
#                     'min': 'does not exist',
#                     'middle': 'does not exist',
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
#                     'max': 'does not exist',
#                     'min': 'does not exist',
#                     'middle': 'does not exist',
#                     'records': [],
#                 },
#             },
#         ]
#         self.assertEqual(main(), expected_value)

#     @patch('builtins.input', return_value='1')
#     @patch.object(InstAPI, "get_last_feed")
#     def test_one_record(self, get_last_feed, mock_count):
#         mock_posts = [{
#             'pk': 1,
#             'taken_at': 1528797322,
#             'text': '',
#             'like_count': 100500,
#         }]
#         get_last_feed.return_value = mock_posts
#         expected_value = [
#             {
#                 42415631327: {
#                     'max': 100500,
#                     'min': 100500,
#                     'middle': 100500.0,
#                     'records': [
#                         {
#                             'id': 1,
#                             'date': '12-06-2018, 12:55',
#                             'description': '',
#                             'count': 100500,
#                         },
#                     ],
#                 },
#             },
#         ]
#         self.assertEqual(main(), expected_value)

#     @patch('builtins.input', return_value='1')
#     @patch.object(InstAPI, "get_last_feed")
#     def test_two_records(self, get_last_feed, mock_count):
#         mock_posts = [
#             {
#                 'pk': 1,
#                 'taken_at': 1528797322,
#                 'text': '',
#                 'like_count': 2,
#             },
#             {
#                 'pk': 2,
#                 'taken_at': 1528797322,
#                 'text': 'text',
#                 'like_count': 3,
#             },
#         ]

#         get_last_feed.return_value = mock_posts
#         expected_value = [
#             {
#                 42415631327: {
#                     'max': 3,
#                     'min': 2,
#                     'middle': 2.5,
#                     'records': [
#                         {
#                             'id': 1,
#                             'date': '12-06-2018, 12:55',
#                             'description': '',
#                             'count': 2,
#                         },
#                         {
#                             'id': 2,
#                             'date': '12-06-2018, 12:55',
#                             'description': 'text',
#                             'count': 3,
#                         },
#                     ],
#                 },
#             },
#         ]
#         self.assertEqual(main(), expected_value)
