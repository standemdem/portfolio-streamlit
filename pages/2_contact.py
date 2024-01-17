import streamlit as st

st.markdown(
    """
    Check out my github: [https://github.com/standemdem/](https://github.com/standemdem/)
    """
)


def show():
    st.title("Download File Button")

    # Button to trigger file download
    if st.button("Download File"):
        # Link to the file you want to download
        file_url = "https://docs.google.com/document/d/1YtuSRYQdEetNHZOAY2L5ePslNBOKWNSwudhJrhJs698/edit?usp=sharing"

        # Display link (hidden)
        st.markdown(f"Download [file]({file_url})", unsafe_allow_html=True)

        # Trigger file download using JavaScript
        st.markdown(
            """
            <script>
                const downloadLink = document.createElement("a");
                downloadLink.href = '""" + file_url + """';
                downloadLink.download = 'downloaded_file.txt';
                document.body.appendChild(downloadLink);
                downloadLink.click();
                document.body.removeChild(downloadLink);
            </script>
            """,
            unsafe_allow_html=True
        )
