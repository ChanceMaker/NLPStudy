# reddit-text-classification
# Introduction
This project evaluates two classification problems of Subreddit prediction and Discourse prediction of Reddit data. This read me gives a description, development and reasoning behind the solutions. 

# Requirements
- JupyterNotebook or run on Google Colab
- python 3.5+



### Selected Features
#### Feature 1: Metadata, Subreddit with Author
The property of author combined with the subreddit - thread['subreddit'] + "," +  post.get('author', "")-can give valuable underlying information. This could give a pattern of repeat authors in subreddit, indicating what kind of post they usually participate in. For example, if it’s a gaming subreddit, there is more change of reactionary posts, but if they are linked with a subreddit such as ‘relationship’, the posts tend to be answers or elaborations.
#### Feature 2: Content and Punctuation, Tokenizer that keeps punctuation
As described during the error analysis(question 3.ii), the use of punctuation is pivotal to recognize the different sentiment that echo classes that might be ignored in a tokenizer that removes punctuation. This feature plays an important role to recognize different discourse types such as ‘negativereaction’, ‘humor’, ‘questions’, and even ‘appreciation’. In this implementation, the tokenizer takes a string input and passes it onto the normalization function that has a token.is_punct check to keep the punctuation, and returns a tokenized string. 
#### Feature 3: Structure, Post depth and length
For the implementation of the post depth, the ‘post_depth’ was classified into three subcategories, as described in the following table, during the preprocessing stage. This was done to differ between a deeper post, mid-level post, and the first post. A deeper post may contain different discourses such as ‘agreement’, ‘disagreement’, ‘elaborations’, ‘appreciation’, and an ‘answer’. 
Body length, ‘body_length’ is another is another attribute that is subcategorized. This gives information of a post and its underlying meaning. For instance, a shorter post may mean that it is of ‘humor’ or ‘reaction’ discourse types, likewise, a longer post may correlate with an ‘elaboration’ or an ‘answer’. It was also implemented in the preprocessing stage into categories show below.
#### Feature 4: Author, Same current author as the author of the initial post
If the top author of a thread is the same as one of the authors of the body posts, it indicates that the author is engaged in a conversation. It could be a further question, a positive or negative reaction, or even an appreciation. Therefore, it is an important feature to implement. To check if it’s the same author, there is a check for self_loop first, if the thread is a self loop, then thread[‘top_author’] is compared to the first author of the thread - thread['posts'][0].get('author',""). 
#### Feature 5: Thread Features, Total comments
Total comments (len(thread[‘posts’]) of a thread plays a pivotal role to classify a discourse type. More comments indicate more ‘answers’, ‘agreements’, ‘elaboration’, ‘disagreements’, and could even mean deeper conversations. On the other hand, a smaller conversation may mean less detailed content and more reactionary posts. To add total comments as an integer into the pipeline, a one line wrapper class was created that returns the reshaped ‘total_comments’ column.
#### Feature 6: Community, Subreddit
One of the most imperative features the subreddit(thread[‘subreddit’]). Each subreddit contains different type of topics, language, and engagement. For instance, a certain subreddit such as ‘movies’ might have many different types of discourse, a thread could contain a movie spoiler, to which there could be many negative and positive reactions, humor, disagreements, agreements, so on. 



