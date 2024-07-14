from controller.authentication_controller import router as auth
from controller.vocab_controller import router as vocab
from controller.group_controller import router as group

all_routers = [
    auth,
    vocab,
    group,
]
