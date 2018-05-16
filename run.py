#!/bin/bash python

from eve import Eve
import os
import pymysql
import json

app = Eve()

if 'PORT' in os.environ:
    port = os.environ.get('PORT')
    host = '0.0.0.0'
    debug = False
else:
    port = 5000
    host = '0.0.0.0'
    debug = True

@app.route('/legacyposts')
def legacyposts():
    db = pymysql.connect(host=app.config['LEGACY_HOST'],
                         port=app.config['LEGACY_PORT'],
                         user=app.config['LEGACY_USER'],
                         passwd=app.config['LEGACY_PASS'],
                         db=app.config['LEGACY_DB'])
    cursor = db.cursor()

    command = r"""
        select 
            wpgj_posts.ID, 
            display_name, 
            post_title, 
            post_content 
        from wpgj_posts 
        left join wpgj_users 
            on wpgj_users.ID = post_author 
        where post_status = 'publish';
    """
    cursor.execute(command)
    posts = [{
        'id': pid,
        'author': author,
        'title': title,
        'content': content} 
        for pid, author, title, content in cursor]

    cursor.close()
    db.close()

    return json.dumps(posts)

if __name__ == '__main__':
    app.run(host=host, port=port, debug=debug)

