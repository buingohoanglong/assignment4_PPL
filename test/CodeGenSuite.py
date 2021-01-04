import unittest
from TestUtils import TestCodeGen
from AST import *


class CheckCodeGenSuite(unittest.TestCase):
    # test operand stack
    def test_operand_stack_1(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x[2][2] = {{1.1,2.2},{3.3,4.4}};
                        print(string_of_float(x[0][0]));
                   EndBody."""
        expect = "1.1"
        self.assertTrue(TestCodeGen.test(input,expect,500))

    def test_operand_stack_2(self):
        """Simple program: int main() {} """
        input = """Function: main
                   Body: 
                        Var: x[2][2] = {{"a","b"},{"c","d"}};
                        print(x[0][0]);
                   EndBody."""
        expect = "a"
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
                            If (x % 2 == 1) Then
                                Continue;
                            EndIf.
                            printStrLn(string_of_int(x));
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

    def test_return_5(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: x = 5;
                        print(string_of_bool(is_equal(x + 1, 6)));
                    EndBody.
                Function: is_equal
                    Parameter: x, y
                    Body:
                        Return x == y;
                    EndBody."""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,550))

    # test array
    def test_array_1(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: x[3] = {1,2,3};
                        print(string_of_int(x[1]));
                    EndBody."""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,551))

    def test_array_2(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: x[3] = {1,2,3};
                        x = {4,5,6};
                        print(string_of_int(x[1]));
                    EndBody."""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,552))

    def test_array_3(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: x[3] = {1,2,3};
                        x[1] = 4;
                        print(string_of_int(x[1]));
                    EndBody."""
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,553))

    def test_array_4(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                   Body: 
                        Var: x[3] = {1,2,3}, i = 0;
                        x[1] = x[0] + x[2];
                        For (i = 0, i < 3, 1) Do
                            print(string_of_int(x[i]));
                        EndFor.
                   EndBody."""
        expect = "143"
        self.assertTrue(TestCodeGen.test(input,expect,554))

    def test_array_5(self):
        """Simple program: int main() {} """
        input = """
                Var: x[5] = {1,2,3,4,5};
                Function: main
                   Body: 
                        Var: i = 0;
                        For (i = 0, i < 5, 1) Do
                            x[i] = x[i] * 2 + 1;
                        EndFor.
                        For (i = 0, i < 5, 1) Do
                            print(string_of_int(x[i]));
                        EndFor.
                   EndBody."""
        expect = "357911"
        self.assertTrue(TestCodeGen.test(input,expect,555))

    def test_array_6(self):
        """Simple program: int main() {} """
        input = """
                Var: x[3] = {1,2,3};
                Function: main
                   Body: 
                        Var: i = 0;
                        x = {4,5,6};
                        For (i = 0, i < 3, 1) Do
                            x[i] = x[i] * 2 + 1;
                        EndFor.
                        For (i = 0, i < 3, 1) Do
                            print(string_of_int(x[i]));
                        EndFor.
                   EndBody."""
        expect = "91113"
        self.assertTrue(TestCodeGen.test(input,expect,556))

    def test_array_7(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: x[3] = {1.1,2.2,3.3};
                        print(string_of_float(x[1]));
                    EndBody."""
        expect = "2.2"
        self.assertTrue(TestCodeGen.test(input,expect,557))

    def test_array_8(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: x[3] = {1.1,2.2,3.3};
                        x = {4.4,5.5,6.6};
                        print(string_of_float(x[1]));
                    EndBody."""
        expect = "5.5"
        self.assertTrue(TestCodeGen.test(input,expect,558))

    def test_array_9(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: x[3] = {1.1,2.2,3.3};
                        x[1] = 4.4;
                        print(string_of_float(x[1]));
                    EndBody."""
        expect = "4.4"
        self.assertTrue(TestCodeGen.test(input,expect,559))

    def test_array_10(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                   Body: 
                        Var: x[3] = {1.1,2.2,3.3}, i = 0;
                        x[1] = x[0] +. x[2];
                        For (i = 0, i < 3, 1) Do
                            print(string_of_float(x[i]));
                        EndFor.
                   EndBody."""
        expect = "1.14.43.3"
        self.assertTrue(TestCodeGen.test(input,expect,560))

    def test_array_11(self):
        """Simple program: int main() {} """
        input = """
                Var: x[5] = {1.1,2.2,3.3,4.4,5.5};
                Function: main
                   Body: 
                        Var: i = 0;
                        For (i = 0, i < 5, 1) Do
                            x[i] = x[i] *. float_to_int(2) +. 1.0;
                        EndFor.
                        For (i = 0, i < 5, 1) Do
                            print(string_of_float(x[i]));
                        EndFor.
                   EndBody."""
        expect = "3.25.47.69.812.0"
        self.assertTrue(TestCodeGen.test(input,expect,561))

    def test_array_12(self):
        """Simple program: int main() {} """
        input = """
                Var: x[3] = {1.1,2.2,3.3};
                Function: main
                   Body: 
                        Var: i = 0;
                        x = {4.4,5.5,6.6};
                        For (i = 0, i < 3, 1) Do
                            x[i] = x[i] *. 2.0 +. 1.0;
                        EndFor.
                        For (i = 0, i < 3, 1) Do
                            print(string_of_float(x[i]));
                        EndFor.
                   EndBody."""
        expect = "9.812.014.2"
        self.assertTrue(TestCodeGen.test(input,expect,562))

    def test_array_13(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: x[3] = {True,False,True};
                        print(string_of_bool(x[1]));
                    EndBody."""
        expect = "false"
        self.assertTrue(TestCodeGen.test(input,expect,563))

    def test_array_14(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: x[3] = {True,False,True};
                        x = {False,True,False};
                        print(string_of_bool(x[1]));
                    EndBody."""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,564))

    def test_array_15(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: x[3] = {True,False,True};
                        x[1] = True;
                        print(string_of_bool(x[1]));
                    EndBody."""
        expect = "true"
        self.assertTrue(TestCodeGen.test(input,expect,565))

    def test_array_16(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                   Body: 
                        Var: x[3] = {True,False,True}, i = 0;
                        x[1] = x[0] && x[2];
                        For (i = 0, i < 3, 1) Do
                            print(string_of_bool(x[i]));
                        EndFor.
                   EndBody."""
        expect = "truetruetrue"
        self.assertTrue(TestCodeGen.test(input,expect,566))

    def test_array_17(self):
        """Simple program: int main() {} """
        input = """
                Var: x[3] = {True, False, True};
                Function: main
                   Body: 
                        Var: i = 0;
                        For (i = 0, i < 3, 1) Do
                            x[i] = !x[i] || False;
                        EndFor.
                        For (i = 0, i < 3, 1) Do
                            print(string_of_bool(x[i]));
                        EndFor.
                   EndBody."""
        expect = "falsetruefalse"
        self.assertTrue(TestCodeGen.test(input,expect,567))

    def test_array_18(self):
        """Simple program: int main() {} """
        input = """
                Var: x[3] = {True, False, True};
                Function: main
                   Body: 
                        Var: i = 0;
                        x = {False, True, False};
                        For (i = 0, i < 3, 1) Do
                            x[i] = !x[i] && True;
                        EndFor.
                        For (i = 0, i < 3, 1) Do
                            print(string_of_bool(x[i]));
                        EndFor.
                   EndBody."""
        expect = "truefalsetrue"
        self.assertTrue(TestCodeGen.test(input,expect,568))

    def test_array_19(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: x[3] = {"Hello", "World", "!"};
                        print(x[1]);
                    EndBody."""
        expect = "World"
        self.assertTrue(TestCodeGen.test(input,expect,569))

    def test_array_20(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: x[3] = {"Hello","World","!"};
                        x = {"I","am","Long"};
                        print(x[1]);
                    EndBody."""
        expect = "am"
        self.assertTrue(TestCodeGen.test(input,expect,570))

    def test_array_21(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: x[3] = {"Hello","World","!"};
                        x[1] = "Long";
                        print(x[1]);
                    EndBody."""
        expect = "Long"
        self.assertTrue(TestCodeGen.test(input,expect,571))

    def test_array_22(self):
        """Simple program: int main() {} """
        input = """
                Var: x[3] = {"Hello", "World", "!"};
                Function: main
                   Body: 
                        Var: i = 0;
                        x = {"Hello", "Long", "!"};
                        For (i = 0, i < 3, 1) Do
                            print(x[i]);
                        EndFor.
                   EndBody."""
        expect = "HelloLong!"
        self.assertTrue(TestCodeGen.test(input,expect,572))

    def test_array_23(self):
        """Simple program: int main() {} """
        input = """
                Var: x[3] = {"Hello", "World", "!"};
                Function: main
                   Body: 
                        Var: i = 0;
                        For (i = 0, i < 3, 1) Do
                            x[i] = "i";
                        EndFor.
                        For (i = 0, i < 3, 1) Do
                            print(x[i]);
                        EndFor.
                   EndBody."""
        expect = "iii"
        self.assertTrue(TestCodeGen.test(input,expect,573))

    def test_array_24(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: x[3][2] = {{1,2},{3,4},{5,6}};
                        print(string_of_int(x[0][1]));
                    EndBody."""
        expect = "2"
        self.assertTrue(TestCodeGen.test(input,expect,574))

    def test_array_25(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: x[2][2] = {{1,2},{3,4}};
                        x = {{5,6},{7,8}};
                        print(string_of_int(x[1][1]));
                    EndBody."""
        expect = "8"
        self.assertTrue(TestCodeGen.test(input,expect,575))

    def test_array_26(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                    Body:
                        Var: x[2][2] = {{1,2},{3,4}};
                        x[0][1] = 5;
                        print(string_of_int(x[0][1]));
                    EndBody."""
        expect = "5"
        self.assertTrue(TestCodeGen.test(input,expect,576))

    def test_array_27(self):
        """Simple program: int main() {} """
        input = """
                Var: x[2][2] = {{1,2},{3,4}};
                Function: main
                   Body: 
                        Var: i = 0, j = 0;
                        x = {{5,6},{7,8}};
                        For (i = 0, i < 2, 1) Do
                            For (j = 0, j < 2, 1) Do
                                print(string_of_int(x[i][j]));
                            EndFor.
                        EndFor.
                   EndBody."""
        expect = "5678"
        self.assertTrue(TestCodeGen.test(input,expect,577))

    def test_array_28(self):
        """Simple program: int main() {} """
        input = """
                Var: x[2][2] = {{1,2},{3,4}};
                Function: main
                   Body: 
                        Var: i = 0, j = 0;
                        For (i = 0, i < 2, 1) Do
                            For (j = 0, j < 2, 1) Do
                                x[i][j] = i + j;
                            EndFor.
                        EndFor.
                        For (i = 0, i < 2, 1) Do
                            For (j = 0, j < 2, 1) Do
                                print(string_of_int(x[i][j]));
                            EndFor.
                        EndFor.
                   EndBody."""
        expect = "0112"
        self.assertTrue(TestCodeGen.test(input,expect,578))

    def test_array_29(self):
        """Simple program: int main() {} """
        input = """
                Var: x[2][2][3] = {{{1,2,3},{4,5,6}},{{7,8,9},{10,11,12}}};
                Function: main
                   Body: 
                        Var: i = 0, j = 0, k = 0, sum = 0;
                        For (i = 0, i < 2, 1) Do
                            For (j = 0, j < 2, 1) Do
                                For (k = 0, k < 3, 1) Do
                                    x[i][j][k] = x[i][j][k] * 2;
                                EndFor.
                            EndFor.
                        EndFor.
                        For (i = 0, i < 2, 1) Do
                            For (j = 0, j < 2, 1) Do
                                For (k = 0, k < 3, 1) Do
                                    sum = sum + x[i][j][k];
                                EndFor.
                            EndFor.
                        EndFor.
                        print(string_of_int(sum));
                   EndBody."""
        expect = "156"
        self.assertTrue(TestCodeGen.test(input,expect,579))

    def test_array_30(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                   Body:
                        Var: x[2][2][3] = {{{1,2,3},{4,5,6}},{{7,8,9},{10,11,12}}}; 
                        Var: i = 0, j = 0, k = 0, sum = 0;
                        For (i = 0, i < 2, 1) Do
                            For (j = 0, j < 2, 1) Do
                                For (k = 0, k < 3, 1) Do
                                    x[i][j][k] = x[i][j][k] * 2 + 1;
                                EndFor.
                            EndFor.
                        EndFor.
                        For (i = 0, i < 2, 1) Do
                            For (j = 0, j < 2, 1) Do
                                For (k = 0, k < 3, 1) Do
                                    sum = sum + x[i][j][k];
                                EndFor.
                            EndFor.
                        EndFor.
                        print(string_of_int(sum));
                   EndBody."""
        expect = "168"
        self.assertTrue(TestCodeGen.test(input,expect,580))

    # test return
    def test_return_6(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                   Body:
                        Var: i = 0, j = 0, k = 0;
                        Var: x[2][2][3] = {{{12,11,10},{9,8,7}},{{6,5,4},{3,2,1}}};
                        For (i = 0, i < 2, 1) Do
                            For (j = 0, j < 2, 1) Do
                                For (k = 0, k < 3, 1) Do
                                    print(string_of_int(x[i][j][k]));
                                EndFor.
                            EndFor.
                        EndFor.
                        printLn();
                        x = foo();
                        For (i = 0, i < 2, 1) Do
                            For (j = 0, j < 2, 1) Do
                                For (k = 0, k < 3, 1) Do
                                    print(string_of_int(x[i][j][k]));
                                EndFor.
                            EndFor.
                        EndFor.
                   EndBody.
                Function: foo
                    Body:
                        Return {{{1,2,3},{4,5,6}},{{7,8,9},{10,11,12}}};
                    EndBody."""
        expect = "121110987654321\n123456789101112"
        self.assertTrue(TestCodeGen.test(input,expect,581))

    def test_return_7(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                   Body:
                        Var: i = 0, j = 0, k = 0;
                        Var: x[2][2][3] = {{{12,11,10},{9,8,7}},{{6,5,4},{3,2,1}}};
                        For (i = 0, i < 2, 1) Do
                            For (j = 0, j < 2, 1) Do
                                For (k = 0, k < 3, 1) Do
                                    print(string_of_int(x[i][j][k]));
                                EndFor.
                            EndFor.
                        EndFor.
                        printLn();
                        x = foo();
                        For (i = 0, i < 2, 1) Do
                            For (j = 0, j < 2, 1) Do
                                For (k = 0, k < 3, 1) Do
                                    print(string_of_int(x[i][j][k]));
                                EndFor.
                            EndFor.
                        EndFor.
                   EndBody.
                Function: foo
                    Body:
                        Var: x[2][2][3] = {{{1,2,3},{4,5,6}},{{7,8,9},{10,11,12}}};
                        Return x;
                    EndBody."""
        expect = "121110987654321\n123456789101112"
        self.assertTrue(TestCodeGen.test(input,expect,582))

    # test funccall
    def test_funccall_1(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                   Body:
                        Var: i = 0, j = 0, k = 0;
                        Var: x[2][2][3] = {{{12,11,10},{9,8,7}},{{6,5,4},{3,2,1}}};
                        For (i = 0, i < 2, 1) Do
                            For (j = 0, j < 2, 1) Do
                                For (k = 0, k < 3, 1) Do
                                    print(string_of_int(x[i][j][k]));
                                EndFor.
                            EndFor.
                        EndFor.
                        printLn();
                        foo(x);
                        For (i = 0, i < 2, 1) Do
                            For (j = 0, j < 2, 1) Do
                                For (k = 0, k < 3, 1) Do
                                    print(string_of_int(x[i][j][k]));
                                EndFor.
                            EndFor.
                        EndFor.
                   EndBody.
                Function: foo
                    Parameter: y[2][2][3]
                    Body:
                        Var: i = 0, j = 0, k = 0;
                        For (i = 0, i < 2, 1) Do
                            For (j = 0, j < 2, 1) Do
                                For (k = 0, k < 3, 1) Do
                                    y[i][j][k] = i + j + k;
                                EndFor.
                            EndFor.
                        EndFor.
                    EndBody."""
        expect = "121110987654321\n012123123234"
        self.assertTrue(TestCodeGen.test(input,expect,583))

    def test_funccall_2(self):  # ????????????????????????????????
        """Simple program: int main() {} """
        input = """
                Function: main
                   Body:
                        Var: i = 0, j = 0, k = 0;
                        Var: x[2][2][3] = {{{12,11,10},{9,8,7}},{{6,5,4},{3,2,1}}};
                        For (i = 0, i < 2, 1) Do
                            For (j = 0, j < 2, 1) Do
                                For (k = 0, k < 3, 1) Do
                                    print(string_of_int(x[i][j][k]));
                                EndFor.
                            EndFor.
                        EndFor.
                        printLn();
                        foo(x);
                        For (i = 0, i < 2, 1) Do
                            For (j = 0, j < 2, 1) Do
                                For (k = 0, k < 3, 1) Do
                                    print(string_of_int(x[i][j][k]));
                                EndFor.
                            EndFor.
                        EndFor.
                   EndBody.
                Function: foo
                    Parameter: x[2][2][3]
                    Body:
                        Var: y[2][2][3] = {{{1,2,3},{4,5,6}},{{7,8,9},{10,11,12}}};
                        Var: i = 0, j = 0, k = 0;
                        y = x;
                        For (i = 0, i < 2, 1) Do
                            For (j = 0, j < 2, 1) Do
                                For (k = 0, k < 3, 1) Do
                                    y[i][j][k] = i + j + k;
                                EndFor.
                            EndFor.
                        EndFor.
                    EndBody."""
        expect = "121110987654321\n012123123234"
        self.assertTrue(TestCodeGen.test(input,expect,584))

    def test_funccall_3(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                   Body:
                        Var: x = 5, y = 6;
                        no_swap(x,y);
                        print(string_of_int(x));
                        print(string_of_int(y));
                   EndBody.
                Function: no_swap
                    Parameter: x, y
                    Body:
                        Var: temp = 0;
                        temp = x;
                        x = y;
                        y = temp;
                    EndBody."""
        expect = "56"
        self.assertTrue(TestCodeGen.test(input,expect,585))

    # test assign
    def test_assign_4(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                   Body:
                        Var: x = "Hello", y = "World";
                        y = x;
                        print(x);
                        print(y);
                   EndBody."""
        expect = "HelloHello"
        self.assertTrue(TestCodeGen.test(input,expect,586))

    def test_assign_5(self):
        """Simple program: int main() {} """
        input = """
                Function: main
                   Body:
                        Var: x[3] = {1,2,3}, y[3] = {4,5,6}, i = 0;
                        y = x;
                        x[1] = 10;
                        For (i = 0, i < 3, 1) Do
                            print(string_of_int(x[i]));
                        EndFor.
                        printLn();
                        For (i = 0, i < 3, 1) Do
                            print(string_of_int(x[i]));
                        EndFor.
                   EndBody."""
        expect = "1103\n1103"
        self.assertTrue(TestCodeGen.test(input,expect,587))

    # test full program
    def test_full_program_1(self):
        input = """
        Var: arr[4] = {"This", "is", "a", "testcase"};
        ** This
        * is
        * a
        * block
        * comment ** 
        Function: printSth
            Parameter: arr[4]
            Body:
                Var : count = 0;
                While count < 4 Do
                    If (count % 2 == 0) Then
                        printStrLn("Skip");
                        count = count + 1;
                        Continue;
                    EndIf.
                    print(arr[count]);
                    count = count + 1;
                EndWhile.
                Return;
            EndBody.

        Function: main
            Body:
                printSth(arr);
                Return;
            EndBody."""
        expect = "Skip\nisSkip\ntestcase"
        self.assertTrue(TestCodeGen.test(input,expect,588))

    def test_full_program_2(self):
        input = """
        ** This is a global variable **
        Var: arr[5] = {5,   7, 1,2, 6};

        ** Sort function **
        Function: sort
            Parameter: arr[5]
            Body:
                Var: i = 50;
                For (i = 0, i < 5, 1) Do
                    Var: j = 3;
                    For (j = i + 1, j < 5, 1) Do
                        If arr[i] < arr[j] Then
                            Var: temp = 0;
                            temp = arr[i];
                            arr[i] = arr[j];
                            arr[j] = temp;
                        EndIf.
                    EndFor.
                EndFor.
                Return arr;
            EndBody.

        ** Entry of program **
        Function: main
            Body:
                Var: i = 100;
                For (i = 0, i < 5, 1) Do
                    print(string_of_int(arr[i]));
                EndFor.
                printLn();
                arr = sort(arr);
                For (i = 0, i < 5, 1) Do
                    print(string_of_int(arr[i]));
                EndFor.
            EndBody."""
        expect = "57126\n76521"
        self.assertTrue(TestCodeGen.test(input,expect,589))

    def test_full_program_3(self):
        input = """
        Function: sqrt
            Parameter: x
            Body:
                Return 1.1;
            EndBody.
        Function: radius
            Parameter: x, y
            Body:
                Var: r = 5.5;
                r = sqrt(x*.x +. y*.y);
                Return r;
            EndBody.
        Function: main
            Body:
                Var : x = 3.5e0, y = 4.6e-0;
                printStrLn(string_of_float(radius(x, y)));
                Return;
            EndBody."""
        expect = "1.1\n"
        self.assertTrue(TestCodeGen.test(input,expect,590))

    def test_full_program_4(self):
        input = """Var: x[5] = {1,2,3,4,5};
        Function: sum
            Parameter: x[5]
                Body:
                    Var: s = 0, i = 0;
                    For (i = 0 , i < 5, 1) Do
                        s = s + x[i];
                    EndFor.
                    Return s;
                EndBody.
        Function: main
            Body:
                Var: y = 0;
                y = sum(x);
                print(string_of_int(y));
                Return;
            EndBody."""
        expect = "15"
        self.assertTrue(TestCodeGen.test(input,expect,591))

    def test_full_program_5(self):
        input = """Var: x = 5;
        Function: fact
            Parameter: n
                Body:
                    If n == 0 Then
                        Return 1;
                    Else
                        Return n * fact (n - 1);
                    EndIf.
                EndBody.
        Function: main
            Body:
                x = 10;
                print(string_of_int(fact(x)));
                Return;
            EndBody."""
        expect = "3628800"
        self.assertTrue(TestCodeGen.test(input,expect,592))

    def test_full_program_6(self):
        input = """           
        Function: main
            Body:
                Var: a[3][2] = {{1,2},{3,4},{5,6}}, i = 0;
                While i < 3 Do
                    Var: j = 0;
                    If i < j Then
                        Continue;
                    EndIf.
                    While (j < 2) Do
                        print(string_of_int(a[i][j]));
                        j =  j + 1;
                        If j == 3 Then
                            Continue;
                        EndIf.
                    EndWhile.
                    i = i + 1;           
                EndWhile.
                Return;
            EndBody."""
        expect = "123456"
        self.assertTrue(TestCodeGen.test(input,expect,593))

    def test_full_program_7(self):
        input = """
        Function: foo
            Parameter: a[5]
            Body:
                Var: x[6] = {1,2,3,4,5,6}, y = 1;
                a[y] = x[a[x[a[x[y]]]]];
                Return a[y] + y;
            EndBody.
        Function: main
            Body:
                print(string_of_int(foo({1,2,3,4,5})));
                Return;
            EndBody."""
        expect = "7"
        self.assertTrue(TestCodeGen.test(input,expect,594))

    def test_full_program_8(self):
        input = """
        Function: sum
            Parameter: x,y
            Body:
                Return x + y;
            EndBody.
        Function: power
            Parameter: x,y
            Body:
                Var: result = 1, i = 0;
                For (i = 1, i <= y, 1) Do
                    result = result * x;
                EndFor.
                Return result;
            EndBody.
        Function: sqrt
            Parameter: x
            Body:
                Return 1;
            EndBody.            
        Function: main
            Body:
                Var: a[10] = {1,2,3,4,5,6,7,8,9,10}, x = 2, y = 3;
                printStrLn(string_of_int(a[1]));
                a[x * y - sum(x,y)] = a[sum(x,y) * 2 + a[x*y] - sqrt(power(x,2))*10] * (power(x+y,x*y) - power(x,y));
                print(string_of_int(a[1]));
                Return;
            EndBody."""
        expect = "2\n124936"
        self.assertTrue(TestCodeGen.test(input,expect,595))

    def test_full_program_9(self):
        input = """           
        Function: main
            Body:
                Var: a[9][6] = {{1,2,3,4,5,6}, {3,4,5,6,7,8}, {5,3,4,8,9,10}, {7,8,10,11,12,13}, {9,10,11,12,13,14}, {11,12,13,14,15,16}, {13,14,15,16,17,18}, {15,16,17,18,19,20}, {16,17,18,19,20,21}}, x = 2, y = 1;
                printStrLn(string_of_int(a[8][4]));
                printStrLn(string_of_int(a[x+y][x-y]));
                printStrLn(string_of_int(a[x*y][x\y]));
                a[a[x+y][x-y]][a[x*y][x\y]] = a[a[x+y][x-y]][a[x*y][x\y]] + 100;
                print(string_of_int(a[8][4]));
            EndBody."""
        expect = "20\n8\n4\n120"
        self.assertTrue(TestCodeGen.test(input,expect,596))

    # test short circuit evaluation
    def test_short_circuit_evaluation_1(self):
        input = """           
        Function: main
            Body:
                Var: x = 5, y = 0;
                If ((x > y) || ((x \ y) > 1)) Then
                    print("Hello");
                Else
                    print("World");
                EndIf.
            EndBody."""
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input,expect,597))
    
    def test_short_circuit_evaluation_2(self):
        input = """           
        Function: main
            Body:
                Var: x = 5, y = 0;
                If ((x < y) && ((x \ y) > 1)) Then
                    print("Hello");
                Else
                    print("World");
                EndIf.
            EndBody."""
        expect = "World"
        self.assertTrue(TestCodeGen.test(input,expect,598))

    def test_short_circuit_evaluation_3(self):
        input = """           
        Function: main
            Body:
                Var: x = 5, y = 1;
                If ((x < y) || ((x \ y) > 1)) Then
                    print("Hello");
                Else
                    print("World");
                EndIf.
            EndBody."""
        expect = "Hello"
        self.assertTrue(TestCodeGen.test(input,expect,599))

    # test if
    def test_if_8(self):
        input = """           
        Function: main
            Body:
                Var: x = 5, a = 5, b = 6;
                If (a < b) Then
                    Var: x = 4;
                    x = x + 6;
                    print(string_of_int(x));
                Else
                    x = x - 6;
                    print(string_of_int(x));
                EndIf.
                print(string_of_int(x));
            EndBody."""
        expect = "105"
        self.assertTrue(TestCodeGen.test(input,expect,600))

    def test_if_9(self):
        input = """           
        Function: main
            Body:
                Var: x = 5, a = 5, b = 6;
                If (a > b) Then
                    Var: x = 4;
                    x = x + 6;
                    print(string_of_int(x));
                Else
                    x = x - 6;
                    print(string_of_int(x));
                EndIf.
                print(string_of_int(x));
            EndBody."""
        expect = "-1-1"
        self.assertTrue(TestCodeGen.test(input,expect,601))

    # test while
    def test_while_3(self):
        input = """           
        Function: main
            Body:
                Var: x = 5, i = 0;
                While (i < 1) Do
                    Var: x = 1.1;
                    print(string_of_float(x));
                    i = i + 1;
                EndWhile.
                print(string_of_int(x));
            EndBody."""
        expect = "1.15"
        self.assertTrue(TestCodeGen.test(input,expect,602))

    def test_while_4(self):
        input = """           
        Function: main
            Body:
                Var: x = 5, i = 0;
                While (i < 1) Do
                    x = 6;
                    print(string_of_int(x));
                    i = i + 1;
                EndWhile.
                print(string_of_int(x));
            EndBody."""
        expect = "66"
        self.assertTrue(TestCodeGen.test(input,expect,603))

    # test dowhile
    def test_dowhile_3(self):
        input = """           
        Function: main
            Body:
                Var: x = 1;
                Do
                    Var: x = 1.5;
                    x = x +. 1.5;
                    print(string_of_float(x));
                While (x < 1)
                EndDo.
                print(string_of_int(x));
            EndBody."""
        expect = "3.01"
        self.assertTrue(TestCodeGen.test(input,expect,604))

    def test_dowhile_4(self):
        input = """           
        Function: main
            Body:
                Var: x = 1;
                Do
                    x = 6;
                    print(string_of_int(x));
                While (x < 1)
                EndDo.
                print(string_of_int(x));
            EndBody."""
        expect = "66"
        self.assertTrue(TestCodeGen.test(input,expect,605))

    # test for
    def test_for_3(self):
        input = """           
        Function: main
            Body:
                Var: x = 5;
                For (x = 0, x < 2, 1) Do
                    Var: x = 1.5;
                    x = x +. 1.5;
                    print(string_of_float(x));
                EndFor.
                print(string_of_int(x));
            EndBody."""
        expect = "3.03.02"
        self.assertTrue(TestCodeGen.test(input,expect,606))

    def test_for_4(self):
        input = """           
        Function: main
            Body:
                Var: x = 5;
                For (x = 0, x < 10, 1) Do
                    x = x + 3;
                    print(string_of_int(x));
                EndFor.
                print(string_of_int(x));
            EndBody."""
        expect = "371112"
        self.assertTrue(TestCodeGen.test(input,expect,607))

    # test int literal
    def test_int_literal_1(self):
        input = """
        Function: main
            Body:
                Var: x = 0x123ABC;
                print(string_of_int(x));
            EndBody."""
        expect = "1194684"
        self.assertTrue(TestCodeGen.test(input,expect,608))

    def test_int_literal_2(self):
        input = """
        Function: main
            Body:
                Var: x = 0o1234567;
                print(string_of_int(x));
            EndBody."""
        expect = "342391"
        self.assertTrue(TestCodeGen.test(input,expect,609))

    # test arraycell
    def test_arraycell_1(self):
        input = """ 
        Function: foo
            Body:
                Var: x[5] = {1,2,3,4,5};
                Return x;
            EndBody.          
        Function: main
            Body:
                Var: x = 1;
                x = x + foo()[2];
                print(string_of_int(x));
            EndBody."""
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,610))

    def test_arraycell_2(self):
        input = """ 
        Function: foo
            Body:
                Return {{1,2,3},{4,5,6}};
            EndBody.          
        Function: main
            Body:
                Var: x = 1;
                x = x + foo()[x - 1][x + 1];
                print(string_of_int(x));
            EndBody."""
        expect = "4"
        self.assertTrue(TestCodeGen.test(input,expect,611))

    def test_arraycell_3(self): # allow assign foo()[x - 1][x + 1] = 7 ????????????????????????????
        input = """ 
        Function: foo
            Body:
                Return {{1,2,3},{4,5,6}};
            EndBody.          
        Function: main
            Body:
                Var: x = 1, i = 0, j = 0;
                For (i = 0, i < 2, 1) Do
                    For (j = 0, j < 3, 1) Do
                        print(string_of_int(foo()[i][j]));
                    EndFor.
                EndFor.
                printLn();
                foo()[x - 1][x + 1] = 7;
                For (i = 0, i < 2, 1) Do
                    For (j = 0, j < 3, 1) Do
                        print(string_of_int(foo()[i][j]));
                    EndFor.
                EndFor.
            EndBody."""
        expect = "123456\n123456"
        self.assertTrue(TestCodeGen.test(input,expect,612))

    def test_arraycell_4(self):
        input = """ 
        Var: arr[2][3] = {{1,2,3},{4,5,6}};
        Function: foo
            Body:
                Return arr;
            EndBody.          
        Function: main
            Body:
                Var: x = 1, i = 0, j = 0;
                For (i = 0, i < 2, 1) Do
                    For (j = 0, j < 3, 1) Do
                        print(string_of_int(foo()[i][j]));
                    EndFor.
                EndFor.
                printLn();
                foo()[x - 1][x + 1] = 7;
                For (i = 0, i < 2, 1) Do
                    For (j = 0, j < 3, 1) Do
                        print(string_of_int(foo()[i][j]));
                    EndFor.
                EndFor.
            EndBody."""
        expect = "123456\n127456"
        self.assertTrue(TestCodeGen.test(input,expect,613))

    # test if
    def test_if_10(self):
        input = """Function: main
        Body:
        Var: n = 120,  array[2][3] = {{867,345,987},{76,12,744}};
            If n > 10 Then
                If (n%11 < 10) || (n > array[1][0]) Then 
                    n = array[0][1] * n % 9 \ 3;
                EndIf.
                print(string_of_int(n));
            EndIf.
        EndBody."""
        expect = "0"
        self.assertTrue(TestCodeGen.test(input,expect,614))