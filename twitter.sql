CREATE TABLE tweets (
	id_str			BIGINT	PRIMARY KEY,
	id 				BIGINT,
	created_at 		TIMESTAMP,
	text			VARCHAR(500),
	source 			VARCHAR(1000),
	truncated		BOOLEAN,
	in_reply_to_status_id	BIGINT,
	in_reply_to_user_id		BIGINT,
	in_reply_to_screen_name	VARCHAR(1000),
	quoted_status_id		BIGINT,
	is_quote_status			BOOLEAN,
	quote_count		INT,
	reply_count		INT,
	retweet_count 	INT,
	favorite_count	INT,
	favorited		BOOLEAN,
	retweeted		BOOLEAN,
	lang			VARCHAR(10),
	retweeted_status_id		BIGINT,
	search_stamp		TIMESTAMP
	);

CREATE TABLE users (
	tweet_id		BIGINT,
	id				BIGINT,
	id_str			BIGINT,
	name			VARCHAR(100),
	screen_name		VARCHAR(100),
	location		VARCHAR(1000),
	url				TEXT,
	description		VARCHAR(1000),
	verified		BOOLEAN,
	followers_count	INT,
	friends_count	INT,
	listed_count	INT,
	favourites_count		INT,
	statuses_count	INT,
	created_at		TIMESTAMP,


	FOREIGN KEY (tweet_id)
	REFERENCES tweets (id_str) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE hashtag (
	tweet_id 		BIGINT,
	text			VARCHAR(1200),

	FOREIGN KEY (tweet_id)
	REFERENCES tweets (id_str) ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE experts (
	twitter_id	VARCHAR(100) PRIMARY KEY
);

CREATE TABLE keywords (
	keyword		VARCHAR(100) PRIMARY KEY,
	category	VARCHAR(100)
);

