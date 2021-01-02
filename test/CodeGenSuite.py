import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # Predefined testcases
    def test_int(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        print(string_of_int(120));
                   EndBody."""
        expect = "120"
        self.assertTrue(TestCodeGen.test(input,expect,500))
    def test_int_ast(self):
    	input = Program([
    		FuncDecl(Id("main"),[],([],[
    			CallStmt(Id("print"),[
                    CallExpr(Id("string_of_int"),[IntLiteral(120)])])]))])
    	expect = "120"
    	self.assertTrue(TestCodeGen.test(input,expect,501))

    # test binop
    def test_binop_01(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        print(string_of_int(5 + 6));
                   EndBody."""
        expect = "11"
        self.assertTrue(TestCodeGen.test(input,expect,502))

    def test_binop_02(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        print(string_of_int(5 - 6));
                   EndBody."""
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input,expect,503))

    def test_binop_03(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        print(string_of_int(5 * 6));
                   EndBody."""
        expect = "30"
        self.assertTrue(TestCodeGen.test(input,expect,504))

    def test_binop_04(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        print(string_of_int(10 \\ 3));
                   EndBody."""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,505))

    def test_binop_05(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        print(string_of_int(10 % 3));
                   EndBody."""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,506))

    def test_binop_06(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        print(string_of_int(5 + 6 \\ 4 - 2 * 3 + 7 % 2));
                   EndBody."""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,507))

    def test_binop_07(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6;
                        print(string_of_int(5 + x));
                   EndBody."""
        expect = "11"
        self.assertTrue(TestCodeGen.test(input,expect,508))

    def test_binop_08(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6;
                        print(string_of_int(5 + x \\ 4 - 2 * 3 + 7 % 2));
                   EndBody."""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,509))

    def test_binop_09(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6.5;
                        print(string_of_float(5.5 +. x));
                   EndBody."""
        expect = "12.0"
        self.assertTrue(TestCodeGen.test(input,expect,510))

    def test_binop_10(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6.5;
                        print(string_of_float(5.5 +. x -. float_to_int(4)));
                   EndBody."""
        expect = "8.0"
        self.assertTrue(TestCodeGen.test(input,expect,511))

    def test_binop_11(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6.5;
                        print(string_of_float((5.5 +. x) \. float_to_int(4)));
                   EndBody."""
        expect = "3.0"
        self.assertTrue(TestCodeGen.test(input,expect,512))

    def test_binop_12(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = True;
                        print(string_of_bool(x));
                   EndBody."""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,513))

    def test_binop_13(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6;
                        print(string_of_bool(x > 5));
                   EndBody."""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,514))

    def test_binop_14(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6.5;
                        print(string_of_bool(x >. 5.5));
                   EndBody."""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,515))

    def test_binop_15(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6.5;
                        print(string_of_bool(!(x >. 5.5)));
                   EndBody."""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,516))

    def test_binop_16(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6;
                        print(string_of_bool(x != 5));
                   EndBody."""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,517))

    def test_binop_17(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6;
                        print(string_of_bool(x == 6));
                   EndBody."""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,518))

    def test_binop_18(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6.6;
                        print(string_of_bool(x =/= 6.5));
                   EndBody."""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,519))

    # test unop
    def test_unop_1(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6.6;
                        print(string_of_int(5 + ---6));
                   EndBody."""
        expect = "-1"
        self.assertTrue(TestCodeGen.test(input,expect,520))  

    def test_unop_2(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6;
                        print(string_of_float(5.5 +. -.-.-.float_to_int(x)));
                   EndBody."""
        expect = "-0.5"
        self.assertTrue(TestCodeGen.test(input,expect,521))

    # test assign
    def test_assign_1(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6, y = 5;
                        x = x + y - 1;
                        print(string_of_int(x));
                   EndBody."""
        expect = "10"
        self.assertTrue(TestCodeGen.test(input,expect,522))  

    def test_assign_2(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6, y = 5.5;
                        x = x \\ 2 + int_of_float(y) * 2 - 1;
                        print(string_of_int(x));
                   EndBody."""
        expect = "12"
        self.assertTrue(TestCodeGen.test(input,expect,523))  

    def test_assign_3(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6, y = 5.5, z = 4;
                        x = int_of_float(y) + x - z;
                        print(string_of_int(x));
                   EndBody."""
        expect = "7"
        self.assertTrue(TestCodeGen.test(input,expect,524))

    # test if stmt
    def test_if_1(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6;
                        If (x % 2 == 0) Then
                            x = 0;
                        Else
                            x = 1;
                        EndIf.
                        print(string_of_int(x));
                   EndBody."""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,525))    

    def test_if_2(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 5;
                        If (x % 4 == 0) Then
                            x = 0;
                        ElseIf (x % 4 == 1) Then
                            x = 1;
                        ElseIf (x % 4 == 2) Then
                            x = 2;
                        Else
                            x = 3;
                        EndIf.
                        print(string_of_int(x));
                   EndBody."""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,526)) 

    def test_if_3(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 6;
                        If (x % 4 == 0) Then
                            x = 0;
                        ElseIf (x % 4 == 1) Then
                            x = 1;
                        ElseIf (x % 4 == 2) Then
                            x = 2;
                        Else
                            x = 3;
                        EndIf.
                        print(string_of_int(x));
                   EndBody."""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,527))


    def test_if_4(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 7;
                        If (x % 4 == 0) Then
                            x = 0;
                        ElseIf (x % 4 == 1) Then
                            x = 1;
                        ElseIf (x % 4 == 2) Then
                            x = 2;
                        Else
                            x = 3;
                        EndIf.
                        print(string_of_int(x));
                   EndBody."""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,528))

    def test_if_5(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 8;
                        If (x % 4 == 0) Then
                            Var: y = 0;
                            x = y;
                        ElseIf (x % 4 == 1) Then
                            Var: y = 1;
                            x = y;
                        ElseIf (x % 4 == 2) Then
                            Var: y = 2;
                            x = y;
                        Else
                            Var: y = 3;
                            x = y;
                        EndIf.
                        print(string_of_int(x));
                   EndBody."""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,529))

    def test_if_6(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 7;
                        If (x % 4 == 0) Then
                            Var: y = 0;
                            x = y;
                        ElseIf (x % 4 == 1) Then
                            Var: y = 1;
                            x = y;
                        ElseIf (x % 4 == 2) Then
                            Var: y = 2;
                            x = y;
                        Else
                            Var: y = 3;
                            x = y;
                        EndIf.
                        print(string_of_int(x));
                   EndBody."""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,530))

    def test_if_7(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 5;
                        If (x % 4 == 0) Then
                            Var: y = 0;
                            x = y;
                        ElseIf (x % 4 == 1) Then
                            Var: y = 1;
                            x = y;
                        ElseIf (x % 4 == 2) Then
                            Var: y = 2;
                            x = y;
                        Else
                            Var: y = 3;
                            x = y;
                        EndIf.
                        print(string_of_int(x));
                   EndBody."""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,531))

    # test while
    def test_while_1(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 5, y = 3;
                        While (y > 0) Do
                            x = x + 1;
                            y = y - 1;
                        EndWhile.
                        print(string_of_int(x));
                        print(string_of_int(y));
                   EndBody."""
        expect = "80"
        self.assertTrue(TestCodeGen.test(input,expect,532))  

    def test_while_2(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 5, y = 3;
                        While (y > 0) Do
                            x = x + y;
                            y = y - 1;
                        EndWhile.
                        printStrLn(string_of_int(x));
                        print(string_of_int(y));
                   EndBody."""
        expect = "11\n0"
        self.assertTrue(TestCodeGen.test(input,expect,533))

    # test dowhile
    def test_dowhile_1(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 5, y = 3;
                        Do
                            x = x + 1;
                            y = y - 1;
                        While (y > 0)
                        EndDo.
                        print(string_of_int(x));
                        print(string_of_int(y));
                   EndBody."""
        expect = "80"
        self.assertTrue(TestCodeGen.test(input,expect,534))  

    def test_dowhile_2(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 5, y = 3;
                        Do
                            x = x + y;
                            y = y - 1;
                        While (y > 0)
                        EndDo.
                        printStrLn(string_of_int(x));
                        print(string_of_int(y));
                   EndBody."""
        expect = "11\n0"
        self.assertTrue(TestCodeGen.test(input,expect,535))

    # test break
    def test_break_1(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 0;
                        While (x < 10) Do
                            If (x == 5) Then
                                Break;
                            EndIf.
                            print(string_of_int(x));
                            x = x + 1;
                        EndWhile.
                   EndBody."""
        expect = "01234"
        self.assertTrue(TestCodeGen.test(input,expect,536))

    # test continue
    def test_continue_1(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 0;
                        While (x < 10) Do
                            If (x % 2 == 0) Then
                                x = x + 1;
                                Continue;
                            EndIf.
                            print(string_of_int(x));
                            x = x + 1;
                        EndWhile.
                   EndBody."""
        expect = "13579"
        self.assertTrue(TestCodeGen.test(input,expect,537))

    # test for
    def test_for_1(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 0;
                        For (x = 1, x <= 5, 1) Do
                            print(string_of_int(x));
                        EndFor.
                   EndBody."""
        expect = "12345"
        self.assertTrue(TestCodeGen.test(input,expect,538))

    def test_for_2(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x = 0;
                        For (x = 1, x <= 10, 1) Do
                            If (x % 2 == 0) Then
                                printStrLn(string_of_int(x));
                            EndIf.
                        EndFor.
                   EndBody."""
        expect = "2\n4\n6\n8\n10\n"
        self.assertTrue(TestCodeGen.test(input,expect,539))

    # test funcdecl
    def test_funcdecl_1(self):
        """Simple program: int main() {} """
        input = """
                Function: foo
                Body:
                    print(string_of_int(1));
                EndBody.
                Function: main
                   Body: 
                        foo();
                   EndBody."""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,540))

    def test_funcdecl_2(self):
        """Simple program: int main() {} """
        input = """
                Function: foo
                Parameter: x
                Body:
                    print(string_of_int(x));
                EndBody.
                Function: main
                   Body: 
                        foo(1);
                   EndBody."""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,541))

    def test_funcdecl_3(self):
        """Simple program: int main() {} """
        input = """
                Var: x = 0;
                Function: foo
                    Body:
                        x = 1;
                    EndBody.
                Function: main
                    Body: 
                        foo();
                        print(string_of_int(x));
                    EndBody."""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,542))

    def test_funcdecl_4(self):
        """Simple program: int main() {} """
        input = """
                Var: x = 0;
                Function: main
                    Body: 
                        foo();
                        print(string_of_int(x));
                    EndBody.
                Function: foo
                    Body:
                        x = 1;
                    EndBody."""
        expect = "1"
        self.assertTrue(TestCodeGen.test(input,expect,543))

    def test_funcdecl_5(self):
        """Simple program: int main() {} """
        input = """
                Var: x = 0;
                Function: goo
                    Body:
                        print(string_of_int(x));
                        x = 2;
                    EndBody.
                Function: main
                    Body: 
                        foo();
                        print(string_of_int(x));
                    EndBody.
                Function: foo
                    Body:
                        print(string_of_int(x));
                        x = 1;
                        goo();
                    EndBody."""
        expect = "012"
        self.assertTrue(TestCodeGen.test(input,expect,544))

    def test_funcdecl_6(self):
        """Simple program: int main() {} """
        input = """
                Var: x = "Hello World";
                Function: main
                    Body:
                        foo();
                        print(x);
                    EndBody.
                Function: foo
                    Body:
                        x = "My name is Long";
                    EndBody."""
        expect = "My name is Long"
        self.assertTrue(TestCodeGen.test(input,expect,545))

    # test return
    def test_return_1(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: a = 1, b = 2;
                        print(string_of_int(sum(a, b)));
                    EndBody.
                Function: sum
                    Parameter: x, y
                    Body:
                        Return x + y;
                    EndBody."""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,546))

    def test_return_2(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: a = 1.5, b = 2.0;
                        print(string_of_float(foo(a, b)));
                    EndBody.
                Function: sum
                    Parameter: x, y
                    Body:
                        Return x +. y;
                    EndBody.
                Function: foo
                    Parameter: x, y
                    Body:
                        Return sum(x, y);
                    EndBody."""
        expect = "3.5"
        self.assertTrue(TestCodeGen.test(input,expect,547))

    def test_return_3(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: a = 1, b = 2;
                        foo(a, b);
                    EndBody.
                Function: foo
                    Parameter: x, y
                    Body:
                        print(string_of_int(x + y));
                        Return;
                    EndBody."""
        expect = "3"
        self.assertTrue(TestCodeGen.test(input,expect,548))

    def test_return_4(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        print(foo());
                    EndBody.
                Function: foo
                    Body:
                        Return "Hello World";
                    EndBody."""
        expect = "Hello World"
        self.assertTrue(TestCodeGen.test(input,expect,549))