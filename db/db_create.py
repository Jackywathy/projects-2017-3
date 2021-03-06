from os import path
import sqlite3

DB_FILE = path.realpath(path.join(path.dirname(path.realpath(__file__)),'../db.db'))

with sqlite3.connect(DB_FILE) as conn:
    cur = conn.cursor()

    # Drop tables if they exist
    cur.execute('DROP TABLE IF EXISTS comments')
    cur.execute('DROP TABLE IF EXISTS photos')
    cur.execute('DROP TABLE IF EXISTS posts')
    cur.execute('DROP TABLE IF EXISTS users')

    # Create the `users` table
    cur.execute(
    '''
    CREATE TABLE users
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    nickname TEXT,
    email TEXT NOT NULL,
    gender TEXT,
    dob TEXT,
    bio TEXT,
    picture TEXT,
    creation_date TEXT)
    '''
    )

    # Create the `posts` table
    cur.execute(
    '''
    CREATE TABLE posts
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    description TEXT,
    title TEXT NOT NULL,
    post_date TEXT NOT NULL,
    file TEXT NOT NULL,
    FOREIGN KEY(user_id) REFERENCES users(id))
    '''
    )

    # Create the comments table
    cur.execute(
    '''
    CREATE TABLE comments
    (id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    post_id INTEGER NOT NULL,
    parent_id INTEGER,
    text TEXT NOT NULL,
    date TEXT NOT NULL,
	loc_latitude REAL,
	loc_longitude REAL,
    score INTEGER,
    FOREIGN KEY(parent_id) REFERENCES comments(id),
    FOREIGN KEY(user_id) REFERENCES users(id),
    FOREIGN KEY(post_id) REFERENCES posts(id))
    '''
    )
    conn.commit()


    # ---- Populate the database with dummy data

    # Create dummy users
    cur.execute(
    '''
    INSERT INTO users VALUES
    (NULL, 'george', '15a6aea1009a94bfb97901572724cf3e6c77c5bb22e6835d61fdd865cfcdfc1773e287f9df6e6e061244dffa475cfd0ce8033cf386039993a063249a25d2482a', 'G', 'some@email.com', 'Male', '01/01/2000', 'I''m a cool kid.', '', '11/1/2017'),
    (NULL, 'tim', '15a6aea1009a94bfb97901572724cf3e6c77c5bb22e6835d61fdd865cfcdfc1773e287f9df6e6e061244dffa475cfd0ce8033cf386039993a063249a25d2482a', 'TimmyD', 'some@email.com', 'Male', '01/01/1990', 'Only tutor who knows what a Finite State Automata is :\).', '', '07/1/2017'),
    (NULL, 'will', '15a6aea1009a94bfb97901572724cf3e6c77c5bb22e6835d61fdd865cfcdfc1773e287f9df6e6e061244dffa475cfd0ce8033cf386039993a063249a25d2482a', '', 'some@email.com', 'Male', '01/01/1993', 'Full Full-stack developer', '', '07/1/2017'),
    (NULL, 'steph',	'15a6aea1009a94bfb97901572724cf3e6c77c5bb22e6835d61fdd865cfcdfc1773e287f9df6e6e061244dffa475cfd0ce8033cf386039993a063249a25d2482a', 'Stiff', 'some@email.com', 'Female', '01/01/2000', 'New Zealand is the best country', '', '08/01/2016'),
    (NULL, 'evan', '15a6aea1009a94bfb97901572724cf3e6c77c5bb22e6835d61fdd865cfcdfc1773e287f9df6e6e061244dffa475cfd0ce8033cf386039993a063249a25d2482a', 'CompSci', 'some@email.com', 'Male',	'01/01/1995', 'Computer Science is obviously the best subject', '', '08/01/2016'),
    (NULL, 'liam', '15a6aea1009a94bfb97901572724cf3e6c77c5bb22e6835d61fdd865cfcdfc1773e287f9df6e6e061244dffa475cfd0ce8033cf386039993a063249a25d2482a', '', 'some@email.com', 'Male', '01/01/1995', 'Don''t scare me please :O', '', '08/01/2017'),
    (NULL, 'james', '15a6aea1009a94bfb97901572724cf3e6c77c5bb22e6835d61fdd865cfcdfc1773e287f9df6e6e061244dffa475cfd0ce8033cf386039993a063249a25d2482a', 'God', 'some@email.com', 'Male', '01/01/1989', 'God to NCSS students. I read stories to children for a living. I lost my hat :\(', '', '08/01/2016'),
    (NULL, 'luke', '15a6aea1009a94bfb97901572724cf3e6c77c5bb22e6835d61fdd865cfcdfc1773e287f9df6e6e061244dffa475cfd0ce8033cf386039993a063249a25d2482a', 'GitOut', 'some@email.com', 'Male', '01/01/1999', 'Git King. Git Kraken. Git Merge without mr merge monkey',	'', '08/01/2016'),
    (NULL, 'lucy', '15a6aea1009a94bfb97901572724cf3e6c77c5bb22e6835d61fdd865cfcdfc1773e287f9df6e6e061244dffa475cfd0ce8033cf386039993a063249a25d2482a', '', 'some@email.com', 'Female', '01/01/1990', 'Atlassian.', '', '08/01/2016'),
    (NULL, 'julia', '15a6aea1009a94bfb97901572724cf3e6c77c5bb22e6835d61fdd865cfcdfc1773e287f9df6e6e061244dffa475cfd0ce8033cf386039993a063249a25d2482a', '', 'some@email.com', 'Female', '01/01/1990', ':)', '', '08/01/2016'),
    (NULL, 'robot', '15a6aea1009a94bfb97901572724cf3e6c77c5bb22e6835d61fdd865cfcdfc1773e287f9df6e6e061244dffa475cfd0ce8033cf386039993a063249a25d2482a', 'Mr Robot', 'some@email.com', '', '01/01/1999', 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean non mattis odio. Suspendisse mollis tristique sapien. Proin ac mi ornare nibh tempus luctus. Ut in ex scelerisque felis lacinia hendrerit. Nulla scelerisque ultricies tempus. Vestibulum ullamcorper eros mi, non ultricies erat dapibus sed. Aenean pretium nisi a magna vestibulum varius. Phasellus odio ex, porta quis erat rhoncus, malesuada cursus libero. Nam nec nibh eget felis eleifend vestibulum. Aenean lobortis eleifend dolor vitae elementum. Nullam tincidunt tellus id dolor tempus, laoreet hendrerit lorem commodo.', '', '01/01/1970'),
    (NULL, 'generic', '15a6aea1009a94bfb97901572724cf3e6c77c5bb22e6835d61fdd865cfcdfc1773e287f9df6e6e061244dffa475cfd0ce8033cf386039993a063249a25d2482a', 'Generico', 'some@email.com', '', '01/01/2017', 'Your Generic User Bio', '', '11/01/2017')
    '''
    )

    # Create dummy posts
    cur.execute(
    '''
    INSERT INTO posts VALUES
    (NULL, 1, 'I was walking down Sydney the other day, and I saw this amazing backpack. Does anyone know which company made this?', 'Where is this backpack from?', '01/01/2017', 'uploads/questions/1.jpeg'),
    (NULL, 1, 'I''ve always loved this book series, but got out of touch with it some time ago. I decided to pick it back up, but I wasn''t sure where to start.', 'Which part of the series is this book from?', '01/01/2017', 'uploads/questions/2.jpg'),
    (NULL, 3, 'I''m looking into purchasing a new pet. I saw this cat the other day, but I''m not sure what breed it is. Could anyone tell me?', 'What breed of kitten is this?', '01/01/2017', 'uploads/questions/3.jpg'),
    (NULL, 4, '', 'Where could I buy this particular dice?', '01/01/2017', 'uploads/questions/4.jpg'),
    (NULL, 7, 'I''ve had my eye on these pair of shoes, but the shops near me don''t have them. Does anyone know of stores in Canberra who have this pair of shoes for sale?', 'Where can I buy these shoes?', '01/01/2017', 'uploads/questions/5.jpg'),
    (NULL, 8, 'Anyone know where these socks are from?', 'Game-themed socks', '01/01/2017', 'uploads/questions/6.jpg'),
    (NULL, 10, 'Is this t-shirt limited edition? It looks amazing O_O', 'Fancy T-Shirt', '01/01/2017', 'uploads/questions/7.jpg'),
    (NULL, 12, 'It looks really simplistic, and I would like to know where I could purchase it in Sydney', 'What watch is this?', '01/01/2017', 'uploads/questions/8.jpg')
    '''
    )

    # Create dummy comments
    cur.execute(
    '''
    INSERT INTO comments VALUES
    (NULL, 0, 0, NULL, 'Nice meme!', '01/01/2017', 1, -33.8883064, 151.1941413),
    (NULL, 1, 0, 1, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 4, 0, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 4, 2, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 4, 4, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 6, 6, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 7, 7, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 9, 8, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 4, 8, 9, 'Nice meme!', '01/01/2017', 1, -33.8883064, 151.1941413),
    (NULL, 4, 8, 9, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 4, 8, 10, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 4, 10, NULL, 'Nice meme!', '01/01/2017', 1, -33.8883064, 151.1941413),
    (NULL, 2, 10, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 0, 11, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 0, 14, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 0, 17, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 6, 17, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 0, 18, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 0, 20, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 12, 20, 19, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 0, 21, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL),
    (NULL, 0, 22, NULL, 'Nice meme!', '01/01/2017', 1, NULL, NULL)
    '''
    )

    conn.commit()
