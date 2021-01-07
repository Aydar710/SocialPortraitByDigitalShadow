from VK_API import VK_API

vk_api = VK_API('nursabir')
sex, followers_count, user_id = vk_api.get_sex_and_followers_count_and_user_id()
# print(sex)
# print(followers_count)
# print(user_id)

# friends_count = vk_api.get_friends_count(user_id)
# print(friends_count)

# video_count = vk_api.get_video_count(user_id)
# print(video_count)

profile_photos_count = vk_api.get_profile_photos_count(user_id)
print(profile_photos_count)