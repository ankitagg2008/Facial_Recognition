import os
import streamlit as st
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        # Display the frame in the Streamlit app
        st.image(frame)

        # Save the frame to a folder
        save_path = st.session_state.get("save_path")
        if save_path:
            frame.save(save_path, format="JPEG")

        return frame

def main():
    st.title("Dataset Recorder")
    st.write("Enter your Banner ID and Name:")
    banner_id = st.text_input("Banner ID")
    name = st.text_input("Name")

    # Initialize the save path
    save_path = st.session_state.get("save_path")

    # Display webcam streamer
    webrtc_ctx = webrtc_streamer(key="example", video_processor_factory=VideoTransformer, sendback_audio=False)

    if st.button("Record Dataset"):
        if banner_id and name:
            folder_name = f"{banner_id}_{name}"
            if not os.path.exists(folder_name):
                os.makedirs(folder_name)
            save_path = os.path.join(folder_name, "frame.jpg")
            st.session_state["save_path"] = save_path
        else:
            st.write("Please enter your Banner ID and Name.")

    if save_path:
        st.write("Dataset recording in progress...")
    else:
        st.write("Click 'Record Dataset' to start recording.")

if __name__ == "__main__":
    main()
