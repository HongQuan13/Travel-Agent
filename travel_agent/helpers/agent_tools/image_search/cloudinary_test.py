import getpass
import os

# import cloudinary
# import cloudinary.uploader
# from cloudinary.utils import cloudinary_url

# # Configuration
# cloudinary.config(
#     cloud_name="ducz9g7pb",
#     api_key="923794611174869",
#     api_secret="6FPjbrtdahz5ch0HQRwP2KI0nf4",  # Click 'View API Keys' above to copy your API secret
#     secure=True,
# )

# # Upload an image
# upload_result = cloudinary.uploader.upload(
#     "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSlcY06-Ar-SMr3uWTbL7_avJWxZjt4b7oxDWNxQA9fSAramw7Qbzclc3oEZg&s",
#     public_id="samples",
# )
# print(upload_result["secure_url"])

# # Optimize delivery by resizing and applying auto-format and auto-quality
# optimize_url, _ = cloudinary_url("samples", fetch_format="auto", quality="auto")
# print(optimize_url)

# # Transform the image: auto-crop to square aspect_ratio
# auto_crop_url, _ = cloudinary_url(
#     "samples", width=500, height=500, crop="auto", gravity="auto"
# )
# print(auto_crop_url)
