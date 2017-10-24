
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'KEYWORD PRE CODE STYLE REST NEWLINE HRULE GRIDmain : head bodyhead : head keyword\n            | head NEWLINE\n            |\n    body : body style\n            | body REST\n            | body newline\n            | body pre\n            | body code\n            | body fakekeyword\n            | body hrule\n            | body grid\n            |\n    pre : PRE \n           |  \n    code : CODE\n\t\t   |\n\tstyle : STYLEnewline : NEWLINEhrule : HRULEgrid : GRIDkeyword : KEYWORDfakekeyword : KEYWORD'
    
_lr_action_items = {'KEYWORD':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[-4,4,10,-22,-3,-2,-21,-16,-11,-23,-8,-19,-9,-18,-20,-5,-14,-7,-6,-12,-10,]),'STYLE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[-4,-13,14,-22,-3,-2,-21,-16,-11,-23,-8,-19,-9,-18,-20,-5,-14,-7,-6,-12,-10,]),'GRID':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[-4,-13,7,-22,-3,-2,-21,-16,-11,-23,-8,-19,-9,-18,-20,-5,-14,-7,-6,-12,-10,]),'CODE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[-4,-13,8,-22,-3,-2,-21,-16,-11,-23,-8,-19,-9,-18,-20,-5,-14,-7,-6,-12,-10,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[-4,0,-13,-1,-22,-3,-2,-21,-16,-11,-23,-8,-19,-9,-18,-20,-5,-14,-7,-6,-12,-10,]),'REST':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[-4,-13,19,-22,-3,-2,-21,-16,-11,-23,-8,-19,-9,-18,-20,-5,-14,-7,-6,-12,-10,]),'HRULE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[-4,-13,15,-22,-3,-2,-21,-16,-11,-23,-8,-19,-9,-18,-20,-5,-14,-7,-6,-12,-10,]),'PRE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[-4,-13,17,-22,-3,-2,-21,-16,-11,-23,-8,-19,-9,-18,-20,-5,-14,-7,-6,-12,-10,]),'NEWLINE':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,],[-4,5,12,-22,-3,-2,-21,-16,-11,-23,-8,-19,-9,-18,-20,-5,-14,-7,-6,-12,-10,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'body':([2,],[3,]),'keyword':([2,],[6,]),'style':([3,],[16,]),'fakekeyword':([3,],[21,]),'grid':([3,],[20,]),'hrule':([3,],[9,]),'newline':([3,],[18,]),'pre':([3,],[11,]),'main':([0,],[1,]),'head':([0,],[2,]),'code':([3,],[13,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> main","S'",1,None,None,None),
  ('main -> head body','main',2,'p_main','interpreter.py',1091),
  ('head -> head keyword','head',2,'p_head','interpreter.py',1095),
  ('head -> head NEWLINE','head',2,'p_head','interpreter.py',1096),
  ('head -> <empty>','head',0,'p_head','interpreter.py',1097),
  ('body -> body style','body',2,'p_body','interpreter.py',1105),
  ('body -> body REST','body',2,'p_body','interpreter.py',1106),
  ('body -> body newline','body',2,'p_body','interpreter.py',1107),
  ('body -> body pre','body',2,'p_body','interpreter.py',1108),
  ('body -> body code','body',2,'p_body','interpreter.py',1109),
  ('body -> body fakekeyword','body',2,'p_body','interpreter.py',1110),
  ('body -> body hrule','body',2,'p_body','interpreter.py',1111),
  ('body -> body grid','body',2,'p_body','interpreter.py',1112),
  ('body -> <empty>','body',0,'p_body','interpreter.py',1113),
  ('pre -> PRE','pre',1,'p_pre','interpreter.py',1121),
  ('pre -> <empty>','pre',0,'p_pre','interpreter.py',1122),
  ('code -> CODE','code',1,'p_code','interpreter.py',1130),
  ('code -> <empty>','code',0,'p_code','interpreter.py',1131),
  ('style -> STYLE','style',1,'p_style','interpreter.py',1139),
  ('newline -> NEWLINE','newline',1,'p_newline','interpreter.py',1143),
  ('hrule -> HRULE','hrule',1,'p_hrule','interpreter.py',1147),
  ('grid -> GRID','grid',1,'p_grid','interpreter.py',1151),
  ('keyword -> KEYWORD','keyword',1,'p_keyword','interpreter.py',1155),
  ('fakekeyword -> KEYWORD','fakekeyword',1,'p_fakekeyword','interpreter.py',1162),
]
