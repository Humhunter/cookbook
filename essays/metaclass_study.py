#!/usr/bin/python3
# -*- coding: utf-8 -*-
# author: JinSong.xiao(61627515@qq.com)
# time: 2019/12/11 22:53

import yaml


class Monster(yaml.YAMLObject):
    yaml_tag = u'!Monster'

    def __init__(self, name, hp, ac, attacks):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.attacks = attacks

    def __repr__(self):
        return '{0}(name={1}, hp={2}, ac={3}, attacks={4})'.format(self.__class__.__name__, self.name, self.ac,
                                                                   self.attacks)


# class YAMLObjectMetaclass(type):
#     def __init__(cls, name, bases, kwds):
#         super(YAMLObjectMetaclass, cls).__init__(name, bases, kwds)
#         if 'yaml_tag' in kwds and kwds['yaml_tag'] is not None:
#             cls.yaml_loader.add_constructor(cls.yaml_tag, cls.from_yaml)
#
#
# class YAMLObject(metaclass=YAMLObjectMetaclass):
#     yaml_loader = Loader
#     pass

class MyClass:
    data = 1


if __name__ == '__main__':
    # yaml.load("""
    # --- !Monster
    # name: Cave spider
    # hp: [2, 6] # 2d6
    # ac: 16
    # attacks: [BITE,HURT]
    # """)

    Monster(name='Cave spider', hp=[2, 6], ac=16, attacks=['BITE', 'HURT'])

    print(yaml.dump(Monster(name='Cave spider', hp=[2, 6], ac=16, attacks=['BITE', 'HURT'])))

    # test
    instance = MyClass()
    print(MyClass, instance)
    print(instance.data)

    # type manul
