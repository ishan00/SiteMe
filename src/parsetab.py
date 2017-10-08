
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'KEYWORD PRE STYLE REST NEWLINE HRULEmain : head bodyhead : head keyword\n            | head NEWLINE\n            |\n    body : body style\n            | body REST\n            | body newline\n            | body pre\n            | body fakekeyword\n            | body hrule\n            |\n    pre : PRE \n           |  \n    style : STYLEnewline : NEWLINEhrule : HRULEkeyword : KEYWORDfakekeyword : KEYWORD'
    
_lr_action_items = {'PRE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,],[-4,-11,-17,-2,15,-3,-18,-8,-16,-6,-14,-9,-5,-10,-12,-7,-15,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,],[-4,0,-11,-17,-2,-1,-3,-18,-8,-16,-6,-14,-9,-5,-10,-12,-7,-15,]),'STYLE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,],[-4,-11,-17,-2,11,-3,-18,-8,-16,-6,-14,-9,-5,-10,-12,-7,-15,]),'HRULE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,],[-4,-11,-17,-2,9,-3,-18,-8,-16,-6,-14,-9,-5,-10,-12,-7,-15,]),'REST':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,],[-4,-11,-17,-2,10,-3,-18,-8,-16,-6,-14,-9,-5,-10,-12,-7,-15,]),'KEYWORD':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,],[-4,3,-17,-2,7,-3,-18,-8,-16,-6,-14,-9,-5,-10,-12,-7,-15,]),'NEWLINE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,],[-4,6,-17,-2,17,-3,-18,-8,-16,-6,-14,-9,-5,-10,-12,-7,-15,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'hrule':([5,],[14,]),'main':([0,],[1,]),'head':([0,],[2,]),'pre':([5,],[8,]),'newline':([5,],[16,]),'keyword':([2,],[4,]),'body':([2,],[5,]),'fakekeyword':([5,],[12,]),'style':([5,],[13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> main","S'",1,None,None,None),
  ('main -> head body','main',2,'p_main','interpreter.py',657),
  ('head -> head keyword','head',2,'p_head','interpreter.py',661),
  ('head -> head NEWLINE','head',2,'p_head','interpreter.py',662),
  ('head -> <empty>','head',0,'p_head','interpreter.py',663),
  ('body -> body style','body',2,'p_body','interpreter.py',671),
  ('body -> body REST','body',2,'p_body','interpreter.py',672),
  ('body -> body newline','body',2,'p_body','interpreter.py',673),
  ('body -> body pre','body',2,'p_body','interpreter.py',674),
  ('body -> body fakekeyword','body',2,'p_body','interpreter.py',675),
  ('body -> body hrule','body',2,'p_body','interpreter.py',676),
  ('body -> <empty>','body',0,'p_body','interpreter.py',677),
  ('pre -> PRE','pre',1,'p_pre','interpreter.py',685),
  ('pre -> <empty>','pre',0,'p_pre','interpreter.py',686),
  ('style -> STYLE','style',1,'p_style','interpreter.py',694),
  ('newline -> NEWLINE','newline',1,'p_newline','interpreter.py',698),
  ('hrule -> HRULE','hrule',1,'p_hrule','interpreter.py',702),
  ('keyword -> KEYWORD','keyword',1,'p_keyword','interpreter.py',706),
  ('fakekeyword -> KEYWORD','fakekeyword',1,'p_fakekeyword','interpreter.py',713),
]
