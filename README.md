# rasa assistant

Enviroment setup:

    Ubuntu 19
    python version: 3.7.5
    pip version: 20.1.2
    pip install rasa
    
Or use virtual env (will be have to be done for every tmux window):

    source ./venv/bin/activate

To run rasa with command line shell:

    rasa train
    rasa run actions (in seperate window)
    rasa shell
    
To run tests:

    rasa test --stories tests/conversation_tests.md
