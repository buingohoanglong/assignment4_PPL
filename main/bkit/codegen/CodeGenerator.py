'''
 *   @author Nguyen Hua Phung
 *   @version 1.0
 *   23/10/2015
 *   This file provides a simple version of code generator
 *
'''
from Visitor import BaseVisitor
from Emitter import Emitter
from Frame import Frame
from abc import ABC, abstractmethod
from AST import *   # add this line
from copy import deepcopy # add this line

class MethodEnv():
    def __init__(self, frame, sym):
        self.frame = frame
        self.sym = sym

class Symbol:
    def __init__(self,name,mtype,value = None):
        self.name = name
        self.mtype = mtype
        self.value = value
class CName:
    def __init__(self,n):
        self.value = n
class Index:
    def __init__(self,n):
        self.value = n
class Type(ABC): pass
class IntType(Type): pass
class FloatType(Type): pass
class VoidType(Type): pass
class ClassType(Type):
    def __init__(self,n):
        self.cname = n
class StringType(Type):pass
class BoolType(Type): pass
class MType(Type):
    def __init__(self,i,o):
        self.partype = i #List[Type]
        self.rettype = o #Type	
class ArrayType(Type):
    def __init__(self,et,*s):
        self.eleType = et #Type
        self.dimen = s   #List[int]  

class Access():
    def __init__(self, frame, sym, isLeft):
        self.frame = frame
        self.sym = sym
        self.isLeft = isLeft        

class CodeGenerator():
    def __init__(self):
        self.libName = "io"

    def init(self):
        return [
            Symbol("read", MType([], StringType()), CName(self.libName)),
            Symbol("printLn", MType([], VoidType()), CName(self.libName)),
            Symbol("printStrLn", MType([StringType()], VoidType()), CName(self.libName)),
            Symbol("print", MType([StringType()], VoidType()), CName(self.libName)),
		    Symbol("string_of_int", MType([IntType()], StringType()), CName(self.libName)),
Symbol("int_of_float", MType([FloatType()],IntType()), CName(self.libName)),
Symbol("float_to_int", MType([IntType()],FloatType()), CName(self.libName)),
Symbol("int_of_string", MType([StringType()],IntType()), CName(self.libName)),
Symbol("float_of_string", MType([StringType()],FloatType()), CName(self.libName)),
Symbol("string_of_float", MType([FloatType()],StringType()), CName(self.libName)),
Symbol("bool_of_string", MType([StringType()],BoolType()), CName(self.libName)),
Symbol("string_of_bool", MType([BoolType()],StringType()), CName(self.libName)),
        ]                   

    def gen(self, ast, dir_):
        #ast: AST
        #dir_: String

        gl = self.init()
        gc = CodeGenVisitor(ast, gl, dir_)
        gc.visit(ast, None)



