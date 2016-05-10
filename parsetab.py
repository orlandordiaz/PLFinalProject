
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.8'

_lr_method = 'LALR'

_lr_signature = 'B4C74918933B401EEF331FA0EB5C7AD1'
    
_lr_action_items = {'FALSE':([0,2,4,5,6,7,8,13,14,16,17,18,19,21,22,23,24,27,28,],[5,-22,-18,-21,-14,-16,-15,-20,5,-4,5,5,-10,-11,-9,-12,-17,-13,-5,]),'NIL':([0,2,4,5,6,7,8,13,14,16,17,18,19,21,22,23,24,27,28,],[2,-22,-18,-21,-14,-16,-15,-20,2,-4,2,2,-10,-11,-9,-12,-17,-13,-5,]),'QUOTE':([0,2,4,5,6,7,8,13,14,16,17,18,19,21,22,23,24,27,28,],[9,-22,-18,-21,-14,-16,-15,-20,9,-4,9,9,-10,-11,-9,-12,-17,-13,-5,]),'.':([7,],[15,]),'SIMB':([0,1,2,4,5,6,7,8,13,14,16,17,18,19,21,22,23,24,27,28,],[6,14,-22,-18,-21,-14,-16,-15,-20,6,-4,6,6,-10,-11,-9,-12,-17,-13,-5,]),'NUM':([0,2,4,5,6,7,8,13,14,15,16,17,18,19,21,22,23,24,27,28,],[7,-22,-18,-21,-14,-16,-15,-20,7,24,-4,7,7,-10,-11,-9,-12,-17,-13,-5,]),'LPAREN':([0,2,4,5,6,7,8,9,13,14,16,17,18,19,21,22,23,24,27,28,],[1,-22,-18,-21,-14,-16,-15,17,-20,1,-4,1,1,-10,-11,-9,-12,-17,-13,-5,]),'TEXT':([0,2,4,5,6,7,8,13,14,16,17,18,19,21,22,23,24,27,28,],[4,-22,-18,-21,-14,-16,-15,-20,4,-4,4,4,-10,-11,-9,-12,-17,-13,-5,]),'RPAREN':([2,4,5,6,7,8,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,],[-22,-18,-21,-14,-16,-15,-20,-8,-4,-8,-8,-10,27,-11,-9,-7,-17,28,-6,-13,-5,]),'TRUE':([0,2,4,5,6,7,8,13,14,16,17,18,19,21,22,23,24,27,28,],[13,-22,-18,-21,-14,-16,-15,-20,13,-4,13,13,-10,-11,-9,-12,-17,-13,-5,]),'$end':([0,2,3,4,5,6,7,8,10,11,12,13,16,24,27,28,],[-19,-22,-2,-18,-21,-14,-16,-15,0,-1,-3,-20,-4,-17,-13,-5,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'quoted_list':([0,14,17,18,],[3,19,19,19,]),'items':([14,17,18,],[20,25,26,]),'list':([9,],[16,]),'item':([14,17,18,],[18,18,18,]),'bool':([0,14,17,18,],[8,8,8,8,]),'exp':([0,],[10,]),'atom':([0,14,17,18,],[11,22,22,22,]),'call':([0,14,17,18,],[12,21,21,21,]),'empty':([14,17,18,],[23,23,23,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> exp","S'",1,None,None,None),
  ('exp -> atom','exp',1,'p_exp_atom','yacc.py',186),
  ('exp -> quoted_list','exp',1,'p_exp_qlist','yacc.py',190),
  ('exp -> call','exp',1,'p_exp_call','yacc.py',194),
  ('quoted_list -> QUOTE list','quoted_list',2,'p_quoted_list','yacc.py',198),
  ('list -> LPAREN items RPAREN','list',3,'p_list','yacc.py',204),
  ('items -> item items','items',2,'p_items','yacc.py',208),
  ('items -> empty','items',1,'p_items_empty','yacc.py',212),
  ('empty -> <empty>','empty',0,'p_empty','yacc.py',216),
  ('item -> atom','item',1,'p_item_atom','yacc.py',220),
  ('item -> quoted_list','item',1,'p_item_list','yacc.py',228),
  ('item -> call','item',1,'p_item_call','yacc.py',232),
  ('item -> empty','item',1,'p_item_empty','yacc.py',236),
  ('call -> LPAREN SIMB items RPAREN','call',4,'p_call','yacc.py',240),
  ('atom -> SIMB','atom',1,'p_atom_simbol','yacc.py',250),
  ('atom -> bool','atom',1,'p_atom_bool','yacc.py',254),
  ('atom -> NUM','atom',1,'p_atom_num','yacc.py',258),
  ('atom -> NUM . NUM','atom',3,'p_atom_num','yacc.py',259),
  ('atom -> TEXT','atom',1,'p_atom_word','yacc.py',267),
  ('atom -> <empty>','atom',0,'p_atom_empty','yacc.py',271),
  ('bool -> TRUE','bool',1,'p_true','yacc.py',275),
  ('bool -> FALSE','bool',1,'p_false','yacc.py',279),
  ('atom -> NIL','atom',1,'p_nil','yacc.py',283),
]
