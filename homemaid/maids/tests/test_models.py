import os
from datetime import date
from unittest.mock import MagicMock

from django.core.files import File
from django.test import TestCase

from ..models import Maid


class TestMaid(TestCase):
    def test_model_should_have_defined_fields(self):
        # Given
        Maid.objects.create(
            name='BB',
            birthdate=date(1998, 4, 29),
            description='Super Maid of the Year',
            certificate='Best Maid 2012',
            salary=3000
        )

        # When
        maid = Maid.objects.last()

        # Then
        assert maid.name == 'BB'
        assert maid.birthdate == date(1998, 4, 29)
        assert maid.description == 'Super Maid of the Year'
        assert maid.certificate == 'Best Maid 2012'
        assert maid.salary == 3000

    def test_model_should_have_image_field(self):
        # Given
        mock = MagicMock(spec=File)
        mock.name = 'profile.png'

        Maid.objects.create(
            name='BB',
            profile_image=mock,
            birthdate=date(1998, 4, 29),
            description='Super Maid of the Year',
            certificate='Best Maid 2012',
            salary=3000
        )

        # When
        maid = Maid.objects.last()

        # Then
        self.assertEqual(maid.profile_image.name, 'profile.png')

        os.remove('profile.png')

    def test_model_should_have_created_and_modified_fields(self):
        # Given
        Maid.objects.create(
            name='BB',
            birthdate=date(1998, 4, 29),
            description='Super Maid of the Year',
            certificate='Best Maid 2012',
            salary=3000
        )

        # When
        maid = Maid.objects.last()

        # Then
        self.assertTrue(maid.created)
        self.assertTrue(maid.modified)

        assert maid.created is not None
        assert maid.modified is not None