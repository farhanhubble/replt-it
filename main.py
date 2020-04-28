from multiprocessing import Process, Queue
import os
from time import sleep


def repr(x):
    return object.__repr__(x)


class Agent(object):
    def __init__(self, env, id):
        self.env = env
        self.id = id
        self.x = 0

    def step(self):
        self.x += 1

    def __repr__(self):
        return ('[' + os.getpid() + '\n' + repr(self) + '\nenv: ' + str(self.env) + '\nid: ' + str(
            self.id) + '\nx: ' + str(self.x) + ']')


class AgentLauncher(Agent, Process):
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        super().__init__()
        print(self)
        self.start()
        sleep(1)
        print('pid: ', os.getpid())
        print(self.agent)

    def run(self):
        print("\n")
        print(self)
        self.step()
        self.env['d'] = 4
        print(self)
        print('\n')


launcher = AgentLauncher(env={'a': 2, 'b': 3}, id=10)

