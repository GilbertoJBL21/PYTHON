# CHATBOT USING NLTK AND TENSORFLOW🤖
This is a simple chatbot created using natural language processing (nlp) tools from the nltk library and tensorflow. the chatbot is capable of recognizing user input and providing appropriate responses based on pre-defined intents.

**(Table of Contents)**

[TOC]

## Installation
To use this chatbot, you need to have Python 3 and the following libraries installed:
- nltk
- tflearn
- tensorflow
- numpy
- json
- pickle
- discord
- Tkinter

You can install these libraries using pip:
`pip install nltk tflearn tensorflow numpy json pickle discord`

## Usage
1.Clone this repository to your local machine.

2.Download the required NLTK packages by opening a Python console and running the following commands:

    import nltk
    nltk.download('punkt')
    nltk.download('wordnet').
3.Create a file named intents.json with the following format:

    {
      "intents": [
        {
          "tag": "greeting",
          "patterns": [
            "Hi",
            "Hello",
            "Hey",
            "What's up"
          ],
          "responses": [
            "Hello!",
            "Hi there!",
            "Greetings!",
            "Hey!"
          ]
        },
        {
          "tag": "goodbye",
          "patterns": [
            "Goodbye",
            "See you later",
            "Bye",
            "Later"
          ],
          "responses": [
            "Goodbye!",
            "See you later!",
            "Bye!",
            "Later!"
          ]
        }
      ]
    }
This file defines the intents of the chatbot, containing tags, patterns, and responses.

4.Run the first file to train the chatbot:
```python
  python training.py
```
5.Before going to the next step you need to install the Tkinter package
```python
pip install tk
```
6.Now that you have installed the tkinter package, run the main.py file to see if the chatbot answers your questions correctly:
```python
python trainig.py
```
7.You need to run the main.py file to see if the chatbot responds to you correctly:
```python
python main.py
```
8.You will need to create a discord account and create a server, then go to the discord developer portal and log in with your account then create an application and create a bot then in the link  https://discordapp.com/oauth2/authorize?client_id=--hereyourclient--&scope=bot&permissions=0 on this page paste your client id of your chatbot with this you are already adding your chatbot to the server.

9.Now open the bot.py file and add your Discord bot token to the TOKEN variable in the code.

10.Now if you can finally run your bot.py file and talk to your chatbot:
```python
python bot.py
```
## Functionality
The chatbot uses NLTK to preprocess user input and extract key words from the input. These words are then used to predict the appropriate intent based on the pre-defined intents in the intents.json file. Once the intent is predicted, the chatbot selects a response from the appropriate intent and sends it back to the user.

The chatbot uses a neural network with three fully connected layers to predict the intent from the input. The network is trained using the training data from the intents.json file.

## Future Improvements
Add more training data to improve the accuracy of the model.
Allow for more complex user input, such as multiple intents in a single message.
Use a more advanced neural network architecture for better accuracy.
## Customization
You can customize the chatbot's responses by editing the intents.json file. This file contains a list of intents and their associated patterns and responses. You can add, remove, or modify intents and their associated patterns and responses to make the chatbot more relevant to your use case.
## Credits
This chatbot was created by Gilberto J. Barrios López as a demonstration of natural language processing and neural networks. It is based on the following technologies:
- [Python](https://www.python.org/ "Python")
- [NLTK](https://www.nltk.org/ "NLTK")
- [TFLearn](http://tflearn.org/ "TFLearn")
- [TensorFlow](https://www.tensorflow.org/?hl=es-419 "TensorFlow")
- [Discord](https://discord.com/developers/docs/intro "Discord")
- [NumPy](https://numpy.org/ "NumPy")
- [JSON](https://www.json.org/json-es.html "JSON")
- [Pickle](https://docs.python.org/3/library/pickle.html#:~:text=%E2%80%9CPickling%E2%80%9D%20is%20the%20process%20whereby,back%20into%20an%20object%20hierarchy. "Pickle")
