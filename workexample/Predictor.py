from strategy.MultinomialLogisticRegressionStrategy import MultinomialLogisticRegressionStrategy
from strategy.Oracle import Oracle
from strategy.PredictionStrategy import PredictionStrategy
from strategy.RandomForestStrategy import RandomForestStrategy
from vkapi.VK_API import VK_API


class Predictor:

    def __init__(self):
        self.vk_api = VK_API()
        self.oracle = Oracle(MultinomialLogisticRegressionStrategy())

    def set_strategy(self, strategy: PredictionStrategy):
        self.oracle.strategy = strategy

    def convert_class_to_value(self, score: int) -> str:
        if score == 1: return 'низкая'
        if score == 2: return 'средняя'
        if score == 3: return 'высокая'

    def predict_social_portrait(self, vk_url: str):
        screen_name = vk_url.split('/')[-1]
        self.vk_api.screen_name = screen_name

        print("Анализ пользователя " + screen_name)

        # get features
        sex, followers_count, user_id = self.vk_api.get_sex_and_followers_count_and_user_id()
        friends_count = self.vk_api.get_friends_count(user_id)
        video_count = self.vk_api.get_video_count(user_id)
        profile_photos_count = self.vk_api.get_profile_photos_count(user_id)

        print(sex, followers_count, friends_count, video_count, profile_photos_count)

        prediction: map = self.oracle.predict_classes(
            [sex, followers_count, friends_count, video_count, profile_photos_count])

        print("Открытость к опыту: " + str(self.convert_class_to_value(prediction['O'])) + "\n" +
              "Добросовестность: " + str(self.convert_class_to_value(prediction['C'])) + "\n" +
              "Экстраверсия: " + str(self.convert_class_to_value(prediction['E'])) + "\n" +
              "Дружелюбие / Уступчивость: " + str(self.convert_class_to_value(prediction['A'])) + "\n" +
              "Эмоциональная стабильность: " + str(self.convert_class_to_value(prediction['N'])))
