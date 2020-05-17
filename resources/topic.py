from flask_restful import Resource

from handlers.topic_handler import TopicHandler
from models.query_models.topic_model import TopicQueryModel
from models.response_models.topic_model import TopicResponseModel
from resources import ApiResponse, schema


class Topic(Resource):
    @schema(query_model=TopicQueryModel, response_model=TopicResponseModel)
    def get(self, topic_id) -> ApiResponse:
        topic = TopicHandler(topic_id).get_topic()
        return ApiResponse().ok(topic)

    @schema(query_model=TopicQueryModel, response_model=TopicResponseModel)
    def put(self, topic_id) -> ApiResponse:
        kwargs = self.parsed_args
        topic = TopicHandler(topic_id).update_topic(**kwargs)
        return ApiResponse().ok(topic)

    @schema(query_model=TopicQueryModel, response_model=TopicResponseModel)
    def delete(self, topic_id) -> ApiResponse:
        TopicHandler(topic_id).delete_topic()
        return ApiResponse().ok()


class Topics(Resource):
    @schema(query_model=TopicQueryModel, response_model=TopicResponseModel)
    def get(self) -> ApiResponse:
        topics = TopicHandler().get_topics()
        return ApiResponse().ok(topics)

    @schema(query_model=TopicQueryModel, response_model=TopicResponseModel)
    def post(self) -> ApiResponse:
        kwargs = self.parsed_args
        topic = TopicHandler().create_topic(**kwargs)

        return ApiResponse().ok(topic)
