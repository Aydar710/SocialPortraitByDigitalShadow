import pandas

from vkapi.VK_API import VK_API

vk_api = VK_API('aydarrr')

answers_frame = pandas.read_csv('../answerprocessing/answers.csv', delimiter=',')
vk_pages = answers_frame['Ссылка на страницу ВК         '].values

answers_frame['sex'] = -1
answers_frame['followers count'] = -1
answers_frame['friends count'] = -1
answers_frame['video count'] = -1
answers_frame['profile photos count'] = -1

for i in range(len(vk_pages)):
    screen_name = vk_pages[i].split('/')[-1]
    print('fetching', screen_name)
    vk_api.screen_name = screen_name

    # get features
    sex, followers_count, user_id = vk_api.get_sex_and_followers_count_and_user_id()
    friends_count = vk_api.get_friends_count(user_id)
    video_count = vk_api.get_video_count(user_id)
    profile_photos_count = vk_api.get_profile_photos_count(user_id)

    print(sex, followers_count, friends_count, video_count, profile_photos_count)

    # set features
    answers_frame['sex'][i] = sex
    answers_frame['followers count'][i] = followers_count
    answers_frame['friends count'][i] = friends_count
    answers_frame['video count'][i] = video_count
    answers_frame['profile photos count'][i] = profile_photos_count

answers_frame.to_csv('../answerprocessing/answers.csv', index=False)
