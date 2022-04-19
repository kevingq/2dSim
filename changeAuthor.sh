#!/bin/sh

# Credits: http://stackoverflow.com/a/750191

git filter-branch -f --env-filter "
    GIT_AUTHOR_NAME='kevingq'
    GIT_AUTHOR_EMAIL='kevin.gracequist@gmail.com'
    GIT_COMMITTER_NAME='kevingq'
    GIT_COMMITTER_EMAIL='kevin.gracequist@gmail.com'
  " HEAD

