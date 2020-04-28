from multiprocessing import Process, Queue
import os
from time import sleep
# def f(a,b):
#   print(a)
#   print(b)


# def wrap_f(*args,**kwargs):
#   print('args:',args,' kwargs:',kwargs)
#   f(*args,**kwargs)


# wrap_f(1,2)
# wrap_f(3,b=4)
# wrap_f(a=5,b=6)

def repr(x):
  return object.__repr__(x)


class Agent(object):
  def __init__(self, env, id):
    self.env = env
    self.id = id
    self.x = 0
  
  def step(self):
    self.x += 1

  def __str__(self):
    return 'env:'+ str(self.env) + ' ' + 'id:' + str(self.id) + ' x:' + str(self.x)



class AgentWrapper(Process):
  def __init__(self, *args, **kwargs):
    super().__init__()
    self.id = args[1] if (args and len(args) >= 2) else kwargs['id']
    self.agent = Agent(*args, **kwargs)
    self.input_queue = Queue()
    self.output_queue = Queue()
    print('pid',os.getpid())
    print('Self', repr(self), self)
    print('id',repr(self.id), self.id)
    print('agent',repr(self.agent), self.agent)
    print('env', repr(self.agent.env), self.agent.env)
    print('input queue', self.input_queue)
    print('output queue', self.output_queue)
    self.start()
    sleep(1)
    print('env',repr(self.agent.env), self.agent.env)


  
  def run(self):
    print("\n")
    print('pid',os.getpid())
    print('Self', repr(self), self)
    print('id',repr(self.id), self.id)
    print('agent',repr(self.agent), self.agent)
    print('env', repr(self.agent.env), self.agent.env)
    print('input queue', self.input_queue)
    print('output queue', self.output_queue)
    self.agent.step()
    self.agent.env['d'] = 4
    print('env',repr(self.agent.env), self.agent.env)
    print('\n')



wrapper = AgentWrapper(env={'a':2,'b':3},id=0)
print('------------------')
print('pid',os.getpid())
print(repr(wrapper))
print(repr(wrapper.agent))
print(repr(wrapper.agent.env))





