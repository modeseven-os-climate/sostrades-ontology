'''
Copyright 2024 Capgemini

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
'''
mode: python; py-indent-offset: 4; tab-width: 8; coding:utf-8
'''
import unittest
import pprint
from sostrades_core.tools.check_headers import check_headers


class Testheader(unittest.TestCase):
    """
    Check headers test class
    """

    def setUp(self):
        '''
        Initialize third data needed for testing
        '''
        self.pp = pprint.PrettyPrinter(indent=4, compact=True)
        self.ExtensionToIgnore = ["xlsx","owl","pkl", "png", "jpg", "csv", "md", "markdown", "avif", "json", "in", "gitignore", "cfg", "puml", "pdf", "txt", "ipynb", "zip", "rst"]
        #Add here the files to ignore       
        self.FilesToIgnore = []
        #commit from where to compare added, modeified deleted ...
        self.airbus_rev_commit = "9ce0e11f2dfcef0a8b6b5079932249b363ea3d5b"

    def test_Headers(self):
        check_headers(self.ExtensionToIgnore,self.FilesToIgnore,self.airbus_rev_commit)

        
