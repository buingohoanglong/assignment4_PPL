.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static sum(II)I
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
Label0:
	iload_0
	iload_1
	iadd
	ireturn
Label1:
	iconst_0
	ireturn
.limit stack 2
.limit locals 2
.end method

.method public static power(II)I
.var 0 is x I from Label0 to Label1
.var 1 is y I from Label0 to Label1
.var 2 is result I from Label0 to Label1
	iconst_1
	istore_2
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
Label0:
	iconst_1
	istore_3
Label2:
	iload_3
	iload_1
	if_icmpgt Label6
	iconst_1
	goto Label7
Label6:
	iconst_0
Label7:
	ifle Label5
	iload_2
	iload_0
	imul
	istore_2
Label3:
Label4:
	iconst_1
	iload_3
	iadd
	istore_3
	goto Label2
Label5:
	iload_2
	ireturn
Label1:
	iconst_0
	ireturn
.limit stack 8
.limit locals 4
.end method

.method public static sqrt(I)I
.var 0 is x I from Label0 to Label1
Label0:
	iconst_1
	ireturn
Label1:
	iconst_0
	ireturn
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	dup
	iconst_5
	bipush 6
	iastore
	dup
	bipush 6
	bipush 7
	iastore
	dup
	bipush 7
	bipush 8
	iastore
	dup
	bipush 8
	bipush 9
	iastore
	dup
	bipush 9
	bipush 10
	iastore
	astore_1
.var 2 is x I from Label0 to Label1
	iconst_2
	istore_2
.var 3 is y I from Label0 to Label1
	iconst_3
	istore_3
Label0:
	aload_1
	iconst_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	aload_1
	iload_2
	iload_3
	imul
	iload_2
	iload_3
	invokestatic MCClass/sum(II)I
	isub
	aload_1
	iload_2
	iload_3
	invokestatic MCClass/sum(II)I
	iconst_2
	imul
	aload_1
	iload_2
	iload_3
	imul
	iaload
	iadd
	iload_2
	iconst_2
	invokestatic MCClass/power(II)I
	invokestatic MCClass/sqrt(I)I
	bipush 10
	imul
	isub
	iaload
	iload_2
	iload_3
	iadd
	iload_2
	iload_3
	imul
	invokestatic MCClass/power(II)I
	iload_2
	iload_3
	invokestatic MCClass/power(II)I
	isub
	imul
	iastore
	aload_1
	iconst_1
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
	return
	return
.limit stack 22
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
