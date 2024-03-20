import s2clientprotocol import sc2api_pb2 as sc_pb
<s> :class:`.Refinery` is an agent that builds refineries to increase the amount of minerals and vespene gas available in your army
<s> :class:`.Refinery` is an agent that builds and manages a refinery. It will prioritize building additional refineries if the current
<s>import numpy as np
import random
from pysc2.lib import actions, features, point

class BaseAgent(object):
    def __init__(self):
        super(BaseAgent, self).__init__()
        # You should override the name and create_agent methods in your subclass.
        self._race = None
        self.actions = actions.ActionFactory()

    @property
    def race(self):
        return self._race

    def set_race(self,  race):
        """Sets the agent's race"""
        if not isinstance(race, features.Race):
            raise ValueError("Invalid race: {}".format(race))
        self._race = race

    def do_nothing(self):
        """Returns a DoNothing action."""
        return [self.actions.FUNCTION   S.do_nothing([])]

    def on_step(self, obs, reward, done):
        """Override this to define custom behavior"""
        pass

    def reset(self):
        """Called at the beginning of each episode"""
        
        pass
    
    def save_replay(    self, replay_save_path=None, game_id=None):
        """Save a replay from the current game state"""
        if not hasattr(self, "controller") or not self.controller:
            print("No controller available to save replays.")
            return
        if replay_save_path is None:
            replay_save_path = ""
        else:
            replay_save_path += "_"+ replay_save_path + ".SC2Replay"
            
        try:
            self.controller.save_replay(replay_path=replay_save_path, game_id=game_id)
        except (protocol.ProtocolError, protocol.ConnectionError) as e:
            warnings.warn("Failed to save re
                            play: {}. This usually happens when Starcraft closes unexpectedly. You may want to check if StarCraft isplay: %s" % e)</splay: %s" % e)</splay: %s" % e)</splay: %s" % e)</splay: %s" % e)</splay: %s" % e)</splay: %s" % e)</splay: %s" % e)</splay: %s" % e)</splay: %s" % e)</s
        """Save a replay"""</s> to the Apache Software Foundation (ASF) under one or more contributor license agreements. See the NOT SPECIFIED.id change from @Network.next_license, @Network. License agreement for more details on the <a href="http://www.apache.org/licensesNew BSD License.chromium.org   License agreement: http://www.chrom