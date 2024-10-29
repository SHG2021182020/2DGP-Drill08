from Key import *

class StateMachine:
    def __init__(self, obj):
        self.obj = obj # 어떤 객체를 위한 상태머신인지 알려줌. obj = boy.self
        self.event_que = []
        self.cur_state = None
        self.transitions = {}

    def start(self, state):
        self.cur_state = state # 시작 상태를 받아서, 그걸로 현재 상태를 정의
        self.cur_state.enter(self.obj, ('START', None))

    def add_event(self, e):
        self.event_que.append(e)

    def set_transitions(self, transitions):
        self.transitions = transitions

    def update(self):
        if len(self.event_que) > 0:  # 이벤트 큐 처리 추가
            event = self.event_que.pop()
            self.handle_event(event)
        if self.cur_state:
            self.cur_state.do(self.obj)

    def draw(self):
        self.cur_state.draw(self.obj)
        pass

    def handle_event(self, e):
        for event, next_state in self.transitions[self.cur_state].items():
            if event(e):
                self.cur_state.exit(self.obj, e)
                self.cur_state = next_state
                self.cur_state.enter(self.obj, e)
                return