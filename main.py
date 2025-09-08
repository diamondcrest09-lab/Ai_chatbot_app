from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.label import Label
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# === Train AI model ===
texts = ["I love coding", "Python is great", "I enjoy learning AI",
         "I hate bugs", "Coding is hard", "I dislike errors"]
labels = ["positive", "positive", "positive", 
          "negative", "negative", "negative"]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)
model = MultinomialNB()
model.fit(X, labels)

# === App Layout ===
class ChatBotApp(App):
    def build(self):
        self.layout = BoxLayout(orientation="vertical", padding=10, spacing=10)
        
        self.chat_label = Label(text="🤖 AI Chatbot Ready!", size_hint=(1, 0.2))
        self.layout.add_widget(self.chat_label)
        
        self.user_input = TextInput(hint_text="Type your message here", size_hint=(1, 0.2))
        self.layout.add_widget(self.user_input)
        
        self.button = Button(text="Send", size_hint=(1, 0.2))
        self.button.bind(on_press=self.respond)
        self.layout.add_widget(self.button)
        
        return self.layout
    
    def respond(self, instance):
        user_text = self.user_input.text
        if user_text.strip() == "":
            self.chat_label.text = "Chatbot: Please type something!"
            return
        
        X_test = vectorizer.transform([user_text])
        prediction = model.predict(X_test)
        
        if prediction[0] == "positive":
            self.chat_label.text = "Chatbot: That sounds great! 😃"
        else:
            self.chat_label.text = "Chatbot: Oh, I see... don’t give up 💪"

# Run App
ChatBotApp().run()