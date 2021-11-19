import streamlit as st
st.title("Get some magic into your life!")

if 'magic_click' not in st.session_state:
    st.session_state.magic_click = None

if st.session_state.magic_click is None:
    button_clicked = st.button ("Click for magic ✨")
    if button_clicked:
        st.session_state.magic_click = True
        st.experimental_rerun()
# click = st.button("Click for magic ✨")
# if click:
#     st.image("https://i.pinimg.com/originals/68/8e/9e/688e9eb45c2f5cc82361d5c305ccc0ca.gif")
#
# pick = st.radio("Choose your magic",["I want to fly","Making dinner instantly","Sleep forever"])
# st.write("You chose",pick)
#
# select = st.checkbox("I want all the magic in the world")
if st.session_state.magic_click:
    st.image("https://i.pinimg.com/originals/68/8e/9e/688e9eb45c2f5cc82361d5c305ccc0ca.gif", caption = 'Sparkles GIF by Cliply')
    st.header("Woohoo! What magic do you want?")

    user_said = st.text_input("I want to...")
    if user_said == "fly":
        st.header("You got it! Now you can fly!!!")
        st.image("https://media3.giphy.com/media/l0HlTvwNTvPpJVQNG/giphy.gif", caption='Crash Falling GIF by Nikki Desautelle on Giphy')
    elif user_said == "":
        pass
    elif user_said == "time travel":
        st.header("Wow! You can see your younger self!")
        st.image("https://media2.giphy.com/media/RW9dleey6rACDCBbkD/giphy.gif", caption='Illustration Hello GIF by jojofalkillustration on Giphy')
    elif user_said == "live forever":
        st.header("Great choice! This is how you'll look in 100 years...")
        st.image("https://media4.giphy.com/media/idMsVB8Xva2kjm0FLS/giphy.gif", caption='Head Skull GIF by GIFTHEMHELL on Giphy')
    else:
        st.header(f"We're very sorry... {user_said} was so popular, it sold out and is currently unavailable. Goodbye!")
        st.image("https://media3.giphy.com/media/MSCVGndNcdQWI/giphy.gif", caption='Cat GIF by Giphy')
        st.write("On second thought...please have a coffee break ☕ and try again! Refresh this magical app to do so.")

    if user_said == "fly" or user_said == "live forever":
        finish = st.download_button("Click to download your magic! 🪄", data = "Hi Magic Seeker! Thank you for downloading your magic. To make your magic come true, close your eyes and turn until you feel dizzy. When you feel dizzy, lie down and take a nap. Better yet, eat a cookie 🍪 before taking a nap! After you wake up, cancel all meetings, leave at home your computer and your phone, and go outside for the rest of the day. When you come back, eats lots of yummy food and sleep for a very long time. Don't set the alarm. Wake up the next day naturally. Now, sit up and ask yourself one question. How do you feel? You feel magically reborn, do you not? We thought so! It feels like you can do anything, right? It feels like you can fly! It feels like you can live forever! It feels like you can do time travel! There you go! That's your magic! We're very happy that you're happy with your purchase. Please send us lots of balloons 🎈, and pass on your magic to someone else. We're looking forward to hearing your very own stories of magic!", file_name = "Your magic is here! 💫")
        if finish:
            st.session_state.magic_click = None
            st.experimental_rerun()


    # if 'user_said' not in st.session_state:
    #     st.session_state.magic_choice = None
    #
    # if st.session_state.magic_choice is None:
    #     choice_clicked = st.radio ("Choose your magic",["I want to fly","I want my food to cook itself","I want to sleep forever"])
    #     if choice_clicked:
    #         st.session_state.magic_choice = True
    #         st.experimental_rerun()


# st.write("You chose",pick)
