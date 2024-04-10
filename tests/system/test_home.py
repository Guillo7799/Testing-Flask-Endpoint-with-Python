from tests.system.base_test import BaseTest
import json

class TestHome(BaseTest):
    def test_home(self):
        with self.app() as c: #all the block is called context_manager, Flask give us a client service to make a request
            resp = c.get('/')

            self.assertEqual(resp.status_code,200)
            self.assertEqual(json.loads(resp.get_data()),
                             {'message': 'Hello world!'}) #we need to convert string into json