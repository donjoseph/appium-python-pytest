import pytest

from config.ApiConfig import ApiConfig
from utilities import ApiUtils, GenericMethods
from utilities.BaseClassApi import BaseClassApi


class TestApi(BaseClassApi):

    # hit url for get posts
    # get the posts validate the status is 200
    # validate the count of posts
    def test_GetPosts(self):
        log = self.log
        response = ApiUtils.httpGet(URL=ApiConfig.postURL)
        ApiUtils.httpStatusValidation(response)
        body = response.json()
        log.info(body)

        assert len(body) == 100, "Posts count is not matching"
        log.info("Validation completed for get service")

    # hit url for post posts
    # validate the response status code is 200
    # validate new id is generated
    def test_PostPosts(self, getPostData):
        log = self.log
        payload = {
            'title': getPostData["title"],
            'body': getPostData["body"],
            'userId': getPostData["userid"]
        }
        response = ApiUtils.httpPost(URL=ApiConfig.postURL, payload=payload)
        ApiUtils.httpStatusValidation(response)
        body = response.json()
        log.info(body)
        assert body['id'] is not None
        log.info("Validation completed for post service")

    # to create fake users
    @pytest.fixture(params=GenericMethods.createUsersPost(noOfUsers=3))
    def getPostData(self, request):
        return request.param
