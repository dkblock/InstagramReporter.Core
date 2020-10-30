# import unittest
# from unittest.mock import patch

# from instapi.instapi import InstAPI
# from tasks.task_4 import main


# class TestFourthTask(unittest.TestCase):

#     @patch('builtins.input', return_value='0')
#     def test_count_is_zero(self, mock_count):
#         expected_value = [
#             {
#                 42415631327: {
#                     'geotags': [],
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
#                     'geotags': [],
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
#                     'geotags': [],
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
#             'location': {
#                 'name': 'Yaroslavl',
#             },
#         }]
#         get_last_feed.return_value = mock_posts
#         expected_value = [
#             {
#                 42415631327: {
#                     'geotags': ['Yaroslavl'],
#                     'records': [
#                         {
#                             'id': 1,
#                             'date': '12-06-2018, 12:55',
#                             'description': '',
#                             'geotag': 'Yaroslavl',
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
#                 'location': {
#                     'name': 'Yaroslavl',
#                 },
#             },
#             {
#                 'pk': 2,
#                 'taken_at': 1528797322,
#                 'text': 'something',
#                 'location': {
#                     'name': 'Moscow',
#                 },
#             },
#             {
#                 'pk': 3,
#                 'taken_at': 1528797322,
#                 'text': 'text',
#                 'location': {
#                     'name': 'Yaroslavl',
#                 },
#             },
#         ]
#         get_last_feed.return_value = mock_posts
#         expected_value = [
#             {
#                 42415631327: {
#                     'geotags': ['Yaroslavl', 'Moscow'],
#                     'records': [
#                         {
#                             'id': 1,
#                             'date': '12-06-2018, 12:55',
#                             'description': '',
#                             'geotag': 'Yaroslavl',
#                         },
#                         {
#                             'id': 2,
#                             'date': '12-06-2018, 12:55',
#                             'description': 'something',
#                             'geotag': 'Moscow',
#                         },
#                         {
#                             'id': 3,
#                             'date': '12-06-2018, 12:55',
#                             'description': 'text',
#                             'geotag': 'Yaroslavl',
#                         },
#                     ],
#                 },
#             },
#         ]
#         self.assertEqual(main(), expected_value)
