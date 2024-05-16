

from collections import deque


class Logger:

    def __init__(self):
        self.lastPrintedOn = dict()
        self.lastTimestampSeen = 0

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        print(f'lastprintedOn {self.lastPrintedOn} lastTimestampSeen {self.lastTimestampSeen}')
        if message is None:
            return False

        if timestamp > self.lastTimestampSeen + 10:
            self.lastPrintedOn.clear()
            
        self.lastTimestampSeen = timestamp

        if message in self.lastPrintedOn:
            print(f'message exists in cache')
            if timestamp < self.lastPrintedOn[message] + 10:
                print(f'message has been printed less than 10 sec ago')
                return False

        self.lastPrintedOn[message]=timestamp
        print(f'save message timestamp in dict {self.lastPrintedOn}')

        return True
    
class Logger2:

    def __init__(self, limiter_threshold: int =10):
        self.lastPrintedOn = dict()
        self.limiterThreshold = 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        print(f'incoming {message} timestamp {timestamp}')
        print(f'lastprintedOn cache contains {self.lastPrintedOn}')

        # clearing old messages timestamps (rolling time window)
        self._cleanup_cache(timestamp)

        if message is None:
            return False

        if message in self.lastPrintedOn:
            print(f'message exists in cache {message} - ts {self.lastPrintedOn[message]}')
            # if timestamp < self.lastPrintedOn[message] + 10:
            print(f'message has been printed less than 10 sec ago')
            return False

        self.lastPrintedOn[message]=timestamp
        print(f'save message timestamp in dict {self.lastPrintedOn}')

        return True
    
    def _cleanup_cache(self, current_timestamp: int):
        # Remove entries that are older than the cleanup threshold
        keys_to_delete = [msg for msg, timst in self.lastPrintedOn.items()
                          if timst + self.limiterThreshold <= current_timestamp ]
        
        for key in keys_to_delete:
            del self.lastPrintedOn[key]

class Logger3(object): # with deque and set

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._msg_set = set()
        self._msg_queue = deque() # old message to the left, new messages to the right
    
    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        """
        """
        Idea: we keep only a set of the messages that cannot be printed
        We managed this set using a deque where we pop them left when they expire and delete the corresponding 
        message from the set.
        """

        print(f'Incoming message {message} with timestamp {timestamp}')
        print(f'...Message queue {self._msg_queue}')
        print(f'...Message set {self._msg_set}')
        while self._msg_queue:
            msg, ts = self._msg_queue[0]
            if timestamp - ts >= 10:
                self._msg_queue.popleft()
                self._msg_set.remove(msg)
                print(f'...Message queue after cleaning {self._msg_queue}')
                print(f'...Message set after cleaning {self._msg_set}')
            else:
                break
        
        if message not in self._msg_set:
            self._msg_set.add(message)
            self._msg_queue.append((message, timestamp)) # new message added to the right
            return True
        else:
            return False