class CodeGenVisitor(BaseVisitor):
    def __init__(self, astTree, env, dir_):
        #astTree: AST
        #env: List[Symbol]
        #dir_: File

        self.astTree = astTree
        self.env = env
        self.className = "MCClass"
        self.path = dir_
        self.emit = Emitter(self.path + "/" + self.className + ".j")

    def visitProgram(self, ast, c):
        #ast: Program
        #c: Any

        self.emit.printout(self.emit.emitPROLOG(self.className, "java.lang.Object"))
        # call other visit here
        # e = MethodEnv(None, self.env) # for testing only
        # self.genMain(e) # for testing only
        for decl in ast.decl:
            self.env.append(self.visit(decl, MethodEnv(None, self.env)))
        # for sym in self.env:
        #     print(sym.name)
        # generate default constructor
        self.genInit()
        # generate class init if necessary
        self.emit.emitEPILOG()
        return c

    def genInit(self):
        methodname,methodtype = "<init>",MType([],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,False,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "this",ClassType(self.className),frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        self.emit.printout(self.emit.emitREADVAR(varname, vartype, varindex, frame))
        self.emit.printout(self.emit.emitINVOKESPECIAL(frame))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))

    # The following code is just for initial, students should remove it and write your visitor from here
    def genMain(self,o):
        methodname,methodtype = "main",MType([ArrayType(StringType())],VoidType())
        frame = Frame(methodname, methodtype.rettype)
        self.emit.printout(self.emit.emitMETHOD(methodname,methodtype,True,frame))
        frame.enterScope(True)
        varname,vartype,varindex = "args",methodtype.partype[0],frame.getNewIndex()
        startLabel, endLabel = frame.getStartLabel(), frame.getEndLabel()
        self.emit.printout(self.emit.emitVAR(varindex, varname, vartype, startLabel, endLabel,frame ))
        self.emit.printout(self.emit.emitLABEL(startLabel,frame))
        self.emit.printout(self.emit.emitPUSHICONST(120, frame))
        sym = next(filter(lambda x: x.name == "string_of_int",o.sym))
        self.emit.printout(self.emit.emitINVOKESTATIC(sym.value.value+"/string_of_int",sym.mtype,frame))
        sym = next(filter(lambda x: x.name == "print",o.sym))
        self.emit.printout(self.emit.emitINVOKESTATIC(sym.value.value+"/print",sym.mtype,frame))
        self.emit.printout(self.emit.emitLABEL(endLabel, frame))
        self.emit.printout(self.emit.emitRETURN(methodtype.rettype, frame))
        self.emit.printout(self.emit.emitENDMETHOD(frame))



    def visitVarDecl(self,ast, c):
        var_type = None
        if isinstance(ast.varInit, IntLiteral):
            var_type = IntType()
        elif isinstance(ast.varInit, FloatLiteral):
            var_type = FloatType()
        elif isinstance(ast.varInit, BooleanLiteral):
            var_type = IntType()
        elif isinstance(ast.varInit, StringLiteral):
            var_type = StringType()
        elif isinstance(ast.varInit, ArrayLiteral):
            pass

        if c.frame == None: # global variable
            self.emit.printout(self.emit.emitATTRIBUTE(ast.variable.name, var_type, False, CName(self.className)))
            self.push_value_on_stack(str(ast.varInit.value), var_type, c.frame)
            self.emit.printout(self.emit.emitPUTSTATIC(ast.variable.name, var_type, c.frame))
            return Symbol(ast.variable.name, var_type, CName(self.className))
        else:   # local variable
            index = c.frame.getNewIndex()
            self.emit.printout(self.emit.emitVAR(index, ast.variable.name, var_type, c.frame.getStartLabel(), c.frame.getEndLabel(), c.frame))
            self.push_value_on_stack(str(ast.varInit.value), var_type, c.frame)
            self.emit.printout(self.emit.emitWRITEVAR(ast.variable.name, var_type, index, c.frame))
            return Symbol(ast.variable.name, var_type, Index(index))


    def visitFuncDecl(self,ast, c):
        c.frame = Frame(ast.name, VoidType())
        c.frame.enterScope(True)
        if ast.name.name == 'main':
            self.emit.printout(self.emit.emitMETHOD('main',MType([ArrayType(StringType())],VoidType()),True,c.frame))
            self.emit.printout(self.emit.emitVAR(c.frame.getNewIndex(), 'args', ArrayType(StringType()), c.frame.getStartLabel(), c.frame.getEndLabel(), c.frame))
        else:
            self.emit.printout(self.emit.emitMETHOD(ast.name.name, MType([param.mtype for param in ast.param], VoidType()), True, c.frame))

        local = deepcopy(c)
        for param in ast.param:
            local.sym.append(self.visit(param, local))

        for vardecl in ast.body[0]:
            local.sym.append(self.visit(vardecl, local))

        self.emit.printout(self.emit.emitLABEL(local.frame.getStartLabel(), local.frame))

        for stmt in ast.body[1]:
            self.visit(stmt, local)

        self.emit.printout(self.emit.emitLABEL(local.frame.getEndLabel(), local.frame))
        self.emit.printout(self.emit.emitRETURN(VoidType(), local.frame))
        self.emit.printout(self.emit.emitENDMETHOD(local.frame))
        c.frame.exitScope()

        return Symbol(ast.name, MType([param.mtype for param in ast.param], VoidType()), CName(self.className))

    def visitAssign(self,ast, c):
        rhs, rhs_type = self.visit(ast.rhs, Access(c.frame, c.sym, False))
        self.emit.printout(rhs)
        lhs, lhs_type = self.visit(ast.lhs, Access(c.frame, c.sym, True))
        self.emit.printout(lhs)

    def visitIf(self,ast, c):
        label_lst = [c.frame.getNewLabel() for i in range(len(ast.ifthenStmt) + 1)]
        for i in range(len(ast.ifthenStmt)):
            if i > 0:   # emit if/elif block label
                self.emit.printout(self.emit.emitLABEL(label_lst[i-1], c.frame))
            exp, exp_type = self.visit(ast.ifthenStmt[i][0], Access(c.frame, c.sym, False))
            self.emit.printout(exp) # emit condition expression
            self.emit.printout(self.emit.emitIFFALSE(label_lst[i], c.frame)) # emit branching code

            # if/elif body
            c.frame.enterScope(False)

            local = deepcopy(c)
            local.frame = c.frame   # reference c.frame to update c.frame

            for vardecl in ast.ifthenStmt[i][1]:
                local.sym.append(self.visit(vardecl, local))

            self.emit.printout(self.emit.emitLABEL(local.frame.getStartLabel(), local.frame))

            for stmt in ast.ifthenStmt[i][2]:
                self.visit(stmt, local)
            
            self.emit.printout(self.emit.emitLABEL(local.frame.getEndLabel(), local.frame))

            c.frame.exitScope()

            # goto endif
            self.emit.printout(self.emit.emitGOTO(label_lst[-1], c.frame))

        # visit else part
        self.emit.printout(self.emit.emitLABEL(label_lst[-2], c.frame)) # emit else label
        # else body
        c.frame.enterScope(False)

        local = deepcopy(c)
        local.frame = c.frame   # reference c.frame to update c.frame

        for vardecl in ast.elseStmt[0]:
            local.sym.append(self.visit(vardecl, local))

        self.emit.printout(self.emit.emitLABEL(local.frame.getStartLabel(), local.frame))

        for stmt in ast.elseStmt[1]:
            self.visit(stmt, local)

        self.emit.printout(self.emit.emitLABEL(local.frame.getEndLabel(), local.frame))

        c.frame.exitScope()

        # emit endif label
        self.emit.printout(self.emit.emitLABEL(label_lst[-1], c.frame))


    def visitFor(self,ast, c):
        c.frame.enterScope(False)
        c.frame.enterLoop()

        # init
        exp1, type1 = self.visit(ast.expr1, Access(c.frame, c.sym, False))
        self.emit.printout(exp1)
        idx, idx_type = self.visit(ast.idx1, Access(c.frame, c.sym, True))
        self.emit.printout(idx)

        # condition
        self.emit.printout(self.emit.emitLABEL(c.frame.getContinueLabel(), c.frame))    # continue label
        exp2, type2 = self.visit(ast.expr2, Access(c.frame, c.sym, False))
        self.emit.printout(exp2)
        self.emit.printout(self.emit.emitIFFALSE(c.frame.getBreakLabel(), c.frame))        

        # loop body
        local = deepcopy(c)
        local.frame = c.frame
        for vardecl in ast.loop[0]:
            local.sym.append(self.visit(vardecl, local))

        self.emit.printout(self.emit.emitLABEL(local.frame.getStartLabel(), local.frame))

        for stmt in ast.loop[1]:
            self.visit(stmt, local)

        self.emit.printout(self.emit.emitLABEL(local.frame.getEndLabel(), local.frame))

        # update
        exp3, type3 = self.visit(ast.expr3, Access(c.frame, c.sym, False))  # load exp3
        self.emit.printout(exp1)
        idx, idx_type = self.visit(ast.idx1, Access(c.frame, c.sym, False)) # load idx
        self.emit.printout(idx)
        self.emit.printout(self.emit.emitADDOP('+', IntType(), c.frame))    # add
        idx, idx_type = self.visit(ast.idx1, Access(c.frame, c.sym, True))  # store back to idx
        self.emit.printout(idx)

        # goto continue label
        self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(), c.frame))
        # break label
        self.emit.printout(self.emit.emitLABEL(c.frame.getBreakLabel(), c.frame))

        c.frame.exitLoop()
        c.frame.exitScope()

    def visitBreak(self,ast, c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getBreakLabel(), c.frame))

    def visitContinue(self,ast, c):
        self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(), c.frame))

    def visitReturn(self,ast, c):
        pass

    def visitDowhile(self,ast, c):
        c.frame.enterScope(False)
        c.frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(c.frame.getContinueLabel(), c.frame))    # emit continue label

        # loop body
        local = deepcopy(c)
        local.frame = c.frame
        for vardecl in ast.sl[0]:
            local.sym.append(self.visit(vardecl, local))

        self.emit.printout(self.emit.emitLABEL(local.frame.getStartLabel(), local.frame))

        for stmt in ast.sl[1]:
            self.visit(stmt, local)

        self.emit.printout(self.emit.emitLABEL(local.frame.getEndLabel(), local.frame))

        # loop contidtion
        exp, exp_type = self.visit(ast.exp, Access(c.frame, c.sym, False))
        self.emit.printout(exp) # condition expression
        self.emit.printout(self.emit.emitIFTRUE(c.frame.getContinueLabel(), c.frame)) # if condition true, continue loop

        # emit end loop label
        self.emit.printout(self.emit.emitLABEL(c.frame.getBreakLabel(), c.frame))

        c.frame.exitLoop()
        c.frame.exitScope()

    def visitWhile(self,ast, c):
        c.frame.enterScope(False)
        c.frame.enterLoop()
        self.emit.printout(self.emit.emitLABEL(c.frame.getContinueLabel(), c.frame))    # emit continue label

        # loop contidtion
        exp, exp_type = self.visit(ast.exp, Access(c.frame, c.sym, False))
        self.emit.printout(exp) # condition expression
        self.emit.printout(self.emit.emitIFFALSE(c.frame.getBreakLabel(), c.frame)) # if condition false, go out loop

        # loop body
        local = deepcopy(c)
        local.frame = c.frame
        for vardecl in ast.sl[0]:
            local.sym.append(self.visit(vardecl, local))

        self.emit.printout(self.emit.emitLABEL(local.frame.getStartLabel(), local.frame))

        for stmt in ast.sl[1]:
            self.visit(stmt, local)

        self.emit.printout(self.emit.emitLABEL(local.frame.getEndLabel(), local.frame))

        # go to begin of loop
        self.emit.printout(self.emit.emitGOTO(c.frame.getContinueLabel(), c.frame))
        # emit end loop label
        self.emit.printout(self.emit.emitLABEL(c.frame.getBreakLabel(), c.frame))

        c.frame.exitLoop()
        c.frame.exitScope()

    def visitCallStmt(self,ast, c):
        for sym in c.sym:
            if sym.name == ast.method.name and isinstance(sym.mtype, MType):
                buffer = ""
                params = []
                for param in ast.param:
                    paramcode, paramtype = self.visit(param, Access(c.frame, c.sym, False))
                    buffer += paramcode
                buffer += self.emit.emitINVOKESTATIC(sym.value.value + "/" + sym.name, sym.mtype, c.frame)
                self.emit.printout(buffer)
                

    def visitBinaryOp(self,ast, c):
        left, ltype = self.visit(ast.left, Access(c.frame, c.sym, False))
        right, rtype = self.visit(ast.right, Access(c.frame, c.sym, False))
        if ast.op in ['+', '+.', '-', '-.']:
            return (left + right + self.emit.emitADDOP(ast.op[0], ltype, c.frame), ltype)
        elif ast.op in ['*', '*.', '\\', '\\.']:
            return (left + right + self.emit.emitMULOP(ast.op[0], ltype, c.frame), ltype)
        elif ast.op in ['%']:
            return (left + right + self.emit.emitMOD(c.frame), ltype)
        elif ast.op in ['&&']:  # short-circuit evaluation
            return (left + right + self.emit.emitANDOP(c.frame), BoolType())
        elif ast.op in ['||']:  # short-circuit evaluation
            return (left + right + self.emit.emitOROP(c.frame), BoolType())
        elif ast.op in ['>', '<', '>=', '<=', '==', '!=']:
            return (left + right + self.emit.emitREOP(ast.op, ltype, c.frame), BoolType())
        elif ast.op in ['>.', '<.', '>=.', '<=.']:
            return (left + right + self.emit.emitREOP(ast.op[:-1], ltype, c.frame), BoolType())
        elif ast.op in ['=/=']:
            return (left + right + self.emit.emitREOP('!=', ltype, c.frame), BoolType())

    def visitUnaryOp(self,ast, c):
        body, bodytype = self.visit(ast.body, c)
        if ast.op in ['-', '-.']:
            return (body + self.emit.emitNEGOP(bodytype, c.frame), bodytype)
        elif ast.op in ['!']:
            return (body + self.emit.emitNOT(IntType(), c.frame), bodytype)
    
    def visitCallExpr(self,ast, c):
        for sym in c.sym:
            if sym.name == ast.method.name and isinstance(sym.mtype, MType):
                buffer = ""
                params = []
                for param in ast.param:
                    paramcode, paramtype = self.visit(param, Access(c.frame, c.sym, False))
                    buffer += paramcode
                buffer += self.emit.emitINVOKESTATIC(sym.value.value + "/" + sym.name, sym.mtype, c.frame)
                # self.emit.printout(buffer)
                return (buffer, sym.mtype.rettype)

    def visitArrayCell(self,ast, c):
        pass

    def visitId(self,ast, c):
        for sym in c.sym:
            if sym.name == ast.name and not isinstance(sym.mtype, MType):
                if c.isLeft:    # Id in lhs
                    if isinstance(sym.value, Index):    # local variable
                        return (self.emit.emitWRITEVAR(sym.name, sym.mtype, sym.value.value, c.frame), sym.mtype)
                    elif isinstance(sym.value, CName):  # global variable
                        return (self.emit.emitPUTSTATIC(self.className + "/" + sym.name, sym.mtype, c.frame), sym.mtype)
                else:
                    if isinstance(sym.value, Index):    # local variable
                        return (self.emit.emitREADVAR(sym.name, sym.mtype, sym.value.value, c.frame), sym.mtype)
                    elif isinstance(sym.value, CName):  # global variable
                        return (self.emit.emitGETSTATIC(self.className + "/" + sym.name, sym.mtype, c.frame), sym.mtype)   

    def visitIntLiteral(self,ast, c):
        return (self.emit.emitPUSHICONST(str(ast.value), c.frame), IntType())

    def visitFloatLiteral(self,ast, c):
        return (self.emit.emitPUSHFCONST(str(ast.value), c.frame), FloatType())

    def visitStringLiteral(self,ast, c):
        return (self.emit.emitPUSHCONST(ast.value, StringType(), c.frame), StringType())

    def visitBooleanLiteral(self,ast, c):
        return (self.emit.emitPUSHICONST(str(ast.value), c.frame), BoolType())

    def visitArrayLiteral(self,ast, c):
        pass

    def push_value_on_stack(self, value, value_type, frame):
        if isinstance(value_type, IntType) or isinstance(value_type, BoolType):
            self.emit.printout(self.emit.emitPUSHICONST(value, frame))
        elif isinstance(value_type, FloatType):
            self.emit.printout(self.emit.emitPUSHFCONST(value, frame))
        elif isinstance(value_type, StringType):
            self.emit.printout(self.emit.emitPUSHCONST(value, value_type, frame))







































































