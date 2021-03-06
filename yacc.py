import ply.yacc as yacc

# Get the token map from the lexer.  This is required.
from lex import tokens

DEBUG = True

# Namespace & built-in functions

name = {}
let_dict = {} # Dictionary that stores variable name and value ( Example: {'a' : 3} )

global AST
AST = []

def _print(l):
    print lisp_str(l[0])

name['print'] = _print


#  Evaluation functions

def lisp_eval(simb, items):
    if simb in name:
        return call(name[simb], eval_lists(items))
    else:
        if simb not in let_dict: # Variable is not already in the dictionary
            let_dict[simb] = items[0] # Add the variable and value to the dictionary
        return [simb] + items

def call(f, l):
    try:
        return f(eval_lists(l))
    except TypeError:
        return f

def eval_lists(l):
    r = []
    for i in l:
        if is_list(i):
            if i:
                r.append(lisp_eval(i[0], i[1:]))
            else:
                r.append(i)
        else:
            r.append(i)
    return r

# Utilities functions

def is_list(l):
    return type(l) == type([])

def lisp_str(l):
    if type(l) == type([]):
        if not l:
            return "()"
        r = "("
        for i in l[:-1]:
            r += lisp_str(i) + " "
        r += lisp_str(l[-1]) + ")"
        return r
    elif l is True:
        return "#t"
    elif l is False:
        return "#f"
    elif l is None:
        return 'nil'
    else:
        return str(l)

# BNF

def p_exp_atom(p):
    'exp : atom'
    p[0] = p[1]

def p_exp_qlist(p):
    'exp : quoted_list'
    p[0] = p[1]

def p_exp_call(p):
    'exp : call'
    p[0] = p[1]

def p_quoted_list(p):
    'quoted_list : QUOTE list'
    #p[0] = p[2]
    #p[0] = [p[1]] + p[2]
    p[0] = ["quote"] + [p[2]]


def p_list(p):
    'list : LPAREN items RPAREN'
    p[0] = p[2]

def p_items(p):
    'items : item items'
    p[0] = [p[1]] + p[2]

def p_items_op(p):
    'items : item OP item'
    p[0] = [p[2]] + [p[1]] +[p[3]]
'''def p_item_op(p):
    ''atom : SIMB OP NUM
            |  SIMB OP SIMB''
    p[0] = [p[2]] + [p[1]] +[p[3]]'''
def p_items_empty(p):
    'items : empty'
    p[0] = []

def p_empty(p):
    'empty :'
    pass
def p_item_atom(p):
    'item : atom'
    p[0] = p[1]
'''def p_item_atoms(p):
    'item : atom1'
    p[0] = p[1]'''

def p_item_list(p):
    '''item : list
          | quoted_list'''
    p[0] = p[1]


def p_item_call(p):
    'item : call'
    p[0] = p[1]

def p_item_empty(p):
    'item : empty'
    p[0] = p[1]

def p_call_print(p):
    'call : PRINT LPAREN items RPAREN'
    global AST
    if DEBUG: print "Calling", p[1], "with", p[3]
    AST = [p[1]] + [i for i in p[3]]
    print "AST is: ", AST
    p[0] = AST
def p_call(p):
    '''call : LET items
            | VAR items
            | LPAREN LET items RPAREN
            | LPAREN SIMB items RPAREN
            | LPAREN OP items RPAREN'''
    global AST
    if len(p) <4:
        if DEBUG: print "Calling", p[1], "with", p[2]
        AST = [p[1]] + [i for i in p[2]]
    else:
       if DEBUG: print "Calling", p[2], "with", p[3]
    #if isinstance(p[3], list) and isinstance(p[3][0], list) and p[3][0][0] == "'":
    #p[3] = [["quote"] + [p[3][0][1:]]] # Replace single quote with the word "quote"
       AST = [p[2]] + [i for i in p[3]]
    print "AST is: ", AST
    p[0] = AST




def p_item_dq(p):
    '''item : atom1 BACKSLASH LPAREN items atom2
             | atom1 DOUBLEQ'''
    if len(p) == 6:
        p[0] = (["list"]+[p[1]] + [p[4]] +[p[5]]) if len(p[4])>1  else (["list"]+[p[1]] + [["list"]+p[4]] +[p[5]])

    elif len(p) == 3:
        p[0] = ["list"] + [str(p[1]) + str(p[2])]

##############################
def p_atom2_c(p):
    'atom2 : atom2 DOUBLEQ'
    p[0] = p[1]+ p[2]
def p_atom2_a(p):
    'atom2 : atom2 SIMB'
    if p[2] in "!?.,%":
       p[0] = p[1]+ p[2]
    else:
        p[0] = p[1]+" "+ p[2]

def p_atom2_chec(p):
    '''atom2 : RPAREN SIMB
          |  RPAREN DOUBLEQ'''
    p[0] = p[2]

def p_atoms_check(p):
    'atom1 : atom1 BACKSLASH'
    p[0] = p[1]
def p_atoms_st(p):
    'atom1 : atom1 SIMB'
    p[0] = p[1]+" "+ p[2]

def p_atoms_s(p):
    'atom1 : DOUBLEQ SIMB'
    p[0] = p[1]+ p[2]
###############################
def p_atom_simbol(p):
    '''atom : SIMB '''
    #if len(p) == 2:
    p[0] = p[1]
    #else:
       # print p[2]
       # p[0] = p[2]

def p_atom_bool(p):
    'atom : bool'
    p[0] = p[1]

def p_atom_num(p):
    '''atom : NUM
            | NUM '.' NUM'''
    if len(p) == 2:
      p[0] = p[1]
    else:
        p[0] = float(str(p[1]) + str(p[2])+str(p[3]))
def p_atom_op(p):
    'atom : OP'
    print p[1]
    p[0] = p[1]
def p_atom_word(p):
    'atom : TEXT'
    p[0] = p[1]

def p_atom_empty(p):
    'atom :'
    pass

def p_true(p):
    'bool : TRUE'
    p[0] = True

def p_false(p):
    'bool : FALSE'
    p[0] = False

def p_nil(p):
    'atom : NIL'
    p[0] = None

# Error rule for syntax errors
def p_error(p):
    print "Syntax error!! ",p

# Build the parser
# Use this if you want to build the parser using SLR instead of LALR
# yacc.yacc(method="SLR")
yacc.yacc()


