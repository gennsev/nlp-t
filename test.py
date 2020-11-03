import preprocess


example_text1 = "I'm happy to test this neew library!! Check:http://gennsev.com"
example_text2 = "<div> Not COVID again 😔 #badbadvirus </div>"


print(preprocess.remove_url(example_text1))
print(preprocess.remove_punct(example_text1))
print(preprocess.decontract(example_text1))
print(preprocess.remove_stopwords(preprocess.decontract(example_text1)))
print(preprocess.correct_spelling(example_text1))


print(preprocess.remove_emoji(example_text2))
print(preprocess.remove_html(example_text2))
print(preprocess.split_attached_words(example_text2))