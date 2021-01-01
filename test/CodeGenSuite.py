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