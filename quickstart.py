from tinderbotz.helpers.gpt_helper import GPTHelper
from tinderbotz.session import Session
from tinderbotz.helpers.constants_helper import *
from tinderbotz.helpers.env_parser import env_vars

if __name__ == "__main__":
    from tinderbotz.helpers.env_parser import env_vars
    
    gpt_helper = GPTHelper()
    user_data = env_vars.get("USER_DATA")
    # you can login first using a specific user_data folder then load the user_data
    session = Session(user_data=user_data)
    
    # login doesnt work at the moment
    #session.like(amount=2, ratio="72.5%", sleep=0.5)
    #session.dislike(amount=0)
    # session.superlike(amount=1)
    
    # new match list is a list of matches that you haven't interacted with yet
    new_matches = []
    new_matches = session.get_new_matches(amount=10, quickload=True)

    # get already interacted with matches (matches with whom you've chatted already)
    # messaged_matches = session.get_messaged_matches()
    
    # you can store the data and images of these matches now locally in data/matches
    # For now let's just store the messaged_matches
    # for match in messaged_matches:
    #     session.store_local(match)

    # Pick up line with their personal name so it doesn't look spammy

    # loop through my new matches and send them the first message of the conversation
for match in new_matches:
    # store name and chatid in variables so we can use it more simply later on
    name = match.get_name()
    id = match.get_chat_id()
    # Skip this iteration if name is empty
    if not name:
        print("Skipping match with empty name and id ="+id)
        continue
        
    print(name, id)
    
    bio = match.get_bio()
    if not bio:
        print("Skipping match with empty bio and name ="+name)
        bio = "aucune bio, ignorez"

    message = gpt_helper.generate_pickup_line(name, bio)
    if message:
        session.send_message(chatid=id, message=message)

        # send a funny gif
        #session.send_gif(chatid=id, gifname="")

        # send a funny song
        #session.send_song(chatid=id, songname="")

        # send instagram or other socials like facebook, phone number, and snapchat
        #session.send_socials(chatid=id, media=Socials.INSTAGRAM, value="Fredjemees")

        # you can also unmatch
        #session.unmatch(chatid=id)

    #let's scrape some geomatches now
# for _ in range(5):
#     # get profile data (name, age, bio, images, ...)
#     geomatch = session.get_geomatch(quickload=False)
#     # store this data locally as json with reference to their respective (locally stored) images
#     session.store_local(geomatch)
#     # dislike the profile, so it will show us the next geomatch (since we got infinite amount of dislikes anyway)
#     name = geomatch.get_name()
#     age = geomatch.get_age()
#     work = geomatch.get_work()
#     study = geomatch.get_study()
#     home = geomatch.get_home()
#     gender = geomatch.get_gender()
#     bio = geomatch.get_bio()
#     distance = geomatch.get_distance()
#     passions = geomatch.get_passions()
#     image_urls = geomatch.image_urls
    
#     print(f"Name: {name}")
#     print(f"Age: {age}")
#     print(f"Work: {work}")
#     print(f"Study: {study}")
#     print(f"Home: {home}")
#     print(f"Gender: {gender}")
#     print(f"Bio: {bio}")
#     print(f"Distance: {distance}")
#     print(f"Passions: {passions}")
#     print(f"Image URLs: {image_urls}")


#     session.dislike()
