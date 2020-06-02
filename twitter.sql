CREATE TABLE tweets (
	id_str			BIGINT	PRIMARY KEY,
	id 				BIGINT,
	screen_name VARCHAR(100),
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


CREATE TABLE hashtag (
	tweet_id 		BIGINT,
	text			VARCHAR(1200),

	FOREIGN KEY (tweet_id)
	REFERENCES tweets (id_str) ON UPDATE CASCADE ON DELETE CASCADE
);


CREATE TABLE experts (
	twitter_id	VARCHAR(100) PRIMARY KEY
	since_id BIGINT
);

CREATE TABLE keywords (
	keyword		VARCHAR(100) PRIMARY KEY,
	category	VARCHAR(100)
);