# """
#  * @author nhphung
# """
# from abc import ABC, abstractmethod, ABCMeta
# from dataclasses import dataclass
# from typing import List, Tuple
# from AST import * 
# from Visitor import *
# from StaticError import *
# from functools import *
# from copy import deepcopy

# class Type(ABC):
#     __metaclass__ = ABCMeta
#     pass
# class Prim(Type):
#     __metaclass__ = ABCMeta
#     pass

# @dataclass
# class IntType(Prim):
#     _type: str = 'int'

# @dataclass
# class FloatType(Prim):
#     _type: str = 'float'

# @dataclass
# class StringType(Prim):
#     _type: str = 'string'

# @dataclass
# class BoolType(Prim):
#     _type: str = 'bool'

# @dataclass
# class VoidType(Type):
#     _type: str = 'void'

# @dataclass
# class Unknown(Type):
#     _type: str = 'unknown'


# @dataclass
# class ArrayType(Type):
#     dimen:List[int]
#     eletype: Type

# @dataclass
# class MType:
#     intype:List[Type]
#     restype:Type

# @dataclass
# class Symbol:
#     name: str
#     mtype:Type

# class StaticChecker(BaseVisitor):
#     def __init__(self,ast):
#         self.ast = ast
#         self.global_envi = [
# Symbol("int_of_float",MType([FloatType()],IntType())),
# Symbol("float_to_int",MType([IntType()],FloatType())),
# Symbol("int_of_string",MType([StringType()],IntType())),
# Symbol("string_of_int",MType([IntType()],StringType())),
# Symbol("float_of_string",MType([StringType()],FloatType())),
# Symbol("string_of_float",MType([FloatType()],StringType())),
# Symbol("bool_of_string",MType([StringType()],BoolType())),
# Symbol("string_of_bool",MType([BoolType()],StringType())),
# Symbol("read",MType([],StringType())),
# Symbol("printLn",MType([],VoidType())),
# Symbol("print",MType([StringType()],VoidType())),
# Symbol("printStrLn",MType([StringType()],VoidType()))]                      
   
