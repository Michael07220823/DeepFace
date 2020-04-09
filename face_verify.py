from deepface import DeepFace

result = DeepFace.verify("face_images/Gates/1.jpg", "face_images/Gates/2.jpg")
print(result)