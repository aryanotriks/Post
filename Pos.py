from FB import graph
from FB.tools import PostCloning
from time import sleep
from sys import exit

sess = graph.API()
if (sess.load_token() == False):
    if (sess.new("xx@gmail.com", "xxx1234") == False):
        exit()

pc = PostCloning(api_session=sess)

while True:
    pc.open_target("1xxxx5173419917")
    newAct_printed = False
    for _, status, post in pc.check_activity(limit=5):
        if (status):
            if (newAct_printed==False):
                print("Found new activity!")
                newAct_printed = True
            realPostId, clonedPostId, postType = pc.clone_post(post, to_lang="ms")
            if (clonedPostId != False):
                print(f"[NEW]: {realPostId} {clonedPostId} [{postType}]")
                sleep(500)
    sleep(900) #15m
