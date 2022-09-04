#!/usr/bin/python3
""" BaseTest module """


from datetime import datetime, timedelta
from models.base_model import BaseModel
import time
import unittest


class BaseModelTest(unittest.TestCase):
    """ BaseTest class """

    def testClassDocumentation(self):
        """
            Class  documentation
        """
        self.assertGreater(len(BaseModel.__doc__), 0)

    def testConstructorDocumentation(self):
        """
            Constructor documentation
        """
        self.assertGreater(len(BaseModel.__init__.__doc__), 0)

    def testStrDocumentation(self):
        """
            __str__ function documentation
        """
        self.assertGreater(len(BaseModel.__str__.__doc__), 0)

    def testSaveDocumentation(self):
        """
            save function documentation
        """
        self.assertGreater(len(BaseModel.save.__doc__), 0)

    def testToDictDocumentation(self):
        """
            to_dict function have documentation
        """
        self.assertGreater(len(BaseModel.to_dict.__doc__), 0)

    def testStr(self):
        """
            Test __str__ function
        """
        b1 = BaseModel()
        b1.name = "Alx"
        b1.my_number = 89
        b1.my_wrong_test = None
        self.assertEqual(
            b1.__str__(), "[{}] ({}) {}".format(
                b1.__class__.__name__,
                b1.id,
                b1.__dict__
            )
        )

    def testSave(self):
        """
            Test save function
        """
        import os
        import json
        from models import storage

        b1 = BaseModel()
        b1.name = "Alx"
        b1.my_number = 89
        b1.my_wrong_test = None
        b1.save()
        self.assertGreater(b1.updated_at, b1.created_at)
        self.assertDictEqual(
            b1.to_dict(),
            {
                '__class__': 'BaseModel',
                'created_at': b1.created_at.strftime("%Y-%m-%dT%H:%M:%S.%f"),
                'id': b1.id,
                'my_number': 89,
                'name': "Alx",
                'updated_at': b1.updated_at.strftime("%Y-%m-%dT%H:%M:%S.%f")
            }
        )

        tmpDict = {}
        for key, value in storage.all().items():
            tmpDict[key] = value.to_dict()
        b1 = BaseModel()
        key = "{}.{}".format("BaseModel", b1.id)
        storage.new(b1)
        b1.save()
        tmpDict[key] = b1.to_dict()
        inputStr = json.dumps(tmpDict)
        self.assertTrue(os.path.exists("file.json"))
        with open("file.json", "r") as file:
            output = file.read()
        self.assertEqual(json.loads(inputStr), json.
