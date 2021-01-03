.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	bipush 9
	anewarray [I
	dup
	iconst_0
	bipush 6
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
	aastore
	dup
	iconst_1
	bipush 6
	newarray int
	dup
	iconst_0
	iconst_3
	iastore
	dup
	iconst_1
	iconst_4
	iastore
	dup
	iconst_2
	iconst_5
	iastore
	dup
	iconst_3
	bipush 6
	iastore
	dup
	iconst_4
	bipush 7
	iastore
	dup
	iconst_5
	bipush 8
	iastore
	aastore
	dup
	iconst_2
	bipush 6
	newarray int
	dup
	iconst_0
	iconst_5
	iastore
	dup
	iconst_1
	iconst_3
	iastore
	dup
	iconst_2
	iconst_4
	iastore
	dup
	iconst_3
	bipush 8
	iastore
	dup
	iconst_4
	bipush 9
	iastore
	dup
	iconst_5
	bipush 10
	iastore
	aastore
	dup
	iconst_3
	bipush 6
	newarray int
	dup
	iconst_0
	bipush 7
	iastore
	dup
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	bipush 10
	iastore
	dup
	iconst_3
	bipush 11
	iastore
	dup
	iconst_4
	bipush 12
	iastore
	dup
	iconst_5
	bipush 13
	iastore
	aastore
	dup
	iconst_4
	bipush 6
	newarray int
	dup
	iconst_0
	bipush 9
	iastore
	dup
	iconst_1
	bipush 10
	iastore
	dup
	iconst_2
	bipush 11
	iastore
	dup
	iconst_3
	bipush 12
	iastore
	dup
	iconst_4
	bipush 13
	iastore
	dup
	iconst_5
	bipush 14
	iastore
	aastore
	dup
	iconst_5
	bipush 6
	newarray int
	dup
	iconst_0
	bipush 11
	iastore
	dup
	iconst_1
	bipush 12
	iastore
	dup
	iconst_2
	bipush 13
	iastore
	dup
	iconst_3
	bipush 14
	iastore
	dup
	iconst_4
	bipush 15
	iastore
	dup
	iconst_5
	bipush 16
	iastore
	aastore
	dup
	bipush 6
	bipush 6
	newarray int
	dup
	iconst_0
	bipush 13
	iastore
	dup
	iconst_1
	bipush 14
	iastore
	dup
	iconst_2
	bipush 15
	iastore
	dup
	iconst_3
	bipush 16
	iastore
	dup
	iconst_4
	bipush 17
	iastore
	dup
	iconst_5
	bipush 18
	iastore
	aastore
	dup
	bipush 7
	bipush 6
	newarray int
	dup
	iconst_0
	bipush 15
	iastore
	dup
	iconst_1
	bipush 16
	iastore
	dup
	iconst_2
	bipush 17
	iastore
	dup
	iconst_3
	bipush 18
	iastore
	dup
	iconst_4
	bipush 19
	iastore
	dup
	iconst_5
	bipush 20
	iastore
	aastore
	dup
	bipush 8
	bipush 6
	newarray int
	dup
	iconst_0
	bipush 16
	iastore
	dup
	iconst_1
	bipush 17
	iastore
	dup
	iconst_2
	bipush 18
	iastore
	dup
	iconst_3
	bipush 19
	iastore
	dup
	iconst_4
	bipush 20
	iastore
	dup
	iconst_5
	bipush 21
	iastore
	aastore
	astore_1
.var 2 is x I from Label0 to Label1
	iconst_2
	istore_2
.var 3 is y I from Label0 to Label1
	iconst_1
	istore_3
Label0:
	aload_1
	bipush 8
	aaload
	iconst_4
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	aload_1
	iload_2
	iload_3
	iadd
	aaload
	iload_2
	iload_3
	isub
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	aload_1
	iload_2
	iload_3
	imul
	aaload
	iload_2
	iload_3
	idiv
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/printStrLn(Ljava/lang/String;)V
	aload_1
	aload_1
	iload_2
	iload_3
	iadd
	aaload
	iload_2
	iload_3
	isub
	iaload
	aaload
	aload_1
	iload_2
	iload_3
	imul
	aaload
	iload_2
	iload_3
	idiv
	iaload
	aload_1
	aload_1
	iload_2
	iload_3
	iadd
	aaload
	iload_2
	iload_3
	isub
	iaload
	aaload
	aload_1
	iload_2
	iload_3
	imul
	aaload
	iload_2
	iload_3
	idiv
	iaload
	iaload
	bipush 100
	iadd
	iastore
	aload_1
	bipush 8
	aaload
	iconst_4
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 64
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
