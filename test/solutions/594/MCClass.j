.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo([I)I
.var 0 is a [I from Label0 to Label1
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
	astore_1
.var 2 is y I from Label0 to Label1
	iconst_1
	istore_2
Label0:
	aload_0
	iload_2
	aload_1
	aload_0
	aload_1
	aload_0
	aload_1
	iload_2
	iaload
	iaload
	iaload
	iaload
	iaload
	iastore
	aload_0
	iload_2
	iaload
	iload_2
	iadd
	ireturn
Label1:
	iconst_0
	ireturn
.limit stack 11
.limit locals 3
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
Label0:
	iconst_5
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
	invokestatic MCClass/foo([I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	return
Label1:
	return
	return
.limit stack 9
.limit locals 1
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
