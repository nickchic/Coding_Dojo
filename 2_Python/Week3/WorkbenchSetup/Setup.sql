USE twitter;

--
-- handle and tweets for Allen Iverson
--

SELECT users.handle, tweets.tweet 
FROM users
LEFT JOIN tweets 
ON users.id = tweets.user_id
WHERE user_id = 3;

--
-- Kobe's tweets that Carter favorited
--
SELECT tweets.tweet as 'Carter faved Kobe'
FROM tweets
LEFT JOIN faves
ON tweets.id = faves.tweet_id
WHERE faves.user_id = 2 and tweets.user_id = 1;

