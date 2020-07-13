# rasa assistant

Enviroment setup:

    Ubuntu 19
    python version: 3.7.5
    pip version: 20.1.2
    pip3 install -r requirements.txt
    
Or use virtual env (will be have to be done for every tmux window):

    python3 -m venv ./venv
    source /venv/bin/activate
    pip install -r requirements.txt

To run rasa with command line shell:

    rasa train
    rasa run actions (in seperate window)
    rasa shell
    
To run tests:

    rasa test --stories tests/conversation_tests.md
