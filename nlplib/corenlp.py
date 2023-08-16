# from textblob import TextBlob
# import wikipedia


# def search_wikipedia(name):
#     """Search Wikipedia"""
#     print(f"Searching for name: {name}")
#     return wikipedia.search(name)


# def summarize_wikipedia(name):
#     """Summarize Wikipedia"""
#     print(f"Finding wikipedia summary for name: {name}")


# def get_text_blob(text):
#     "Getting text blob object and returns"

#     blob = TextBlob(text)

#     return blob


# def get_phrases(name):
#     """Find wikipedia name and return back phrases"""

#     text = summarize_wikipedia(name)
#     blob = get_text_blob(text)
#     phrases = blob.noun_phrases
#     return phrases


# golden_state_warriors_text = wikipedia.summary("Golden State Warriors")
# # blob.noun_phrases


from textblob import TextBlob
import wikipedia

def search_wikipedia(name):
    """Search Wikipedia"""
    print(f"Searching for name: {name}")
    return wikipedia.search(name)


def summarize_wikipedia(name):
    """Summarize Wikipedia"""
    print(f"Finding wikipedia summary for name: {name}")
    summary = wikipedia.summary(name)
    return summary

def get_text_blob(text):
    "Getting text blob object and returns"

    blob = TextBlob(text)

    return blob



def get_phrases(name):
    """Find Wikipedia summary and return noun phrases"""
    text = summarize_wikipedia(name)
    blob = TextBlob(text)
    phrases = blob.noun_phrases
    return phrases


golden_state_warriors_phrases = get_phrases("Golden State Warriors")
print("Noun phrases extracted from the Wikipedia summary:")
# for phrase in golden_state_warriors_phrases:
#     print(phrase)
