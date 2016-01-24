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
        "A great marriage is not when the perfect couple comes together. It is when an imperfect couple learns to enjoy their differences. -Dave Meurer",
        "You miss 100% of the shots you don't take. -Wayne Gretzky",
        "Ask, and it will be given to you; seek, and you will find; knock, and it will be opened to you. Matthew 7:7",
        "No one can serve two masters; for either he will hate the one and love the other, or else he will be loyal to the one and despise the other. You cannot serve God and money. Matthew 6:24",
        "Cast all of your anxiety on Him, for He cares for you. First Peter 5:7",
        "For I know the thoughts that I think toward you, says the Lord, thoughts of peace and not of evil, to give you a future and a hope. Jeremiah 29:11",
        "Life is 10% what happens to me and 90% how I react to it. -Charles Swindoll",
        "Jesus said to him, You shall love the Lord your God with all your heart, with all your soul, and with all your mind. This is the first and great commandment. And the second is like it: You shall love your neighbor as yourself. Matthew 22:27-39",
        "",
        "Argue naked - And it won't last long...",
        "What then shall we say in response to this? If God is for us, who can be against us? -Romans 8:31",
        "Health is the greatest gift, contentment the greatest wealth, faithfulness the best relationship. -Buddha",
        "Love the Lord your God with all your heart and with all your sould and with all your mind and with all your strength. -Mark 12:30",
        "And now these three remain: faith, hope, and love. But the greatest of these is love. -First Corinthians 13:13",
        "If you're along, I'll be your shadow. If you want to cry, I'll be your shoulder. If you want a hug, I'll be your pillow. If you need to be happy, I'll be your smile. But anytime you need a friend, I'll just be me",
        "I don't regret the things I've done, I regre the things I didn't do when I had the chance.",
        "Challenges are what make life interesting and overcoming them is what makes life meaningful. -Joshua Marine",
        "Friendship isn't about whom you have known the longest. It's about who came, and left your side",
        "Everyone hears what you say. Friends listen to what you say. Best friends listen to what you don't say.",
        "Husbands are like the best bra you've ever had. Supportive, hard to find, and always close to your heart.",
        "The people who influence you are the people who believe in you. -Henry Drummond",
        "It is during our darkest moments that we must focus to see the light. -Aristotle Onassis",
        "You can never cross the ocean until you have the courage to lose sight of the shore. -Columbus",
        "A true friend sees the first tear, catches the second, and stops the third. -Angelique",
        "I pray that, out of His glorious riches, he may strengthen you with power through his Spirit in your inner being. -Ephesians 3:16",
        "One of the most important keys to success is having the discipline to do what you know you should do, even when you don't feel like doing it.",
        "There is no fear in love. But perfect love drives out fear, because fear has to do with punishment. The one who fears is not made perfect in love. We love because He firts loved us. -First John 4:18-19",
        "But love your enemies, do good to them and lend to them without expecting to get anything back. Then your reward will be great, and you will be sons of the Most High, because He is kind to the ungrateful and wicked. -Luke 6:35",
        "You can't fall if you don't climb. But there's no joy in living your whole life on the ground.",
        "For God so loved the world that He gave His one and only Son, that whosoever believes in Him shall not perish but have eternal life. -John 3:16",
        "For God did not give us a spirit of timidity, but a spirit of power, of love, and of self-discipline. -Second Timothy 1:7",
        "When two people really care about each other, they always find a way to make it work. No matter how hard it is.",
        "There are two ways of spreading light; to be the candle or the mirror that reflects it. -Edith Wharton",
        "There comes a point in your life when you realize who really matters, who never did, and who always will.",
        "But the fruit of the Spirit is love, joy, peace, longsuffering, kindness, goodness, faithfulness, gentleness, and self-control. Against such there is no law. -Galatians 5:22-23",
        "Be strong and courageous. Do not be afraid or terrified because of them, for the Lord your God goes with you; He will never leave you nor forsake you. Deuteronomy 31:6",
        "Peace I leave with you; my peace I give you. I do not give to you as the world gives. Do not let your hearts be troubled and do not be afraid. -John 14:27",
        "But those who wait on the Lord will renew their strength; they will soar on wings like eagles, they will run and nt grow weary, they will walk and not faint. -Isaiah 40:31",
        "Deep calls to deep at the noise of Your waterfalls; All your waves and billows have gone over me. -Psalm 42:7",
        "Go where you are celebrated, not tolerated. If they can't see the real value of you, it's time for a new start.",
        "A relationship with no arguments is a relationship with a lot of secrets.",
        "A friend is someone who knows the song in your heart and can sing it back to you when you have forgotten the words.",
        "The most beautifl discovery true friends make is that they can grow separately without growing apart.",
        "When you compromise your beliefs for the sake of gain, that is a lack of integrity. When you compromise your beliefs for the sake of greater understanding with your spouse, that's called wisdom.",
        "Husbands, love your wives, just as Christ loved the Church and gave Himself up for her. -Ephesians 5:25",
        "You know you're in love when you can't fall asleep because reality is finally better than your dreams. -Dr. Seuss",
        "I have set the Lord always before me. Because He is at my right hand, I will not be shaken. -Psalm 16:8",
        "If you do what you've always done, you'll get what you've always gotten. -Tony Robbins",
        "Sometimes couples have to argue not to prove who's right or wrong, but to be reminded that their love is worth fighting for.",
        "Love is that condition in which the happiness of another person is essential to your own -Robert Heinlein",
        "Do to others as you would have them do to you. -Luke 6:31",
        "Rejoicing in hope, patient in trials, continuing steadfastly in prayer. -Romans 12:12",
        "Dear friends, let us love one another, for love comes from God. Everyone who loves has been born of God and knows God. -First John 4:7",
        "The most difficult thing is the decision to act, the rest is merely tenacity. -Amelia Earhart",
        "There is no greater happiness for a man than approaching a door at the end of a day knowning someone on the other side of that door is waiting for the sound of his footsteps. -Ronald Reagan",
        "So do not fear, for I am with you; do not be dismayed, for I am your God. I will strengthen you and help you; I will uphold you with my righteous right hand. -Isaiah 41:10",
        "When you say, It's hard, it actually means, I'm not strong enough to fight for it. Stop saying it's hard. Think positively!",
        "Do not make friends with a hot-tempered man, do not associate with one easily angered, or you may learn his ways and get yourself ensnared. -Proverbs 13:20",
        "If you want to conquer fear, don't sit home and think about it. Go out and get busy. -Dale Carnegie",
        "What's money? A man is a success if he gets up in the morning and goes to bed at night and in between does what he wants to do. -Bob Dylan",
        "You are my refuge and my shield; I have put my hope in your word. Away from me, you evil doers, that I may keep the commands of my God! -Psalm 119:114-115",
        "I didn't fail the test. I just foun 100 ways to do it wrong. -Benjamin Franklin",
        "Limitations live only in our minds. But if we use our imaginations, our possibilities become endless. -Jamie Paolinetti",
        "A successful marriage requires falling in love many times, always with the same person. -Mignon McLaughlin",
        "Either you run the day, or the day runs you. -Jim Rohn",
        "Our lives begin to end the day we come silent about things that matter. -Martin Luther King Junior",
        "Laughter is often the best medicine and can be a quick remedy for many arguments.",
        "When you look at a person, any person, remmber that everyone has a story. Everyone has gone through something that has changed them.",
        "A friend is someone who can see the truth and pain in you even when you are fooling everyone else.",
        "I can do all things through Him who strengthens me. -Philippians 4:13",
        "Every copule needs to argue now and then. Just to prove the relationship is strong enough to survive. -Nicholas Sparks",
        "You've gotta dance like there's nobody watching, love like you'll never be hurt, sing like there's nobody listening, and live like it's heaven on earth. -William Purkey",
        "Life is not measured by the number of breaths we take, but by the moments that take our breath away. -Maya Angelou",
        "A truly rich man is one whose children run into his arms when his hands are empty.",
        "The most common way people give up their power is by thinking they don't have any. -Alice Walker",
        "The difference between an ordinary marriage and an extraordinary marriage is in giving just a little extra every day, as often as possible, for as long as we both shall live. -Fawn Weaver",
        "I've learned that people will forget what you said, people will forget what you did, but people will never forget how you made them feel. -Maya Angelou",
        "However, each one of you also must love his wife as he loves himself, and the wife must respect her husband. -Ephesians 5:33",
        "Be completely humble and gentle; be patient, bearing with one another in love. -Ephesians 4:2",
        "Whatever the mind of man can conceive and believe, it can achieve. -Napoleon Hill",
        "Strive not to be a success, but rather to be of value. -Albert Einstein",
        "People who are too weak to follow their own dreams, will alwyas find a way to discourage yours.",
        "One of the most amazing gifts in life is to find someone who knows all your flaws, differences, and mistakes, yet still loves everything about you.",
        "There comes a time when you have to stop crossing oceans for people who wouldn't even jump puddles for you.",
        "Nothing is impossible, the word itself says, I'm possible! -Audrey Hepburn",
        "The two most importatn days in your life are the day you are born and the day you find out why. -Mark Twain",
        "If you look at what you have in life, you'll always have more. If you look at what you don't have in life, you'll never have enough. -Oprah",
        "For in the gospel a righteousness from God is revealed, a righteousness that is by faith from first to last, just as it is written: The righteous will live by faith. -Romans 1:17",
        "Knowing is not enough, we must apply. Willing is not enough, we must do.",
        #"",
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