#     def check(self):
#         return self.visit(self.ast,self.global_envi)

#     def visitProgram(self,ast, c):
#         for decl in ast.decl:
#             if isinstance(decl, VarDecl):
#                 self.visit(decl, c)
#             else:
#                 funcname = decl.name.name
#                 intype_lst = []
#                 for param in decl.param:
#                     paramtype = Unknown() if param.varDimen == [] else ArrayType(deepcopy(param.varDimen), Unknown())
#                     intype_lst.append(paramtype)
#                 c.append(Symbol(funcname, MType(intype_lst, Unknown())))
                
#         for decl in ast.decl:
#             if isinstance(decl, FuncDecl):
#                 self.visit(decl, c)


#     def visitVarDecl(self,ast, c):
#         idname = ast.variable.name
#         idtype = Unknown() if not ast.varInit else self.visit(ast.varInit, c)
#         if ast.varDimen != []:  # array type
#             if idtype == Unknown():
#                 idtype = ArrayType(deepcopy(ast.varDimen), Unknown())
#         c.append(Symbol(idname, idtype))


#     def visitFuncDecl(self,ast, c):
#         # visit param
#         param_envir = []
#         for param in ast.param:
#             paramname = param.variable.name
#             paramtype = Unknown() if param.varDimen == [] else ArrayType(deepcopy(param.varDimen), Unknown())
#             param_envir.append(Symbol(paramname, paramtype))
      
