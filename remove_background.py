import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("Background Remover")

# Allow the user to upload an image
uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    try:
        # Open the uploaded image
        image = Image.open(uploaded_file)

        # Remove the background
        st.text("Processing... Please wait.")
        output = remove(image)

        # Create a BytesIO buffer and save the output image to it
        with io.BytesIO() as buffer:
            output.save(buffer, format="PNG")
            buffer.seek(0)

            # Display the original and processed images
            st.subheader("Original Image")
            st.image(image, use_column_width=True)

            st.subheader("Image with Background Removed")
            st.image(output, use_column_width=True)

            # Provide a download link for the processed image
            st.download_button(
                label="Download Image with Background Removed",
                data=buffer,
                file_name=f"{uploaded_file.name}_removed_bg.png",
                mime="image/png"
            )

            st.success("Image processed successfully!")

    except Exception as e:
        st.error(f"Error processing image: {e}")
