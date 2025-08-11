import unittest
from unittest.mock import patch
import workgroup_assistant_api_client
from workgroup_assistant_api_client import DefaultApi, ApiClient
from workgroup_assistant_api_client.rest import ApiException
import warnings

class TestDefaultApi(unittest.TestCase):
    def setUp(self):
        docker_container = "localhost"
        server_port = "4042"
        namespace = '/v1/gss'
        self.api_instance =  workgroup_assistant_api_client.api.default_api.DefaultApi()
        self.api_instance.api_client.configuration.host = 'http://' + docker_container + ':' + server_port + '' + namespace

    def tearDown(self):
        pass

    """Test case for execute_login_post

    Submit a login with user credential payload for group member with existing AI service agent  # noqa: E501
    """

    def test_execute_login_post_200(self):
        response = self.api_instance.execute_login_post_with_http_info(name='testuser', password='testpass', inviter_default_app_id="", inviter_user_role="")[1]
        self.assertEqual(response, 200)
        pass

    def test_execute_login_post_404(self):
        try:
            response = self.api_instance.execute_login_post_with_http_info(name='testuser', password='testpass', inviter_default_app_id="", inviter_user_role="")[1]
        except ApiException as e:
            self.assertEqual(e.status, 404)
        pass

    def test_execute_login_post_500(self):
        try:
            response = self.api_instance.execute_login_post_with_http_info(name='testuser', password='testpass', inviter_default_app_id="", inviter_user_role="")[1]
        except ApiException as e:
            self.assertEqual(e.status, 500)
        pass

    def test_execute_login_post_400(self):
        try:
            response = self.api_instance.execute_login_post_with_http_info(name='testuser', password='testpass', inviter_default_app_id="", inviter_user_role="")[1]
        except ApiException as e:
            self.assertEqual(e.status, 400)
        pass

    """Test case for execute_logout_post

    Load logout payload as group member for existing AI service agent  # noqa: E501
    """

    def test_execute_logout_post_200(self):
        response = self.api_instance.execute_logout_post_with_http_info()[1]
        self.assertEqual(response, 200)
        pass

    def test_execute_logout_post_404(self):
        try:
            response = self.api_instance.execute_logout_post_with_http_info()[1]
        except ApiException as e:
            self.assertEqual(e.status, 404)
        pass

    def test_execute_logout_post_500(self):
        try:
            response = self.api_instance.execute_logout_post_with_http_info()[1]
        except ApiException as e:
            self.assertEqual(e.status, 500)
        pass

    def test_execute_logout_post_400(self):
        try:
            response = self.api_instance.execute_logout_post_with_http_info()[1]
        except ApiException as e:
            self.assertEqual(e.status, 400)
        pass

    """Test case for execute_signup_post

    Commit a new sign-up application payload for group member with new AI service agent onto Researcher Hub  # noqa: E501
    """

    def test_execute_signup_post_200(self):
        response = self.api_instance.execute_signup_post_with_http_info(avatar='robotPurple.png', name='testuser', email='test@example.com', password='testpass', slackname='testslack', researchgate='testresearchgate', default_app_id='testapp', default_app_description='testdesc')[1]
        self.assertEqual(response, 200)
        pass

    def test_execute_signup_post_404(self):
        try:
            response = self.api_instance.execute_signup_post_with_http_info(avatar='robotPurple.png', name='testuser', email='test@example.com', password='testpass', slackname='testslack', researchgate='testresearchgate', default_app_id='testapp', default_app_description='testdesc')[1]
        except ApiException as e:
            self.assertEqual(e.status, 404)
        pass

    def test_execute_signup_post_500(self):
        try:
            response = self.api_instance.execute_signup_post_with_http_info(avatar='robotPurple.png', name='testuser', email='test@example.com', password='testpass', slackname='testslack', researchgate='testresearchgate', default_app_id='testapp', default_app_description='testdesc')[1]
        except ApiException as e:
            self.assertEqual(e.status, 500)
        pass

    def test_execute_signup_post_400(self):
        try:
            response = self.api_instance.execute_signup_post_with_http_info(avatar='robotPurple.png', name='testuser', email='test@example.com', password='testpass', slackname='testslack', researchgate='testresearchgate', default_app_id='testapp', default_app_description='testdesc')[1]
        except ApiException as e:
            self.assertEqual(e.status, 400)
        pass

    """Test case for load_login_post

    Load login payload as group member for existing AI service agent  # noqa: E501
    """

    def test_load_login_post_200(self):
        response = self.api_instance.load_login_post_with_http_info(id=1)[1]
        self.assertEqual(response, 200)
        pass

    def test_load_login_post_404(self):
        try:
            response = self.api_instance.load_login_post_with_http_info(id=1)[1]
        except ApiException as e:
            self.assertEqual(e.status, 404)
        pass

    def test_load_login_post_500(self):
        try:
            response = self.api_instance.load_login_post_with_http_info(id=1)[1]
        except ApiException as e:
            self.assertEqual(e.status, 500)
        pass

    def test_load_login_post_400(self):
        try:
            response = self.api_instance.load_login_post_with_http_info(id=1)[1]
        except ApiException as e:
            self.assertEqual(e.status, 400)
        pass

    """Test case for load_members_profile_post

    Get member's profile and voting preferences of AI service agent  # noqa: E501
    """

    def test_load_members_profile_post_200(self):
        response = self.api_instance.load_members_profile_post_with_http_info(id=1)[1]
        self.assertEqual(response, 200)
        pass

    def test_load_members_profile_post_404(self):
        try:
            response = self.api_instance.load_members_profile_post_with_http_info(id=1)[1]
        except ApiException as e:
            self.assertEqual(e.status, 404)
        pass

    def test_load_members_profile_post_500(self):
        try:
            response = self.api_instance.load_members_profile_post_with_http_info(id=1)[1]
        except ApiException as e:
            self.assertEqual(e.status, 500)
        pass

    def test_load_members_profile_post_400(self):
        try:
            response = self.api_instance.load_members_profile_post_with_http_info(id=1)[1]
        except ApiException as e:
            self.assertEqual(e.status, 400)
        pass

    """Test case for load_signup_post

    Load sign-up application payload as group member for new AI service agent  # noqa: E501
    """

    def test_load_signup_post_200(self):
        response = self.api_instance.load_signup_post_with_http_info(id=1)[1]
        self.assertEqual(response, 200)
        pass

    def test_load_signup_post_404(self):
        try:
            response = self.api_instance.load_signup_post_with_http_info(id=1)[1]
        except ApiException as e:
            self.assertEqual(e.status, 404)
        pass

    def test_load_signup_post_500(self):
        try:
            response = self.api_instance.load_signup_post_with_http_info(id=1)[1]
        except ApiException as e:    
            self.assertEqual(e.status, 500)
        pass

    def test_load_signup_post_400(self):
        try:
            response = self.api_instance.load_signup_post_with_http_info(id=1)[1]
        except ApiException as e:  
            self.assertEqual(e.status, 400)
        pass

    """Test case for load_workgroup_post

    Get workgroup for AI service agent  # noqa: E501
    """

    def test_load_workgroup_post_200(self):
        response = self.api_instance.load_workgroup_post_with_http_info(id=1, default_app_id='testapp')[1]
        self.assertEqual(response, 200)
        pass

    def test_load_workgroup_post_404(self):
        try:
            response = self.api_instance.load_workgroup_post_with_http_info(id=1, default_app_id='testapp')[1]
        except ApiException as e:  
            self.assertEqual(e.status, 404)
        pass

    def test_load_workgroup_post_500(self):
        try:
            response = self.api_instance.load_workgroup_post_with_http_info(id=1, default_app_id='testapp')[1]
        except ApiException as e:
            self.assertEqual(e.status, 500)
        pass

    def test_load_workgroup_post_400(self):
        try:
            response = self.api_instance.load_workgroup_post_with_http_info(id=1, default_app_id='testapp')[1]
        except ApiException as e:
            self.assertEqual(e.status, 400)
        pass

if __name__ == '__main__':
    warnings.filterwarnings(action="ignore", category=ResourceWarning)
    unittest.main()