#         # update param of this function from outer environment
#         for index in range(len(param_envir)):
#             param_envir[index].mtype = self.symbol(ast.name.name, c).mtype.intype[index]

#         # visit local var declare
#         local_envir = deepcopy(param_envir)
#         for vardecl in ast.body[0]:
#             self.visit(vardecl, local_envir)
        
#         # visit statement
#         total_envir = deepcopy(local_envir)
#         for name in self.nameList(c):
#             if name not in self.nameList(local_envir):
#                 total_envir.append(self.symbol(name,c))


#         total_envir.append(Symbol("Current Function", self.symbol(ast.name.name, c).mtype))
#         current_function = self.symbol(ast.name.name, total_envir)
#         del total_envir[self.index(ast.name.name, total_envir)]
#         total_envir.append(current_function)   # append current function to the end of dictionary
#         # visit stmt
#         for stmt in ast.body[1]:
#             result = self.visit(stmt, total_envir)

#             # type inference for function parameters
#             if isinstance(total_envir[-1].mtype, MType): # current function is not hiden in local scope (by same name variable)
#                 for index in range(len(param_envir)):
#                     type1 = total_envir[index].mtype
#                     type2 = self.symbol(total_envir[-1].name, total_envir).mtype.intype[index]
#                     type1, type2 = self.mutual_infer(type1=type1, type2=type2)
#                     total_envir[index].mtype = type1
#                     self.symbol(total_envir[-1].name, total_envir).mtype.intype[index] = type2

#                     self.symbol("Current Function", total_envir).mtype.intype[index] = type2

#         # update global environment
#         for name in self.nameList(c):
#             if name not in self.nameList(local_envir):
#                 self.symbol(name, c).mtype = self.symbol(name, total_envir).mtype
#             else:
#                 if not isinstance(self.symbol(total_envir[-1].name, total_envir).mtype, MType):
#                     self.symbol(total_envir[-1].name, c).mtype.restype = self.symbol("Current Function", total_envir).mtype.restype

#         if self.symbol(total_envir[-1].name, c).mtype.restype == Unknown():
#             self.symbol(total_envir[-1].name, c).mtype.restype = VoidType()


#     def visitAssign(self,ast, c):   # left hand side can be in any type except VoidType
#         ltype = self.visit(ast.lhs, c)
#         rtype = self.visit(ast.rhs, c)
#         ltype = self.visit(ast.lhs, c)

