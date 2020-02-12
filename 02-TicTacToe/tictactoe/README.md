
# AWS Tic Tac Toe game 

https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TicTacToe.html
https://github.com/aws-samples/dynamodb-tictactoe-example-app

Additions:
- added docker logic. Even as the App still uses legacy boto and is built for python2.7, it works smooth with Python 3.8, latest flask etc. 
- tiny patch to ensure local mode points to dynamodb
- lookup results container


## Build and run using Docker
'''
# build
docker-compose build

# 
docker-compose up -d

# play by browsing to http://localhost:5000
# note 2nd user must use different browser env and/ or incognito window

# 
# docker-compose down


## Challenge
For those looking for a small coding challenge, it would be neat if some-one ported it to boto3.
