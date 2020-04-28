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
        return ('[' + repr(self) + '\nenv: ' + str(self.env) + '\nid: ' + str(
            self.id) + '\nx: ' + str(self.x) + ']')


class AgentLauncher(Process):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.agent = Agent(*args, **kwargs)
        print('pid: ', os.getpid())
        print('launcher: ', self)
        print('agent: ', self.agent)
        self.start()
        sleep(1)
        print('pid: ', os.getpid())
        print('agent: ', self.agent)

    def run(self):
        print("\n")
        print('pid: ', os.getpid())
        print('launcher: ', self)
        print('agent: ', self.agent)
        self.agent.step()
        self.agent.env['d'] = 4
        print('agent: ', self.agent)
        print('\n')


launcher = AgentLauncher(env={'a': 2, 'b': 3}, id=0)
# print('------------------')
# print('pid',os.getpid())
# print('launcher:',launcher)
# print('agent: ',launcher.agent)