#         # type inference
#         ltype, rtype = self.mutual_infer(type1=ltype, type2=rtype)
#         # lhs type update
#         self.direct_infer(e=ast.lhs, inferred_type=ltype, c=c)
#         # rhs type update
#         self.direct_infer(e=ast.rhs, inferred_type=rtype, c=c)
        

#     def visitIf(self,ast, c):
#         current_function_name = c[-1].name
#         for ifthenstmt in ast.ifthenStmt:
#             # visit condition expression
#             exptype = self.visit(ifthenstmt[0], c)
#             if exptype == Unknown():    # exp is Id, CallExpr, ArrayCell
#                 exptype = BoolType()
#                 self.direct_infer(e=ifthenstmt[0], inferred_type=exptype, c=c)

#             # visit if/elif local var declare
#             local_envir = []
#             for vardecl in ifthenstmt[1]:
#                 self.visit(vardecl, local_envir)

#             # visit if/elif statement
#             total_envir = deepcopy(c)
#             for name in self.nameList(local_envir):
#                 if name in self.nameList(c):
#                     self.symbol(name, total_envir).mtype = self.symbol(name, local_envir).mtype
#                 else:
#                     total_envir.append(self.symbol(name, local_envir))
#             current_function = self.symbol(current_function_name, total_envir)
#             del total_envir[self.index(current_function_name, total_envir)]
#             total_envir.append(current_function)   # append current function to the end of dictionary

#             # visit stmt
#             for stmt in ifthenstmt[2]:
#                 self.visit(stmt, total_envir)

#             # update outer environment
#             for name in self.nameList(c):
#                 if name not in self.nameList(local_envir):
#                     self.symbol(name, c).mtype = self.symbol(name, total_envir).mtype
        
#         # visit else local var declare
#         local_envir = []
#         for vardecl in ast.elseStmt[0]:
#             self.visit(vardecl, local_envir)

#         # visit else statement
#         total_envir = deepcopy(c)
#         for name in self.nameList(local_envir):
#             if name in self.nameList(c):
#                 self.symbol(name, total_envir).mtype = self.symbol(name, local_envir).mtype
#             else:
#                 total_envir.append(self.symbol(name, local_envir))
#         current_function = self.symbol(current_function_name, total_envir)
#         del total_envir[self.index(current_function_name, total_envir)]
#         total_envir.append(current_function)   # append current function to the end of dictionary

#         # visit stmt
#         for stmt in ast.elseStmt[1]:
#             self.visit(stmt, total_envir)
        
#         # update outer environment
#         for name in self.nameList(c):
#             if name not in self.nameList(local_envir):
#                 self.symbol(name, c).mtype = self.symbol(name, total_envir).mtype

    

#     def visitFor(self,ast, c):
#         # visit scalar variable
#         indextype = self.visit(ast.idx1, c)
#         if indextype == Unknown():
#             indextype = IntType()
#             self.symbol(ast.idx1.name, c).mtype = indextype

#         # visit initExpr (expr1)
#         exptype1 = self.visit(ast.expr1, c)
#         if exptype1 == Unknown():    # exp is Id, CallExpr, ArrayCell
#             exptype1 = IntType()
#             self.direct_infer(e=ast.expr1, inferred_type=exptype1, c=c)

#         # visit conditionExpr (expr2)
#         exptype2 = self.visit(ast.expr2, c)
#         if exptype2 == Unknown():    # exp is Id, CallExpr, ArrayCell
#             exptype2 = BoolType()
#             self.direct_infer(e=ast.expr2, inferred_type=exptype2, c=c)

#         # visit updateExpr(expr3)
#         exptype3 = self.visit(ast.expr3, c)
#         if exptype3 == Unknown():    # exp is Id, CallExpr, ArrayCell
#             exptype3 = IntType()
#             self.direct_infer(e=ast.expr3, inferred_type=exptype3, c=c)

#         # visit local (For body) var declare
#         local_envir = []
#         for vardecl in ast.loop[0]:
#             self.visit(vardecl, local_envir)

#         # visit local statement
#         total_envir = deepcopy(c)
#         for name in self.nameList(local_envir):
#             if name in self.nameList(c):
#                 self.symbol(name, total_envir).mtype = self.symbol(name, local_envir).mtype
#             else:
#                 total_envir.append(self.symbol(name, local_envir))
#         current_function_name = c[-1].name
#         current_function = self.symbol(current_function_name, total_envir)
#         del total_envir[self.index(current_function_name, total_envir)]
#         total_envir.append(current_function)   # append current function to the end of dictionary

#         # visit stmt
#         for stmt in ast.loop[1]:
#             self.visit(stmt, total_envir)

#         # update outer environment
#         for name in self.nameList(c):
#             if name not in self.nameList(local_envir):
#                 self.symbol(name, c).mtype = self.symbol(name, total_envir).mtype


#     def visitBreak(self,ast, c):
#         pass

#     def visitContinue(self,ast, c):
#         pass

#     def visitReturn(self,ast, c):
#         returntype = VoidType() if ast.expr == None else self.visit(ast.expr, c)
#         current_returntype = self.symbol("Current Function", c).mtype.restype

