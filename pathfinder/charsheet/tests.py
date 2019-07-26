# from django.test import TestCase
# from django.urls import reverse
#
# from charsheet.models import Character
#
#
# class CharacterTest(TestCase):
#     def test_get_strength_modifier(self):
#         expected = {
#             0: -5,
#             7: -2,
#             8: -1,
#             9: -1,
#             10: 0,
#             11: 0,
#             12: 1,
#             13: 1,
#             20: 5,
#             31: 10,
#             43: 16,
#         }
#
#         for k, v in expected.items():
#             assert Character(base_strength=k).strength_modifier() == v
#
#
# class ViewTest(TestCase):
#     def test_index(self):
#         response = self.client.get(reverse('charsheet:index'))
#         self.assertEqual(response.status_code, 200)
#         self.assertContains(response, "No characters are available.")
#         self.assertQuerysetEqual(response.context['characters'], [])
