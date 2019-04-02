from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
import uuid

from .models import Notes


class ModelTestCase(TestCase):

    def setUp(self):
        self.notes_title = 'Some title.'
        self.notes_text = 'Some text!!'
        self.notes = Notes(title=self.notes_title, text=self.notes_text)

    def test_model_create_notes(self):
        old_count = Notes.objects.count()
        self.notes.save()
        new_count = Notes.objects.count()
        self.assertNotEqual(old_count, new_count)


class ViewTestCase(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.notes_title = 'Some title.'
        self.notes_text = 'Some text!!'
        self.notes = Notes(title=self.notes_title, text=self.notes_text)
        self.notes.save()

    def test_api_get(self):
        notes = Notes.objects.get()
        response = self.client.get(
            reverse('Notedetails', kwargs={'pk': notes.id}), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_api_put(self):
        notes = Notes.objects.get()
        change_note = {'title': 'Some new title.', 'text': 'Some new text!!'}
        result = self.client.put(
            reverse('Notedetails', kwargs={'pk': notes.id}),
            change_note, format='json')
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        new_note = Notes.objects.get()
        self.assertNotEqual(notes.title, new_note.title)

    def test_api_delete(self):
        notes = Notes.objects.get()
        response = self.client.delete(
            reverse('Notedetails', kwargs={'pk': notes.id}),
            format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_api_fake_delete(self):
        response = self.client.delete('Notedetails', kwargs={'pk': uuid.uuid4},
                                      format='json', follow=True)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