#         # type inference
#         current_returntype, returntype = self.mutual_infer(type1=current_returntype, type2=returntype)
#         # current return type update
#         self.symbol("Current Function", c).mtype.restype = current_returntype
#         if isinstance(c[-1].mtype, MType):
#             self.symbol(c[-1].name, c).mtype.restype = current_returntype
#         # expr type update 
#         self.direct_infer(e=ast.expr, inferred_type=returntype, c=c)


#     def visitDowhile(self,ast, c):
#         # visit local (DoWhile body) var declare
#         local_envir = []
#         for vardecl in ast.sl[0]:
#             self.visit(vardecl, local_envir)

#         # visit local statement
#         total_envir = deepcopy(c)
#         for name in self.nameList(local_envir):
#             if name in self.nameList(c):
#                 self.symbol(name, total_envir).mtype = self.symbol(name, local_envir).mtype
#             else:
#                 total_envir.append(self.symbol(name, local_envir))
#         current_function_name = c[-1].name
#         current_function = self.symbol(current_function_name, total_envir)
#         del total_envir[self.index(current_function_name, total_envir)]
#         total_envir.append(current_function)   # append current function to the end of dictionary

#         # visit stmt
#         for stmt in ast.sl[1]:
#             self.visit(stmt, total_envir)

#         # update outer environment
#         for name in self.nameList(c):
#             if name not in self.nameList(local_envir):
#                 self.symbol(name, c).mtype = self.symbol(name, total_envir).mtype

#         # visit expression
#         exptype = self.visit(ast.exp, c)
#         if exptype == Unknown():    # exp is Id, CallExpr, ArrayCell
#             exptype = BoolType()
#             self.direct_infer(e=ast.exp, inferred_type=exptype, c=c)


#     def visitWhile(self,ast, c):
#         # visit expression
#         exptype = self.visit(ast.exp, c)
#         if exptype == Unknown():    # exp is Id, CallExpr, ArrayCell
#             exptype = BoolType()
#             self.direct_infer(e=ast.exp, inferred_type=exptype, c=c)

#         # visit local (While body) var declare
#         local_envir = []
#         for vardecl in ast.sl[0]:
#             self.visit(vardecl, local_envir)

#         # visit local statement
#         total_envir = deepcopy(c)
#         for name in self.nameList(local_envir):
#             if name in self.nameList(c):
#                 self.symbol(name, total_envir).mtype = self.symbol(name, local_envir).mtype
#             else:
#                 total_envir.append(self.symbol(name, local_envir))
#         current_function_name = c[-1].name
#         current_function = self.symbol(current_function_name, total_envir)
#         del total_envir[self.index(current_function_name, total_envir)]
#         total_envir.append(current_function)   # append current function to the end of dictionary

#         # visit stmt
#         for stmt in ast.sl[1]:
#             self.visit(stmt, total_envir)

#         # update outer environment
#         for name in self.nameList(c):
#             if name not in self.nameList(local_envir):
#                 self.symbol(name, c).mtype = self.symbol(name, total_envir).mtype


#     def visitCallStmt(self,ast, c):
#         for i in range(len(ast.param)):
#             type2 = self.visit(ast.param[i], c)     # argument type
#             type1 = self.symbol(ast.method.name, c).mtype.intype[i]    # param type
#             # type inference
#             type1, type2 = self.mutual_infer(type1=type1, type2=type2)
#             # param type update
#             self.symbol(ast.method.name, c).mtype.intype[i] = type1
#             # argument type update 
#             self.direct_infer(e=ast.param[i], inferred_type=type2, c=c)

#             # if func call inside the same func declare
#             # update param of declared function in every agument iteration
#             if ast.method.name == c[-1].name and isinstance(c[-1].mtype, MType):
#                 for j in range(len(ast.param)):
#                     type1 = self.symbol(ast.method.name, c).mtype.intype[j]
#                     type2 = c[j].mtype
#                     self.symbol(ast.method.name, c).mtype.intype[j], c[j].mtype = self.mutual_infer(type1=type1, type2=type2)

#                     self.symbol("Current Function", c).mtype.intype[j] = self.symbol(ast.method.name, c).mtype.intype[j]

#         # check/infer return type
#         if self.symbol(ast.method.name, c).mtype.restype == Unknown():
#             self.symbol(ast.method.name, c).mtype.restype = VoidType()


#     def visitBinaryOp(self,ast, c):
#         typedict = {}
#         typedict.update({operator: {'operand_type': IntType(), 'return_type': IntType()} for operator in ['+', '-', '*', '\\', '%']})
#         typedict.update({operator: {'operand_type': IntType(), 'return_type': BoolType()} for operator in ['==', '!=', '<', '>', '<=', '>=']})
#         typedict.update({operator: {'operand_type': FloatType(), 'return_type': FloatType()} for operator in ['+.', '-.', '*.', '\\.']})
#         typedict.update({operator: {'operand_type': FloatType(), 'return_type': BoolType()} for operator in ['=/=', '<.', '>.', '<=.', '>=.']})
#         typedict.update({operator: {'operand_type': BoolType(), 'return_type': BoolType()} for operator in ['&&', '||']})
        
#         # lhs type inference
#         ltype = self.visit(ast.left, c)
#         if ltype == Unknown():
#             ltype = typedict[ast.op]['operand_type']
#             self.direct_infer(e=ast.left, inferred_type=ltype, c=c)

