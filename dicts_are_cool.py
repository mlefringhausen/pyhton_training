# Here's the raw data, since the article only provides a graphic.
USAGE = {
    'JavaScript': 57.4,
    'Java': 47.3,
    'SQL': 47.1,
    'C#': 30.9,
    'Python': 30.7,
    'PHP': 30.4,
    'C++': 22.3,
    'TypeScript': 9.6,
    'Ruby': 8.0,
    'Swift': 6.4,
    'Assembly': 5.9,
    'Objective-C': 5.9,
    'Perl': 5.0,
    'VBA': 5.0,
    'R': 4.9,
    'Matlab': 4.7,
    'Go': 4.4,
    'VB.NET': 4.2,
    'Lua': 4.0,
    'Groovy': 3.9,
    'Scala': 3.8,
    'CoffeeScript': 3.2,
    'Haskell': 2.6,
    'Visual Basic 6': 2.3
}

POPULARITY = {
    'JavaScript': 41.3,
    'Python': 32.7,
    'Java': 31.4,
    'SQL': 30.5,
    'C#': 27.3,
    'C++': 26.8,
    'PHP': 16.2,
    'TypeScript': 15.4,
    'C': 15.4,
    'Go': 15.2,
    'Swift': 11.1,
    'Rust': 10.8,
    'Scala': 8.8,
    'Ruby': 8.6,
    'Haskell': 6.6,
    'R': 5.9,
    'Assembly': 5.5,
    'Elixir': 4.0,
    'F#': 4.0,
    'Lua': 3.7,
    'Objective-C': 3.4,
    'Perl': 3.3,
    'Erlang': 2.9,
    'Groovy': 2.9,
    'CoffeeScript': 2.8
}

# Exercise 1: Calculate the relative popularity for all languages.
# E.g. for Javascript, the relative popularity is
#print POPULARITY['JavaScript'] / USAGE['JavaScript']

# Note: Some languages appear only in USAGE but not in POPULARITY, or vice versa.
#       Use the "in" operation to check for availability. Ignore those languages
#       where data is unavailable

def get_relative_popularity():
    RELPOP = dict()
    for language, lang_popularity in POPULARITY.items():
        if language in USAGE:
            pop = POPULARITY[language] / USAGE[language]
            RELPOP[language] = pop
    return RELPOP


# Should print a dict like {'JavaScript': 0.7195, 'Java':....}
print get_relative_popularity()

# Exercise 2: Find the most popular and the least popular
#             programming language, as calculated in excercise 1.
best_value = -1
best_lang = ''
worst_value = 99999
worst_lang = ''
for key, value in get_relative_popularity().iteritems():
    if value > best_value:
        best_value = value
        best_lang = key
    elif value < worst_value:
        worst_value = value
        worst_lang = key
print best_value, best_lang, worst_value, worst_lang

# Exercise 3: Print all programming languages, sorted by popularity.
for key, value in sorted(get_relative_popularity().iteritems(), key=lambda (k,v): v):
    print key, value