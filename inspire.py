"""
Ken Sanderson
1/18/2016
- My first shot at an Alexa Skill

Inspire -- Provide daily inspiration to lift everyone up.

"""

from __future__ import print_function
from random import randint

inspiration = [
        "Isn't Alyssa the best wife ever?",
        'Wow, Stevie is just so furry!',
        "Trust in me. Rely on me. I will never leave your side. -Alyssa",
        "You will never be alone in your decisions. Whether we agree or disagree on things, I will always work together with you to find a common ground. - Alyssa",
        "We can do anything we put our minds to. -Alyssa",
        "Even when you're tired and can't think rationally, remember that I am probably feeling the same way. Take a deep breath. -Alyssa",
        "I promise to be patient with you and to work through tough times, no matter how stressful they may seem. -Alyssa",
        "Whenever you need a guiding and helping hand, I will always be here for you. -Alyssa",
        "Never go to bed angry, sad, or upset. It will only make things worse. -Alyssa",
        "I am wrong about things too. -Alyssa",
        "I hate fighting with the one person who I want to be closest with. -Alyssa",
        "You are my world, my everything. I'd rather be alone than with anyone else. -Alyssa",
        "Be patient. Even the slightest breath in between words can save us from an explosion. -Alyssa",
        "You brighten up my day just by looking at you. -Alyssa",
        "The best kind of friend is the kind you can sit on a porch swing with, never say a word, then walk away feeling like it was the best conversation that you ever had. This is you, baby! -Alyssa",
        "Trust in the Lord with all your heart and lean not on your own understanding; in all your ways acknowledge him, and he will make your paths straight. Proverbs 3:5-6",
        "A great marriage is not when the perfect couple comes toether. It is when an imperfect couple learns to enjoy their differences. -Dave Meurer",
        "You miss 100% of the shots you don't take. -Wayne Gretzky",
        "Ask, and it will be given to you; seek, and you will find; knock, and it will be opened to you. Matthew 7:7",
        "No one can serve two masters; for either he will hate the one and love the other, or else he will be loyal to the one and despise the other. You cannot serve God and money. Matthew 6:24",
        "Cast all of your anxiety on Him, for He cares for you. First Peter 5:7",
        "For I know the thoughts that I think toward you, says the Lord, thoughts of peace and not of evil, to give you a future and a hope. Jeremiah 29:11",
        "Life is 10% what happens to me and 90% how I react to it. -Charles Swindoll",
        "Jesus said to him, You shall love the Lord your God with all your heart, with all your soul, and with all your mind. This is the first and great commandment. And the second is like it: You shall love your neighbor as yourself. Matthew 22:27-39",

        ]

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Skill's application ID to prevent someone else from configuring a skill that 
    sends requests to this function.
    """
    if (event['session']['application']['applicationId'] !=
             "amzn1.echo-sdk-ams.app.4fe4a004-d42c-418d-82dd-cab81b8d8ada"):
         raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    """ Called when the session starts """

    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "InspireMeIntent":
        return get_inspiration()
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

# --------------- Functions that control the skill's behavior ------------------

def get_inspiration():
    session_attributes = {}
    card_title = 'Inspire - by Ken'
    rand_index = randint(0, len(inspiration)-1)
    speech_output = inspiration[rand_index] 
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))



def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """
    session_attributes = {}
    card_title = 'Inspire - by Ken'
    rand_index = randint(0, len(inspiration)-1)
    speech_output = "Welcome to Ken's Inspire App. " \
                    "Here is today's inspiration. " + inspiration[rand_index]
    reprompt_text = ""
    should_end_session = True
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