#         # rhs type inference
#         rtype = self.visit(ast.right, c)
#         if rtype == Unknown():
#             rtype = typedict[ast.op]['operand_type']
#             self.direct_infer(e=ast.right, inferred_type=rtype, c=c)

#         return typedict[ast.op]['return_type']


#     def visitUnaryOp(self,ast, c):
#         typedict = {
#             '-': {'operand_type': IntType(), 'return_type': IntType()},
#             '-.': {'operand_type': FloatType(), 'return_type': FloatType()},
#             '!': {'operand_type': BoolType(), 'return_type': BoolType()}
#         }

#         # type inference
#         exptype = self.visit(ast.body, c)
#         if exptype == Unknown():
#             exptype = typedict[ast.op]['operand_type']
#             self.direct_infer(e=ast.body, inferred_type=exptype, c=c)

#         return typedict[ast.op]['return_type']
    
                
#     # check intype
#     # return restype
#     def visitCallExpr(self,ast, c):
#         for i in range(len(ast.param)):
#             type2 = self.visit(ast.param[i], c)     # argument type
#             type1 = self.symbol(ast.method.name, c).mtype.intype[i]    # param type
#             # type inference
#             type1, type2 = self.mutual_infer(type1=type1, type2=type2)
#             # param type update
#             self.symbol(ast.method.name, c).mtype.intype[i] = type1
#             # argument type update 
#             self.direct_infer(e=ast.param[i], inferred_type=type2, c=c)

#             # if func call inside the same func declare
#             # update param of declared function in every agument iteration
#             if ast.method.name == c[-1].name and isinstance(c[-1].mtype, MType):
#                 for j in range(len(ast.param)):
#                     type1 = self.symbol(ast.method.name, c).mtype.intype[j]
#                     type2 = c[j].mtype
#                     self.symbol(ast.method.name, c).mtype.intype[j], c[j].mtype = self.mutual_infer(type1=type1, type2=type2)

#                     self.symbol("Current Function", c).mtype.intype[j] = self.symbol(ast.method.name, c).mtype.intype[j]
        
#         return self.symbol(ast.method.name, c).mtype.restype

#     # check Undeclare, check index
#     # return innermost eletype
#     def visitArrayCell(self,ast, c):
#         for i in range(len(ast.idx)):
#             index = ast.idx[i]
#             indextype = self.visit(index, c)
#             if indextype == Unknown():  # index is Id or CallExpr or ArrayCell
#                 indextype = IntType()
#                 self.direct_infer(e=index, inferred_type=indextype, c=c)

#         return self.visit(ast.arr, c).eletype


#     def visitId(self,ast, c):
#         return self.symbol(ast.name, c).mtype


#     def visitIntLiteral(self,ast, c):
#         return IntType()

#     def visitFloatLiteral(self,ast, c):
#         return FloatType()

#     def visitStringLiteral(self,ast, c):
#         return StringType()

#     def visitBooleanLiteral(self,ast, c):
#         return BoolType()

#     def visitArrayLiteral(self,ast, c):
#         eletype = Unknown()
#         dimen = [len(ast.value)]
#         innertype = Unknown()
#         innerdimen = []
#         for ele in ast.value:
#             inner_ele_type = self.visit(ele, c)
#             innertype = inner_ele_type
#             if isinstance(ele, ArrayLiteral):
#                 eletype = innertype.eletype
#                 innerdimen = innertype.dimen
#             else:
#                 eletype = innertype
#         dimen += innerdimen
#         return ArrayType(dimen, eletype)

    
#     # Support methods
#     def symbol(self, name, lst):
#         for symbol in lst:
#             if symbol.name == name:
#                 return symbol
#         return None

#     def index(self, name, lst):
#         for index in range(len(lst)):
#             if lst[index].name == name:
#                 return index
#         return None

#     def nameList(self, lst):
#         return [symbol.name for symbol in lst]


#     def mutual_infer(self, type1, type2):
#         if type1 == Unknown() and type2 != Unknown():
#             type1 = type2
#         elif type1 != Unknown() and type2 == Unknown():
#             type2 = type1
#         elif type1 != Unknown() and type2 != Unknown():
#             if isinstance(type1, ArrayType) and isinstance(type2, ArrayType):
#                 if type1.eletype == Unknown() and type2.eletype != Unknown():
#                     type1.eletype = type2.eletype
#                 elif type1.eletype != Unknown() and type2.eletype == Unknown():
#                     type2.eletype = type1.eletype
        
#         return (type1, type2)

    
#     def direct_infer(self, e, inferred_type, c):
#         if isinstance(e, Id):
#             self.symbol(e.name, c).mtype = inferred_type
#         elif isinstance(e, CallExpr):
#             self.symbol(e.method.name, c).mtype.restype = inferred_type
#         elif isinstance(e, ArrayCell):
#             if isinstance(e.arr, Id):
#                 self.symbol(e.arr.name, c).mtype.eletype = inferred_type
#             elif isinstance(e.arr, CallExpr):
#                 self.symbol(e.arr.method.name, c).mtype.restype.eletype = inferred_type  