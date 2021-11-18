import streamlit as st
st.title("Get some Streamlit magic!")

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
    st.image("https://i.pinimg.com/originals/68/8e/9e/688e9eb45c2f5cc82361d5c305ccc0ca.gif")
    st.header("Congratulations! What magic do you want:")

    user_said = st.text_input("I want to...")
    if user_said == "fly":
        st.header("Yay! You can fly!!!")
        st.image("https://64.media.tumblr.com/a9111782557ab9e1d5250f67997d235f/tumblr_mtxrkvvm0J1s04rsio1_400.gif")
    elif user_said == "":
        pass
    elif user_said == "live forever":
        st.header("Great choice! This is how you will look in 100 years...")
        st.image("https://media4.giphy.com/media/idMsVB8Xva2kjm0FLS/giphy.gif")
    else:
        st.header(f"We're very sorry... {user_said} is currently unavailable.")
        st.image("https://64.media.tumblr.com/16c8b1524422f21fbc3ee39a747a3fc2/tumblr_o3g4d4XzHF1u4rl68o1_500.gifv")
        st.write("Please have a coffee break ☕ and try again!")

    if user_said == "fly" or user_said == "live forever":
        finish = st.download_button("Now, download your magic!", data = "Here is your magic!", file_name = "Your magic is here!")
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
