#Task 1 Language Translation Tool

from googletrans import Translator

print("Welcome to Language Translation Tool!")

translator = Translator()

# Languages codes are attached iver here 
print("Available languages: en (English), ur (Urdu), fr (French), es (Spanish), de (German)")

source_lang = input("Enter source language code: ")
target_lang = input("Enter target language code: ")
text_to_translate = input("Enter text you want to translate: ")

# We are going to translate our text via it...
result = translator.translate(text_to_translate, src=source_lang, dest=target_lang)

print("Translated text: " + result.text)

# save it or not user choise
copy_option = input("Do you want to copy the translated text to a file? (yes/no): ")
if copy_option == "yes":
    file = open("translated.txt", "w")
    file.write(result.text)
    file.close()
    print("Text saved to translated.txt")



# Task 2 Chatbot for FAQs
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')

print("Welcome to FAQ Chatbot!")

# Hardcoded Questions 
questions = [
    "What is your return policy?",
    "How can I track my order?",
    "What payment methods do you accept?",
    "Do you ship internationally?",
    "How do I contact customer support?"
]

answers = [
    "Our return policy allows returns within 30 days of purchase.",
    "You can track your order using the tracking number sent to your email.",
    "We accept credit cards, debit cards, and PayPal.",
    "Yes, we ship to many countries around the world.",
    "You can contact our customer support via email or phone."
]

# Processing layer 
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    user_vector = vectorizer.transform([user_input])

    similarities = cosine_similarity(user_vector, question_vectors)

    index = similarities.argmax()
    best_score = similarities[0][index]

    # User will get answer based on his matching score with question
    if best_score > 0.2: 
        print("Bot:", answers[index])
    else:
        print("Bot: Sorry, I don't understand your question.")


# Task 4 Object Detection and Tracking

from ultralytics import YOLO
import cv2

print("Welcome to Object Detection and Tracking Task!")

model = YOLO("yolov8n.pt")

print("\nChoose an option:")
print("1. Use webcam to detect and track objects")
print("2. Detect objects in existing images")

choice = input("Enter your choice (1 or 2): ")

if choice == "1":
    print("Starting webcam...")
    cap = cv2.VideoCapture(0)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        results = model.track(frame, persist=True)

        annotated_frame = results[0].plot()

        cv2.imshow("Webcam Object Detection & Tracking", annotated_frame)

        # Stop if user presses 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

elif choice == "2":
    print("Detecting objects in images...")

    # List of images to process
    images = ["Myimage.jpg", "Myimage2.jpg"]

    for img_path in images:
        print(f"Processing {img_path}")
        results = model.predict(source=img_path, save=True)

    print("Detection done! Check the 'runs/detect' folder for results.")

else:
    print("Invalid choice. Please run the program again and choose 1 or 2.")
