import vk_api
import requests
import time

from humandetection.HumanCounter import HumanCounter

api_version = "5.126"
token = 'f047c883f6419bdf4fa39be425dc7a2c9c3ff6e07226d5386467f11d83f3fe961cd1c40f99f31f844aeb5'
BASE_VK_URL = 'https://api.vk.com/method/'


class VK_API(object):

    def __init__(self, screen_name):
        self.screen_name = screen_name
        self.human_counter = HumanCounter()

    # returns access_token
    def authorize(self):
        vk_session = vk_api.VkApi('aydar710@gmail.com', 'some pass')
        vk_session.auth()
        return vk_session.token['access_token']

    def get_sex_and_followers_count_and_user_id(self):
        profile_info_url = BASE_VK_URL + "users.get"
        user_info_response = requests.get(profile_info_url, params={
            'access_token': token,
            'v': api_version,
            'user_ids': self.screen_name,
            'fields': 'sex, followers_count'
        }).json()['response'][0]

        # print(user_info_response)
        sex = user_info_response['sex']
        try:
            followers_count = user_info_response['followers_count']
        except Exception:
            print('followers count is not available')
            followers_count = -1
        user_id = user_info_response['id']
        return sex, followers_count, user_id

    #:param user_id: Int
    #:return friends_count : Int
    def get_friends_count(self, user_id):
        friends_url = BASE_VK_URL + "friends.get"

        friends_response = requests.get(friends_url, params={
            'access_token': token,
            'v': api_version,
            'user_id': user_id,
        }).json()['response']

        return friends_response['count']

    #:param user_id : Int
    #:return video_count : Int
    def get_video_count(self, user_id):
        video_url = BASE_VK_URL + 'video.get'

        video_response = requests.get(video_url, params={
            'access_token': token,
            'v': api_version,
            'owner_id': user_id
        }).json()['response']

        return video_response['count']

    #:param user_id : Int
    #:return profile_photos_count : Int
    def get_profile_photos_count(self, user_id):
        photos_url = BASE_VK_URL + 'photos.get'

        photos_response = requests.get(photos_url, params={
            'access_token': token,
            'v': api_version,
            'owner_id': user_id,
            'album_id': 'profile'
        }).json()['response']

        return photos_response['count']

    def get_user_photos_in_company_count(self) -> int:
        profile_info_url = BASE_VK_URL + "users.get"
        photos_url = BASE_VK_URL + "photos.getAll"
        user_info_response = requests.get(profile_info_url, params={
            'access_token': token,
            'v': api_version,
            'user_ids': self.screen_name,
        }).json()['response'][0]

        user_id = user_info_response['id']

        photo_items = requests.get(photos_url, params={
            'access_token': token,
            'v': api_version,
            'owner_id': user_id,
        }).json()['response']['items']

        user_photos_in_company_count = 0
        for photo_item in photo_items:
            # photo_url = photo_item['sizes'][len(photo_item['sizes']) // 2]['url']
            photo_url = photo_item['sizes'][-1]['url']
            print("photo url", photo_url)
            if self.human_counter.has_more_than_one_person(photo_url):
                user_photos_in_company_count += 1

        return user_photos_in_company_count

    def get_wall_posts_count_for_last_6_months(self) -> int:
        wall_get_url = BASE_VK_URL + "wall.get"

        posts_are_not_empty_or_reached_6_months: bool = False
        posts_count: int = 0
        current_page = 0
        posts_in_page = 100
        while not posts_are_not_empty_or_reached_6_months:
            posts = requests.get(wall_get_url, params={
                'access_token': token,
                'v': api_version,
                'domain': self.screen_name,
                'count': posts_in_page,
                'offset': current_page * posts_in_page,
                'filter': 'owner'
            }).json()['response']['items']

            if len(posts) == 0:
                break

            millis_after_six_months = (time.time() * 1000) + (6 * 30 * 24 * 60 * 60 * 1000)
            for post in posts:
                post_date = post['date']
                if post_date < millis_after_six_months:
                    posts_count += 1
                else:
                    break

            current_page += 1
        return posts_count
