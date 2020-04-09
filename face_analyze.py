from deepface import DeepFace

demography = DeepFace.analyze("face_images/Gates/1.jpg")

print("Age: ", demography["age"])
print("Gender: ", demography["gender"])
print("Emotion: ", demography["dominant_emotion"])
print("Race: ", demography["dominant_race"])
# print(demography)