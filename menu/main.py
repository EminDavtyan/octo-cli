from collections import deque
from abc import ABCMeta, abstractstaticmethod, abstractmethod
from pynput import keyboard

class Session(metaclass=ABCMeta):
    __instance = None
    history = deque()
    indicator = None
    currentCapsule = None

    @classmethod
    def get_instance(cls):
        if cls.__instance is None:
            cls.__instance = cls
        return cls.__instance

    @classmethod
    def define_capsule(cls, title):
        cls.currentCapsule = Capsule(cls, title)
        return cls.currentCapsule

    @classmethod
    def control(cls):
        """ Control of menu """
        def __on_press(key):
            try:
                print('alphanumeric key {0} pressed'.format(key.char))
            except AttributeError:
                print('special key {0} pressed'.format(key))

        def __on_release(key):
            print('{0} released'.format(
                key))
            if key == keyboard.Key.esc:
                # Stop listener
                return False

        with keyboard.Listener(
                on_press=__on_press,
                on_release=__on_release) as listener:
            listener.join()

    @classmethod
    def run(cls):
        print(cls.currentCapsule.components)


class Capsule:
    def __init__(self, session: Session, title: str):
        assert session, 'Session not created'
        self.title = title
        self.components = deque()
        self.status = False

    def add(self, component_type, status: bool, label: str):
        component = Component(component_type, status, label)
        self.components.append(component)

class Component:
    available_components = ['Label', 'SimpleButton']

    def __init__(self, component_type: available_components, status: bool, label: str):
        self.component_type = component_type
        self.status = status
        self.label = label

    def focussed(self):
        """ Design and animation of component while focused """
        pass

    def operating_on(self):
        """ Component functionality """
        pass

    def __repr__(self):
        return f'(Type: {self.component_type}, Status: {self.status}, Label: "{self.label}")'

class Label(Component):
    def __init__(self, parent_capsule: Capsule, text):
        super().__init__(component_type='Label', label=text, status=True)
        self.text = text
        parent_capsule.components.append(self)

    def __repr__(self):
        return self.text

class SimpleButton(Component):
    def __init__(self, parent_capsule: Capsule, title):
        super().__init__(component_type='SimpleButton')
        self.title = title
        parent_capsule.components.append(self)

s = Session()
c1 = s.define_capsule('Main')
c1.add('Label', True, 'Label1')
c1.add('Label', True, 'Label2')
s.run()